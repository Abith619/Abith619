from odoo import models, api, fields
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta 
from odoo.exceptions import  ValidationError
# from barcode import EAN13
import qrcode
from io import BytesIO
import base64
from builtins import bytes, dict, super
from string import _string

class QueueManagement(models.Model):
    _name = 'queue.management'
    _rec_name = 'name'

    name = fields.Char(string='Queue ID')
    patient_id = fields.Many2one('res.partner', string='Patient Name', required=True,domain=[('is_patient','=',True)])
    sample_test = fields.Boolean(string='Sample')
    approval = fields.Boolean(string='Approval')
    sex = fields.Selection([('m', 'Male'),('f', 'Female')], string ="Sex", required=True)
    patient_type = fields.Selection([('new',"New Patient"),('exi',"Existing patient")], string='Patient Type')
    patient_activity = fields.Selection([
        ('wait',"Waiting"),('doctor',"Doctor Assigned"),('doc','Diet Assigned'),('app','Approved'),('dis','Dispached'),
        ('lab','Lab Bill Assigned'),('pres','Pharmacy Bill Assigned'),('scan','Scan Bill Assigned'),
        ('labs','Lab Test Completed'),('scans','Scan Test Completed'),
        ('bill',"Pharmacy Bill Assigned"),('discontinued','Discontinued'),('completed',"Completed"),('sample','Sample Collected')],
        default='wait',track_visibility='always', string='Status')
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
            ], string='Priority', default='low')
    start_date = fields.Datetime(string='Date', default=datetime.now())
    sex_age = fields.Char(string='Gender/Age')
    dispached = fields.Boolean(string='Dispached')

    @api.depends('patient_activity')
    def write_activity(self):
        if self.patient_activity:
            self.activity = True

    @api.model
    def create(self, val):
        ser_id  = self.env['ir.sequence'].next_by_code('queue.management')
        result = super(QueueManagement, self).create(val)
        result.name = ser_id
        return result

