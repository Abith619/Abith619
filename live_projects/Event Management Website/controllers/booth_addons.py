from odoo import http, tools
import werkzeug, json
from odoo.http import request, route
from odoo.addons.website_event_booth.controllers.event_booth import WebsiteEventBoothController

class WebsiteEventBoothCustomController(WebsiteEventBoothController):

    @http.route('/event/<model("event.event"):event>/booth/confirm',
                type='http', auth='public', methods=['POST'], website=True, sitemap=False)
    def event_booth_registration_confirm(self, event, booth_category_id, event_booth_ids, **kwargs):
        booths = self._get_requested_booths(event, event_booth_ids)

        error_code = self._check_booth_registration_values(booths, kwargs['contact_email'])
        if error_code:
            return json.dumps({'error': error_code})

        booth_values = self._prepare_booth_registration_values(event, kwargs)
        booths.action_confirm(booth_values)

        return self._prepare_booth_registration_success_values(event.name, booth_values)

    def _prepare_booth_registration_partner_values(self, event, kwargs):
        if request.env.user._is_public():
            conctact_email_normalized = tools.email_normalize(kwargs['contact_email'])
            contact_name_email = tools.formataddr((kwargs['contact_name'], conctact_email_normalized))
            partner = request.env['res.partner'].sudo().find_or_create(contact_name_email)
            if not partner.name and kwargs.get('contact_name'):
                partner.name = kwargs['contact_name']
            if not partner.phone and kwargs.get('contact_phone'):
                partner.phone = kwargs['contact_phone']
        else:
            partner = request.env.user.partner_id
        return {
            'partner_id': partner.id,
            'contact_name': kwargs.get('contact_name') or partner.name,
            'contact_email': kwargs.get('contact_email') or partner.email,
            'contact_phone': kwargs.get('contact_phone') or partner.phone or partner.mobile,
            'sales_persons': kwargs.get('sales_person'),
        }

    @route('/event/<model("event.event"):event>/booth/addons-package', auth='public', website=True)
    def booth_addons_package(self, event, **kwargs):
        booth_a = request.env['product.template'].sudo().search([('id', '=', 72)])
        booth_b = request.env['product.template'].sudo().search([('id', '=', 73)])
        booth_d = request.env['product.template'].sudo().search([('id', '=', 74)])
        booth_f = request.env['product.template'].sudo().search([('id', '=', 75)])
        booth_g = request.env['product.template'].sudo().search([('id', '=', 76)])
        booth_h = request.env['product.template'].sudo().search([('id', '=', 77)])

        return request.render("custom_event.booth_addons_template", {
            'event': event,
            'booth_a': booth_a,
            'booth_b': booth_b,
            'booth_d': booth_d,
            'booth_f': booth_f,
            'booth_g': booth_g,
            'booth_h': booth_h,
        })