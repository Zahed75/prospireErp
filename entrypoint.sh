#!/bin/bash

set -e

if [ -z "${SMTP_USER:-}" ] || [ -z "${SMTP_PASSWORD:-}" ]; then
    echo "ERROR: SMTP_USER and SMTP_PASSWORD must be set in the production environment."
    exit 1
fi

echo "========================================="
echo "Odoo Production Deployment Starting..."
echo "========================================="

# Wait for database to be ready
echo "Waiting for database connection..."
until pg_isready -h "${DB_HOST:-db}" -p 5432 -U "${DB_USER:-odoo}"; do
    echo "Database is unavailable - sleeping"
    sleep 2
done
echo "Database is ready!"

# Migrate legacy module name in the database (raptron_admin -> prospire_login)
# so existing installs keep their state, views and settings after the rename.
echo "Migrating legacy module name if present..."
PGPASSWORD="${DB_PASSWORD:-}" psql \
    -h "${DB_HOST:-db}" -p 5432 -U "${DB_USER:-odoo}" -d "${DB_NAME:-prospire_hq}" \
    -c "UPDATE ir_module_module SET name='prospire_login' WHERE name='raptron_admin';" \
    -c "UPDATE ir_model_data SET module='prospire_login' WHERE module='raptron_admin';" \
    || echo "Module rename migration skipped (fresh database or already migrated)."

# ALWAYS ensure prospire_login and prospire_elearning are installed and up-to-date on every startup
# --init installs if missing, --update applies changes if already installed
echo "Installing / Updating prospire_login, prospire_elearning modules..."
python3 /opt/odoo/odoo-bin -c /opt/odoo/odoo.conf \
    -d "${DB_NAME:-prospire_hq}" \
    --init=prospire_login,prospire_elearning,vexanext_brand \
    --update=prospire_login,prospire_elearning,vexanext_brand \
    --stop-after-init

# Enforce correct base URL and website domain settings
echo "Enforcing base URL and website domain settings..."
python3 -c "
import os, odoo
from odoo.modules.registry import Registry
db = os.environ.get('DB_NAME', 'prospire_hq')
base_url = os.environ.get('BASE_URL', 'https://hq.prospirenext.com')
website_domain = os.environ.get('WEBSITE_DOMAIN', 'hq.prospirenext.com')
try:
    odoo.tools.config.parse_config(['-c', '/opt/odoo/odoo.conf'])
    registry = Registry(db)
    with registry.cursor() as cr:
        env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
        
        # 1. Freeze web.base.url so assets generate correctly
        param = env['ir.config_parameter'].sudo()
        param.set_param('web.base.url', base_url)
        param.set_param('web.base.url.freeze', '1')
        print(f'[entrypoint] web.base.url set to {base_url} (frozen)')
        
        # 2. Keep database expiration far in the future and clear any expiration reason
        param.set_param('database.expiration_date', '2126-12-31 23:59:59')
        param.set_param('database.expiration_reason', 'none')
        print('[entrypoint] database expiration set to 2126-12-31')
        
        # 3. Ensure website domain is set correctly
        Website = env['website'].sudo()
        for website in Website.search([]):
            if website.domain != website_domain:
                website.write({'domain': website_domain})
                print(f'[entrypoint] Website {website.id} domain set to {website_domain}')

        # 4. Disable base auto-vacuum cron
        # With workers=0, cron threads run in-process and can grab SHARE locks on
        # ir_attachment while a user is signing a PDF, causing lock-timeout 502s.
        autovacuum = env.ref('base.autovacuum_job', raise_if_not_found=False)
        if autovacuum and autovacuum.active:
            autovacuum.write({'active': False})
            print('[entrypoint] Base auto-vacuum cron disabled')

        env.cr.commit()
        print('[entrypoint] URL settings enforced successfully')
except Exception as e:
    print(f'[entrypoint] URL enforcement warning: {e}')
" || echo "URL enforcement skipped"

