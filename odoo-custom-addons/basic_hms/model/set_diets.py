from odoo import api, fields, models, _

class SetDiets(models.Model):
    _name = 'set.diets'

    name = fields.Char('Name', required = True)
    # code = fields.Char('Code')
    diet_line = fields.One2many('set.diet.line','name',string="Diet Advisied")

class DietAssign(models.Model):
    _name='set.diet.line'

    name=fields.Many2one('set.diets')
    start_time = fields.Float(string="Time")
    meridiem = fields.Selection([('am',"Am"),('pm',"Pm")],string="Am/Pm")
    diet = fields.Char(string="Diet Advised")


class diet(models.Model):
    _name='set.diet.lines'
