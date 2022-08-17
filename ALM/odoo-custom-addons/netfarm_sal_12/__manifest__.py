# -*- coding: utf-8 -*-
{
    'name': "Netfarm Sal Planning 12",
    'author': "Netfarm Srl",
    'version': '12.0.1',
    'license':'OPL-1',
    'category': 'Project',
    #'sequence': 99,
    #'price': '',
    'summary': """Netfarm Sal Planning""",
    'description': """
        Il modulo Netfarm Sal Planning è stato ideato e progettato
        per la gestione delle risorse umane, per l'assegnamento dei task
        e la semplificazione della rendicontazione.
        3 funzioni: pianificazione, rendicontazione e controllo.
        """,
    'website': "https://www.netfarm.it/",
    'support':'odoo@netfarm.it',

    'depends': [
        'web',
        'base',
        'hr',
        'snailmail',
    ],
    'data': [
        'views/assets.xml',
        'data/data.xml',
        'security/netfarm_sal_planning_security.xml',
        'security/ir.model.access.csv',
        'views/calendar.xml',
        'views/views.xml',
        'views/config.xml'
    ],
    'qweb': [
        'static/src/xml/record_activity.xml',
        'static/src/xml/employee_block.xml',
        'static/src/xml/activity_block.xml',
        'static/src/xml/buttons.xml',
        'static/src/xml/hour_block.xml',
    ],
    'images': ['static/description/banner.gif','static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
