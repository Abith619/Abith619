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
        'data/mail_template.xml',
        'views/header_template.xml',
        'views/about_us.xml',
        'views/home_page.xml',
        'views/crm_inherit.xml',
        'views/config_views.xml',
        'views/slide_inherit_views.xml',
        'views/channel_inherit.xml',
        'views/courses_inherit.xml',
        'views/footer_template.xml',
        'views/form_template_inherit.xml',
        'views/respartner.xml',
        'views/sale_order.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'moodle_connector/static/src/js/address_patch.js',

        ],

        'web.assets_backend': [
            'moodle_connector/static/src/js/image_preview_widget.js',
            'moodle_connector/static/src/xml/image_preview.xml',
        ],
    },
    'application': True,
    'license': 'LGPL-3',
}
