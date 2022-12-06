
from builtins import super
from inspect import signature
from odoo import api, fields, models, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta 
import qrcode
import base64
from io import BytesIO
from odoo.exceptions import ValidationError
import sys

class medical_directions(models.Model):
    _name = 'medical.doctor'
    _rec_name = 'patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company']._company_default_get('medical.doctor'))
    doctor = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string="Doctor" ,track_visibility='always')
    age=fields.Char(string='Age')
    address = fields.Char(string="Address")
    marital_status = fields.Selection([('s','Single'),('m','Married'),('w','Widowed'),('d','Divorced'),('x','Seperated')],string='Marital Status')
    height = fields.Float(string="Height in Cms")
    weight = fields.Float(string="Weight in Kgs")
    bp = fields.Char(string='BP in mmHg')
    patient_timing=fields.Datetime(string='Patient Timing')
    treatment = fields.Char(string="Treatment Adviced")
    opnumber =fields.Char(string="OP Number")
    patient = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name",required=True)
    since = fields.Integer(string='Since')
    sign_symptoms = fields.Many2many('medical.symptoms',string="Signs/Symptoms")
    history = fields.Text(string ="History")
    sex = fields.Selection([('m', 'Male'),('f', 'Female')],  string ="Sex", required= True)
    prescription_date= fields.Datetime(string='Date', default=fields.Datetime.now())
    name = fields.Char('Prescription ID')
    ailments=fields.Many2one('medical.pathology',string="Current Ailments")
    habbit=fields.One2many('medical.habits','doz',string="Habit")
    diet_fields=fields.One2many('diet.field.for','diet2',string='Diet')
    patient_status = fields.Boolean(string='Patient Status')
    adoption_details = fields.Boolean(track_visibility='onchange')
    designation = fields.Char(string="Designation",readonly=True)
    date1=fields.Date(default=datetime.today())
    medicine_name = fields.Many2one('product.product',string='Medicine Name')
    medicine_id = fields.Many2one('medical.prescription.order',string='Medicine Name')
    diet_id = fields.Many2one('prescribe.diet',string='Diet')
    no_fees = fields.Boolean(string='No Consulting Fees', default=False, required=False)
    
    #   one2many
    pervious_medication = fields.One2many('pervious.medication','diseases',string="Past Complaints")
    surgery_history = fields.Char(string ="Surgery History")
    family_history = fields.Char(string ="Family History")
    
    # ailments=fields.Many2one('medical.pathology',string="Current Ailments")

    lab_test_line = fields.One2many('lab.test.line','lab_id',string='Lab/Tests')

    scan_test = fields.One2many('scan.line','scan',string="Scan/Tests")

    green_agreement=fields.One2many('green.agreement','agreement',string="Green Agreement")
    
    history_surgery = fields.One2many('patient.surgery', 'doc', string="Assigned Lab/Scans", ondelete='cascade')

    history_family = fields.One2many('patient.family','doct',string="History of Family")

    documents = fields.One2many('patient.document','docc',string="Documents")

    treatment_initial=fields.One2many('treatment.form','treatment1',string='Treatment')

    prescription_patient = fields.One2many( 'patient.prescription','medical_doctor',string ='Prescription')

    currents_ailments = fields.One2many('current.ailments','doctor_aliments',string="Current Ailments")

    lab_reports = fields.Many2one('medical.lab',string ="Lab Reports")
    scan_reports = fields.Many2one('medical.lab',string ="Scan Reports")
    diet= fields.Char(string=" For Diet")
    image = fields.Binary()
    videos = fields.Binary(string ="Videos")
    notes = fields.Text(string="Special Notes To Self/Other Staffs")

    image1=fields.Binary(string="Image")
    
    user_doctor = fields.Many2one('res.users',string="User Doctor")
    required_field = fields.Boolean()
    
    def completed_pat(self):
        self.patient_activity = 'completed'
        file = self.env['res.partner'].search([('display_name','=',self.patient.name)])
        file.write({'patient_activity':'completed'})
        
        reg = self.env['medical.patient'].search([('patient_id','=',self.patient.id)])
        reg.write({'patient_activity':'completed'})
        
        bill = self.env['patient.bills'].search([('patient_name','=',self.patient.id)])
        bill.write({'patient_activity':'completed'})
        
        lab = self.env['lab.scan.form'].search([('patient_id','=',self.patient.id)])
        lab.write({'patient_activity':'completed'})
        
        scan = self.env['scan.test'].search([('patient_id','=',self.patient.id)])
        scan.write({'patient_activity':'completed'})
        
        prescription = self.env['medical.prescription.order'].search([('patient_id','=',self.patient.id)])
        prescription.write({'patient_activity':'completed'})
    
    @api.onchange('currents_ailments')
    def on_required(self):
        self.required_field = True

    @api.onchange('doctor')
    def login_orm(self):
        login_doc = self.env['res.users'].search([('partner_id', '=', self.doctor.id)])
        self.user_doctor = login_doc.id

    experince = fields.Char(string="Experience")

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

    bmi_value= fields.Char(string="BMI",readonly=True)

