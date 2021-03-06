{
    'name': 'Student Record',
'summary': """This module will add a record to store student details""",
'version': '0.1',
'description': """This module will add a record to store student details"""
,'author': 'Abith',
'company': 'Xmedia Solutions',
'website': 'https://www.xmedia.in',
'category': 'Tools',
'depends': ['base','web','mail','contacts','account','kanban_draggable', "sale"],
'license': 'AGPL-3',

'data': ['security/ir.model.access.csv',
    'views/model.xml',
    'views/teacher.xml',
    'views/Inherit.xml',
    'reports/reports.xml',
    'reports/pdf.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': True,
}