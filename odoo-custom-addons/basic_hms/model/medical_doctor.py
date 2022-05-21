
from inspect import signature
from odoo import api, fields, models, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta 
import qrcode
import base64
from io import BytesIO


class medical_directions(models.Model):
    _name = 'medical.doctor'
    _rec_name = 'patient'
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
    opnumber =fields.Char(string="OP Number")
    patient = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name",required=True)
    since = fields.Integer(string='Since')
    sign_symptoms = fields.Many2many('medical.family.disease',string="Signs/Symptoms")
    history = fields.Text(string ="History")
    sex = fields.Selection([('m', 'Male'),('f', 'Female')],  string ="Sex", required= True)
    prescription_date= fields.Datetime(string='Date', default=fields.Datetime.now())
    name = fields.Char('Prescription ID')
    ailments=fields.Many2one('medical.pathology',string="Current Ailments")
    habbit=fields.One2many('medical.habits','doz',string="Habit")
    diet_fields=fields.One2many('diet.field','diet1',string='Diet')

    #one2many
    pervious_medication = fields.One2many('pervious.medication','diseases',string="Pervious Medication")
    surgery_history = fields.Char(string ="Surgery History")
    family_history = fields.Char(string ="Family History")

    ailments=fields.Many2one('medical.pathology',string="Current Ailments")

    green_agreement=fields.One2many('green.agreement','agreement',string="Green Agreement")
    
    history_surgery = fields.One2many('patient.surgery', 'doc', string="History of Surgery")

    history_family = fields.One2many('patient.family','doct',string="History of Family")

    documents = fields.One2many('patient.document','docc',string="Documents")

    treatment_initial=fields.One2many('treatment.form','treatment1',string='Treatment')

    

    lab_reports = fields.Many2one('medical.lab',string ="Lab Reports")
    scan_reports = fields.Many2one('medical.lab',string ="Scan Reports")
    diet= fields.Char(string=" For Diet")
    image = fields.Binary()
    videos = fields.Binary(string ="Videos")
    notes = fields.Text(string="Special Notes To Self/Other Staffs")

    image1=fields.Binary(string="Image")

    @api.onchange('height','weight')
    def _calculate_bmi(self):
        bmi = 0
        for rec in self:
            if rec.height and rec.weight:
                bmi = rec.weight/(rec.height/100)**2
            else:
                rec.bmi_value = 0.0
            if bmi <= 18.5:
                status = "Underweight"
            elif bmi >= 18.5 and bmi <= 25:
                status = "Normal"
            else:
                status = "Obesity"
            self.bmi_value = f"{bmi:.{2}f} {status}" 

    bmi_value= fields.Char(string="BMI")




# new fields 
    father_name=fields.Char(string="Father/Husband")
    image = fields.Binary()
    videos = fields.Binary(string ="Green Document")
    treat_for = fields.Selection([('rev','Reversable'),('main','Maintenance'),('tdo','Test Dose'),('cho','Chromic ')],string ="Treatment For")
    
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


    # qr_id=fields.Char('serial_number')
    serial_number = fields.Char(string="Patient ID", readonly=True,copy=False,required=True, default='Patient ID')
   
    phone_number=fields.Char(string="Contact Number")
    contact_number=fields.Char(string="Whatsapp Number")
    stages= fields.Selection([('draft',"New"),('done',"Done")])
    diagnosis = fields.Text(string='Initial Diagnosis')
    final_diagnosis =  fields.Text(string='Final Diagnosis')

    # def _get_default_stage(self):
        # self.qr_id=self.serial_number

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
            'default_height': self.height,
            'default_weight': self.weight,
            },
            'target': 'new'
            }

    # @api.multi
    # def button_prescription(self):
    #     select_plan = False
    #     return {
    #         'name': 'Medicine prescription',
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         'res_model': 'medical.prescription.order',
    #         'views': [(select_plan, 'form')],
    #         'view_id':self.env.ref('basic_hms.prescription_form').id,
    #         'target': 'new',
    #     }

#       scan/test:
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
                'name': 'Assign Diet',
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

# @api.onchange('dates')
# 	def rolls(self):
# 		date_today=datetime.datetime.now()
# 		vals=self.env['medical.appointment'].search([('dates','=',date_today)]),([('doctor_id','=',self.doctor_id.id)])
# 		if len(vals)>=2:
# 			raise UserError("Appointment Slots are full")
# 		raise UserError(len(vals[0]))

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

