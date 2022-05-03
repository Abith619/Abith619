import string
from odoo import models, fields, api, _

class medical_directions(models.Model):
    _name = 'medical.doctor'
    _rec_name = 'doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    doctor = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string="Doctor" ,track_visibility='always')
    age=fields.Char(string='Age')
    address = fields.Char(string="Address")
    marital_status = fields.Selection([('s','Single'),('m','Married'),('w','Widowed'),('d','Divorced'),('x','Seperated')],string='Marital Status')
    height = fields.Float(string="Height in Cms")
    weight = fields.Float(string="Weight in Kgs")
    bp = fields.Float(string='BP in mmHg')
    patient_timing=fields.Datetime(string='Patient Timing')
    treatment = fields.Char(string="Treatment for")
    ailments=fields.Char(string='Ailments')

    patient = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient",required=True)
    diagnosis = fields.Text(string='Diagnosis')
    since = fields.Integer(string='Since')
    sign_symptoms = fields.Text(string="Signs/Symptoms")
    history = fields.Text(string ="History")
    sex = fields.Selection([('m', 'Male'),('f', 'Female')],  string ="Sex", required= True)
    prescription_date= fields.Datetime(string='Date', default=fields.Datetime.now())
    name = fields.Char('Prescription ID')

    def action_send_email(self):
        self.ensure_one()
        compose_form_id = False
        return {
            'name': 'Compose Email',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            }


#           prescription
    def prescription_button(self):
            return{
        'name': "Paid ",
        'type': 'ir.actions.act_window',
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'medical.prescription.order',
        'view_id': self.env.ref('basic_hms.medical_prescription_order_form_view').id,
        'context': {
#   'default_name_id': self.patient.id,
            'default_doctor_id': self.doctor.id,
            'default_prescription_date': self.prescription_date,
            'default_patient_id': self.patient.id,
            'default_age': self.age,
            'default_sex': self.sex,
        },
        'target': 'new'
    }

#scan/test:
    def scan_button(self):
            return{
        'name': "Scan/Tests",
        'type': 'ir.actions.act_window',
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'medical.patient.lab.test',
        'context': {
            # 'default_name_id': self.patient.id,
            'default_doctor_id': self.doctor.id,
            # 'default_prescription_date': self.prescription_date,
            'default_patient_id': self.patient.id,
            # 'default_age': self.age,
            # 'default_sex': self.sex,
        },
        'target': 'new'
    }


#Smart Button
    @api.multi
    def patient_prescription(self, cr,  context=None):
        return {
    'name': "Patient Prescription",
    'domain':[('patient_id', '=', self.patient.id)],
    'view_mode': 'tree,form',
    'res_model': 'medical.prescription.order',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }

#Count in Smart Button
    def patient_count(self):
        count2 = self.env['medical.prescription.order'].search_count([('patient_id', '=', self.patient.id)])
        self.patients= count2

    patients = fields.Integer(compute='patient_count',string="Prescriptions")


#sacns and tests
    @api.multi
    def scans_prescription(self, cr,  context=None):
        return {
    'name': "Scans tests",
    'domain':[('patient_id', '=', self.patient.id)],
    'view_mode': 'tree,form',
    'res_model': 'medical.patient.lab.test',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }
#      Count in Smart Button
    def scan_count(self):
        count1 = self.env['medical.patient.lab.test'].search_count([('patient_id', '=', self.patient.id)])
        self.scans_tests= count1

    scans_tests = fields.Integer(compute='scan_count',string="Scans/Tests")


#       one2many
    pervious_medication = fields.One2many('pervious.medication','signs',string="Pervious Medication")
    surgery_history = fields.Char(string ="Surgery History")
    family_history = fields.Char(string ="Family History")

    history_surgery = fields.One2many('patient.surgery', 'doc', string="History of Surgery")

    history_family = fields.One2many('patient.family','pati',string="History of Family")

    lab_reports = fields.Many2one('medical.lab',string ="Lab Reports")
    scan_reports = fields.Many2one('medical.lab',string ="Scan Reports")
    diet= fields.Char(string="Diet")
    image = fields.Binary()
    videos = fields.Binary(string ="Videos")
    notes = fields.Text(string="Special Notes To Self/Other Staffs")


class Perviousmedication(models.Model):
    _name='pervious.medication'

    diseases= fields.Many2one('medical.pathology',string="Diseases")
    signs = fields.Many2one('medical.doctor',string="Signs")
    medication_from = fields.Date(string="Mediaction From")
    medication_to = fields.Date(string="Mediaction to")
    medicine = fields.Char(string="Medicines")
    diets = fields.Char(string="Diets")

class Patientsurgery(models.Model):
    _name = 'patient.surgery'


    doc = fields.Many2one('medical.doctor',string="Doctor")
    surgery_date = fields.Date(string="Surgery Date")
    surgery_type = fields.Many2one('medical.pathology',string="Surgery Type")
    surgery_reason = fields.Char(string="Surgery Reason")
    surgery_status = fields.Selection([('done','Done'),('cancel','Cancel')],string="Surgery Status")
    surgery_notes = fields.Text(string="Surgery Notes")
    
class patient_family(models.Model):
    _name = 'patient.family'

    pati = fields.Char('medical.doctor')
    name_f = fields.Char(string="Name")
    doct = fields.Char(string="Realtionship")
    family_date = fields.Char(string="Contact Number")
    family_type = fields.Many2one('medical.pathology',string="Family Type")
    family_reason = fields.Char(string="Family Disease Reason")
    family_status = fields.Selection([('done','Done'),('cancel','Cancel')],string="Family Status")
    family_notes = fields.Text(string="Family Notes")