# new fields 
    father_name=fields.Selection([('1','Father'),('2','Husband'),('3','Mother'),('4','Wife'),('5','Gaurdian'),('6','Relative')])
    image = fields.Binary()
    name_father=fields.Char(string="Name")

    videos = fields.Binary(string ="Green Document")
    treat_for = fields.Selection([('rev','Reversable'),('main','Maintanance'),('tdo','Test Dose'),('cho','Chromic '),('con','Control')],string ="Treatment For")
    
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
    name_father = fields.Char()
    # habits = fields.Many2many('habit.for',string="Habits")
    patient_habits = fields.Many2many('habit.for',string="Habits")

    write_date=fields.Date(string='Date')

    patient_waiting = fields.Char(string="Waiting Time")
    wait_date=fields.Datetime(string='Datetime', default=datetime.now())
    patient_activity = fields.Selection([('wait',"Waiting"),('doctor',"Doctor Assigned"),('doc','Diet Assigned'),
                                         ('lab','Lab Bill Assigned'),('pres','Pharmacy Bill Assigned'),('scan','Scan Bill Assigned'),
                                         ('labs','Lab Test Completed'),('scans','Scan Test Completed'),
                                         ('bill',"Pharmacy Bill Assigned"),('discontinued','Discontinued'),('completed',"Completed")],default='wait', track_visibility='onchange')

    
    med_cancell = fields.Selection([('cancell','Cancelled'),('discontinued','Discontinued'),('Completed','Purchased')], string='Medicine Details')
    reg_type=fields.Selection([('dir',"Direct"),('on',"Online"),('app',"Appointment"),('rev',"Review"),('package','Package'),('stop',"Stopped"),('cam','Camp')],string="Registration Type")
    
    @api.onchange('ailments')
    def onchange_test(self):
        for rec in self:
            return {'domain':{'sign_symptoms':[('diseases', '=', rec.ailments.id)]}}

    def med_cancell_fun(self):
        self.patient_activity = 'discontinued'
        orm = self.env['medical.patient'].search([('patient_id', '=', self.patient.id)])
        orm.write({'patient_activity':'discontinued'})
        self.prescription_patient = [(5,0,0)]
        orm1 = self.env['patient.bills'].search([('patient_name','=',self.patient.id)])
        # raise ValidationError(orm1)
        orm1.write({
            'pres_bill':[(5,0,0)],
            'med_cancell':'cancell',
            })
        
    @api.onchange('bp','patient_habits','currents_ailments','pervious_medication')
    def adapt_req(val):
        if val['adoption_details'] == False:
            raise ValidationError('Adoption Agreement is Mandatory')
        

    @api.model
    def create(self, vals):
        vals['serial_number'] = self.env['ir.sequence'].next_by_code('medical.doctor') or 'EB'
        
        res = super(medical_directions, self).create(vals)
        return res

    def done_action(self):
        self.appoinment_status=False

    @api.depends('prescription_date')
    def date_today(self):
        count_d = self.env['medical.doctor'].search([('prescription_date', '=', datetime.datetime.now())])
        if count_d == True:
            self.appoinment_status=True
        else:
            self.appoinment_status=False

    def edit_button(self):
        return {
        'name': "Edit Symptoms",
        'view_mode': 'tree',
        'res_model': 'medical.symptoms',
        'view_type': 'form',
        'type': 'ir.actions.act_window',
        'view_id': self.env.ref('basic_hms.symptoms_tree_view').id,
        'target': 'new'
        }
        
    def upload_ebook(self):
        return{
            'name': "Upload Ebook",
            'view_mode': 'form',
            'domain':[('name', '=', self.patient.id)],
            'res_model': 'document.type.line',
            'view_type': 'form',
            'type': 'ir.actions.act_window',
            # 'target': 'create',
            'context':{
                'default_name' : self.patient.name,
            }
        }

