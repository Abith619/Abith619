{
    'name': "SarDe Traffic",
    'description': "",
    'version': "1.0",
    'depends': ['base', 'purchase', 'stock', 'project', 'mrp', 'crm', 'sale'],
    'author': "Abith",
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        # 'views/estimate_masters.xml',
        'views/purchase_inherit_views.xml',
        'views/stock_inherit_views.xml',
        'views/bom_inherit.xml',
        'views/crm_inherit.xml',
        'views/estimate_form.xml',
        # 'views/quotation_estimate.xml',
        'views/manufacturing_inherit.xml',
        'reports/quotation_estimate_report.xml',
        'wizards/purchase_wizard.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # 'sar_de_traffic/static/src/js/moves_list_renderer_ext.js',
            # 'sar_de_traffic/static/src/xml/moves_list_row_ext.xml',
        ],
    },
    'application': True,
    'license': 'LGPL-3',
}
