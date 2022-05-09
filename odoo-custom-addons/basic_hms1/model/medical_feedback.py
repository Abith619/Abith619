from odoo import fields, models

class medical_feedback(models.Model):
    _name = 'medical.feedback'
    _rec_name = 'name'

    # feedback = fields.Many2many(string="How you came to know about Daisy Health Care (p) Ltd.,?")
    name = fields.Char(string="Name",required = True)
