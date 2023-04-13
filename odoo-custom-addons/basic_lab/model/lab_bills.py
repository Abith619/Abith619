from odoo import models, api, fields
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta 
from odoo.exceptions import  ValidationError

class LabBills(models.Model):
    _name = 'lab.bills.name'
    _rec_name = 'ref_num'

    patient_photo = fields.Binary(string='Photo')
    name = fields.Char(string='S.No')
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
    order_date = fields.Datetime(string='Order Date', default=datetime.now())
    ref_num = fields.Char(string='Refrence Number')
    ref_date = fields.Date(string='Refrence Date')
    order_from = fields.Selection([('op','OP'),('ip','IP')], string='Order From')
    order_status = fields.Selection([('new','New'),('progress','Progress'),('completed','Completed')], String='Order Status', default='new')
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
            ], string='Priority', default='medium')
    approved_status = fields.Selection([('not','Not Approved'),('approved','Approved'),('dispach','Dispach')], string='Status', default='not')
    contact_number=fields.Char(string="Whatsapp Number")
    whatsapp_check = fields.Boolean(string='')
    stages = fields.Selection([('wait','Waiting'),('dis','Dispached')],default='wait')
    payment_type = fields.Selection([('cash','Cash'),('card','Card'),('upi','Upi')],default='cash', string='Payment Type')

    physician_id = fields.Many2one('res.partner', string='Physician')
    tech_id = fields.Many2one('res.partner', string='Technician')

    bill_lines = fields.One2many('lab.bill.lines', 'related', string='Lab Bills')
    total_tax = fields.Integer(string='Total Tax', compute='calc_total')
    grand_total = fields.Integer(string='Grand Total', compute='calc_total')
    sub_total = fields.Integer(string='Sub Total', compute='calc_total')

    def calc_total(self):
        sums=[]
        for i in self.bill_lines:
            sums.append(i.total_amount)
            self.sub_total = sum(sums)
            for j in i.gst_percent:
                self.total_tax = ((self.sub_total / 100) * j.amount)
        self.grand_total = (self.total_tax + self.sub_total)

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

    def concatinate_name_age(self):
        if self.age:
            ages = self.age.split()[0]
        else:
            ages = 'Age'
        var = dict(self._fields['sex'].selection).get(self.sex)
        self.name_age_sex = '{} /{}/{}'.format(self.patient_id.name,ages,var)

    @api.onchange('patient_id')
    def on_patient(self):
        patient_orm = self.env['res.partner'].search([('id','=',self.patient_id.id)])
        orm_city = self.env['res.city'].search([('name','=',patient_orm.city)])
        reg_orm = self.env['medical.patient'].search([('patient_id','=',self.patient_id.id)],limit=1)
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
            'reg_id':reg_orm.name,
            'last_visit':reg_orm.create_date,
                })

    def dispach(self):
        self.stages = 'dis'
        orm = self.env['queue.management'].search([('patient_id','=',self.patient_id.id)],limit=1)
        orm.dispached = True
        orm.patient_activity = 'dis'
        lab_orm = self.env['lab.clinic'].search([('patient_id','=',self.patient_id.id)],limit=1)
        lab_orm.approved_status = 'dispach'
    
class LabBillLines(models.Model):
    _name = 'lab.bill.lines'
    _rec_name = 'test_name'

    related = fields.Many2one('lab.bills.name', string='Related')
    test_name = fields.Many2one('lab.master', string='Test Name')
    dept_name = fields.Many2one('lab.department.masters', string='Department')
    test_amount = fields.Integer(string='Amount')
    disc_amount = fields.Integer(string='Discount')
    total_amount = fields.Integer(string='Total', compute='calc_total')
    gst_percent = fields.Many2many('account.tax', string='GST', related='test_name.gst')
    
    @api.onchange('disc_amount')
    def calc_total(self):
        for i in self:
            i.total_amount = (i.test_amount - i.disc_amount)

