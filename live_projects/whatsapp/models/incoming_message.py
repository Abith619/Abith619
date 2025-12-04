from odoo import models, fields, api, _

class WhatsappIncomingMessage(models.Model):
    _name = 'whatsapp.incoming.message'
    _description = 'WhatsApp Incoming Message'

    wa_account_id = fields.Many2one('whatsapp.account', string='WhatsApp Account')
    message = fields.Char(string='Message')
    sender = fields.Char(string='Sender')
    content = fields.Text(string='Message Content')
    timestamp = fields.Datetime(string='Received At', default=fields.Datetime.now)

    @api.model_create_multi
    def create(self, vals_list):
        """Create a new incoming message from webhook data."""
        return super(WhatsappIncomingMessage, self).create(vals_list)
