{
    'name': 'Prospire eLearning (SDTEK Course)',
    'version': '19.0.1.0.0',
    'summary': 'SDTEKH — Odoo Technical Training course content for the eLearning app',
    'category': 'Website',
    'author': 'ProspireNext',
    'website': 'https://prospirenext.com',
    'license': 'LGPL-3',
    'depends': ['website_slides', 'website'],
    'data': [
        'views/course_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'prospire_elearning/static/src/scss/prospire_elearning.scss',
        ],
    },
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': False,
}
