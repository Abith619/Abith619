{
    'name': "basics",
    'description': "basics of code",
    'version': "1.0",
    'depends': ['base','mail','sale'],
    'author': "suruthisuji",
    'data': [
        "security/ir.model.access.csv",
        "views/basic_views.xml",
        "views/sale_order_inherit.xml",
        'data/email_template.xml',
        'data/ir_cron.xml',
        'reports/report_action.xml',
        'reports/report_template.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
