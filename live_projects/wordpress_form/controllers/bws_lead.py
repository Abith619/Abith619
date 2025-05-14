from odoo.http import request, Controller, route
from odoo.exceptions import ValidationError

class BWSLeadController(Controller):

    @route('/api/bws_lead', type='json', auth='public', csrf=False, website=True, cors="*")
    def create_bws_lead(self):
        data = request.get_json_data()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        company = data.get('company')
        message = data.get('message')
        phone = data.get('phone' if 'phone' in data else '')
        form_from = data.get('form_from')

        try:
            lead = request.env['crm.lead'].sudo().create({
                'name': f"{first_name} {last_name}",
                'email_from': email,
                'partner_name': company,
                'description': message,
                'x_form_from': form_from,
                'phone': phone,
            })
            return {
                "id": lead.id,
                "status": "created",
                "message": "Lead successfully created"
            }

        except Exception as e:
            return {
                "error": "Lead creation failed",
                "details": str(e)
            }
