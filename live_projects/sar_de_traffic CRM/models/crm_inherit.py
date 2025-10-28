from odoo import models, fields, _, api

class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    estimate_ids : fields.Many2many = fields.Many2many('quotation.estimate', 'lead_id', string="Estimates")
    estimate_count = fields.Integer(string="Estimate Count", compute="_compute_estimate_count")
    project_id : fields.Many2one = fields.Many2one('project.project', string='Projects')

    @api.depends('estimate_ids')
    def _compute_estimate_count(self):
        Estimate = self.env['quotation.estimate']
        for lead in self:
            lead.estimate_count = Estimate.search_count([('lead_id', '=', lead.id)])

    def action_view_estimates(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Estimates'),
            'res_model': 'quotation.estimate',
            'view_mode': 'list,form',
            'domain': [('lead_id', '=', self.id)],
            'context': {'default_lead_id': self.id},

        }

    def action_new_estimate(self):
        self.ensure_one()
        new_estimate = self.env['quotation.estimate'].create({
            'customer_id': self.partner_id.id,
            'date_from': fields.Date.today(),
            'amount_total': self.expected_revenue,
            'lead_id': self.id,
        })

        return {
            'type': 'ir.actions.act_window',
            'name': _('Quotation Estimate'),
            'res_model': 'quotation.estimate',
            'view_mode': 'form',
            'res_id': new_estimate.id,
            'target': 'current',
        }
