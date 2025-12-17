# -*- coding: utf-8 -*-
{
    'name': "Zoho Books Connector",

    'summary': """
        It helps to Connects Odoo with Zoho Books """,

    'description': """
         It helps to Connects Odoo with Zoho Books 
    """,

    'author': "AgaramSoft",
    'website': "http://agaramsoft.com",
    'live_test_url':'https://www.youtube.com/watch?v=oe_hNCqNOWI',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Zoho',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
    'security/ir.model.access.csv',
    'views/contact_view.xml',
    'views/item_view.xml',
    'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "images":['static/description/icon.png']
}