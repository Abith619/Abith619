from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import requests, re
import logging

_logger = logging.getLogger(__name__)

class WhatsappIncomingMessage(models.Model):
    _name = 'whatsapp.incoming.message'
    _description = 'WhatsApp Incoming Message'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'sender'

    wa_account_id : fields.Many2one = fields.Many2one('whatsapp.account', string='WhatsApp Account')
    message = fields.Char(string='Message')
    sender = fields.Char(string='Sender')
    content = fields.Text(string='Message Content')
    reply = fields.Text(string="Reply")
    timestamp = fields.Datetime(string='Received At', default=fields.Datetime.now)
    conversation_line_ids : fields.One2many = fields.One2many('whatsapp.conversation.line', 'incoming_message_id', string='Conversation Lines')

    @api.model_create_multi
    def create(self, vals_list):
        """Create a new incoming message from webhook data."""
        return super(WhatsappIncomingMessage, self).create(vals_list)

    def action_send_reply(self):
        whatsapp_account = self.env['whatsapp.account'].search([('phone_uid', '=', '581968055005402')], limit=1)
        url = f"https://graph.facebook.com/v22.0/{whatsapp_account.phone_uid}/messages"
        headers = {
            "Authorization": f"Bearer {whatsapp_account.token}",
            "Content-Type": "application/json"
        }
        if self.reply:
            cleaned_number = re.sub(r'\D', '', self.sender)
            payload = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": cleaned_number,
                "type": "text",
                "text": {
                    "body": self.reply,
                }
            }

            response = requests.post(url, json=payload, headers=headers)
            data = response.json()
            if response.status_code == 200:
                self.write({
                    'conversation_line_ids': [(0, 0, {
                        'message': self.reply,
                        'time_stamp': fields.Datetime.now(),
                        'message_type': 'sent',
                    })]
                })
                _logger.info(f"WhatsApp API response success for {self.sender}: {data}")
                mail_message_id = self.message_post(
                        body = self.reply,
                        message_type='comment',
                        subtype_xmlid='mail.mt_note',
                    )
                self.env['whatsapp.message'].create({
                        'wa_account_id': whatsapp_account.id,
                        'mobile_number': cleaned_number,
                        'state': 'sent',
                        'create_uid': self.env.user.id,
                        'create_date': fields.Datetime.now(),
                        'body': self.reply,
                        'mail_message_id': mail_message_id.id,
                    })
            else:
                error_message = data.get("error", {}).get("message", response.text)
                raise ValidationError(f"Failed to send message to {cleaned_number}: {error_message}")

class WhatsappConversationLines(models.Model):
    _name='whatsapp.conversation.line'
    _description='Message Conversation'

    incoming_message_id : fields.Many2one = fields.Many2one('whatsapp.incoming.message', string='Message')
    message = fields.Char(string='Message')
    time_stamp = fields.Datetime(string='Received At', default=fields.Datetime.now)
    message_type = fields.Selection([
        ('sent', 'Sent'),
        ('received', 'Received'),
    ], string='Type')
