{
    'name': "RRR Module",
    'version': "1.0",
    'depends': ['base', 'web', 'website', 'website_sale', 'website_event_booth', 'google_recaptcha', 'mail', 'crm', 'event', 'website_event', 'event_booth', "event_booth_sale", 'sale', 'website_event_exhibitor', 'auth_signup', 'portal'],
    'author': "Abith",
    'data': [
        'views/event_booth_inherit.xml',
        'views/inherit_views.xml',
        'views/get_booth.xml',
        'views/exhibitor_form.xml',
        'views/signup.xml',
        'views/powerbi_iframe.xml',
        'data/email_signup.xml',
        'data/users_cron.xml',
        'views/res_users_custom.xml',
        'security/ir.model.access.csv',
        'views/booth_addons.xml',
        'views/sales_persons.xml',
        # 'security/user_groups.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'custom_event/static/src/js/booth_addons.js',
        ],
    },
    'application': True,
    'license': 'LGPL-3',
}