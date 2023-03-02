# -*- coding: utf-8 -*-
{
    'name': "Appointment",

    'summary': "Report an Appointment",

    'description': "Appointment",

    'author': "Dinakaran",
    'website': "http://erpjellyfish.my.id/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
      'security/ir.model.access.csv',
      'views/slots.xml',
      'views/consultation.xml',
      'views/day_slots.xml',
      'views/monthly_slots.xml',
      'views/partner.xml',




   



    ],
    # only loaded in demonstration mode
  

    'application': True,
}

