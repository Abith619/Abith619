# -*- coding: utf-8 -*-

{
    'name': 'WebShop',
    'version': '16',
    'license': 'AGPL-3',
    'summary': 'Webshop Design',
    'description': 'Webshop Customaization for Website',
    'author': 'Insoft',
    'company': 'Insoft',
    'maintainer': 'Insoft',
    'website': 'https://insoft.com',
    'depends': ['base', 'base_setup', 'mail', 'website', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/webshop.xml',
        'views/login.xml',
        # 'views/test.xml',
    ],
    # 'external_dependencies': {'python': ['openai']},
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
