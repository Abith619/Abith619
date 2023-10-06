from odoo import api, fields, models

class Assigned_Diet(models.Model):
    _name="assign.diet"

    name=fields.Char(string='Name')
    line1=fields.One2many("assign.diet.line",'name',string='Diet Advisied')

class Assign_diet_line(models.Model):
    _name='assign.diet.line'

    name=fields.Many2one("set.diets")

    wakeup=fields.Char(string="Morning")
    note=fields.Char('Notes')
