# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from ast import Pass
from odoo import api, fields, models, _
#from datetime import datetime, date
from datetime import datetime, timedelta
from odoo.exceptions import UserError
import datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import  ValidationError



class medical_appointment(models.Model):
	_name = "medical.appointment"
	_inherit = 'mail.thread'

	appoinment_by=fields.Many2one('res.users',string='Appointment By',default=lambda self: self.env.user,readonly='1')
	contact_number=fields.Char(string='Whatsapp Number')
	stages= fields.Selection([('draft',"Draft"),('done',"Registered")],default="draft")
	date=fields.Datetime('', default=datetime.datetime.now())
	treatment_for=fields.Many2one('medical.pathology',string="Treatment For")
	name = fields.Char(string="Appointment ID", readonly=True ,copy=True)
	is_invoiced = fields.Boolean(copy=False,default = False)
	institution_partner_id = fields.Many2one('res.partner',domain=[('is_institution','=',True)],string="Health Center")
	inpatient_registration_id = fields.Many2one('medical.inpatient.registration',string="Inpatient Registration")
	patient_status = fields.Selection([
			('ambulatory', 'Ambulatory'),
			('outpatient', 'Outpatient'),
			('inpatient', 'Inpatient'),
		], 'Patient status', sort=False,default='outpatient')
	patient_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string='Patient Name',required=True)
	urgency_level = fields.Selection([
			('a', 'Normal'),
			('b', 'Urgent'),
			('c', 'Medical Emergency'),
		], 'Urgency Level', sort=False,default="b")
	appointment_date = fields.Datetime('Appointment Date')
	appointment_end = fields.Datetime('Appointment End')
	doctor_id = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor',required=True)
	no_invoice = fields.Boolean(string='Bill exempt',default=True)
	validity_status = fields.Selection([
			('invoice', 'Bill'),
			('tobe', 'To be Bill'),
		], 'Status', sort=False,readonly=True,default='tobe')
	appointment_validity_date = fields.Datetime('Validity Date')
	consultations_id = fields.Many2one('product.product','Consultation Service')
	comments = fields.Text(string="Info")
	state = fields.Selection([('draft','Draft'),('confirmed','Confirm'),('cancel','Cancel'),('done','Done')],string="State",default='draft')
	invoice_to_insurer = fields.Boolean('Invoice to Insurance')
	medical_patient_psc_ids = fields.Many2many('medical.patient.psc',string='Pediatrics Symptoms Checklist')
	medical_prescription_order_ids = fields.One2many('medical.prescription.order','appointment_id',string='Prescription')
	insurer_id = fields.Many2one('medical.insurance','Insurer')
	duration = fields.Integer('Duration')
	# new fields
	appointment_slot=fields.Many2one("time.slot",string='Appointment Slot')
	patient_name=fields.Char(string="Patient Name")
	gender=fields.Selection([('m', 'Male'),('f', 'Female')],  string ="Sex", required= True)
	age= fields.Char(string="Age")
	phone_number=fields.Char(string="Contact Number")
	region= fields.Many2one('res.city',string="Area")	
	father_name=fields.Char(string="Father's Name")
	doctor_availability=fields.Selection([('available', 'Available'),('not available','Not Available')],  string ="Doctor Availability")
	fixed_by=fields.Many2one('res.partner',string="Appointment Fixed By")
	came_through=fields.Many2one('medical.feedback',string="How do you Came to known about 'Daisy Hospital' :")
	patient_selection = fields.Selection([('new',"New Patient"),('exi',"Existing Patient")],default="new",string="Patient Status")
	# fix_appoinment_line=fields.One2many('fix.appointment.line','fixed',string="Appoinment Slot")
	dates= fields.Date(string="Date")
	appointment_from=fields.Selection([('09:00 Am - 10:00 Am','09:00 Am - 10:00 Am'),('10:00 Am - 11:00 Am','10:00 Am - 11:00 Am'),('11:00 Am - 12:00 Pm',"11:00 Am - 12:00 Pm"),
    ('12:00 Pm - 01:00 Pm','12:00 Pm - 01:00 Pm'),('02:00 Pm - 03:00 Pm','02:00 Pm - 03:00 Pm'),('03:00 Pm - 04:00 Pm','03:00 Pm - 04:00 Pm'),('04:00 Pm - 05:00 Pm','04:00 Pm - 05:00 Pm'),
    ('05:00 Pm - 06:00 Pm','05:00 Pm - 06:00 Pm'),('06:00 Pm - 07:00 Pm','06:00 Pm - 07:00 Pm')],string='Appointment Slot')

	appoinment_through =fields.Selection([('onl',"Online"),('of',"Offline")],required=True,default='onl',string ="Appointment Through")

	fees = fields.Float(string='Fees')
	whatsapp_check=fields.Boolean()
	patient_signs_symptoms = fields.Many2many('medical.symptoms',string="Signs/Symptoms")

	company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company']._company_default_get('medical.prescription.order'))
	feedback = fields.Many2many('medical.feedback', string="How you came to know about Daisy Health Care(P)LTD.")

	types_app = fields.Selection([('Tele','Telecaller'),('web','Website')], string='')


	# @api.onchange("patient_selection")
    # def new_change(self):
    #     if patient_selection == 'new':
    #         return {'domain':{'patient_id':rage:('id','in',None)]}}
	
	def send_msg(self):
		if self.whatsapp_check == True:
			return {
					'type': 'ir.actions.act_window',
					'name': 'Whatsapp Message',
					'res_model': 'whatsapp.wizard',
					'target': 'new',
					'view_mode': 'form',
					'view_type': 'form',
					'context': {'default_user_id': self.patient_id.id,
					'default_mobile':self.phone_number,
					'default_message':"Hi "+self.patient_id.name+",\n\nYour Appointment is fixed with "+self.doctor_id.name+"\nFeedback : https://www.mouthshut.com/product-reviews/Daisy-Hospital-Chromepet-Chennai-reviews-925999566"
					},
					}
		else:
			return {
				'type': 'ir.actions.act_window',
				'name': 'Whatsapp Message',
				'res_model': 'whatsapp.wizard',
				'target': 'new',
				'view_mode': 'form',
				'view_type': 'form',
				'context': {'default_user_id': self.patient_id.id,
				'default_mobile':self.contact_number,
				'default_message':"Hi "+self.patient_id.name+",\n\nYour Appointment is fixed with "+self.doctor_id.name+"\nFeedback : https://www.mouthshut.com/product-reviews/Daisy-Hospital-Chromepet-Chennai-reviews-925999566"
				},
				}



	@api.onchange('appoinment_through')
	def fee_change(self):
		if self.appoinment_through =='onl':
			self.fees=float(500)
		else:
			self.fees=float(150)

    		

	# @api.onchange('dates','doctor_id')
	# def roll(self):
	# 	date_today=self.dates
	# 	today=datetime.datetime.now().date()
	# 	if date_today != False:
	# 		if date_today < today:
	# 			raise ValidationError("Date should be greater than today's date")
	# 	vals=self.env['medical.appointment'].search_count([('dates','=',date_today),('doctor_id','=',self.doctor_id.id)])
	# 	if vals >= 20:
	# 		raise ValidationError("Appointment Slots are full")

	# @api.onchange('appointment_from')
	# def date_appointment(self):
	# 	l1 = []

	# 	all_slots = ['09:00 Am - 10:00 Am','10:00 Am - 11:00 Am','11:00 Am - 12:00 Pm',"12:00 Pm - 01:00 Pm","02:00 Pm - 03:00 Pm","03:00 Pm - 04:00 Pm","04:00 Pm - 05:00 Pm","05:00 Pm - 06:00 Pm","06:00 Pm - 07:00 Pm"]
	# 	value=self.env['medical.appointment'].search([('dates','=',self.dates),('doctor_id','=',self.doctor_id.id),('appointment_from','=',self.appointment_from)])
	# 	if len(value) >= 3:
	# 		empty=self.env['medical.appointment'].search([('dates','=',self.dates),('doctor_id','=',self.doctor_id.id)])
	# 		for i in empty:
	# 			slots = i.appointment_from
	# 			l1.append(slots)
	# 			booked_slots = [i for i in all_slots if i not in l1]
	# 			raise ValidationError("Please Select from Available Slots: {}".format(booked_slots))

	@api.model
	def create(self, vals):
		vals['name'] = self.env['ir.sequence'].next_by_code('medical.appointment') or 'APT'
		msg_body = 'Appointment created'
		for msg in self:
			msg.message_post(body=msg_body)
		result = super(medical_appointment, self).create(vals)
		return result

	
