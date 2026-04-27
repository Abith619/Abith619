from odoo import models, fields, api, _
from odoo.exceptions import UserError


class CustomerApplicationRejectWizard(models.TransientModel):
    _name = 'customer.application.reject.wizard'
    _description = 'Customer Application Rejection Wizard'

    application_id = fields.Many2one('customer.application', string='Application', required=True)
    reason = fields.Text(string='Rejection Reason', required=True)

    def action_confirm_reject(self):
        self.ensure_one()
        app = self.application_id
        if app.state != 'submitted':
            raise UserError(_("Only submitted applications can be rejected."))
        app.write({
            'state': 'rejected',
            'rejection_reason': self.reason,
        })
        app.message_post(
            body=_("Application rejected by %s.\n\nReason: %s", self.env.user.name, self.reason),
            subtype_xmlid='mail.mt_note',
        )
        return {'type': 'ir.actions.act_window_close'}
