{
    'name': "Moodle Connector",
    'description': "Sync and push courses and other datas from moodle and odoo",
    'version': "1.0",
    'depends': ['base','web', 'website_slides'],
    'author': "Abith",
    'data': [
        'security/ir.model.access.csv',
        'views/config_views.xml',
        'views/slide_inherit_views.xml',
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
