# -*- coding: utf-8 -*-
{
    'name': 'EESTISOFT Task Attachments',
    'version': '1.0',
    'category': 'Addon',
    'sequence': 1,
    'summary': "Add attachments to project tasks",
    'description': "EESTISOFT module which adds 'attachments' feature to tasks and sub-tasks in Project.",
    'author': 'EESTISOFT, ' 'Mateus Cappellari Vieira, ' 'Tiago Magrini Rigo',
    'website': '',
    'depends': ['base','project'],
    'data': [
        'views/doc_button.xml'
    ],
    'images':['static/description/t_a_front.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'qweb': [],
}
