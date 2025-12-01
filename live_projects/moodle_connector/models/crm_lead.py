from odoo import models, fields
import requests, uuid

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    payment_link = fields.Char(string="Payment Link")
    paypal_order_id = fields.Char("PayPal Order ID", readonly=True)
    paypal_temp_token = fields.Char("Temporary Token", readonly=True)
    course_id : fields.Many2one = fields.Many2one('slide.channel', string="Course Applied For", help="The course for which the lead has applied")

    certificates = fields.Binary(string="Certificates")
    government_id = fields.Binary(string="Government ID")
    photo = fields.Binary(string="Photo Upload")
    electronic_signature = fields.Binary(string="Signature")

    academic_transcript = fields.Many2many('ir.attachment','crm_lead_academic_transcript_rel','lead_id', 'attachment_id',string="Academic Transcript(s)")
    recommendation_letter = fields.Many2many('ir.attachment','crm_lead_recommendation_letter_rel','lead_id', 'attachment_id',string="Recommendation Letter(s)")
    personal_statement = fields.Many2many('ir.attachment','crm_lead_personal_statement_rel','lead_id', 'attachment_id',string="Personal Statement(s)")
    proof_upload = fields.Many2many('ir.attachment','crm_lead_proof_upload_rel','lead_id', 'attachment_id',string="Proof of Document(s)")
    transcript_upload = fields.Many2many('ir.attachment','crm_lead_transcript_upload_rel','lead_id', 'attachment_id',string="Transcript Upload(s)")

    def get_paypal_access_token(self, client_id, client_secret):
        url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
        headers = {
            "Accept": "application/json",
            "Accept-Language": "en_US",
        }
        data = {"grant_type": "client_credentials"}
        auth = (client_id, client_secret)

        response = requests.post(url, headers=headers, data=data, auth=auth)
        response.raise_for_status()
        return response.json()['access_token']

    def create_paypal_order(self, amount, lead_id, client_id, client_secret):
        """
        Create a PayPal order and return the approval URL.
        Uses a unique temp_token for internal tracking to avoid PayPal token conflicts.
        """
        access_token = self.get_paypal_access_token(client_id, client_secret)
        url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"

        web_base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        temp_token = uuid.uuid4().hex

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }

        data = {
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "amount": {
                        "currency_code": "USD",
                        "value": str(amount)
                    },
                    "custom_id": str(lead_id),
                    "description": f"Payment for {self.env['crm.lead'].browse(lead_id).name or 'Course'}"
                }
            ],
            "application_context": {
                "return_url": f"{web_base_url}/paypal/success?lead_id={lead_id}&temp_token={temp_token}",
                "cancel_url": f"{web_base_url}/paypal/cancel?lead_id={lead_id}"
            }
        }

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()

        paypal_order_id = result.get('id')
        approval_url = next(link['href'] for link in result['links'] if link['rel'] == 'approve')

        return approval_url

    def action_approve_lead(self):
        paypal_orm = self.env['payment.provider'].search([('code', '=', 'paypal')], limit=1)
        client_id = paypal_orm.paypal_client_id
        client_secret = paypal_orm.paypal_client_secret
        template = self.env.ref('moodle_connector.email_template_approve_lead', raise_if_not_found=False)
        approved_stage = self.env['crm.stage'].search([('name', '=', 'Qualified')], limit=1)
        if not approved_stage:
            approved_stage = self.env['crm.stage'].create({'name': 'Qualified', 'sequence': 3})
        TAX_PERCENT = 15.0
        for lead in self:
            if not lead.email_from:
                raise ValueError("Email address is missing for this lead.")
            base_amount = lead.expected_revenue or 0.0
            tax_amount = base_amount * (TAX_PERCENT / 100)
            amount = round(base_amount + tax_amount, 2)
            lead.payment_link = self.create_paypal_order(amount, lead.id, client_id, client_secret)

            if template:
                template.sudo().send_mail(lead.id, force_send=True)

                lead.write({'stage_id': approved_stage.id})
                lead.message_post(body=f"✅ Payment link sent: <a href='{lead.payment_link}'>{lead.payment_link}</a>")

        return True

    def action_reject_lead(self):
        template = self.env.ref('moodle_connector.email_template_reject_lead', raise_if_not_found=False)
        rejected_stage = self.env['crm.stage'].search([('name', '=', 'Rejected')], limit=1)
        if not rejected_stage:
            rejected_stage = self.env['crm.stage'].create({'name': 'Rejected', 'sequence': 5})
        for lead in self:
            if template:
                mail_id = template.sudo().send_mail(lead.id, force_send=True)
                if mail_id and rejected_stage:
                    lead.stage_id = rejected_stage
        return True



