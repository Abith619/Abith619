{
    'name': 'Custom Uber',
    'version': '1.0',
    'author': 'Raji',
    'category': 'Custom',
    'summary': 'Simple Uber Custom Module',
    'depends': ['base', 'mail'],

    'data': [
        'security/ir.model.access.csv',

        # Load wizard first
        'wizards/send_message_wizard_view.xml',

        # Then main views
        'views/custom_uber_views.xml',

        # Then reports
        'report/custom_uber_reports.xml',
        'report/custom_uber_templates.xml',

        'data/mail_template.xml', 

    
        'views/templates.xml',

        'data/cron.xml',
],

  
    'installable': True,
    'application': True,
}

