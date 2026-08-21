#!/usr/bin/env python3
"""
Reset the admin user login/password from environment variables.
Run inside the Odoo container:
    docker exec -it prospire_app python3 /opt/odoo/reset_admin.py
"""
import os
import sys

# Allow running from /opt/odoo
sys.path.insert(0, '/opt/odoo')

import odoo

db_name = os.environ.get('DB_NAME', 'prospire_hq')
admin_login = os.environ.get('ADMIN_LOGIN', 'prospirenext@gmail.com')
admin_password = os.environ.get('ADMIN_PASSWORD', 'prospire@2@26')

try:
    odoo.tools.config.parse_config(['-c', '/opt/odoo/odoo.conf'])
    registry = odoo.registry(db_name)
    with registry.cursor() as cr:
        env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
        admin = env.ref('base.user_admin', raise_if_not_found=False)
        if not admin:
            # Fallback: find any user with admin privileges
            admin = env['res.users'].search([('id', '=', 2)], limit=1)
        if not admin:
            print('[reset_admin] ERROR: No admin user found')
            sys.exit(1)

        admin.write({'login': admin_login, 'password': admin_password})
        env.cr.commit()
        print(f'[reset_admin] Admin user {admin.id} updated: login={admin.login}')
except Exception as e:
    print(f'[reset_admin] ERROR: {e}')
    sys.exit(1)