#create new contact patient
	def button_registrations(self):
		self.stages = 'done'
		ces={
        'name': "Scan/Tests",
        'type': 'ir.actions.act_window',
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'medical.patient',
		'context': {
				'default_patient_id':self.patient_id.id,
				'default_sex':self.gender,
				'default_contact_no':self.phone_number,
				# 'default_patient_signs_symptoms':self.patient_signs_symptoms.id,
				'default_contact_number':self.contact_number,
				'default_doctors':self.doctor_id.id,
				# 'default_related_field':self.name,
				'default_dates':datetime.datetime.now(),
				'default_appointment_from':self.appointment_from,
				'default_treatment':self.treatment_for.id,
				'default_whatsapp_check':self.whatsapp_check,
				'default_fees':self.fees,
				'default_city':self.region.id,
				'default_reg_type':'app',
				'default_stages':'on',
				'default_treatment_for':self.treatment_for.id,
				# 'default_patient_movement':datetime.now()
            },
		}		
		val = self.env['res.partner'].search([], order='id desc', limit=1)
		val.write({
			'name':self.patient_id.name,
			'mobile':self.phone_number,
			'patient_gender':self.gender,
			'is_patient':'True',
			})
		
		# res=self.env['medical.patient'].search([('related_field','=',self.name)])
		# for symptom in res.patient_signs_symptoms:
		# 	res.update({'patient_signs_symptoms':symptom.id})
		return ces

	@api.onchange('patient_id')
	def get_details(self):
		val = self.env['res.partner'].search([('id','=',self.patient_id.id)])
		self.phone_number = val.mobile
		self.gender=val.patient_gender

    		
	@api.onchange('whatsapp_check')
	def number_swap(self):
		if self.whatsapp_check == True:
			self.contact_number= self.phone_number



	@api.onchange('duration')
	def start_end(self):
		now  = self.appointment_date
		a_hour = relativedelta(hours=self.duration)
		vals = now + a_hour
		self.appointment_end=vals





	# def create_invoice(self):
	# 	lab_req_obj = self.env['medical.appointment']
	# 	account_invoice_obj  = self.env['account.invoice']
	# 	account_invoice_line_obj = self.env['account.invoice.line']

	# 	lab_req = lab_req_obj
	# 	if lab_req.is_invoiced == True:
	# 		raise UserError(_(' Invoice is Already Exist'))
	# 	if lab_req.no_invoice == False:
	# 		res = account_invoice_obj.create({'partner_id': lab_req.patient_id.patient_id.id,
	# 											   'date_invoice': date.today(),
	# 										 'account_id':lab_req.patient_id.patient_id.property_account_receivable_id.id,
	# 										 })

	# 		res1 = account_invoice_line_obj.create({'product_id':lab_req.consultations_id.id ,
	# 										 'product_uom': lab_req.consultations_id.uom_id.id,
	# 										 'name': lab_req.consultations_id.name,
	# 										 'product_uom_qty':1,
	# 										 'price_unit':lab_req.consultations_id.lst_price,
	# 										 'account_id': lab_req.patient_id.patient_id.property_account_receivable_id.id,
	# 										 'invoice_id': res.id})

	# 		if res:
	# 			lab_req.write({'is_invoiced': True})
	# 			imd = self.env['ir.model.data']
	# 			action = imd.xmlid_to_object('account.action_invoice_tree1')
	# 			list_view_id = imd.xmlid_to_res_id('account.view_order_form')
	# 			result = {
	# 							'name': action.name,
	# 							'help': action.help,
	# 							'type': action.type,
	# 							'views': [ [list_view_id,'form' ]],
	# 							'target': action.target,
	# 							'context': action.context,
	# 							'res_model': action.res_model,
	# 							'res_id':res.id,
	# 						}
	# 			if res:
	# 				result['domain'] = "[('id','=',%s)]" % res.id
	# 	else:
	# 		 raise UserError(_(' The Appointment is invoice exempt'))
	# 	return result

		
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
class FixAppointment(models.Model):
	_name = "fix.appointment.line"

	fixed= fields.Many2one('medical.appointment')
	dates= fields.Datetime(string="Date")
	doctors_id = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string="Doctor")
	days=fields.Selection([('monday','MONDAY'),('tuesday','TUESDAY'),('wednesday','WEDNESDAY'),('thursday','THURSDAY'),('friday','FRIDAY'),('saturday','SATURDAY'),('sunday','SUNDAY')],string='Day')
	period = fields.Selection([('mor',"MORINING"),('eve',"EVENING")],string= "Session")


	appointment_from=fields.Selection([('s1',"09:00 Am - 09:18 Am"),('s2',"09:18 Am - 09:36 Am"),('s3',"09:36 Am - 09:54 Am "),
	('s4',"09:54 Am - 10:12 Am "),('s5',"10:12 Am - 10:30 Am"),('s6',"10:30 Am - 10:48 Am "),('s7',"10:48 Am - 11:06 Am"),('s8',"11:06 Am - 11:24 Am"),
	('s9','11:24 Am - 11:42 Am'),('s10','11:42 Am - 12:00 Am'),('s11','12:00 Am - 12:18 Pm'),('s12','12:18 Pm - 12:36 Pm'),('s13','12:36 Pm - 12:54 Pm'),
	('s14','02:00 Pm - 02:18 Pm'),('s15','02:18 Pm - 02:36 Pm'),('s16','02:36 Pm - 02:54 Pm'),('s17','02:54 Pm - 03:12 Pm'),('s18','03:12 Pm - 03:30 Pm'),
	('s19','03:30 Pm - 03:48 Pm'),('s20','03:48 Pm - 04:00 Pm')]
	,string='Appointment Slot')

