from odoo import models

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    def send(self):
        for order in self:
            template = self.env['mail.template'].browse(self.env.ref('custom_module.mail_template_sale_order').id)
            template.send_mail(order.id, force_send=True)