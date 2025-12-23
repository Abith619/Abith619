from odoo import models, fields, api

class SendMessageWizard(models.TransientModel):
    _name = 'send.message.wizard'
    _description = 'Send Message Wizard'

    message = fields.Text("Message")

    def action_send(self):
        active_id = self.env.context.get('active_id')
        record = self.env['custom.uber'].browse(active_id)

        # Example action: update email field with message
        record.email = self.message
