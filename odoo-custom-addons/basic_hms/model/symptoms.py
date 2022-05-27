from odoo import api, fields, models

class medical_pathology_symptoms(models.Model):
    _name='medical.symptoms'
    _rec_name='name'



    

    name = fields.Char(string="Symptom Name",required=True)
    diseases=fields.Many2one('medical.pathology',string="Diseases")