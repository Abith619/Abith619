{
    'name': "Appointment Booking",
    'description': "Online Appointment Booking System",
    'version': "1.0",
    'depends': ['base', 'calendar', 'website', 'website_sale', 'portal', 'web', 'crm', 'mail'],
    'author': "Abith",
    'data': [
        'security/ir.model.access.csv',
        'data/appointment_email_template.xml',
        'views/affiliate_program.xml',
        'views/affiliate_program_form.xml',
        'views/appointment_booking.xml',
        'views/appointment_booking_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # 'appointment/static/src/js/appointment_frontend.js',
        ],
        'web.assets_backend': [
            # 'appointment/static/src/js/appointment_backend.js',
        ],
        'web.assets_backend_lazy': [
            # 'appointment/static/src/views/gantt/**',
        ],
        'web_editor.backend_assets_wysiwyg': [
            # 'appointment/static/src/js/wysiwyg.js',
        ],
    },
    'application': True,
    'license': 'LGPL-3',
}
