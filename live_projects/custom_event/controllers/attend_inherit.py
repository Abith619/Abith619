from odoo import http
from odoo.http import request

class WebsiteEvent(http.Controller):

    @http.route(['/event/<model("event.event"):event>/registration/confirm'], type='http', auth="public", website=True, csrf=True)
    def registration_confirm(self, event, **post):
        sales_person = post.get('sales_person')

        registration_vals = {
            'event_id': event.id,
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'sales_person': sales_person,
        }

        request.env['event.registration'].sudo().create(registration_vals)

        return request.redirect('/event/thanks')
