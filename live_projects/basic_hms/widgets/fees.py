from odoo import models, fields, api

class selectplan(models.TransientModel):
    _name = 'select.plan'
    

    plan = fields.Many2one("medical.patient",string='Fees',required=True)


    @api.multi
    def added(self):
        if self.env.context.get('active_model') == 'medical.patient':
            active_model_id = self.env.context.get('active_id')
            hr_obj = self.env['medical.patient'].search([('id','=',active_model_id)])
            for record in hr_obj:
                record.write({
                        'plans_offered':self.plan.id,
                    })