from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def send_mail(self):
        for order in self:
            template = self.env['mail.template'].browse(
                self.env.ref('basic_learning.mail_template_sale_order').id
            )
            if template:
                template.send_mail(order.id, force_send=True)
