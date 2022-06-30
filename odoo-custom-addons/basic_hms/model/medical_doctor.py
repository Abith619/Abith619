
from email.policy import default
from inspect import signature
from odoo import api, fields, models, _
from datetime import date,datetime,timedelta
from calendar import monthrange
from dateutil.relativedelta import relativedelta 
import qrcode
import base64
from io import BytesIO
from odoo.exceptions import ValidationError


class medical_directions(models.Model):
    _name = 'medical.doctor'
    _rec_name = 'patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company'].browse(self.env['res.company']._company_default_get('medical.doctor')))
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
    sign_symptoms = fields.Many2many('medical.symptoms',string="Signs/Symptoms")
    history = fields.Text(string ="History")
    sex = fields.Selection([('m', 'Male'),('f', 'Female')],  string ="Sex", required= True)
    prescription_date= fields.Date(string='Date', default=fields.Datetime.now())
    name = fields.Char('Prescription ID')
    ailments=fields.Many2one('medical.pathology',string="Present Complaints")
    habbit=fields.One2many('medical.habits','doz',string="Habit")
    diet_fields=fields.One2many('diet.field','diet1',string='Diet')
    patient_status = fields.Boolean(string='Patient Status')
    time_of_consultation = fields.Datetime('End Time of Consultation')


    #one2many
    pervious_medication = fields.One2many('pervious.medication','diseases',string="Past Complaints")
    surgery_history = fields.Char(string ="Surgery History")
    family_history = fields.Char(string ="Family History")

    # ailments=fields.Many2one('medical.pathology',string="Current Ailments")

    green_agreement=fields.One2many('green.agreement','agreement',string="Green Agreement")
    
    history_surgery = fields.One2many('patient.surgery', 'doc', string="Lab \ Scan",track_visibility='always')

    history_family = fields.One2many('patient.family','doct',string="History o  f Family")

    documents = fields.One2many('patient.document','docc',string="Documents")

    treatment_initial=fields.One2many('treatment.form','treatment1',string='Treatment')


    prescription_patient = fields.One2many( 'patient.prescription','medical_doctor',string ='Prescription',track_visibility='always')

    currents_ailments = fields.One2many('current.ailments','doctor_aliments',string="Present Complaints",track_visibility='always')
    

    lab_reports = fields.Many2one('medical.lab',string ="Lab Reports")
    scan_reports = fields.Many2one('medical.lab',string ="Scan Reports")
    diet= fields.Char(string=" For Diet")
    image = fields.Binary()
    videos = fields.Binary(string ="Videos")
    notes = fields.Text(string="Special Notes To Self/Other Staffs")

    image1=fields.Binary(string="Image")

    last_update = fields.Datetime(string="Last Update")
    date1=fields.Date(default=datetime.today())
    # last_month=fields.Date(default=datetime.today() - timedelta(month=1))
    def last_month(self):
        date_last=datetime.today() - timedelta(days=31)
        
        num_days = monthrange(2019, 2)[1]
        return date_last

    mobile = fields.Char(readonly=True)
    message = fields.Char(string="Message",default='Hi how are you')
    attachment_ids = fields.Many2many(
        'ir.attachment',string='Attachment')

    write_date=fields.Datetime(string='Time')

    patient_waiting = fields.Char(string="Waiting Time")

	
    @api.constrains
    def save(self):   
        self.time_of_consultation = datetime.now()
        raise ValidationError(datetime.now())

    def send_msg(self):
        message_string = ' '
        message_string = message_string + '%20'
        message_string = message_string[:(len(message_string) - 3)]
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        template_id = ir_model_data.get_object_reference('report_print_prescription','prescription_demo_report_template')[1]
        data_record = base64.b64encode(template_id[0], 'utf-8')
        ir_values = {
        'name': "Customer Report",
        'type': 'binary',
        'datas': data_record,
        'store_fname': data_record,
        'res_model':'whatsapp.wizard',
        'res_id': self.id,
        'mimetype': 'application/x-pdf',
        }
        
        self.attachment_ids.create(ir_values)
        data_id = self.env['ir.attachment'].create(ir_values)
        
        template_id.attachment_ids = [(6, 0, [data_id.id])]
        
        ctx = {
        'default_model': 'medical.prescription.order',
        'default_res_id': self.ids[0],
        'default_use_template': template_id,
        'default_template_id': template_id.id,
        'default_body': 'Inspection Report',
        'default_attachment_ids': template_id,
        'default_composition_mode': 'comment',
        'default_user_id': self.patient_id.id,
        'default_mobile':self.contact_number,
        'default_message':"Hi "+self.patient_id.name+",\n\nYour Appointment is fixed with "+self.doctor_id.name+"\nFeedback : https://www.mouthshut.com/product-reviews/Daisy-Hospital-Chromepet-Chennai-reviews-925999566"
        }
        # return ctx
        
        return self.env['ir.attachment'].create({
                'type': 'ir.actions.act_url',
                'url': "https://api.whatsapp.com/send?phone="+self.mobile+"&text=" + message_string,
                'target': 'self',
                'res_id': self.id,
                'datas': data_record,
                'store_fname': data_record,
                'res_model': 'whatsapp.wizard',
                'mimetype': 'application/x-pdf',
                'context': ctx,
                
                })


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
    stages= fields.Selection([('draft'," Waiting"),('done',"On Consultation"),('complete',"Done")])
    diagnosis = fields.Text(string='Initial Diagnosis')
    final_diagnosis =  fields.Text(string='Final Diagnosis')
    name_father = fields.Char()
    # habits = fields.Many2many('habit.for',string="Habits")
    patient_habits = fields.Many2many('habit.for',string="Habits")

    
    # def _get_default_stage(self):
        # self.qr_id=self.serial_number
    # company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company']
    # .browse(self.env['res.company']._company_default_get('medical.prescription.order')))


