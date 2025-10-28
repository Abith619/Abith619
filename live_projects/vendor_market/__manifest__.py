{
    'name': 'Vendor Market Management',
    'category': 'Website',
    'summary': 'Manage your vendor market effectively',
    'version': '1.0',
    'description': """This module provides tools to manage your vendor market, including product listings, vendor profiles, and order management.""",
    'depends': ['web', 'stock', 'sale', 'website'],
    'data': [
        'views/product_inherit.xml',
        'views/vendor_products.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # Don't include dark mode files in light mode
        ],
        "web.assets_web_dark": [
            # 'whatsapp/static/src/**/*.dark.scss',
        ],
        'web.assets_unit_tests': [
            # 'whatsapp/static/tests/**/*',
        ],
    },
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
}
