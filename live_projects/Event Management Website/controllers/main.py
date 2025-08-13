from odoo.http import request, route
from odoo.addons.website_event_booth.controllers.event_booth import WebsiteEventBoothController

class WebsiteEventBoothCustomController(WebsiteEventBoothController):

    @route(['/event/<model("event.event"):event>/booth'], type='http', auth="public", website=True)
    def event_booth_registration(self, event, booth_category_id=None, booth_ids=None, **kwargs):
        values = self._prepare_booth_contact_form_values(event, booth_ids, booth_category_id)

        return request.render("website_event_booth.event_booth_registration_details", values)
