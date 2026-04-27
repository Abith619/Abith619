from odoo import models, fields
from odoo.exceptions import UserError

class CancelLvl2Wizard(models.TransientModel):
    _name = 'cancel.lvl2.wizard'
    _description = 'Cancel Level 2 Wizard'

    sale_id = fields.Many2one('sale.order', string="Sale Order")
    reason = fields.Text(string="Cancel Reason", required=True)

    def action_confirm_cancel(self):
        if self.sale_id.state != 'submitted_lvl2':
            raise UserError("Order must be Submitted Level 2.")

        # Save reason + cancel
        self.sale_id.write({
            'cancel_reason': self.reason
        })
        

        return self.sale_id.action_cancel()