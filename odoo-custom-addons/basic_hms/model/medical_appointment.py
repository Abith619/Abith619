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

	contact_number=fields.Char(string='Whatsapp Number')
	stages= fields.Selection([('draft',"New"),('done',"Done")],default="draft")
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
	patient_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string='Patient',required=True)
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

	patient_name=fields.Char(string="Patient Name")
	gender=fields.Selection([('m', 'Male'),('f', 'Female')],  string ="Sex", required= True)
	age= fields.Char(string="Age")
	phone_number=fields.Char(string="Contact Number")
	region= fields.Char(string="Region")	
	father_name=fields.Char(string="Father's Name")
	doctor_availability=fields.Selection([('available', 'Available'),('not available','Not Available')],  string ="Doctor Availability")
	fixed_by=fields.Many2one('res.partner',string="Appointment Fixed By")
	came_through=fields.Many2one('medical.feedback',string="How do you Came to known about 'Daisy Hospital' :")
	patient_selection = fields.Selection([('new',"New Patient"),('exi',"Existing Patient")],default="new")
	# fix_appoinment_line=fields.One2many('fix.appointment.line','fixed',string="Appoinment Slot")
	dates= fields.Date(string="Date")
	appointment_from=fields.Selection([('s1',"09:00 Am - 09:18 Am"),('s2',"09:18 Am - 09:36 Am"),('s3',"09:36 Am - 09:54 Am "),
    ('s4',"09:54 Am - 10:12 Am "),('s5',"10:12 Am - 10:30 Am"),('s6',"10:30 Am - 10:48 Am "),('s7',"10:48 Am - 11:06 Am"),('s8',"11:06 Am - 11:24 Am"),
	('s9','11:24 Am - 11:42 Am'),('s10','11:42 Am - 12:00 Am'),('s11','12:00 Am - 12:18 Pm'),('s12','12:18 Pm - 12:36 Pm'),('s13','12:36 Pm - 12:54 Pm'),
	('s14','02:00 Pm - 02:18 Pm'),('s15','02:18 Pm - 02:36 Pm'),('s16','02:36 Pm - 02:54 Pm'),('s17','02:54 Pm - 03:12 Pm'),('s18','03:12 Pm - 03:30 Pm'),
	('s19','03:30 Pm - 03:48 Pm'),('s20','03:48 Pm - 04:00 Pm')]
	,string='Appointment Slot')

	# @api.onchange('patient_id')
	# def onchange_name(self):
	# 	ins_obj = self.env['medical.insurance']
	# 	ins_record = ins_obj.search([('medical_insurance_partner_id', '=', self.patient_id.patient_id.id)])
	# 	if len(ins_record)>=1:
	# 		self.insurer_id = ins_record[0].id
	# 	else:
	# 		self.insurer_id = False

	# @api.model
	# def create(self,rec):
	# 	val = self.env['res.partner'].search([], order='id desc', limit=1)
	# 	val.write({
	# 		'mobile':self.phone_number

	# 		})
	# 	return super(medical_appointment, self).create(rec)


	@api.model
	def create(self, vals):
		vals['name'] = self.env['ir.sequence'].next_by_code('medical.appointment') or 'APT'
		msg_body = 'Appointment created'
		for msg in self:
			msg.message_post(body=msg_body)
		result = super(medical_appointment, self).create(vals)
		return result

	@api.onchange('doctor_id')
	def rolls(self):
		date_today=self.dates
		vals=self.env['medical.appointment'].search_count([('dates','=',date_today),('doctor_id','=',self.doctor_id.id)])
		if vals >= 20	:
			raise ValidationError("Appointment Slots are full")
		

	# @api.onchange('inpatient_registration_id')
	# def onchange_patient(self):
	# 	if not self.inpatient_registration_id:
	# 		self.patient_id = ""
	# 	inpatient_obj = self.env['medical.inpatient.registration'].browse(self.inpatient_registration_id.id)
	# 	self.patient_id = inpatient_obj.id

	# def confirm(self):
	# 	self.write({'state': 'confirmed'})

	# def done(self):
	# 	self.write({'state': 'done'})

	# def cancel(self):
	# 	self.write({'state': 'cancel'})

	# def print_prescription(self):
	# 	return self.env.ref('basic_hms.report_print_prescription').report_action(self)


	# def view_patient_invoice(self):
	# 	self.write({'state': 'cancel'})

	
#create new contact patient
	def button_registrations(self):
		create_registration = self.env['medical.patient'].create({
		'patient_id':self.patient_id.id,
		'sex':self.gender,
		'contact_no':self.phone_number,
		'contact_number':self.contact_number,
		'doctors':self.doctor_id.id,
		'dates':self.dates,
		'appointment_from':self.appointment_from,
		'treatment':self.treatment_for,


		'data_value':self.came_through.id,
		# 'stages':'New',
		})
		self.stages == 'done'
		val = self.env['res.partner'].search([], order='id desc', limit=1)
		val.write({
			'mobile':self.phone_number

			})
		# contact = self.env['res.partner'].create({
        # 	'name': self.name,
		# 	'mobile':self.phone_number,
		# 	'gender':self.gender,
		# 	'is_patient' :True,
        # 	})
		return create_registration

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

	a1=fields.Char(string="09:00 Am - 09:18 Am")
	a2=fields.Char(string=

    appointment_from=fields.Selection([('s1',"09:00 Am - 09:18 Am"),('s2',"09:18 Am - 09:36 Am"),('s3',"09:36 Am - 09:54 Am "),
    ('s4',"09:54 Am - 10:12 Am "),('s5',"10:12 Am - 10:30 Am"),('s6',"10:30 Am - 10:48 Am "),('s7',"10:48 Am - 11:06 Am"),('s8',"11:06 Am - 11:24 Am"),
	('s9','11:24 Am - 11:42 Am'),('s10','11:42 Am - 12:00 Am'),('s11','12:00 Am - 12:18 Pm'),('s12','12:18 Pm - 12:36 Pm'),('s13','12:36 Pm - 12:54 Pm'),
	('s14','02:00 Pm - 02:18 Pm'),('s15','02:18 Pm - 02:36 Pm'),('s16','02:36 Pm - 02:54 Pm'),('s17','02:54 Pm - 03:12 Pm'),('s18','03:12 Pm - 03:30 Pm'),
	('s19','03:30 Pm - 03:48 Pm'),('s20','03:48 Pm - 04:00 Pm')]
	,string='Appointment Slot')

