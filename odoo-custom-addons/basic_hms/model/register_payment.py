from odoo import api, fields, models, _

class RegisterPayment(models.Model):
    _name = 'register.payment'


    patient_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name", required= True)  
    date=fields.Datetime(string="Date Of Payment")
    amount = fields.Float(string="Fee Amount")
