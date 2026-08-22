import os

from . import models
from . import controllers


def post_init_hook(env):
    admin_login = os.environ.get("ADMIN_LOGIN", "prospirenext@gmail.com")
    admin_password = os.environ.get("ADMIN_PASSWORD", "prospire@2@26")
    base_url = os.environ.get("BASE_URL", "https://hq.prospirenext.com")
    website_domain = os.environ.get("WEBSITE_DOMAIN", "hq.prospirenext.com")

    # 1. Reset Admin Credentials
    # Search by any known old login
    admin = env['res.users'].search([
        '|', '|',
        ('login', '=', 'admin'),
        ('login', '=', 'tech.syscomatic@gmail.com'),
        ('login', '=', 'fgarshoub@gmail.com'),
    ], limit=1, order='id desc')
    if not admin:
        admin = env.ref('base.user_admin', raise_if_not_found=False)
    # Only write when credentials actually differ: rewriting the password
    # re-hashes it and invalidates all sessions (password is part of the
    # session token), which caused "Session Expired" every few minutes.
    if admin and not env['res.users']._credentials_current(admin, admin_login, admin_password):
        admin.write({
            'login': admin_login,
            'password': admin_password,
        })

    # 1b. Give the admin a proper sender name so outgoing mail shows
    # "Prospire Next <prospirenext@gmail.com>" instead of "Administrator".
    # A generic sender name is one of the signals that lands mail in spam.
    if admin and admin.name == 'Administrator':
        admin.write({'name': 'Prospire Next'})

    # 2. Configure SMTP
    smtp_user = os.environ.get("SMTP_USER", "prospirenext@gmail.com")
    smtp_pass = os.environ.get("SMTP_PASSWORD", "cgnk vwjs yewk pgml")
    Smtp = env['ir.mail_server']
    existing_smtp = Smtp.search([('name', '=', 'Prospire SMTP')], limit=1)
    smtp_values = {
        'name': 'Prospire SMTP',
        'smtp_host': 'smtp.gmail.com',
        'smtp_port': 587,
        'smtp_user': smtp_user,
        'smtp_pass': smtp_pass,
        'smtp_encryption': 'starttls',
        'from_filter': smtp_user,
        'sequence': 1,
    }
    if existing_smtp:
        existing_smtp.write(smtp_values)
    else:
        Smtp.create(smtp_values)

    # 3. Force Expiration
    env['ir.config_parameter'].sudo().set_param('database.expiration_date', '2126-12-31 23:59:59')

    # 3b. Enforce production base URL so invitation emails use the real domain
    param = env['ir.config_parameter'].sudo()
    param.set_param('web.base.url', base_url)
    param.set_param('web.base.url.freeze', '1')
    env.cr.commit()

    # 4. Ensure our login template is applied AFTER website.login_layout.
    # NOTE: ir.ui.view.xml_id is a computed non-stored field in Odoo 19,
    # so it cannot be searched directly — use env.ref() instead.
    login_template = env.ref('prospire_login.garshoub_login_layout', raise_if_not_found=False)
    if login_template:
        # priority=30 -> applied after website.login_layout (priority=20)
        login_template.write({'priority': 30})
        env.cr.commit()

    # 5. Ensure web_layout (favicon) also has high priority
    layout_template = env.ref('prospire_login.garshoub_web_favicon', raise_if_not_found=False)
    if layout_template:
        layout_template.write({'priority': 1})
        env.cr.commit()

    # 6. Ensure website.login_layout keeps its default priority=20
    # Our garshoub_login_layout (priority=30) will apply AFTER it and replace website.layout
    website_login_override = env.ref('website.login_layout', raise_if_not_found=False)
    if website_login_override and website_login_override.priority != 20:
        website_login_override.write({'priority': 20})
        env.cr.commit()