class time_slot(models.Model):
	_name = "time.slot"

	a1=fields.Char(string="09:00 Am - 09:18 Am")
	a2=fields.Char(string="09:18 Am - 09:36 Am")
	a3=fields.Char(string="09:36 Am - 09:54 Am")
	a4=fields.Char(string="09:54 Am - 10:12 Am")
	a5=fields.Char(string="10:12 Am - 10:30 Am")
	a6=fields.Char(string="10:30 Am - 10:48 Am")
	a7=fields.Char(string="10:48 Am - 11:06 Am")
	a8=fields.Char(string="11:06 Am - 11:24 Am")
	a9=fields.Char(string="11:24 Am - 11:42 Am")

	a10=fields.Char(string="11:42 Am - 12:00 Am")
	a11=fields.Char(string="12:00 Am - 12:18 Pm")
	a12=fields.Char(string="12:18 Pm - 12:36 Pm")
	a13=fields.Char(string="12:36 Pm - 12:54 Pm")
	a14=fields.Char(string="02:00 Pm - 02:18 Pm")
	a15=fields.Char(string="02:18 Pm - 02:36 Pm")
	a16=fields.Char(string="02:36 Pm - 02:54 Pm")
	a17=fields.Char(string="02:54 Pm - 03:12 Pm")
	a18=fields.Char(string="03:12 Pm - 03:30 Pm")
	a19=fields.Char(string="03:30 Pm - 03:48 Pm")
	a20=fields.Char(string="03:48 Pm - 04:00 Pm")

	