from odoo import api, fields, models

class res_partner(models.Model):
    _name = 'prescribe.diet'

    name = fields.Many2one('set.diets', string="diets",required = True)
    pre_diet_line = fields.One2many('prescribe.diet.line','name',string="Diet Advisied")
    patient_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name",required=True,readonly=True)
    dates=fields.Date(string='Date',default=fields.Datetime.now(),readonly=True)



    @api.onchange('name')
    def onchange_task(self):
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.name.diet_line:

                val={
                    'start_time': line.start_time,
                    'meridiem':line.meridiem,
                    'diet':line.diet,
                }
                lines.append((0,0,val))
            rec.pre_diet_line=lines


class PrescribeDietAssign(models.Model):
    _name='prescribe.diet.line'


    name=fields.Many2one('prescribe.diet')
    start_time = fields.Float(string="Time")
    meridiem = fields.Selection([('am',"Am"),('pm',"Pm")],string="Am/Pm")
    diet = fields.Char(string="Diet Advised")



