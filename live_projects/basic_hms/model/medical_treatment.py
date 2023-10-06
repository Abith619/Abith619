from odoo import models, fields, api

class ManyTreatment(models.Model):
    
    _name='medical.treatments'

    name = fields.Char(string="Treatment")