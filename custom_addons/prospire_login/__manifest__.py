{
    'name': 'Prospire Next Login',
    'version': '19.0.1.0.0',
    'summary': 'Prospire Next branding: login page, favicon, admin portal and SaaS helpers',
    'category': 'Hidden',
    'author': 'Zahed Hasan',
    'website': 'https://prospirenext.com',
    # website is included so our login/favicon overrides load AFTER website's templates
    'depends': ['base', 'mail', 'web', 'crm', 'account', 'website', 'auth_signup'],
    'data': [
        'security/prospire_login_groups.xml',
        'security/ir.model.access.csv',
        'data/mail_templates.xml',
        'data/auth_signup_mail_templates.xml',
        'data/enforce_settings_cron.xml',
        'views/login_templates.xml',
        'views/web_layout.xml',
        'views/registration_views.xml',
    ],
    'installable': True,
    'application': False,
    'post_init_hook': 'post_init_hook',
    'assets': {
        'web.assets_backend': [
            'prospire_login/static/src/css/cleanup.css',
        ],
        'web.assets_frontend': [
            'prospire_login/static/src/css/prospire_login.css',
            'prospire_login/static/src/js/prospire_login.js',
        ],
        'sign.assets_public_sign': [
            'prospire_login/static/src/js/sign_no_autofill.js',
        ],
    },
    'license': 'LGPL-3',
}
