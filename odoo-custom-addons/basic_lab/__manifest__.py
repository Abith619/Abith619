{
    "name": "Lab Management System",
    "version": "14.0.0.1",
    "currency": 'INR',
    "summary": "Lab Management System",
    "category": "Lab Industry",
    "description": """
            Lab Module
        """,
    "depends": ["base","contacts","web",'account'],
    "data": [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/lab_department.xml',
        'views/lab_bills.xml',
        'data/ir_sequence_data.xml',
        'report/report_views.xml',
        'report/lab_bill.xml',
        'report/lab_department.xml',
            ],
    'qweb': [
        # 'static/src/xml/dicom_image.xml',
    ],
    'demo': [
    ],
    'css': [],
    "author": "Abith",
    "website": "https://www.scopex.in",
    "installable": True,
    "application": True,
    "auto_install": False,
    "images": [],
    "live_test_url": 'https://pydicom.mo.vc/',
}
