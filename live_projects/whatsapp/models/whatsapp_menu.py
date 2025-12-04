import requests, re
from odoo.exceptions import ValidationError
from odoo import models, fields, api, _

class WhatsappEnterpriseCustom(models.Model):
    _inherit = 'mailing.list'

    api_template: fields.Many2one = fields.Many2one('whatsapp.template', string='Message Template', required=True)
    recieptient_group: fields.Many2one = fields.Many2one('mailing.list', string='Recipient Group')
    related_recieptents: fields.Many2many = fields.Many2many('mailing.contact', string="Related Recipients", related='recieptient_group.contact_ids')
    wa_channel_count = fields.Integer(string='WhatsApp Channel Count')

    def action_open_partner_wa_channels(self):
        return {
            'name': _('WhatsApp Chats'),
            'type': 'ir.actions.act_window',
            'domain': [('channel_type', '=', 'whatsapp'), ('channel_partner_ids', 'in', self.ids)],
            'res_model': 'discuss.channel',
            'views': [(self.env.ref('whatsapp.discuss_channel_view_list_whatsapp').id, 'list')],
        }
