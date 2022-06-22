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
    currency = fields.Many2one('res.currency',string="Currency")
    payment_status = fields.Boolean(string="Paid")
    duration_ailments = fields.Char(string="Duration of Ailments")
    doctor_changes=fields.Boolean(string="Change",readonly=True)
    reg_type=fields.Selection([('dir',"Direct"),('on',"Online"),('app',"Appoinment"),('rev',"Review"),('stop',"Stopped")],string="Registration Type")
    # patient_id = fields.Many2one('')
    

    insurance = fields.Boolean(string="Insurance if any")
    type_of_insurance= fields.Text(string='Insurance Details')


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
            'amount':self.fees,

        })
        bill_lines=[]
        bills={
            'name':'Registration Payment',
            'date':datetime.now(),
            'bill_amount':self.fees,
            'payment_status':self.payment_status,

        }
        bill_lines.append((0,0,bills))
        bill_create=self.env['patient.bills'].create({
            'patient_name':self.patient_id.id,
            'bills_lines':bill_lines,
            'insurance':self.insurance,
            'type_of_insurance':self.type_of_insurance,
        })
        payment_count = self.env['medical.doctor'].search_count([('patient', '=', self.patient_id.id)])
        if self.patient_selection == 'new':
            
            if payment_count >0:
                raise ValidationError('Patient already exist '
                '                                                                                                                                                                                                            '
                ' Please select - Existing Patient')
            else:
                # lines=[]
                # val={
                # 'patient_currents_ailments':self.treatment.id,
                # 'duration':self.duration_ailments,
                # }
                # lines.append((0,0,val))
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
                    'opnumber':self.name,
                    # 'currents_ailments':lines,
                    'stages':'done',
                    })
                return create_patient

        elif self.patient_selection == 'exi':
            val = self.env['medical.doctor'].search([('patient','=',self.patient_id.id)])
            val.write({
                'doctor':self.doctors.id,
                'patient_status':True,
                })







        
