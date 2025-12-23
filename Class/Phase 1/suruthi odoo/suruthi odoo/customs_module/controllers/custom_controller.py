from odoo import http
from odoo.http import request, Controller, route

class CustomController(Controller):

    @route(['/custom'], type="http", auth="public", website=True)
    def custom_page(self, **kw):
        return request.render('customs_module.affiliate_program_form_templates')

    @route(['/custom/submit'], type="http", auth="public", website=True, csrf=False)
    def create_lead_submit(self, **kw):

        description_text = (
            f"Company Name: {kw.get('company_name')}\n"
            f"Designation: {kw.get('designation')}\n"
            f"LinkedIn: {kw.get('linked_in_profile')}\n"
            f"Industry Focus: {kw.get('industry_influence_focus')}\n"
            f"Expected Monthly Referrals: {kw.get('expected_monthly_referrals')}"
        )

        vals = {
            "name": kw.get("name"),
            "stage_id": request.env['crm.stage'].sudo().search([('name', '=', 'Qualified')], limit=1).id,
            "phone": kw.get("contact_number"),
            "email_from": kw.get("email"),
            "description": description_text,
        }

        request.env["crm.lead"].sudo().create(vals)

        return request.redirect('/shop')
