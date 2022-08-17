{
    'name': "Yodoo Client",

    'summary': (
        "This is the client addon for the Yodoo Cockpit. "
        "Yodoo Cockpit, allows you to easily manage your odoo installations. "
        "Also, it allows you to easily run your product as SaaS."
    ),

    'author': "Center of Research and Development",
    'website': "https://crnd.pro/yodoo-cockpit",
    'license': 'LGPL-3',

    'version': '12.0.1.23.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'web',
        'base_setup',
        'fetchmail',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'data/ir_config_parameter.xml',
        'data/ir_actions_server.xml',
        'views/yodoo_client_auth_log.xml',
        'views/saas_statistic.xml',
        'views/dbmanager.xml',
        'views/assets.xml',
        'views/ir_module_module.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'qweb': [],
    'category': 'Technical',
    'installable': True,
    'auto_install': True,
    'images': ['static/description/banner.png'],
    "post_load": "_post_load_hook",
    'live_test_url': 'https://yodoo.systems',
    'support': 'info@crnd.pro',
}
