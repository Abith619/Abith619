from odoo.http import request, Controller, route
from odoo.exceptions import ValidationError

class BWSLeadController(Controller):
    @route('/api/bws_lead', type='http', auth='public', csrf=False)
    def create_bws_lead(self, **kwargs):
        name = kwargs.get('first_name', '') + ' ' + kwargs.get('last_name', '')
        email = kwargs.get('email')
        phone = kwargs.get('phone', '')
        message = kwargs.get('message')

        lead = request.env['crm.lead'].sudo().create({
            'name': name,
            'email_from': email,
            'phone': phone,
            'description': message,
        })
        return request.redirect('/submitted-thank-you')

    @route('/embed/contact-form', type='http', auth='public', website=True)
    def embed_contact_form(self):
        return request.render('custom_event.embed_contact_template', {})

    @route('/submitted-thank-you', type='http', auth='public', website=True)
    def contactus_thank_you(self):
        return request.render('custom_event.thank_you_template')