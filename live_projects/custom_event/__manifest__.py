{
    'name': "RRR Module",
    'version': "1.0",
    'depends': ['base', 'web', 'mail', 'crm', 'website', 'event', 'website_event', 'website_event_booth', 'sale', 'website_event_exhibitor', 'auth_signup', 'portal'],
    'author': "Abith",
    'data': [
        'views/inherit_views.xml',
        'views/get_booth.xml',
        'views/exhibitor_form.xml',
        'views/signup.xml',
        'data/email_signup.xml',
        'security/ir.model.access.csv',
        # 'security/user_groups.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'custom_event/static/js/event_booth.js',
        ],
    },
    'application': True,
    'license': 'LGPL-3',
}