# prescription
    def prescription_button(self):
        self.patient_status =False
        # self.patient_activity = 'pres'
        # orm = self.env['medical.patient'].search([('patient_id','=',self.patient.id)])
        # orm.write({'patient_activity':self.patient_activity})

        return{
        'name': "Prescription",
        'type': 'ir.actions.act_window',
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'medical.prescription.order',
        'view_id': self.env.ref('basic_hms.medical_prescription_order_form_view').id,
        'context': {
            'default_doctor_id': self.doctor.id,
            'default_prescription_date': self.prescription_date,
            'default_ebook_id': self.serial_number,
            'default_patient_id': self.patient.id,
            'default_age': self.age,
            'default_sex': self.sex,
            'default_height': self.height,
            'default_weight': self.weight,
            'default_num_days': 'e',
            # 'default_treatments_for':self.treatment,
            # 'default_treatment_for':self.treatment,
            'default_stages':'draft'
            },
            'target': 'new'
            }
        
    def prescription_edit_button(self):
        self.patient_status =False
        self.patient_activity = 'pres'
        orm = self.env['medical.patient'].search([('patient_id','=',self.patient.id)])
        orm.write({'patient_activity':self.patient_activity})

        return{
            'name': "Prescription",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'medical.prescription.order',
            # 'res_id': self.id,
            'view_id': self.env.ref('basic_hms.medical_prescription_order_form_view').id,
            'context': {
                'default_doctor_id': self.doctor.id,
                'default_prescription_date': self.prescription_date,
                'default_ebook_id': self.serial_number,
                'default_patient_id': self.patient.id,
                'default_age': self.age,
                'default_sex': self.sex,
                'default_height': self.height,
                'default_weight': self.weight,
                'default_num_days': 'ed',
                # 'default_treatments_for':self.treatment,
                # 'default_treatment_for':self.treatment,
                'default_stages':'draft'
                },
            'target': 'current'
            }

