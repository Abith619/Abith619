from odoo import http
from odoo.http import request

class MyController(http.Controller):

    # Simple GET request route
    @http.route('/my_module/hello', auth='public', type='http')
    def hello_world(self, **kwargs):
        name = kwargs.get('name', 'Guest')  # Get URL param ?name=John
        return f"<h1>Hello, {name}!</h1>"

    # JSON route for API requests
    @http.route('/my_module/json_api', auth='public', type='json', methods=['POST'])
    def json_api(self, **kwargs):
        data = kwargs.get('data', 'No Data')
        return {'status': 'success', 'received': data}

    # Using a template (optional)
    @http.route('/my_module/template', auth='public', type='http')
    def template_route(self):
        partners = request.env['res.partner'].search([], limit=5)
        return request.render('my_module.template_id', {'partners': partners})