# Sync eLearning course content on every startup (idempotent). The module's
# post_init_hook only runs on install, so the course setup is re-applied here
# to survive module updates and manual uninstalls.
echo "Syncing eLearning course content..."
python3 -c "
import os, odoo
from odoo.modules.registry import Registry
db = os.environ.get('DB_NAME', 'prospire_hq')
try:
    odoo.tools.config.parse_config(['-c', '/opt/odoo/odoo.conf'])
    registry = Registry(db)
    with registry.cursor() as cr:
        env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
        if 'slide.channel' in env:
            from odoo.addons.prospire_elearning import post_init_hook
            post_init_hook(env)
            env.cr.commit()
            print('[entrypoint] eLearning course sync completed')
        else:
            print('[entrypoint] eLearning sync skipped: website_slides not installed')
except Exception as e:
    print(f'[entrypoint] eLearning sync warning: {e}')
" || echo "eLearning sync skipped"

# Clear asset cache to force fresh CSS/JS bundles
echo "Clearing asset cache..."
rm -rf /var/lib/odoo/assets-*

# Create/update initialization marker
touch /var/lib/odoo/.initialized
echo "Module update completed!"

# Update admin user credentials from code (runs on EVERY startup)
echo "Updating admin credentials..."
python3 -c "
import os, odoo
from odoo.modules.registry import Registry
db = os.environ.get('DB_NAME', 'prospire_hq')
admin_login = os.environ.get('ADMIN_LOGIN', 'prospirenext@gmail.com')
admin_password = os.environ.get('ADMIN_PASSWORD', 'prospire@2@26')
try:
    odoo.tools.config.parse_config(['-c', '/opt/odoo/odoo.conf'])
    registry = Registry(db)
    with registry.cursor() as cr:
        env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})

        def credentials_current(user):
            # Only rewrite when different: a password write re-hashes it and
            # invalidates every session (password feeds the session token).
            if user.login != admin_login:
                return False
            cr.execute('SELECT COALESCE(password, %s) FROM res_users WHERE id=%s', ('', user.id))
            row = cr.fetchone()
            if not row or not row[0]:
                return False
            try:
                return bool(user._crypt_context().verify(admin_password, row[0]))
            except Exception:
                return False

        # 1. Update base.user_admin
        admin = env.ref('base.user_admin')
        if not credentials_current(admin):
            admin.write({'login': admin_login, 'password': admin_password})
            print(f'[entrypoint] base.user_admin updated: login={admin.login}')
        else:
            print('[entrypoint] base.user_admin credentials already current, skipped')

        # 2. Also find and update ANY user with the old login
        old_users = env['res.users'].search([
            '|', '|',
            ('login', '=', 'tech.syscomatic@gmail.com'),
            ('login', '=', 'admin'),
            ('login', '=', 'fgarshoub@gmail.com')
        ])
        for old in old_users:
            if old.id != admin.id and not credentials_current(old):
                old.write({'login': admin_login, 'password': admin_password})
                print(f'[entrypoint] Old user {old.id} updated to new credentials')

        env.cr.commit()
        print('[entrypoint] Admin credentials updated successfully')
except Exception as e:
    print(f'[entrypoint] Admin update warning: {e}')
" || echo "Admin update skipped"

# Update SMTP server from environment on every startup
# The post_init_hook only runs once at install, so we re-apply mail server
# settings here to keep the password in sync with .env.
echo "Updating SMTP server configuration..."
python3 -c "
import os, odoo
from odoo.modules.registry import Registry
db = os.environ.get('DB_NAME', 'prospire_hq')
smtp_user = os.environ['SMTP_USER'].strip()
smtp_pass = ''.join(os.environ['SMTP_PASSWORD'].split())
try:
    odoo.tools.config.parse_config(['-c', '/opt/odoo/odoo.conf'])
    registry = Registry(db)
    with registry.cursor() as cr:
        env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
        Smtp = env['ir.mail_server'].sudo()
        existing_smtp = Smtp.search([('name', '=', 'Prospire SMTP')], limit=1)
        smtp_values = {
            'name': 'Prospire SMTP',
            'smtp_authentication': 'login',
            'smtp_host': os.environ.get('SMTP_HOST', 'smtp.gmail.com').strip(),
            'smtp_port': int(os.environ.get('SMTP_PORT', '587')),
            'smtp_user': smtp_user,
            'smtp_pass': smtp_pass,
            'smtp_encryption': os.environ.get('SMTP_ENCRYPTION', 'starttls').strip(),
            'from_filter': smtp_user,
            'sequence': 1,
            'active': True,
        }
        if existing_smtp:
            existing_smtp.write(smtp_values)
            print(f'[entrypoint] SMTP server updated for {smtp_user}')
        else:
            Smtp.create(smtp_values)
            print(f'[entrypoint] SMTP server created for {smtp_user}')
        param = env['ir.config_parameter'].sudo()
        param.set_param('mail.default.from', smtp_user)
        # Never use gmail.com (or any public provider) as catchall domain: the
        # Reply-To alias <alias>@gmail.com can never receive mail — replies are
        # lost and spam filters flag the mismatch. Empty catchall means Odoo
        # replies go to the actual sender's address, which is what a Gmail-SMTP
        # deployment wants. Set MAIL_CATCHALL_DOMAIN in .env only if you run
        # mail for your own domain and created the catchall alias mailbox.
        param.set_param('mail.catchall.domain', os.environ.get('MAIL_CATCHALL_DOMAIN', '').strip())
        for company in env['res.company'].sudo().search([]):
            # VexaNext-branded companies get the Vexa sender (see Vexa SMTP
            # block below), not the Prospire one.
            if not company.email and 'vexanext' not in company.name.lower():
                company.write({'email': smtp_user})
        template = env.ref('auth_signup.set_password_email', raise_if_not_found=False)
        if template:
            template.sudo().write({'email_from': smtp_user})
        env.cr.commit()
        print('[entrypoint] SMTP configuration and sender updated successfully')