class LabClinic(models.Model):
    _name = 'lab.clinic'
    _rec_name = 'name_age_sex'

    patient_photo = fields.Binary(string='Photo')
    patient_id = fields.Many2one('res.partner',string='Name',domain=[('is_patient','=',True)])
    contact_num = fields.Char(string='Contact Number')
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Char(compute='onchange_age',string="Age",store=True,readonly=False)
    sex = fields.Selection([('m', 'Male'),('f', 'Female')], string ="Sex", required=True)
    name_age_sex = fields.Char(string='Patient Name', compute='concatinate_name_age')
    height = fields.Float(string="Height in Cms")
    weight = fields.Float(string="Weight in Kgs")
    blood_type = fields.Selection([('A', 'A'),('B', 'B'),('AB', 'AB'),('O', 'O')], string ="Blood Type")
    rh = fields.Selection([('-+', '+'),('--', '-')], string ="Rh")
    last_visit = fields.Date(string='Last Visit')
    reg_id = fields.Char(string='Registration ID')
    reg_date = fields.Date(string='Registration Date')
    order_date = fields.Date(string='Order Date', default=datetime.now())
    ref_num = fields.Char(string='Refrence Number')
    ref_date = fields.Date(string='Refrence Date')
    order_from = fields.Selection([('op','OP'),('ip','IP')], string='Order From', default='op')
    order_status = fields.Selection([('new','New'),('progress','Progress'),('completed','Completed')], String='Order Status', default='new')
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
            ], string='Priority', default='medium')
    approved_status = fields.Selection([('not','Not Approved'),('approved','Approved'),('dispach','Dispach')], string='Status', default='not')
    contact_number=fields.Char(string="Whatsapp Number")
    whatsapp_check = fields.Boolean(string='')

    physician_id = fields.Many2one('res.partner', string='Physician')
    tech_id = fields.Many2one('res.partner', string='Technician')

    lab_line = fields.One2many('lab.department','related_id', string='Lab Tests')
    report_line = fields.One2many('lab.processing','related_id', string='Lab Reports')
    
    # @api.onchange('report_line')
    # def sample_result(self):
    #     for i in self.lab_line:
    #         for j in self.report_line:
    #             if i.test_name == j.test_name:
                    

    @api.onchange('patient_id')
    def on_patient(self):
        patient_orm = self.env['res.partner'].search([('id','=',self.patient_id.id)])
        orm_city = self.env['res.city'].search([('name','=',patient_orm.city)])
        reg_orm = self.env['lab.clinic'].search([('patient_id','=',self.patient_id.id)],limit=1)
        patient_orm.write({
            'roles_selection':'patient',
            'is_patient':True,
                })
        self.update({
            'contact_num':patient_orm.phone,
            'sex':patient_orm.patient_gender,
            'contact_number':patient_orm.whatsapp,
            'date_of_birth':patient_orm.dob_contact,
            'height':patient_orm.height,
            'weight':patient_orm.weight,
            'blood_type':patient_orm.blood_type,
            'rh':patient_orm.rh,
            'reg_id':reg_orm.ref_num,
            'last_visit':reg_orm.create_date,
                })

    @api.constrains('patient_id')
    def write_partner(self):
        patient_orm = self.env['res.partner'].search([('id','=',self.patient_id.id)])
        self.patient_id.write({
            'phone':self.contact_num,
            'patient_gender':self.sex,
            'whatsapp':self.contact_number,
            'dob_contact':self.date_of_birth,
            'height':self.height,
            'weight':self.weight,
            'blood_type':self.blood_type,
            'rh':self.rh,
                })

    def approved_status_change(self):
        self.approved_status = 'approved'
        orm = self.env['queue.management'].search([('patient_id','=',self.patient_id.id)],limit=1)
        orm.approval = True
        orm.patient_activity = 'app'

    

    def concatinate_name_age(self):
        if self.age:
            ages = self.age.split()[0]
        else:
            ages = 'Age'
        var = dict(self._fields['sex'].selection).get(self.sex)
        self.name_age_sex = '{} /{}/{}'.format(self.patient_id.name,ages,var)

    @api.depends('date_of_birth')
    def onchange_age(self):
        for rec in self:
            if rec.date_of_birth:
                d1 = rec.date_of_birth
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years) + "y" +" "+ str(rd.months) + "m" +" "+ str(rd.days) + "d"
            else:
                rec.age = "Age"

    @api.constrains('lab_line')
    def write_test(self):
        orm = self.env['lab.bills.name'].search([('ref_num','=',self.ref_num)],limit=1)
        lists=[(5,0,0)]
        report_list=[(5,0,0)]
        for i in self.lab_line:
            values={
                'test_name':i.test_name.id,
                'dept_name':i.lab_category.id,
                'test_amount':i.test_name.test_amount,
            }
            lists.append((0,0,values))
            value={
                'test_name':i.test_name.id,
                'unit':i.test_name.unit,
                'normal_range':i.test_name.normal_range,
                }
            report_list.append((0,0,value))
        orm.write({
            'bill_lines':lists
        })
        self.report_line = report_list
        

    @api.model
    def create(self, vals):
        patient_ids  = self.env['ir.sequence'].next_by_code('lab.clinic')
        result = super(LabClinic, self).create(vals)
        result.ref_num = patient_ids
        reg_orm = self.env['lab.clinic'].search([('patient_id','=',result.patient_id.id)],limit=1)
        if reg_orm:
            self.env['queue.management'].create({
                'name':result.ref_num,
                'patient_id':result.patient_id.id,
                'sex_age':result.name_age_sex,
                'start_date':datetime.now(),
                'patient_type':'new',
                'sex':result.sex,
            })
        else:
            self.env['queue.management'].create({
                    'name':result.ref_num,
                    'patient_id':result.patient_id.id,
                    'sex_age':result.name_age_sex,
                    'start_date':datetime.now(),
                    'patient_type':'exi',
                    'sex':result.sex,
                })

        lists=[]
        for i in result.lab_line:
            values={
                'test_name':i.test_name.id,
                'dept_name':i.lab_category.id,
                'test_amount':i.test_name.test_amount,
            }
            lists.append((0,0,values))
        self.env['lab.bills.name'].create({
            'patient_photo':result.patient_photo,
            'patient_id':result.patient_id.id,
            'contact_num':result.contact_num,
            'date_of_birth':result.date_of_birth,
            'age':result.age,
            'sex':result.sex,
            'name_age_sex':result.name_age_sex,
            'height':result.height,
            'weight':result.weight,
            'reg_id':result.reg_id,
            'ref_num':result.ref_num,
            'contact_number':result.contact_number,
            'physician_id':result.physician_id.id,
            'tech_id':result.tech_id.id,
            'bill_lines':lists
                })
        return result

