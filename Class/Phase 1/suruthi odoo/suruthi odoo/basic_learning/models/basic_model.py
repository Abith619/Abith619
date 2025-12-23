from odoo import models, fields,api

class Business(models.Model):
    _name = 'basic.business'
    _description = 'Basic Business Report'

    partnername = fields.Char("Partner Name", required=True)
    phonenumber = fields.Char("Phone Number")
    email = fields.Char("Email")

    # Report print method (like your sir's code)
    def action_print_report(self):
        return self.env.ref('basics.action_business_report').report_action(self)

    @api.model
    def send_mail(self):
        for model in self:
            template = self.env['mail.template'].browse(self.env.ref('basic.learning.mail_template_sale_order').id)
            template.send_mail(model.id, force_send=True)