#scan/test:
    def scan_button(self):
        self.patient_status =False
        if self.patient_status == False:
            return{
                'name': "Lab Tests",
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'lab.scan.form',
                'context': {
                    'default_patient_id': self.patient.id,
                    'default_ebook_id': self.serial_number,
                    'default_num_days': 'e',
                    'default_doctor_id':self.doctor.id,
                    'default_state':'tested'
                },
                'target': 'new'
                }
        else:
            pass
        
        self.patient_activity = 'lab'
        orm = self.env['medical.patient'].search([('patient_id','=',self.patient.id)])
        orm.write({'patient_activity' : self.patient_activity})
        
        # continue
        
    def in_patient(self):
        return{
            'name': "In-Patient Hospitalization",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'in.patient',
            'context': {
                'default_patient_id': self.patient.id,
                'default_doctor_in': self.doctor.id,
                'default_reg_no': self.serial_number,
                'default_contact_num': self.phone_number,
                'default_gender': self.sex,
                'default_age':self.age,
                'default_conditions':[[6,0,[i.id for i in self.currents_ailments.patient_currents_ailments]]],
                'default_bp':self.bp,
                },
                'target': 'new'
            }

    def labscan_button(self):
        self.patient_status =False
        # self.patient_activity = 'scan'
        # orm = self.env['medical.patient'].search([('patient_id','=',self.patient.id)])
        # orm.write({'patient_activity':self.patient_activity})
        # orm_lab = self.env['lab.menu'].search([('patient_id','=',self.patient.id)])
        # orm_lab.write({'ebook_id':self.opnumber,
                #    'patient_id':self.patient})
        return{
            'name': "Scan Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'scan.test',
            'context': {
                'default_patient_id': self.patient.id,
                'default_ebook_id': self.serial_number,
                'default_num_days': 'e',
                # 'default_range': self.range,
                'default_doctor_id':self.doctor.id,
                'default_state':'tested'
                },
                'target': 'new'
            }

    @api.onchange("contact_number")
    def number_val(self):
        if self.contact_number != False:
            x = self.contact_number.isdigit()
            if x == False:
                raise ValidationError("only numbers are Allowed")

    def diet_for(self):
        self.patient_status =False
        self.patient_activity = 'doc'
        orm = self.env['medical.patient'].search([('patient_id','=',self.patient.id)])
        orm.write({'patient_activity':self.patient_activity})
        return{
            'name': "Prescribe Diet",
            'type': 'ir.actions.act_window', 
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'prescribe.diet',
            'context': {
                'default_patient_id': self.patient.id
                },
            'target': 'new'
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



    def prescribe_button(self):
            return {
    'name': "Prescribe Diet",
    'domain':[('patient_id', '=', self.patient.id)],
    'view_mode': 'tree,form',
    'res_model': 'prescribe.diet',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }
#      Count in Smart Button
    def diet_count(self):
        for res in self :
            count_d = self.env['prescribe.diet'].search_count([('patient_id', '=', res.patient.id)])
            self.pre_diet= count_d

    pre_diet = fields.Integer(compute='diet_count',string="Prescribed Diet")



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


    qr_code = fields.Binary("QR Code", attachment=True,compute='generate_qr_code' )
    barcode = fields.Char("Barcode")

    # @api.onchange('bp')
    def generate_qr_code(self):
        for rec in self:
            p_details={
                'Patient Id':rec.serial_number,
                'Patient Name':rec.patient.name,
                # "Phone Number":rec.contact_number,
                'Address':rec.address,
                'Age':rec.age,
                'BP':rec.bp,
                # 'Current Ailment': rec.currents_ailments.patient_currents_ailments,
                # 'Signs & Symptoms':[[6,0,[i for i in self.currents_ailments.patient_signs_symptoms]]],
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

    image_work = fields.One2many('assign.workout','name', string='Images')

    therapy_line = fields.One2many('therapy.ebook','name', string='Therapy')

    

class Therapy_Ebook(models.Model):
    _name = 'therapy.ebook'
    
    name = fields.Many2one('medical.doctor',string="Name",ondelete='cascade')
    time = fields.Char(string='Time')
    therapy = fields.Char(string='Therapy')
    amount = fields.Char(string='Amount')


class assignWorkout(models.Model):
    _name='assign.workout'
    
    name = fields.Char(string="Exercise")
    workout_img = fields.Many2many('ir.attachment', string='Images')
    workout=fields.Many2one('file.room',string='Workout')
    work_image = fields.Many2many('file.room', string='Images')

    @api.onchange('workout')
    def work_out(self):
        for rec in self:
            orm=self.env['file.room'].search([('id','=',rec.workout.id)])
            att_ids = []
            for i in orm.attachment:
                    att_ids.append(i.id)
            rec.write({'workout_img':[(6,0,att_ids)]})


class GreenAgreement(models.Model):
    _name = "green.agreement"
    

    agreement=fields.Binary(string="Agreement", attachment=True, store=True,ondelete='cascade')

class Perviousmedication(models.Model):
    _name='pervious.medication'

    # serial_number=fields.Integer(string="SL")
    write_date=fields.Date(string='Date')
    diseases= fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    diseases_for = fields.Char(string = "Complaints",required=True)
    # signs = fields.Char(string="Signs")
    # medication_from = fields.Date(string="Medication From")
    # medication_to = fields.Date(string="Medication to")
    medicine = fields.Char(string="Notes")
    # diets = fields.Char(string="Diets")

    sequence_ref = fields.Integer('SL.NO', compute="_sequence_ref")

    @api.depends('diseases.pervious_medication', 'diseases.pervious_medication.diseases_for')
    def _sequence_ref(self):
        for line in self:
            no = 0
            line.sequence_ref = no
            for l in line.diseases.pervious_medication:
                no += 1
                l.sequence_ref = no


class Patientsurgery(models.Model):
    _name = 'patient.surgery'

    # pat = fields.Many2one('medical.patient',string="Patient")
    doc = fields.Many2one(string="Patient Name",ondelete='cascade')
    # serial_number=fields.Integer(string="SL")
    lab_scan_alot = fields.Many2one('medical.patient.lab.test',string="Lab")
    lab_type = fields.Many2one('medical.patient.lab.test',string="Lab")

    date= fields.Datetime(string="Date of Lab/Scan")


class Lab_scan_test(models.Model):
    _name = 'lab.test.line'

    name = fields.Char(string='Test Name')
    lab_id = fields.Many2one('medical.doctor',string="Name",ondelete='cascade')
    lab_type = fields.Many2one('lab.scan.form',string="Lab")
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    date= fields.Datetime(string="Date of Lab/Scan")
    ip_name = fields.Many2one('in.patient',string='Ip Name')

    sequence_ref = fields.Integer('SL.NO', compute="_sequence_ref")

    @api.depends('lab_id.lab_test_line', 'lab_id.lab_test_line.lab_type')
    def _sequence_ref(self):
        for line in self:
            no = 0
            line.sequence_ref = no
            for l in line.lab_id.lab_test_line:
                no += 1
                l.sequence_ref = no

class scan_line(models.Model):
    _name = 'scan.line'

    scan = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    scan_id = fields.Many2one('scan.test',string="Scan")
    date= fields.Datetime(string="Date of Scan Test")
    name = fields.Char(string='Test Name')
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
    sequence_ref = fields.Integer('SL.NO', compute="_sequence_ref")
    

    @api.depends('scan.scan_test', 'scan.scan_test.scan_id')
    def _sequence_ref(self):
        for line in self:
            no = 0
            line.sequence_ref = no
            for l in line.scan.scan_test:
                no += 1
                l.sequence_ref = no

class patient_family(models.Model):
    _name = 'patient.family'

    doct = fields.Many2one('medical.doctor',string="Doctor",ondelete='cascade')
    family_details = fields.Char(string="Family Details")


class documents(models.Model):
    _name ="patient.document"

    docc = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    report_name = fields.Selection([('voice','Voice Recording'),('Video','Video'),('ebook','Ebook'),('photo','Photo'),('green','Green Document'),('gov','Gov ID'),
        ('original','Original'),('lab','Lab Document'),('scan','Scan Document')],string='Attachment Type',required=True)
    attachment = fields.Many2many('ir.attachment',string="Attachment")
    patient_id = fields.Many2one('res.partner',string='Name')
    # serial_number=fields.Integer(string="SL")
    sequence_ref = fields.Integer('SL.NO', compute="_sequence_ref")

    @api.depends('docc.documents', 'docc.documents.attachment')
    def _sequence_ref(self):
        for line in self:
            no = 0
            line.sequence_ref = no
            for l in line.docc.documents:
                no += 1
                l.sequence_ref = no


class treatment_for(models.Model):
    _name ="treatment.form"

    treatment1=fields.Many2one('medical.doctor',string='Treatments',ondelete='cascade')
    treatment_for = fields.Selection([('re','Reversable'),('ma','Maintanance'),('td','Test Dose'),('ch','Chromic ')],string= "Treatment")
    diagnosis1 = fields.Char(string='Initial Diagnosis')
    final_diagnosis1 =  fields.Char(string='Final Diagnosis')

class treatmentFor(models.Model):
    _name='treatment.for'

    name= fields.Char(string='Treatment Name')

class diet_field_for(models.Model):
    _name='diet.field.for'

    

    diet2 = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade', index=True, copy=False)
    diet_for = fields.Many2one('set.diets',string="Diet Name")
    diet_seq = fields.Many2one('prescribe.diet',string='Diet S.No')
    dates=fields.Datetime(string='Date')
    name=fields.Many2one('in.patient',string='Name')

    sequence_ref = fields.Integer('SL.NO', compute="_sequence_ref")

    @api.depends('diet2.diet_fields', 'diet2.diet_fields.diet_for')
    def _sequence_ref(self):
        for line in self:
            no = 0
            line.sequence_ref = no
            for l in line.diet2.diet_fields:
                no += 1
                l.sequence_ref = no


# class diet_field(models.Model):
#     _name ="diet.field"

#     diet1 = fields.Many2one('medical.doctor',string="Diet")
#     diet_for = fields.Many2one('diet.for',string="Diets",required=True)
#     followed_duration= fields.Integer(string="Duration Followed/Days")
#     sequence_ref = fields.Integer('SL.NO', compute="_sequence_ref")
#     dates=fields.Datetime(string='Date')
    # serial_number=fields.Integer(string="SL")

    
    # @api.depends('diet1.diet_fields', 'diet1.diet_fields.diet_for')
    # def _sequence_ref(self):
    #     for line in self:
    #         no = 0
    #         line.sequence_ref = no
    #         for l in line.diet1.diet_fields:
    #             no += 1
    #             l.sequence_ref = no


    
class medical_path(models.Model):
    _inherit='medical.pathology'

    ailment1=fields.Char(string='Ailment')
    

class medical_habits(models.Model):
    _name='medical.habits'

    habit=fields.Many2one('habit.for',string="Habit")
    duration=fields.Char(string="Duration")
    days= fields.Char(string="Habit/Day")
    doz=fields.Many2one('medical.doctor',string="Dose",ondelete='cascade',index=True)

class Patientprescription(models.Model):
    _name ='patient.prescription'

    # serial_number=fields.Integer(string="SL")
    medical_doctor = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    # medicine_name = fields.Many2one('product.product',string='Medicine Name')
    patient_name = fields.Many2one('res.partner',string="Patient Name")
    ip_name = fields.Many2one('in.patient', string='Patient Name')
    
    prescription_alot= fields.Many2one('medical.prescription.order',string="Prescriptions",required=True)
    date = fields.Datetime(string="Date of Prescription")
    delivery_option= fields.Selection([('dir','Direct'),('on',"Online")],string="Delivery Option")
    delivery_mode = fields.Selection([('domestic','Domestic'),('international',"International")],string='Courier Mode')
    
    medicine_name = fields.Many2one('product.product',string='Medicine Name',readonly='1')
    all_day=fields.Char(string="Dose")
    prescribed_quantity = fields.Float(string="Prescribed Quantity")
    units= fields.Many2one('uom.uom',string="units")
    bf_af = fields.Selection([('before','Before Food'),('after','After Food')])
    anupana = fields.Char(string="Notes")
    days1= fields.Integer('Days')
    price = fields.Float(string="Price/unit",related='medicine_name.lst_price')
    total_price = fields.Float(string="Total Price")
    company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company']._company_default_get('in.patient'))

    @api.onchange('prescribed_quantity','medicine_name')
    def compute_price(self):
        val=self.price*self.prescribed_quantity
        self.total_price=val

    @api.onchange('medicine_name')
    def prescribe_medicine(self):
        rec= self.env['product.product'].search([('id', '=', self.medicine_name.id)])
        for res in rec.medicine_details:
            self.all_day=res.all_day
            self.units = res.units
            self.anupana = res.anupana
            
    sequence_ref = fields.Integer('SL.NO', compute="_sequence_ref")

    @api.depends('ip_name.medicine_line', 'ip_name.medicine_line.prescription_alot')
    def _sequence_ref(self):
        for line in self:
            no = 0
            line.sequence_ref = no
            for l in line.ip_name.medicine_line:
                no += 1
                l.sequence_ref = no


class Currentailgnments(models.Model):
    _name='current.ailments'


    # serial_number=fields.Integer(string="SL")
    doctor_aliments =fields.Many2one('medical.doctor', string='Patient Name',ondelete='cascade')
    patient_currents_ailments=fields.Many2one('medical.pathology',string="Complaints")
    duration = fields.Char(string="Duration")
    patient_signs_symptoms = fields.Many2many('medical.symptoms',string="Signs/Symptoms")

    sequence_ref = fields.Integer('SL.NO', compute="_sequence_ref")

    @api.depends('doctor_aliments.currents_ailments', 'doctor_aliments.currents_ailments.patient_currents_ailments')
    def _sequence_ref(self):
        for line in self:
            no = 0
            line.sequence_ref = no
            for l in line.doctor_aliments.currents_ailments:
                no += 1
                l.sequence_ref = no
            

    @api.onchange('patient_currents_ailments')
    def onchange_test(self):
        for rec in self:
            return {'domain':{'patient_signs_symptoms':[('diseases', '=', rec.patient_currents_ailments.id)]}}



