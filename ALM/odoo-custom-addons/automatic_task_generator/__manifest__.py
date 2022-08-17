# -*- coding: utf-8 -*-
{
    'name': "Automatic periodic tasks",

    'summary': """
        Periodic task generator allows you to set up tasks so that they are automatically assigned at a specific interval.""",

    'description': """
        Periodic task generator allows you to set up tasks so that they are automatically assigned at a specific interval.
        For example you can set up automatic assignment task for selected project in 7 day interval, then new task with same attributes is created every week.
        Automatic task with selected periodicity simplifies planning and reduces your workload. Assigment of periodic tasks can be stopped and modified.
    """,

    'author': "Implemento",
    'website': "http://implemento.sk/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project',
    'version': '12.0.0.0.1',
    'license': 'LGPL-3',
    'support': 'lagin@implemento.sk',
    'images': ['images/main_screenshot.png'],

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/periodic_task.xml',
        'views/templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}