from odoo import http
from odoo.http import request, route, Controller
import base64

class AffiliateProgramController(Controller):

    @route(['/affiliate/program'], type='http', auth="public", website=True, csrf=False)
    def affiliate_program_page(self, **post):
        return request.render("appointment_booking.affiliate_program_form_templates")

    @route(['/affiliate/program/submit'], type='http', auth="public", website=True, csrf=False)
    def affiliate_program_submit(self, **post):
        image = False
        if post.get('pan_gst'):
            image_file = post.get('pan_gst')
            image = base64.b64encode(image_file.read())

        vals = {
            "name": post.get("name"),
            "company_name": post.get("company_name"),
            "designation": post.get("designation"),
            "contact_number": post.get("contact_number"),
            "email": post.get("email"),
            "linked_in_profile": post.get("linked_in_profile"),
            "industry_influence_focus": post.get("industry_influence_focus"),
            "expected_monthly_referrals": post.get("expected_monthly_referrals"),
            "pan_gst": image,
        }
        request.env["affiliate.program"].sudo().create(vals)

        return request.render("appointment_booking.affiliate_thanks")
