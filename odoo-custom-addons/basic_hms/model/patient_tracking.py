from odoo import api, fields, models, _

class patient_tracking(models.Model):
    _name = 'patient.tracking'

    name = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string='Patient Name', required = True)
    lab_status = fields.Char(string='Lab Status')
    precription_status = fields.Char(string='Prescription Status')
    appoinment_status = fields.Char(string='Appointment Status')
    billing_status= fields.Char(string='Billing Status')

    

