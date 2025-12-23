{
    'name': "Custom Module",
    'description': "Online Appointment Booking System",
    'version': "1.0",
    'depends': ['base','web','crm','sale','mail'],
    'author': "Kanishkka",
    'data': [
        'security/user_groups.xml',
        'data/ir_cron.xml',
        'data/ir_sequence.xml', 
        'data/email_template.xml', 
        'security/ir.model.access.csv',
        'reports/custom_pdf_report.xml',
        'reports/custom_pdf_report_template.xml',
        'views/custom_views.xml',
        'views/crm_lead_view.xml',
        'views/sale_order_inherit.xml',
        'wizard/wizard_view.xml'
    ],
     'application': True,
    'license': 'LGPL-3',
}

