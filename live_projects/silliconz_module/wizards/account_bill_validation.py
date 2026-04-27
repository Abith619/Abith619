from odoo import models, fields
# import logging
# _logger = logging.getLogger(__name__)

class BillValidationWizard(models.TransientModel):
    _name = 'bill.validation.wizard'
    _description = 'Bill Validation Wizard'

    move_id = fields.Many2one('account.move', required=True)
    message = fields.Text(string="Mismatches", readonly=True)

    def action_validate(self):
        self.ensure_one()
        # _logger.info("purchase_id: %s", self.move_id.purchase_id)
        # _logger.info("PO from lines: %s", self.move_id.line_ids.mapped('purchase_line_id.order_id'))
        purchase_orders = self.move_id.line_ids.mapped('purchase_line_id.order_id')
        purchase_orders = purchase_orders.filtered(lambda p: p)
        return purchase_orders.action_amend_order()

    def action_cancel(self):
        return {'type': 'ir.actions.act_window_close'}
