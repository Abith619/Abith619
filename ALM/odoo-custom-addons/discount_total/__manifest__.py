{
    'name': 'Invoice Discount',
    'description': 'Apply discount On Invoice Total And Sales Orders',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'category': 'Sales',
    'author': 'Odoer.GH',
    'website': '',
    'depends': [
        'sale_management',
        'sale',
        'account',
    ],
    'data': [
        # 'views/sale_order_view.xml',
        'views/account_invoice_view.xml',
    ],
    'application': True,
    'installable': True,
}
