from odoo import models, fields, api, _

class medical_directions(models.Model):
    _name = 'medical.doctor'
    _rec_name = 'doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    doctor = fields.Many2one('medical.physician',string="Doctor" ,required=True)
    patient = fields.Many2one('medical.patient',string="Patient",required=True)
    diagnosis = fields.Many2one('medical.test_type',string='Diagnosis')
    since = fields.Integer(string='Since')
    sign_symptoms = fields.Char(string="Signs/Symptoms")
    history = fields.Char(string ="History")

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

#one2many
    pervious_medication = fields.One2many('pervious.medication','signs',string="Pervious Medication")
    surgery_history = fields.Char(string ="Surgery History")
    family_history = fields.Char(string ="Family History")

    history_surgery = fields.One2many('patient.surgery', 'doc', string="History of Surgery")

    history_family = fields.One2many('patient.family','pati',string="History of Family")

    lab_reports = fields.Char(string ="Lab Reports")
    scan_reports = fields.Char(string ="Scan Reports")
    diet= fields.Char(string="Diet")
    image = fields.Binary()
    videos = fields.Char(string ="Videos")
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

    pat = fields.Many2one('medical.patient',string="Patient")
    doc = fields.Many2one('medical.doctor',string="Doctor")
    surgery_date = fields.Date(string="Surgery Date")
    surgery_type = fields.Many2one('medical.pathology',string="Surgery Type")
    surgery_reason = fields.Char(string="Surgery Reason")
    surgery_status = fields.Selection([('done','Done'),('cancel','Cancel')],string="Surgery Status")
    surgery_notes = fields.Text(string="Surgery Notes")
    
class patient_family(models.Model):
    _name = 'patient.family'

    pati = fields.Many2one('medical.patient',string="Patient")
    doct = fields.Many2one('medical.physician',string="Doctor")
    family_date = fields.Date(string="Family Date")
    family_type = fields.Many2one('medical.pathology',string="Family Type")
    family_reason = fields.Char(string="Family Disease Reason")
    family_status = fields.Selection([('done','Done'),('cancel','Cancel')],string="Family Status")
    family_notes = fields.Text(string="Family Notes")