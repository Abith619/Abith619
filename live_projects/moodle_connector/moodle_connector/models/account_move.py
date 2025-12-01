from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    lead_id = fields.Many2one('crm.lead', string="CRM Lead")

    def write(self, vals):
        res = super().write(vals)

        for invoice in self:
            if invoice.payment_state == 'paid' and invoice.lead_id:
                invoice.lead_id.payment_status = 'paid'

        return res

# from odoo import models, api, fields, _
# import logging

# _logger = logging.getLogger(__name__)

# class AccountMove(models.Model):
#     _inherit = 'account.move'

#     def post(self):
#         return super(AccountMove, self).post()

#     def _compute_payment_state(self):
#         res = super(AccountMove, self)._compute_payment_state()

#         for inv in self:
#             try:
#                 if inv.payment_state == 'paid':
#                     sale_orders = self.env['sale.order'].search([
#                         ('invoice_ids', 'in', [inv.id])
#                     ])

#                     for order in sale_orders:
#                         if order.lead_id:
#                             lead = order.lead_id.sudo()
#                             if getattr(lead, 'payment_status', '') != 'paid':
#                                 lead.write({'payment_status': 'paid'})
#                                 lead.message_post(
#                                     body=_("Invoice %s is paid — Lead marked as paid.") % inv.name
#                                 )

#             except Exception as e:
#                 _logger.exception(
#                     "Error updating lead from invoice %s: %s", inv.name, e
#                 )

#         return res
