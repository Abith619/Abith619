from odoo import models, fields, _
from odoo.exceptions import ValidationError, UserError
import requests, re

class WhatsappBulkMessage(models.Model):
    _name = 'whatsapp.bulk.message'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'WhatsApp Bulk Message'

    name = fields.Char(string='Name', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('error', 'Error')
    ], default='draft', string='Status')

    whatsapp_account : fields.Many2one = fields.Many2one('whatsapp.account', string='WhatsApp Account', required=True, help='Select the WhatsApp account to use for sending messages')

    template_id : fields.Many2one = fields.Many2one('whatsapp.template', string='Template',  help='Select a template to use for the message' )
    is_published = fields.Boolean(string='Is Published', default=False, help='Messages will only be sent if published')

    partner_ids : fields.Many2one = fields.Many2one('whatsapp.bulk.line', string='Relation')

    recipient_ids : fields.One2many = fields.One2many(
        'whatsapp.bulk.line', 'bulk_rec_id', string='Recipients',
        help='List of recipients for the bulk message'
    )

    def action_send_bulk_message(self):
        if self.is_published == False:
            raise UserError("Please Enable the message before sending.")
        if not self.template_id:
            raise ValidationError("Please select a WhatsApp template.")
        if not self.recipient_ids:
            raise ValidationError("Please select at least one recipient.")

        url = f"https://graph.facebook.com/v22.0/{self.whatsapp_account.phone_uid}/messages"
        headers = {
            "Authorization": f"Bearer {self.whatsapp_account.token}",
            "Content-Type": "application/json"
        }

        responses = []

        for recipient in self.recipient_ids:
            if recipient.number:
                cleaned_number = re.sub(r'\D', '', recipient.number)
                payload = {
                    "messaging_product": "whatsapp",
                    "recipient_type": "individual",
                    "to": cleaned_number,
                    "type": "template",
                    "template": {
                        "name": self.template_id.template_name,
                        "language": {"code": "en"},
                    }
                }

                try:
                    response = requests.post(url, json=payload, headers=headers)
                    data = response.json()
                except Exception as e:
                    data = {"error": f"Exception occurred: {str(e)}"}
                    print(f"Exception for {cleaned_number}: {data}")
                    raise ValidationError(f"Error sending message to {recipient.number}: {str(e)}")

                print(f"Response for {cleaned_number}: {data}")
                responses.append(data)

                if response.status_code == 200:
                    self.env['whatsapp.message'].create({
                        'wa_account_id': self.whatsapp_account.id,
                        'mobile_number': cleaned_number,
                        'wa_template_id': self.template_id.id,
                        'state': 'sent',
                        'create_uid': self.env.user.id,
                        'create_date': fields.Datetime.now(),
                    })
                    self.state = 'sent'
                    self.message_post(
                        body=f"WhatsApp message sent using template {self.template_id.template_name}.",
                        message_type='comment',
                        subtype_xmlid='mail.mt_note',
                    )
                else:
                    error_message = data.get("error", {}).get("message", response.text)
                    self.state = 'error'
                    raise ValidationError(f"Failed to send message to {recipient.number}: {error_message}")

        return responses


class WhatsappBulkLine(models.Model):
    _name = 'whatsapp.bulk.line'
    _description = 'WhatsApp Bulk Message Line'

    name = fields.Char(string='Name', required=True)
    number = fields.Char(string='Number', required=True, widget='phone', help='Recipient phone number')
    email = fields.Char(string='Email', help='Recipient email address')
    bulk_rec_id : fields.Many2one = fields.Many2one(
        'whatsapp.bulk.message', string='Bulk Message',
        help='Reference to the bulk message this line belongs to'
    )
