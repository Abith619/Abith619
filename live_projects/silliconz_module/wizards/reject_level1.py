from odoo import models, fields

class RejectLvl1Wizard(models.TransientModel):
    _name = 'reject.lvl1.wizard'
    _description = 'Reject Level 1 Wizard'

    sale_id = fields.Many2one('sale.order', string="Sale Order")
    reason = fields.Text(string="Rejection Reason", required=True)

    def action_confirm_reject(self):
        self.sale_id.write({
            'state': 'rejected_lvl1',
            'rejection_reason': self.reason
        })
        self.sale_id._send_notification_email('silliconz_module.email_template_reject_lvl1')
        return {'type': 'ir.actions.act_window_close'}