#existing appoinment 
     
    # @api.onchange('patient')
    # def _existing_contact(self):
    #     if
  

    @api.onchange('ailments')
    def onchange_test(self):
        for rec in self:
            return {'domain':{'sign_symptoms':[('diseases', '=', rec.ailments.id)]}}


    @api.model
    def create(self, vals):
        vals['serial_number'] = self.env['ir.sequence'].next_by_code('medical.doctor') or 'EB'
        msgs_body = 'Ebook Created'
        for msgs in self:
            msgs.message_post(body=msgs_body)
        result = super(medical_directions, self).create(vals)
        return result

    def done_action(self):
        self.appoinment_status=False

    @api.depends('prescription_date')
    def date_today(self):
        count_d = self.env['medical.doctor'].search([('prescription_date', '=', datetime.datetime.now())])
        if count_d == True:
            self.appoinment_status=True
        else:
            self.appoinment_status=False

# prescription
    def prescription_button(self):
        self.patient_status =False
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
            'default_patient_id': self.patient.id,
            'default_age': self.age,
            'default_sex': self.sex,
            'default_height': self.height,
            'default_weight': self.weight,
            'default_stages':'draft'
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
        return{
        'name': "prescribe diet",
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


    qr_code = fields.Binary("QR Code", attachment=True, )
    barcode = fields.Char("Barcode")

    @api.onchange('bp')
    def generate_qr_code(self):
        for rec in self:
            p_details={
                'Patient Id':rec.serial_number,
                'Patient Name':rec.patient.name,


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




    # def document_upload(self):
    #         return{
    #         'name': "Upload Documents",
    #         'type': 'ir.actions.act_window',
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'res_model': 'patient.document',
    #         'context': {},
    #         'target': 'new'
    #             }

class GreenAgreement(models.Model):
    _name = "green.agreement"
    

    agreement=fields.Binary(string="Agreement", attachment=True, store=True)

class Perviousmedication(models.Model):
    _name='pervious.medication'

    # serial_number=fields.Integer(string="SL")
    diseases= fields.Many2one('medical.doctor',string="Patient Name")
    diseases_for = fields.Char(string = "Complaints",required=True)
    # signs = fields.Char(string="Signs")
    # medication_from = fields.Date(string="Medication From")
    # medication_to = fields.Date(string="Medication to")
    medicine = fields.Char(string="Notes")
    # diets = fields.Char(string="Diets")

class Patientsurgery(models.Model):
    _name = 'patient.surgery'

    # pat = fields.Many2one('medical.patient',string="Patient")
    doc = fields.Many2one('medical.doctor',string="Patient Name")
    # serial_number=fields.Integer(string="SL")
    lab_scan_alot = fields.Many2one('medical.patient.lab.test',string="Scan/Lab Alots")
    date= fields.Datetime(string="Date of Lab/Scan")
    # surgery_date = fields.Date(string="Surgery Date")
    # surgery_type = fields.Many2one('medical.pathology',string="Surgery Type")
    # surgery_reason = fields.Char(string="Past Surgery")
    # surgery_status = fields.Selection([('done','Done'),('cancel','Cancel')],string="Surgery Status")
    # surgery_notes = fields.Text(string="Surgery Notes")

    
class patient_family(models.Model):
    _name = 'patient.family'

    doct = fields.Many2one('medical.doctor',string="Doctor")
    family_details = fields.Char(string="Family Details")


class documents(models.Model):
    _name ="patient.document"

    docc = fields.Many2one('medical.doctor',string="Patient Name")
    report_name = fields.Selection([('green',"Green Document"),('o',"Other Documents")],string="Report Name",required=True)
    attachment = fields.Many2many('ir.attachment',string="Attachment")
    # serial_number=fields.Integer(string="SL")

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

    diet1 = fields.Many2one('medical.doctor',string="Patient Name")
    diet_for = fields.Many2one('diet.for',string="Diet Name",required=True)
    followed_duration= fields.Integer(string="Duration Followed/Months")
    # serial_number=fields.Integer(string="SL")

    
    
class medical_path(models.Model):
    _inherit='medical.pathology'

    ailment1=fields.Char(string='Ailment')
    

class medical_habits(models.Model):
    _name='medical.habits'

    habit=fields.Many2one('habit.for',string="Habit")
    duration=fields.Char(string="Duration")
    days= fields.Char(string="Habit/Day")
    doz=fields.Many2one('medical.doctor',string="Dose")

class Patientprescription(models.Model):
    _name ='patient.prescription'

    # serial_number=fields.Integer(string="SL")
    medical_doctor=fields.Many2one('medical.doctor',string="Patient Name")
    # medicine_name = fields.Many2one('product.product',string='Medicine Name')
    # morning= fields.Float('Morning')
    # noon= fields.Float('After Noon')
    # evening= fields.Float('Evening')
    # night= fields.Float('Night')
    # before_after= fields.Selection([('bf',"Before Food"),('af',"After food")],'Before Food')
    # comment= fields.Char('Comment')
    # days1= fields.Integer('Days')
    # units= fields.Many2one('uom.uom',string="units")
    # potency = fields.Char(string="Potency")
    # anupana = fields.Char(string="Anupana")
    prescription_alot= fields.Many2one('medical.prescription.order',string="Prescriptions",required=True)
    date= fields.Datetime(string="Date of Prescription")
    delivery_option= fields.Selection([('dir','Direct'),('on',"Courier")],string="Delivery Option")



class Currentailgnments(models.Model):
    _name='current.ailments'


    # serial_number=fields.Integer(string="SL")
    doctor_aliments =fields.Many2one('medical.doctor',string="Patient Name")
    patient_currents_ailments=fields.Many2one('medical.pathology',string="Complaints",required=True)
    duration = fields.Char(string="Duration")
    patient_signs_symptoms = fields.Many2many('medical.symptoms',string="Signs/Symptoms")

    @api.model
    def create(self,val):
        # appointment = self._context.get('appointment_id')
        patient_orm = self.env['medical.symptoms'].search([('id','=',val['patient_signs_symptoms'])])
        patient_orm.write({'diseases':val.patient_currents_ailments})




                

    @api.onchange('patient_currents_ailments')
    def onchange_test(self):
        for rec in self:
            return {'domain':{'patient_signs_symptoms':[('diseases', '=', rec.patient_currents_ailments.id)]}}



