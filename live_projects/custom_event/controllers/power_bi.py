from odoo.http import request, Controller, route, Response
import json
from odoo.exceptions import ValidationError

class PowerBIController(Controller):
    @route('/powerbi', type='http', auth='public', csrf=False)
    def power_bi(self, **kwargs):
        event = request.env['event.event'].sudo().search([('id', '=', 20)], limit=1)

        data = [{
            'id': event.id,
            'name': event.name,
            'date': event.date_begin.isoformat() if event.date_begin else None
        }]

        return Response(json.dumps(data), content_type='application/json', status=200 )

    @route('/powerbi/dashboard', auth='user', website=True)
    def dashboard(self, **kwargs):
        return request.render('custom_event.powerbi_iframe_template')