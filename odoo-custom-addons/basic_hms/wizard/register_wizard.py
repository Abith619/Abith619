from odoo import models, api, fields
from datetime import datetime, timedelta
from odoo.exceptions import  ValidationError


class Registerwizard(models.TransientModel):

    _name = 'register.wizard'

    patient_selection= fields.Selection([('new',"New Patient"),('exi',"Existing patient")],required=True,default='new')
    doctors = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor')
    patient_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name", required= True)
    sex = fields.Selection([('m', 'Male'),('f', 'Female')], string ="Sex",required= True)
    age = fields.Char(string="Age",store=True)
    contact_no = fields.Char(string="Contact No", required= True)
    contact_number=fields.Char(string="Whatsapp Number")
    marital_status = fields.Selection([('s','Single'),('m','Married'),('w','Widowed'),('d','Divorced'),('x','Seperated')],string='Marital Status')
    address = fields.Char(string="Address")
    father_name = fields.Selection([('1','Father'),('2','Husband'),('3','Mother'),('4','Wife'),('5','Gaurdian'),('6','Relative')])
    name_father=fields.Char(string="Name")
    height = fields.Float(string="Height in Cms")
    weight = fields.Float(string="Weight in Kgs")
    occupation = fields.Char(string="Occupation")
    office_address = fields.Char(string="Office Address")
    bmi_value= fields.Char(string="BMI")
    name = fields.Char(string ="Patient ID",readonly=True)
    treatment = fields.Many2one('medical.pathology',string="Treatment for")
    fees = fields.Float(string="Fees")
    reason=fields.Text(string="Reason")
    currency = fields.Many2one('res.currency',string="Currency",default=20)
    payment_status = fields.Boolean(string="Paid")
    duration_ailments = fields.Char(string="Duration of Ailments")
    doctor_changes=fields.Boolean(string="Change",readonly=True)
    designation = fields.Char(string="Designation")
    ebook_id = fields.Char(string='Patient ID')
    reg_type=fields.Selection([('dir',"Direct"),('on',"Online"),('app',"Appointment"),('rev',"Review"),('package','Package'),('stop',"Stopped"),('cam','Camp')],string="Registration Type")
    # patient_id = fields.Many2one('')

    insurance = fields.Boolean(string="Insurance if any")
    type_of_insurance= fields.Text(string='Insurance Details')
    
    pay_mode = fields.Selection([('cash','Cash'),('card','Card'),('upi','Upi')], string='Payment Mode', default='cash')
    upi_pay = fields.Char(string='UPI')
    card_pay = fields.Char(string='Card Payment')
    due_amount = fields.Float(string='Due Amount')
    amt_paid = fields.Float(string='Amount Paid')
    
    no_fees = fields.Boolean(string='No Consulting Fees')
    
    @api.onchange('amt_paid')
    def fees_due(self):
        self.due_amount = (self.fees - self.amt_paid)
        
    @api.onchange('payment_status')
    def paid_status(self):
        if self.payment_status == True:
            self.amt_paid = self.fees
            
    @api.onchange('doctors')
    def doc_change_orm(self):
        orm = self.env['medical.patient'].search([('patient_id','=',self.patient_id.id)])
        orm.write(({'doctors':self.doctors}))

    @api.onchange('doctors')
    def doctor_change(self):
        if self.doctor_changes == False:
            self.doctor_changes= True
        else:
            self.doctor_changes= False

    def save(self):
        create_payment=self.env['register.payment'].create({
            'patient_id':self.patient_id.id,
            'date':datetime.now().date(),
            'amount':self.fees
        })
        
        record = self.env['medical.patient'].search([('patient_id','=',self.patient_id.id )])
        record.update({
                'payment':self.fees,
            })
        payment_count = self.env['medical.doctor'].search_count([('patient', '=', self.patient_id.id)])
        if self.patient_selection == 'new':
            if payment_count >0:
                raise ValidationError('Patient already exist '
                '                                                                                                                                                                                                            '
                ' Please select - Existing Patient')
            else:

                lines=[]
                val={
                'patient_currents_ailments':self.treatment.id,
                'duration':self.duration_ailments,
                }
                lines.append((0,0,val))
                create_patient = self.env['medical.doctor'].create({
                    'patient':self.patient_id.id ,
                    'age':self.age, 
                    'sex':self.sex,
                    'doctor':self.doctors.id,
                    'phone_number':self.contact_no,
                    'contact_number':self.contact_number,
                    'marital_status':self.marital_status,
                    'address':self.address,
                    'father_name':self.father_name,
                    'name_father':self.name_father,
                    'occupation':self.occupation,
                    'office_address':self.office_address,
                    'height':self.height,
                    'weight':self.weight,
                    'bmi_value':self.bmi_value,
                    'reg_type':self.reg_type,
                    'opnumber':self.name,
                    'currents_ailments':lines,
                    'designation':self.designation,
                    'patient_status':True,
                    'adoption_details':'',
                    'stages':'done',
                    })

        elif self.patient_selection == 'exi':
            val = self.env['medical.doctor'].search([('patient','=',self.patient_id.id)])
            val.write({
                'doctor':self.doctors.id,
                'patient_status':True,
                'reg_type':self.reg_type,
                })
        orm_id=self.env['medical.doctor'].search([('patient','=',self.patient_id.id)])
        bill_lines=[]
        bills={
            'name':'Registration Payment',
            'date':datetime.now(),
            'bill_amount':self.fees,
            'due_rec':self.due_amount,
            'payment_status':self.payment_status
        }
        bill_lines.append((0,0,bills))
        bill_create=self.env['patient.bills'].create({
            'patient_name':self.patient_id.id,
            'doctor_id':self.doctors.id,
            'payment_type':self.pay_mode,
            'payment_id':self.upi_pay,
            'payment_id':self.card_pay,
            'reception_bills':bill_lines,
            'insurance':self.insurance,
            'ebook_id':orm_id.serial_number,
            'type_of_insurance':self.type_of_insurance,
            'file_charges':'200',
        })





        