except Exception as e:
    print(f'[entrypoint] SMTP update FAILED: {e}')
    raise
"

# Optional second outgoing mail server for the VexaNext company.
# Odoo routes each outgoing message through the server whose "From Filtering"
# matches the message From address: VexaNext mail is sent AS vexanext@gmail.com
# through vexanext's own Gmail login (proper auth alignment) instead of
# masquerading through the Prospire login — the pattern Gmail spam-filters.
# VEXA_SMTP_PASSWORD must be a 16-character Gmail app password
# (Google account → 2FA → App passwords) for vexanext@gmail.com.
if [ -n "${VEXA_SMTP_USER:-}" ]; then
echo "Updating Vexa SMTP server configuration..."
python3 -c "
import os, odoo
from odoo.modules.registry import Registry
db = os.environ.get('DB_NAME', 'prospire_hq')
vexa_user = os.environ['VEXA_SMTP_USER'].strip()
vexa_pass = ''.join(os.environ.get('VEXA_SMTP_PASSWORD', '').split())
try:
    odoo.tools.config.parse_config(['-c', '/opt/odoo/odoo.conf'])
    registry = Registry(db)
    with registry.cursor() as cr:
        env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
        Smtp = env['ir.mail_server'].sudo()
        existing = Smtp.search([('name', '=', 'Vexa SMTP')], limit=1)
        values = {
            'name': 'Vexa SMTP',
            'smtp_authentication': 'login',
            'smtp_host': os.environ.get('VEXA_SMTP_HOST', 'smtp.gmail.com').strip(),
            'smtp_port': int(os.environ.get('VEXA_SMTP_PORT', '587')),
            'smtp_user': vexa_user,
            'smtp_pass': vexa_pass,
            'smtp_encryption': os.environ.get('VEXA_SMTP_ENCRYPTION', 'starttls').strip(),
            # Matches any message sent from this exact address
            'from_filter': vexa_user,
            'sequence': 5,
            'active': True,
        }
        if existing:
            existing.write(values)
            print(f'[entrypoint] Vexa SMTP server updated for {vexa_user}')
        else:
            Smtp.create(values)
            print(f'[entrypoint] Vexa SMTP server created for {vexa_user}')
        # Brand the VexaNext company with the Vexa sender
        company = env['res.company'].sudo().search([('name', 'ilike', 'vexanext')], limit=1)
        if company:
            company.write({'email': vexa_user})
            print(f'[entrypoint] Company {company.name} email set to {vexa_user}')
        env.cr.commit()
        print('[entrypoint] Vexa SMTP configuration completed')
except Exception as e:
    print(f'[entrypoint] Vexa SMTP update FAILED: {e}')
    raise
"
else
    echo "VEXA_SMTP_USER not set, skipping Vexa SMTP server configuration."
fi

# Clean old assets on every startup
rm -rf /var/lib/odoo/assets-*

echo "========================================="
echo "Starting Odoo server..."
echo "========================================="

# Execute the main command
exec "$@"
