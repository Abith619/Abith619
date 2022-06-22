# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
import qrcode
import base64
from io import BytesIO


class res_partner(models.Model):
    _inherit = 'res.partner'


    # gender= fields.Char()
    designation = fields.Char(string='Designation')
    whatsapp=fields.Char(string='Whatsapp')
    gov_ids=fields.Binary(string="Government ID's")
    dob_contact = fields.Date(string='Date of Birth')
    password=fields.Char(string='Password')
    user_name=fields.Char(string='User Name')
    branches=fields.Char(string='Branch')
    company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company'].browse(self.env['res.company']._company_default_get('res.partner')))


    invisible=fields.Boolean(string="Boo", default=True)
    roles_selection=fields.Selection([('manager','Manager'),('reception','Reception'),('doctor','Doctor'),('pharmacy','Pharmacy'),
    ('billing','Billing'),('lab','Lab & Scan'),('telecaller','Telecaller'),('patient','Patient')],string='Roles')

    new_pt=fields.Char(string='New Patient')
    review_pt=fields.Char(string='Review Patient')
    ip=fields.Char(string='IP')
    br=fields.Char(string='BR')
    consult=fields.Char(string='Consult')
    courier=fields.Char(string='Courier')
    online=fields.Char(string='Online')

    doctor_idxs = fields.Char(string='Registration ID')

    document_type=fields.One2many('document.type.line','name',string='Documents')


    # gender = fields.Slection(string='gender')
    relationship = fields.Char(string='Relationship')
    relative_partner_id = fields.Many2one('res.partner',string="Relative_id")
    is_patient = fields.Boolean(string='Patient')
    is_person = fields.Boolean(string="Person")
    is_doctor = fields.Boolean(string="Doctor")
    is_insurance_company = fields.Boolean(string='Insurance Company')
    is_pharmacy = fields.Boolean(string="Pharmacy")
    patient_insurance_ids = fields.One2many('medical.insurance','patient_id')
    is_institution = fields.Boolean('Institution')
    company_insurance_ids = fields.One2many('medical.insurance','insurance_compnay_id','Insurance')
    reference = fields.Char('ID Number')
    patient_gender = fields.Selection([('m', 'Male'),('f', 'Female')], string ="Gender")
    # patient_gender = fields.Selection([('m', 'Male'),('f', 'Female')], string ="Sex")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
    @api.onchange('roles_selection')
    def onchange_is_patient(self):
        if self.roles_selection == 'patient':
            self.is_patient = True
        else:
            self.is_patient = False
        if self.roles_selection == 'doctor':
            self.is_doctor = True
        else:
            self.is_doctor = False
        if self.roles_selection == 'pharmacy':
            self.is_pharmacy = True
        else:
            self.is_pharmacy = False

#      QR Code

    qr_code = fields.Binary("QR Code", attachment=True, )
    barcode = fields.Char("Barcode")

    @api.onchange('name')
    def generate_qr_code(self):
        for rec in self:
            p_details={
                'Patient Id':rec.doctor_idxs,
                'Patient Name':rec.name,
                

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


    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = list(args or [])
        if name :
            args += ['|', '|' , ('name', operator, name), ('email', operator, name),
                        ('mobile', operator, name)]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)
    
    
    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         result.append((rec.id, '%s - %s' % (rec.name,rec.mobile)))
    #     return result
    def appointment_count(self):
        for res in self :
            count_appointment1 = self.env['medical.appointment'].search_count([('patient_id', '=', res.name)])
            self.count_appointment= count_appointment1
    count_appointment=fields.Integer(compute='appointment_count',string="Appointment")

    def app_count_button(self):
        return {
    'name': "Appointments",
    'domain':[('patient_id', '=', self.name)],
    'view_mode': 'tree,form',
    'res_model': 'medical.appointment',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }

    def doctor_count(self):
        for res in self :
            doctor_count_appointment1 = self.env['medical.doctor'].search_count([('patient', '=', res.name)])
            self.doctor_count_appointment= doctor_count_appointment1
    doctor_count_appointment=fields.Integer(compute='doctor_count',string="Doctor Visit")

    def doctor_count_button(self):
        return {
    'name': "Doctor Visited",
    'domain':[('patient', '=', self.name)],
    'view_mode': 'tree,form',
    'res_model': 'medical.doctor',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }

    
    
    def doctor_report(self):
        
        
        for res in self :
            doctor_report_appointment1 = self.env['medical.doctor'].search_count([('doctor', '=', res.name)])
            self.doctor_report_appointment= doctor_report_appointment1
    doctor_report_appointment=fields.Integer(compute='doctor_report',string="Doctor Report")


    def doctor_report_button(self):
        return {
    'name': "Doctor Report",
    'domain':[('doctor', '=', self.name)],
    'view_mode': 'tree,form',
    'res_model': 'medical.doctor',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }
    
    def prescription_count(self):
        for res in self :
            prescription_count_appointment1 = self.env['medical.prescription.order'].search_count([('patient_id', '=', res.name)])
            self.prescription_count_appointment= prescription_count_appointment1
    prescription_count_appointment=fields.Integer(compute='prescription_count',string="Prescriptions")

    def prescription_count_button(self):
        return {
    'name': "Prescriptions",
    'domain':[('patient_id', '=', self.name)],
    'view_mode': 'tree,form',
    'res_model': 'medical.prescription.order',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }

    def lab_count(self):
        for res in self :
            lab_count_appointment1 = self.env['medical.patient.lab.test'].search_count([('patient_id', '=', res.name)])
            self.lab_count_appointment= lab_count_appointment1
    lab_count_appointment=fields.Integer(compute='lab_count',string="Lab Test")

    def lab_count_button(self):
        return {
    'name': "Lab Test",
    'domain':[('patient_id', '=', self.name)],
    'view_mode': 'tree,form',
    'res_model': 'medical.patient.lab.test',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }

    def billing_count(self):
        for res in self :
            billing_count_appointment1 = self.env['patient.bills'].search_count([('patient_name', '=', res.name)])
            self.billing_count_appointment= billing_count_appointment1
    billing_count_appointment=fields.Integer(compute='billing_count',string="Billing")

    def billing_count_button(self):
        return {
    'name': "Billing",
    'domain':[('patient_name', '=', self.name)],
    'view_mode': 'tree,form',
    'res_model': 'patient.bills',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }

class MedicineMaster(models.Model):
    _inherit='product.product'

    is_medicine=fields.Boolean(string="Medicine")
    medicine_details = fields.One2many('medicine.line','med',string="Medicine Details")



class medicine_dose(models.Model):
    _name = 'medicine.line'

    med = fields.Many2one('product.product')
    morning=fields.Float(string="Morning")
    noon = fields.Float(string="Noon")
    evening=fields.Float(string="Evening")
    night= fields.Float(string="Night")
    units= fields.Many2one('uom.uom',string="units")
    potency = fields.Char(string="Potency")
    anupana = fields.Char(string="Anupana")

class document_type_upload(models.Model):
    _name = 'document.type.line'

    name = fields.Char(string="Name")
    document_detail=fields.Binary(string="Upload Documents")
    doc_types=fields.Selection([('gov','Gov ID'),('original','Original')],string="Document Type")
