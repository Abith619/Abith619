from odoo import models, fields, api

class habitfor(models.Model):
    _name='habit.for'


    name= fields.Char(string='Habit Name',required=True)