# Documents Button
    def document_button(self):
        return {
    'name': "Documents",
    # 'domain':[('patient_id', '=', self.patient.id)],
    'view_mode': 'tree,form',
    'res_model': 'patient.document',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }

    @api.onchange('documents')
    def count_doc(self):
        for rec in self:
            count = []
            for record in rec.documents:
                count.append(record.report_name)
            self.document_test= len(count)
    document_test = fields.Integer(compute='count_doc',string="Documents")

#      QR Code

    qr_code = fields.Binary("QR Code", attachment=True, store=True)
    barcode = fields.Char("Barcode")

    @api.onchange('patient')
    def generate_qr_code(self):
        for rec in self:
            p_details={
                'name':rec.serial_number,
                'patient_id':rec.patient.name,

            }
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(p_details)
            qr.make(fit=True)
            img = qr.make_image()
            temp = BytesIO()
            img.save(temp, format="PNG")
            qr_image = base64.b64encode(temp.getvalue())
            self.qr_code = qr_image

class GreenAgreement(models.Model):
    _name = "green.agreement"
    
    agreement=fields.Binary(string="Agreement", attachment=True, store=True)

class Perviousmedication(models.Model):
    _name='pervious.medication'

    diseases= fields.Many2one('medical.doctor',string="Diseases")
    diseases_for = fields.Many2one('medical.pathology',string = "Diseases")
    signs = fields.Char(string="Signs")
    medication_from = fields.Date(string="Medication From")
    medication_to = fields.Date(string="Medication to")
    medicine = fields.Char(string="Medicines")
    diets = fields.Char(string="Diets")

class Patientsurgery(models.Model):
    _name = 'patient.surgery'

    pat = fields.Many2one('medical.patient',string="Patient")
    doc = fields.Many2one('medical.doctor',string="Doctor")
    surgery_date = fields.Date(string="Surgery Date")
    surgery_type = fields.Many2one('medical.pathology',string="Surgery Type")
    surgery_reason = fields.Char(string="Past Surgery")
    surgery_status = fields.Selection([('done','Done'),('cancel','Cancel')],string="Surgery Status")
    surgery_notes = fields.Text(string="Surgery Notes")
    
class patient_family(models.Model):
    _name = 'patient.family'

    # pati = fields.Many2one('medical.patient',string="Patient")
    doct = fields.Many2one('medical.doctor',string="Doctor")
    family_details = fields.Char(string="Family Details")
    # family_date = fields.Date(string="Family Date")
    # family_type = fields.Many2one('medical.pathology',string="Family Type")
    # family_reason = fields.Char(string="Family Disease Reason")
    # family_status = fields.Selection([('done','Done'),('cancel','Cancel')],string="Family Status")
    # family_notes = fields.Text(string="Family Notes")
    # family_name = fields.Char(string="Family Name")
    # realtionship = fields.Char(string="Realtionship")
    # familyphone = fields.Integer(string="Phone")
    # name_f = fields.Many2one('medical.pathology',string="Family Disease")

class documents(models.Model):
    _name ="patient.document"

    docc = fields.Many2one('medical.doctor',string="Doctor")
    report_name = fields.Many2one('document.for',string="Report Name")
    attachment = fields.Binary(string="Image/Video Attachment")

class treatment_for(models.Model):
    _name ="treatment.form"

    treatment1=fields.Many2one('medical.doctor',string='Treatments')
    treatment_for = fields.Selection([('re','Reversable'),('ma','Maintanance'),('td','Test Dose'),('ch','Chromic ')],string= "Treatment")
    diagnosis1 = fields.Char(string='Initial Diagnosis')
    final_diagnosis1 =  fields.Char(string='Final Diagnosis')

class treatmentFor(models.Model):
    _name='treatment.for'

    name= fields.Char(string='Treatment Name')

class diet_field(models.Model):
    _name ="diet.field"

    diet1 = fields.Many2one('medical.doctor',string="Diet")
    diet_for = fields.Many2one('diet.for',string="Diets")
    
    
class medical_path(models.Model):
    _inherit='medical.pathology'

    ailment1=fields.Char(string='Ailment')
    

class medical_habits(models.Model):
    _name='medical.habits'

    habit=fields.Many2one('habit.for',string="Habit")
    duration=fields.Char(string="Duration")
    days= fields.Char(string="Habit/Day")
    doz=fields.Many2one('medical.doctor',string="Dose")

