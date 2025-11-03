{
    "name": "Custom Online Courses",
    "version": "1.0",
    "author": "Abith Raj",
    "summary": "Custom module for managing Moodle online courses",
    "description": "A comprehensive solution for creating and managing online courses within Odoo. Sync and push courses and other datas from moodle and odoo",
    "category": "Education",
    "depends": ["base", "web", "website", "crm", "website_slides", "website_sale"],
    "data": [
        'security/ir.model.access.csv',
        "data/mail_template.xml",
        'views/config_views.xml',
        'views/slide_inherit_views.xml',
        'views/channel_inherit.xml',
        'views/courses_inherit.xml',
        'views/footer_template.xml',
        'views/form_template_inherit.xml',
        'views/respartner.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # 'custom_course/static/src/img/*.png',
        ],
        'web.assets_backend': [
            # 'sar_de_traffic/static/src/js/moves_list_renderer_ext.js',
        ],
    },
    'application': True,
    'license': 'LGPL-3',
}
