from odoo import http
from odoo.http import request,Controller,route

class CustomController(Controller):
    # @route(['/custom'], type="http", auth="public", website=True)
    # def custom_page(self,**kw):
    #     return request.render('custom_module.custom_page',{})

    @route(['/custom'], type="http", auth="public", website=True)
    def custom_page(self, **kw):
        return request.render('custom_module.affiliate_program_form_templates', {
            # 'param1': 'value1',
            # 'param2': 'value2',
        })

    @route(['/custom/submit'], type="http", auth="public", website=True, csrf=False)
    def create_lead_submit(self, **kw):
        vals = {
            "name": kw.get("name"),
            # "stage_id": request.env['crm.stage'].sudo().search([('name', '=', 'Qualified')], limit=1).id,
            "description": kw.get("company_name"),
            "description": kw.get("designation"),
            "phone": kw.get("contact_number"),
            "email_from": kw.get("email"),
            "description": kw.get("linked_in_profile"),
            "description": kw.get("industry_influence_focus"),
            "description": kw.get("expected_monthly_referrals"),
        }
        request.env["crm.lead"].sudo().create(vals)

        return request.redirect('/shop')