{
    'name': 'Customer Module',
    'version': '1.0',
    'depends': ['base', 'crm'],
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/customer_views.xml',
        'views/crm_inherit_view.xml',
        'views/wizard_view.xml',
        'reports/customer_care_report.xml',
        'reports/customer_care_report_template.xml',
        'data/ir.sequence.xml'

    ],
    'installable': True,
    'application': True,
}
