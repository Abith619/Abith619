from odoo.http import request, Controller, route
from odoo.exceptions import ValidationError

class ContactFormController(Controller):

    @route('/booth-register', auth='public', website=True)
    def web_form(self, **kwargs):
        event_id = kwargs.get('event_id')
        event = request.env['event.event'].sudo().browse(int(event_id)) if event_id else None

        return request.render('custom_event.booth_registration_form', {
            'event': event,
        })

