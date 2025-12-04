{
    'name': "Custom Module",
    'description': "Online Appointment Booking System",
    'version': "1.0",
    'depends': ['base', 'web', 'crm'],
    'author': "Abith",
    'data': [
        "security/user_groups.xml",
        "data/ir_sequence.xml",
        "security/ir.model.access.csv",
        'reports/custom_pdf_report.xml',
        'reports/custom_pdf_report_template.xml',
        "views/custom_views.xml",
        'views/crm_inherit.xml',
        'wizards/wizard_view.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}