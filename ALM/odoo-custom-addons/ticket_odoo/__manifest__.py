# -*- coding: utf-8 -*-
{
    'name': "Employee Ticket",

    'summary': "Report an employee",

    'description': "Create ticket to report the employees who act indecently",

    'author': "PT Jelly Fish",
    'website': "http://erpjellyfish.my.id/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/seq.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
    'images': ['static/description/banner.png'],
}
