{
    'name': "Customs Module",
    'version': "1.0",
    'depends': ['base', 'crm','mail','website'],
    'author': "Suruthi",
    'data': [
        "security/ir.model.access.csv",
        "data/ir_sequence.xml",
        "views/website_template.xml",
        "views/customs_views.xml",
        "views/crm_inherit.xml",
        "reports/customs_pdf_report.xml",
        "reports/customs_pdf_report_template.xml",
    ],
    'application': True,
    'license': 'LGPL-3',
}
