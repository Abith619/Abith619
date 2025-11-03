from odoo import http
from odoo.http import request, route
import logging
from odoo.addons.website_sale.controllers.main import WebsiteSale

_logger = logging.getLogger(__name__)

class WebsiteSaleController(WebsiteSale):

    @http.route('/shop/address/submit', type='http', methods=['POST'], auth='public', website=True, sitemap=False)
    def shop_address_submit(self, **post):
        admission_data = {
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            # 'dob': post.get('dob'),
            'institution_name': post.get('institution_name'),
            'institution_address': post.get('institution_address'),
            'qualification': post.get('qualification'),
            'street': post.get('street'),
            'city': post.get('city'),
            'zip': post.get('zip'),
            'state_id': post.get('state_id'),
            'country_id': post.get('country_id'),
        }
 
        partner = request.env['res.partner'].sudo().create({
            'name': admission_data.get('name'),
            'email': admission_data.get('email'),
            'mobile': admission_data.get('phone'),
            # 'dob': admission_data.get('dob'),
            'institution_name': admission_data.get('institution_name'),
            'institution_address': admission_data.get('institution_address'),
            'qualification': admission_data.get('qualification'),
            'street': admission_data.get('street'),
            'city': admission_data.get('city'),
            'zip': admission_data.get('zip'),
            'state_id': admission_data.get('state_id'),
            'country_id': admission_data.get('country_id'),
 
        })

        course_revenue = request.env['slide.channel'].sudo().browse(int(post.get('Course_details')))
        expected_revenue = course_revenue.product_id.lst_price

        lead = request.env['crm.lead'].sudo().create({
            'name': f"Admission Enquiry - {admission_data.get('name', '')}",
            'partner_id': partner.id,
            'contact_name': admission_data.get('name'),
            'email_from': admission_data.get('email'),
            'phone': admission_data.get('phone'),
            'course_id': post.get('Course_details'),
            'expected_revenue': expected_revenue,
            'description': (
                "Course Admission Enquiry\n\n"
                f"Qualification: {admission_data.get('qualification', '')}\n"
                f"Institution: {admission_data.get('institution_name', '')}\n"
                f"Address: {admission_data.get('institution_address', '')}\n"
            ),
        })
        _logger.info("Created admission enquiry lead with ID: %s", lead.id)
        return super(WebsiteSaleController, self).shop_address_submit(**post)

    @http.route(['/shop/address'], type='http', auth="public", website=True, sitemap=False)
    def shop_address(self, **kw):
        response = super().shop_address(**kw)
        courses = request.env['slide.channel'].sudo().search([])
        response.qcontext.update({
            'courses': courses,
        })
        return response
