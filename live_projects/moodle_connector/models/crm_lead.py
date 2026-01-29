from odoo import models, fields,api
from odoo.exceptions import ValidationError
import requests, uuid

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    student_id = fields.Many2one(
        'student.master',
        string="Student"
    )
    payment_link = fields.Char(string="Payment Link")
    unique_token = fields.Char("Unique Token for Checkout")
    paypal_order_id = fields.Char("PayPal Order ID", readonly=True)
    paypal_temp_token = fields.Char("Temporary Token", readonly=True)
    course_id : fields.Many2one = fields.Many2one('slide.channel', string="Course Applied For", help="The course for which the lead has applied")
    certificates = fields.Binary(string="Certificates")
    government_id = fields.Binary(string="Government ID")
    photo = fields.Binary(string="Photo Upload")
    electronic_signature=fields.Binary(string="Signature")
    payment_proof = fields.Binary("Payment Proof")
    payment_proof_filename = fields.Char("Proof File Name")
    previous_lead_id = fields.Many2one('crm.lead',string="Previous Lead (Re-admission)")
    payment_status = fields.Selection([('not_paid', 'Not Paid'),('paid', 'Paid')],string="Payment Status",default='not_paid')
    academic_transcript = fields.Many2many('ir.attachment','crm_lead_academic_transcript_rel','lead_id', 'attachment_id',string="Academic Transcript(s)")
    recommendation_letter = fields.Many2many('ir.attachment','crm_lead_recommendation_letter_rel','lead_id', 'attachment_id',string="Recommendation Letter(s)")
    personal_statement = fields.Many2many('ir.attachment','crm_lead_personal_statement_rel','lead_id', 'attachment_id',string="Personal Statement(s)")
    proof_upload = fields.Many2many('ir.attachment','crm_lead_proof_upload_rel','lead_id', 'attachment_id',string="Proof of Document(s)")
    transcript_upload = fields.Many2many('ir.attachment','crm_lead_transcript_upload_rel','lead_id', 'attachment_id',string="Transcript Upload(s)")
    category_ids = fields.Many2many('slide.channel.tag',string="Course Categories",compute="_compute_category_ids",store=True,readonly=True)
    @api.depends('course_id')
    def _compute_category_ids(self):
        for lead in self:
            if lead.course_id:
                lead.category_ids = lead.course_id.tag_ids
            else:
                lead.category_ids = False

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
    
    is_approved = fields.Boolean(compute="_compute_is_approved")
    @api.depends('stage_id')
    def _compute_is_approved(self):
        for rec in self:  
            if rec.stage_id.name != "New":
                rec.is_approved = True
            else:
                rec.is_approved = False
    is_rejected = fields.Boolean(compute="_compute_is_rejected")
    @api.depends('stage_id')
    def _compute_is_rejected(self):
        for rec in self:  
            if rec.stage_id.name == "Rejected":
                rec.is_rejected = True
            else:
                rec.is_rejected = False
        
    is_reset = fields.Boolean(compute="_compute_is_reset")
    @api.depends('stage_id')
    def _compute_is_reset(self):
        for rec in self:  
            if rec.stage_id.name == "New":
                rec.is_reset = True
            else:
                rec.is_reset = False
        
    def action_reset_lead(self):
        reset_stage = self.env['crm.stage'].search([('name', '=', 'New')], limit=1)
        if not reset_stage:
            reset_stage = self.env['crm.stage'].create({'name': 'New', 'sequence': 1})
        for lead in self:
            lead.stage_id = reset_stage
        return True


    def action_approve_lead(self):
        template = self.env.ref('moodle_connector.email_template_approve_lead', raise_if_not_found=False)        
        for lead in self:
            company_email = lead.company_id.email
            if not company_email:
                raise ValidationError("Your company does not have an email configured")
            if not lead.email_from:
                raise ValidationError("Email address is missing for this lead.")
            if not lead.partner_id:
                raise ValidationError("Assign a Customer to this Lead first.")
            if not lead.course_id:
                raise ValidationError("Course is required to checkout.")
            product = lead.course_id.product_id
            if not product:
                raise ValidationError("Selected Course has no Product linked. Please assign a Product.")            
            web_base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            unique_token = uuid.uuid4().hex
            lead.unique_token = unique_token
            lead.payment_link = f"{web_base_url}/lead/checkout?lead_id={lead.id}&token={unique_token}"
            checkout_stage = self.env['crm.stage'].search([('name', '=', 'Approved')], limit=1)
            if not checkout_stage:
                    checkout_stage = self.env['crm.stage'].create({
                        'name': 'Approved',
                        'sequence': 1,
                    })
            lead.stage_id = checkout_stage.id
            if template:
                mail_id = template.sudo().send_mail(lead.id, force_send=True)
                mail = self.env['mail.mail'].sudo().browse(mail_id)
                if mail.exists():
                    if mail.state == 'sent':
                        lead.message_post(body="Email sent successfully")
                    elif mail.state == 'exception':
                        lead.message_post(body=f"Email delivery failed: {mail.failure_reason or 'Unknown error'}")
                    else:
                        lead.message_post(body=f"Email status: {mail.state}")
                else:
                    lead.message_post(body="Email sent")
                    
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
    

# class CrmStage(models.Model):
#     _inherit = 'crm.stage'

#     is_approved = fields.Boolean(string="Approved Stage")

    