class LineLab(models.Model):
    _name = 'lab.department'

    related_id = fields.Many2one('lab.clinic', string='Clinic')
    test_name = fields.Many2one('lab.master', string='Test Name')
    lab_category = fields.Many2one('lab.department.masters', string='Lab Category', related='test_name.dept_name')
    sample_collected = fields.Boolean(string='Sample Collected Status')
    sample_date = fields.Datetime(string='Sample Collected Date')
    sample_num = fields.Char(string='Sample No.')
    barcode = fields.Binary(string='Qr Code')
    received = fields.Boolean(string='Received')
    
    def add_sample(self):
        ser_id  = self.env['ir.sequence'].next_by_code('sample.wizard.sequence')
        self.sample_num = ser_id
                
        for rec in self.related_id:
            p_details={
                'Patient Id': rec.patient_id.id,
                'Patient Name': rec.patient_id.name,
            }
            qr = qrcode.QRCode(
                version = 1,
                error_correction = qrcode.constants.ERROR_CORRECT_H,
                box_size = 10,
                border = 4,
                    )
            qr.add_data(p_details)
            qr.make(fit=True)
            img = qr.make_image()
            temp = BytesIO()
            img.save(temp, format="PNG")
            qr_image = base64.b64encode(temp.getvalue())
            self.barcode = qr_image
            
        self.sample_collected = True
        self.sample_date = datetime.now()

        orm = self.env['queue.management'].search([('patient_id','=',self.related_id.patient_id.id)],limit=1)
        orm.write({'patient_activity':'sample',
            'sample_test':True})
        
class ReportProcess(models.Model):
    _name = 'lab.processing'

    related_id = fields.Many2one('lab.clinic', string='Related')
    test_name = fields.Many2one('lab.master',string='Test Name')
    res_value = fields.Char(string='Result Value')
    unit = fields.Selection([('mcg','Mcg'),('g/dl','g/dL'),('iu/ml','IU/mL'),('μg/ml','μg/mL')])
    normal_range = fields.Char(string='Normal Range')
    ext_lab = fields.Char(string='External Lab')
    comments = fields.Char(string='Comments')
    
class SampleLabUpload(models.Model):
    _name = 'sample.lab'

    patient_id = fields.Many2one('res.partner', string='Patient ID')
    name = fields.Char(string='Serial.No',copy=False, readonly=True)
    sample_barcode = fields.Binary(string="BarCode")
    test_name = fields.Char(string='Test name')

    @api.model
    def create(self, val):
        
        result = super(SampleLabUpload, self).create(val)

        return result

class LabsMasters(models.Model):
    _name = 'lab.master'
    _rec_name = 'test_name'

    test_name = fields.Char(string='Test Name')
    dept_name = fields.Many2one('lab.department.masters', string='Department')
    test_amount = fields.Integer(string='Amount')
    unit = fields.Selection([('mcg','Mcg'),('g/dl','g/dL'),('iu/ml','IU/mL'),('μg/ml','μg/mL')])
    normal_range = fields.Char(string='Normal Range')
    gst = fields.Many2many('account.tax', string='Tax')
    test_type = fields.Selection([('test','Test'),('scan','Scan')], string='Test Type')

class LabDepartmentMaster(models.Model):
    _name = 'lab.department.masters'
    _rec_name = 'dept_name'

    dept_name = fields.Char(string='Department Name')
