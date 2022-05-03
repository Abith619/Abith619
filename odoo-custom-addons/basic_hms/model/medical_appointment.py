# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
#from datetime import datetime, date
from datetime import datetime, timedelta
from odoo.exceptions import UserError
import datetime
from dateutil.relativedelta import relativedelta

class medical_appointment(models.Model):
    _name = "medical.appointment"
    _inherit = 'mail.thread'

    name = fields.Char(string="Appointment ID", readonly=True ,copy=True)
    gender=fields.Selection([('m', 'Male'),('f', 'Female')],  string ="Sex", required= True)
    age= fields.Char(string="Age")
    phone_number=fields.Char(string="Contact Number")
    region= fields.Char(string="Address")
    father_name=fields.Char(string="Father's Name")
    doctor_availability=fields.Selection([('available', 'Available'),('not available','Not Available')],  string ="Doctor Availability", required= True)
    fixed_by=fields.Many2one('res.partner',string="Appointment Fixed By")
    came_through=fields.Many2one('medical.feedback',string="How do you Came to known about 'Daisy Hospital' :")
    is_invoiced = fields.Boolean(copy=False,default = False)
    institution_partner_id = fields.Many2one('res.partner',domain=[('is_institution','=',True)],string="Health Center")
    inpatient_registration_id = fields.Many2one('medical.inpatient.registration',string="Inpatient Registration")
    patient_status = fields.Selection([
            ('outpatient', 'Outpatient'),
            ('inpatient', 'Inpatient'),
        ], 'Patient status', sort=False,default='outpatient')
    patient_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient",required=True)
    urgency_level = fields.Selection([
            ('a', 'Normal'),
            ('b', 'Urgent'),
            ('c', 'Medical Emergency'),
        ], 'Urgency Level', sort=False,default="b")
    appointment_date = fields.Datetime('Appointment Date',required=True,default = fields.Datetime.now)
    appointment_end = fields.Datetime('Appointment End',required=True)
    doctor_id = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string="Doctor ",required=True)
    no_invoice = fields.Boolean(string='Invoice exempt')
    validity_status = fields.Selection([
            ('invoice', 'Invoice'),
            ('tobe', 'To be Invoiced'),
        ], 'Status', sort=False,readonly=True,default='tobe')
    appointment_validity_date = fields.Datetime('Validity Date')
    consultations_id = fields.Many2one('product.product','Consultation Service')
    comments = fields.Text(string="Info")
    state = fields.Selection([('draft','Draft'),('reg','Registered'),('cancel','Cancel')],string="State",default='draft')
    invoice_to_insurer = fields.Boolean('Invoice to Insurance')
    medical_patient_psc_ids = fields.Many2many('medical.patient.psc',string='Pediatrics Symptoms Checklist')
    medical_prescription_order_ids = fields.One2many('medical.prescription.order','appointment_id',string='Prescription')
    insurer_id = fields.Many2one('medical.insurance','Insurer')
    duration = fields.Integer('Duration')
    stage= fields.Selection([('new',"New"),('reg',"Registred"),('cancel',"Cancelled")])

    # @api.onchange('patient_id')
    # def onchange_name(self):
    #     ins_obj = self.env['medical.insurance']
    #     ins_record = ins_obj.search([('medical_insurance_partner_id', '=', self.patient_id.patient_id.id)])
    #     if len(ins_record)>=1:
    #         self.insurer_id = ins_record[0].id
    #     else:
    #         self.insurer_id = False


    @api.onchange('duration')
    def start_end(self):
        now  = self.appointment_date
        a_hour = relativedelta(hours=self.duration)
        vals = now + a_hour
        self.appointment_end=vals

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('medical.appointment') or 'APT'
        msg_body = 'Appointment created'
        self.message_post(body=msg_body)
        result = super(medical_appointment, self).create(vals)
        return result

    @api.onchange('inpatient_registration_id')
    def onchange_patient(self):
        if not self.inpatient_registration_id:
            self.patient_id = ""
        inpatient_obj = self.env['medical.inpatient.registration'].browse(self.inpatient_registration_id.id)
        self.patient_id = inpatient_obj.id

    @api.multi
    def confirm(self):
        self.write({'state': 'confirmed'})

    @api.multi
    def done(self):
        self.write({'state': 'done'})

    @api.multi
    def cancel(self):
        self.write({'state': 'cancel'})

    @api.multi
    def print_prescription(self):
        return self.env.ref('basic_hms.report_print_prescription').report_action(self)


    @api.multi
    def view_patient_invoice(self):
        self.write({'state': 'cancel'})

    @api.multi
    def create_invoice(self):
        lab_req_obj = self.env['medical.appointment']
        account_invoice_obj  = self.env['account.invoice']
        account_invoice_line_obj = self.env['account.invoice.line']

        lab_req = lab_req_obj
        if lab_req.is_invoiced == True:
            raise UserError(_(' Invoice is Already Exist'))
        if lab_req.no_invoice == False:
            res = account_invoice_obj.create({'partner_id': lab_req.patient_id.patient_id.id,
                                                   'date_invoice': date.today(),
                                             'account_id':lab_req.patient_id.patient_id.property_account_receivable_id.id,
                                             })

            res1 = account_invoice_line_obj.create({'product_id':lab_req.consultations_id.id ,
                                             'product_uom': lab_req.consultations_id.uom_id.id,
                                             'name': lab_req.consultations_id.name,
                                             'product_uom_qty':1,
                                             'price_unit':lab_req.consultations_id.lst_price,
                                             'account_id': lab_req.patient_id.patient_id.property_account_receivable_id.id,
                                             'invoice_id': res.id})

            if res:
                lab_req.write({'is_invoiced': True})
                imd = self.env['ir.model.data']
                action = imd.xmlid_to_object('account.action_invoice_tree1')
                list_view_id = imd.xmlid_to_res_id('account.view_order_form')
                result = {
                                'name': action.name,
                                'help': action.help,
                                'type': action.type,
                                'views': [ [list_view_id,'form' ]],
                                'target': action.target,
                                'context': action.context,
                                'res_model': action.res_model,
                                'res_id':res.id,
                            }
                if res:
                    result['domain'] = "[('id','=',%s)]" % res.id
        else:
             raise UserError(_(' The Appointment is invoice exempt'))
        return result


    # @api.multi    
    # def button_registrations(self):
    #     contact={
    #     'name': "Registartion",
    #     'type': 'ir.actions.act_window',
    #     'view_type': 'form',
    #     'view_mode': 'form',
    #     'res_model': 'medical.patient',
    #     'context': {
    #         # 'default_name_id': self.patient.id,
    #         'default_doctor': self.doctor_id.id,
    #         # 'default_prescription_date': self.prescription_date,
    #         'default_patient_id': self.patient_id.id,
    #         'default_contact_no': self.phone_number,
    #         'default_sex': self.gender,
    #         'default_data-value':self.came_through,
    #     },
    #     'target': 'new'
    # }
    #     self.stage = 'reg'
    #     return contact

    @api.multi
    # def button_registrations(self):
    #     create_patient = self.env['medical.patient'].create({  
    #         # 'default_name_id': self.patient.id,
    #         'default_doctor': self.doctor_id.id,
    #         # 'default_prescription_date': self.prescription_date,
    #         # 'default_patient_id': self.patient_id.id,
    #         'default_contact_no': self.phone_number,
    #         'default_sex': self.gender,
    #         'default_data-value':self.came_through,
    #     })

    @api.multi
    def button_registrations(self):
        create_registration = self.env['medical.patient'].create({
            'patient_id':self.patient_id.id ,
            'age':self.age, 
            'doctor':self.doctor_id.id,
            'contact_no':self.phone_number,
            'sex':self.gender,
            'data_value':self.came_through.id,
            'father_name':self.father_name,
            
        })
        self.state='reg'


        
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
