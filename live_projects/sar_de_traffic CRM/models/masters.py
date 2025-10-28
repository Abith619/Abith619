from odoo import models, fields

class MakeMasters(models.Model):
    _name = 'make.master'
    _description = "Make Masters"

    name = fields.Char("Name", required=True)
