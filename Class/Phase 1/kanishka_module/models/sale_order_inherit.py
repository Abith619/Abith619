from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    def send_mail(self):
        # Fetch the mail template by its ID
        for order in self:
            template = self.env['mail.template'].browse(self.env.ref('custom_module.email_template_sale_order').id)
        # Ensure the template exists
        if template:
            # Send the email using the template
            template.send_mail(self.id, force_send=True)