from odoo import http
from odoo.http import request
import json

class ShopApiController(http.Controller):

    @http.route('/api/products', auth='public', type='http', methods=['GET'], csrf=False)
    def get_products(self, **kwargs):
        products = request.env['product.template'].sudo().search([
            ('sale_ok', '=', True),
            ('website_published', '=', True)
        ])

        product_list = []
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for product in products:
            image_url = f"{base_url}/web/image/product.template/{product.id}/image_512"
            product_list.append({
                'id': product.id,
                'name': product.name,
                'price': product.list_price,
                'image_url': image_url,
                'description': product.website_description or product.description_sale,
            })

        return request.make_response(
            json.dumps(product_list),
            headers=[('Content-Type', 'application/json')]
        )
