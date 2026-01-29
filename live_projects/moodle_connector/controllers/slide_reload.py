from odoo import http
from odoo.addons.website_slides.controllers.main import WebsiteSlides


class WebsiteSlidesInherit(WebsiteSlides):

    @http.route('/slides/<int:channel_id>',type='http',auth='user',website=True,csrf=False)
    def slides_channel(self, channel_id, **kw):

        return super().slides(channel_id=channel_id, **kw)
