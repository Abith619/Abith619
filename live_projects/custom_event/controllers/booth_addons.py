from odoo import http
from odoo.http import request, route
from odoo.addons.website_event_booth.controllers.event_booth import WebsiteEventBoothController
import json

class WebsiteEventBoothCustomController(WebsiteEventBoothController):

    @route('/event/<model("event.event"):event>/booth/confirm', type='http', auth='public', methods=['POST'], website=True, sitemap=False)
    def event_booth_registration_confirm(self, event, booth_category_id, event_booth_ids, **kwargs):
        # booths = self._get_requested_booths(event, event_booth_ids)

        # error_code = self._check_booth_registration_values(booths, kwargs['contact_email'])
        # if error_code:
        #     return json.dumps({'error': error_code})

        # booth_values = self._prepare_booth_registration_values(event, kwargs)
        # booths.action_confirm(booth_values)

        # self._prepare_booth_registration_success_values(event.name, booth_values)

        return request.redirect(f"/event/{event.id}/booth/addons-package")

    @route('/event/<model("event.event"):event>/booth/addons-package', auth='public', website=True)
    def booth_addons_package(self, event, **kwargs):
        return request.render("custom_event.booth_addons_template", {
            'event': event,
        })
