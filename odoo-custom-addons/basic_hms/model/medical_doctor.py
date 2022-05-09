
from inspect import signature
from odoo import api, fields, models, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta 


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
    treatment = fields.Char(string="Treatment Adviced")
    ailments=fields.Many2one('medical.pathology',string="Current Ailments")

    patient = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient",required=True)
    diagnosis = fields.Text(string='Initial Diagnosis')
    final_diagnosis =  fields.Text(string='Final Diagnosis')
    since = fields.Integer(string='Since')
    sign_symptoms = fields.Text(string="Signs/Symptoms")
    history = fields.Text(string ="History")
    sex = fields.Selection([('m', 'Male'),('f', 'Female')],  string ="Sex", required= True)
    prescription_date= fields.Datetime(string='Date', default=fields.Datetime.now())
    name = fields.Char('Prescription ID')

#new fields 
    father_name=fields.Char(string="Father/Husband/Guardian")
    image = fields.Binary()
    videos = fields.Binary(string ="Videos")
    habits=fields.Selection([('smoking','Smoking'),('alcohol','Alcohol'),('pan','PAN')],string='Habits')
    blood = fields.Boolean(string="Blood")
    urine=fields.Boolean(string="Urine")
    pulse=fields.Boolean(string="Pulse")
    ecg=fields.Boolean(string="ECG")
    echo=fields.Boolean(string='Echo')
    mri_ct=fields.Boolean(string='MRI/CT')
    x_ray=fields.Boolean(string='X-Ray')
    deaa=fields.Boolean(string='DEAA')
    via_vili=fields.Boolean(string='VIA/VILI')
    hosteler=fields.Boolean(string='Hosteler')
    out_side_food=fields.Boolean(string='OutSide Food')
    control=fields.Boolean(string='Control')
    veg=fields.Boolean(string='Veg')
    non_veg=fields.Boolean(string='Non-Veg')
    not_possible=fields.Boolean(string='Not Possible')
    moderate=fields.Boolean(string='Moderate')
    ok_for_all=fields.Boolean(string='Ok for All')
    occupation = fields.Char(string="Occupation")
    office_address = fields.Text(string="Office Address")

    cure=fields.Boolean(string='Cure')
    test_dose=fields.Boolean(string='Test Dose')
    control=fields.Boolean(string='Control')
    paliation=fields.Boolean(string='Paliation')
    chronic=fields.Boolean(string='Chronic')
    ng=fields.Boolean(string='NG')
    maintance=fields.Boolean(string='Maintance')
    nt=fields.Boolean(string='NT')
    serial_number = fields.Char(string="Patient ID", readonly=True, required=True, copy=False, default='New')
    phone_number=fields.Char(string="Contact Number")
    stages= fields.Selection([('draft',"Draft"),('done',"Done")])





#existing appoinment 

    # @api.onchange('patient')
    # def _existing_contact(self):
    #     if 




    @api.model
    def create(self, vals):
        vals['serial_number'] = self.env['ir.sequence'].next_by_code('medical.doctor') or 'EB'
        msgs_body = 'Ebook Created'
        for msgs in self:
            msgs.message_post(body=msgs_body)
        result = super(medical_directions, self).create(vals)
        return result

# prescription
    def prescription_button(self):
            return{
        'name': "Paid ",
        'type': 'ir.actions.act_window',
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'medical.prescription.order',
        'view_id': self.env.ref('basic_hms.medical_prescription_order_form_view').id,
        'context': {
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

            'default_doctor_id': self.doctor.id,

            'default_patient_id': self.patient.id,

        },
        'target': 'new'
    }


    def diet_for(self):
            select_plan = False
            return {
                'name': 'Diet For',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'view_type': 'form',
                'res_model': 'diet.for',
                'views': [(select_plan, 'form')],
                'view_id':self.env.ref('basic_hms.diet_form').id,
                'target': 'new',
            }

    def treatment_advised(self):
            select_plan = False
            return {
                'name': 'Treatment Advised',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'view_type': 'form',
                'res_model': 'treatment.for',
                'views': [(select_plan, 'form')],
                'view_id':self.env.ref('basic_hms.treatment_form').id,
                'target': 'new',
            }


#Smart Button
    # @api.model
    def patient_prescription(self):
        return {
    'name': "Patient Prescription",
    'domain':[('patient_id', '=', self.patient.id)],
    'view_mode': 'tree,form',
    'res_model': 'medical.prescription.order',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }
#      Count in Smart Button
    def patient_count(self):
        for sf in self :
            count2 = self.env['medical.prescription.order'].search_count([('patient_id', '=', sf.patient.id)])
            self.patients= count2

    patients = fields.Integer(compute='patient_count',string="Prescriptions")



#sacns and tests
    # @api.model
    def scans_prescription(self):
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
        self.sacns_tests= count1

    sacns_tests = fields.Integer(compute='scan_count',string="Scans/Tests")


    def document_button(self):
        return {
    'name': "Documents",
    # 'domain':[('patient_id', '=', self.patient.id)],
    'view_mode': 'tree,form',
    'res_model': 'ir.attachment',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }
#      Count in Smart Button




#one2many
    pervious_medication = fields.One2many('pervious.medication','signs',string="Pervious Medication")
    surgery_history = fields.Char(string ="Surgery History")
    family_history = fields.Char(string ="Family History")

    history_surgery = fields.One2many('patient.surgery', 'doc', string="History of Surgery")

    history_family = fields.One2many('patient.family','doct',string="History of Family")

    documents = fields.One2many('patient.document','docc',string="Documents")

    lab_reports = fields.Many2one('medical.lab',string ="Lab Reports")
    scan_reports = fields.Many2one('medical.lab',string ="Scan Reports")
    diet= fields.Char(string=" For Diet")
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
    doct = fields.Many2one('medical.doctor',string="Doctor")
    family_date = fields.Date(string="Family Date")
    family_type = fields.Many2one('medical.pathology',string="Family Type")
    family_reason = fields.Char(string="Family Disease Reason")
    family_status = fields.Selection([('done','Done'),('cancel','Cancel')],string="Family Status")
    family_notes = fields.Text(string="Family Notes")
    family_name = fields.Char(string="Family Name")
    realtionship = fields.Char(string="Realtionship")
    familyphone = fields.Integer(string="Phone")
    name_f = fields.Char(string="Name")

class documents(models.Model):
    _name ="patient.document"

    docc = fields.Many2one('medical.doctor',string="Doctor")
    report_name = fields.Char(string="Report Name")
    attachment = fields.Binary(string="Image/Video Attachment")
