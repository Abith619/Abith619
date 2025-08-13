from odoo import models, fields, _

class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    def action_new_estimate(self):
        self.ensure_one()
        self.env['quotation.estimate'].create({
            'customer_id': self.partner_id.id,
            'date': fields.Date.today(),
            'amount_total': self.expected_revenue,
        })
