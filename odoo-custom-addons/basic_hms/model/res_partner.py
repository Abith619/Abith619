# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
import qrcode
import base64
from io import BytesIO
import pytz
from datetime import datetime, timedelta
from odoo.exceptions import  ValidationError


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
    # company_id=fields.Many2one('res.company',string='Branch')
    company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company']._company_default_get('res.partner'))

    invisible=fields.Boolean(string="Boo", default=True)

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
    is_reception = fields.Boolean(string='Reception')
    lab_scan = fields.Boolean(string='Lab & Scan')
    is_billing = fields.Boolean(string='Billing')
    is_telecaller = fields.Boolean(string='Telecaller')
    roles_selection=fields.Selection([('manager','Manager'),('reception','Reception'),('doctor','Doctor'),('pharmacy','Pharmacy'),
    ('billing','Billing'),('lab','Lab & Scan'),('telecaller','Telecaller'),('patient','Patient')],string='Roles')
    ebook_print=fields.Many2one('medical.doctor', string='Ebook',compute='orm_ebook')
    experience = fields.Char(string='Experience')
    marital_status = fields.Selection([('s','Single'),('m','Married'),('w','Widowed'),('d','Divorced'),('x','Seperated')],string='Marital Status')
    treatment_for=fields.Many2one('medical.pathology',string="Treatment For")
    abroad_addr = fields.Char(string='Abroad Address')
    
    patient_activity = fields.Selection([('wait',"Waiting"),('doctor',"Doctor Assigned"),('doc','Diet Assigned'),
                                         ('lab','Lab Bill Assigned'),('pres','Pharmacy Bill Assigned'),('scan','Scan Bill Assigned'),
                                         ('labs','Lab Test Completed'),('scans','Scan Test Completed'),
                                         ('bill',"Pharmacy Bill Assigned"),('discontinued','Discontinued'),('completed',"Completed")],default='wait')
    gst_num = fields.Char(string='GST NO :')
    is_vendor = fields.Boolean(string='Vendor')
    file_num = fields.Char(string='File Number')

    
    def orm_ebook(self):
        orm=self.env['medical.doctor'].search([('patient','=',self.name)])
        self.ebook_print = orm

    # @api.model
    # def create(self, vals):
    #     vals['serial_number'] = self.env['ir.sequence'].next_by_code('res.partner') or 'RES'
    #     res = super(res_partner, self).create(vals)
    #     return res


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
    @api.constrains('roles_selection')
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
        if self.roles_selection == 'reception':
            self.is_reception = True
        else:
            self.is_reception = False
        if self.roles_selection == 'lab':
            self.lab_scan = True
        else:
            self.lab_scan = False
        if self.roles_selection == 'telecaller':
            self.is_telecaller = True
        else:
            self.is_telecaller = False
        if self.roles_selection == 'billing':
            self.is_billing = True
        else:
            self.is_billing = False
        if self.roles_selection == 'vendor':
            self.is_vendor = True
        else:
            self.is_vendor = False


#      QR Code

    qr_code = fields.Binary("QR Code", attachment=True, compute='generate_qr_code')
    barcode = fields.Char("Barcode")

    # @api.onchange('name')
    def generate_qr_code(self):
        for rec in self:
            p_details={
                'Id':rec.doctor_idxs,
                'Name':rec.name,
                

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
            lab_count_appointment1 = self.env['lab.scan.form'].search_count([('patient_id', '=', res.name)])
            self.lab_count_appointment= lab_count_appointment1
    lab_count_appointment=fields.Integer(compute='lab_count',string="Lab Test")

    def lab_count_button(self):
        return {
    'name': "Lab Test",
    'domain':[('patient_id', '=', self.name)],
    'view_mode': 'tree,form',
    'res_model': 'lab.scan.form',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }

    def scan_count(self):
        for res in self :
            scan_count_appointment1 = self.env['scan.test'].search_count([('patient_id', '=', res.name)])
            self.scan_count_appointment= scan_count_appointment1
    scan_count_appointment=fields.Integer(compute='scan_count',string="Scan Test")

    def scan_count_button(self):
        return {
            'name': "Scan Test",
            'domain':[('patient_id', '=', self.name)],
            'view_mode': 'tree,form',
            'res_model': 'scan.test',
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

    def document_count(self):
        
        for res in self :
            document_count_appointment1 = self.env['document.type.line'].search_count([('name', '=', res.name)])
            self.document_count_appointment= document_count_appointment1
    document_count_appointment=fields.Integer(compute='document_count',string="Green Documents")

    def document_count_button(self):
        return {
    'name': "Document",
    'domain':[('name', '=', self.name)],
    'view_mode': 'tree,form',
    'res_model': 'document.type.line',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    'context': {
        'default_name': self.name,
        },

    }
class account_organic(models.Model):
    _inherit = 'account.move'

    product_id = fields.Many2one('product.product', domain=[('is_organic','=',True)])
    gst_total = fields.Float(string='GST', compute='gst_amount')

    @api.depends('amount_total','amount_untaxed')
    def gst_amount(self):
        
        self.gst_total = (self.amount_total - self.amount_untaxed)

class MedicineMaster(models.Model):
    _inherit='product.product'

    is_medicine=fields.Boolean(string="Medicine")
    medicine_details = fields.One2many('medicine.line','med',string="Medicine Details")
    company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company']._company_default_get('product.product'))
    is_organic = fields.Boolean(string="Organic")

class medicine_dose(models.Model):
    _name = 'medicine.line'

    med = fields.Many2one('product.product')
    morning=fields.Float(string="Morning")
    all_day=fields.Char(string="Dose")
    noon = fields.Float(string="Noon")
    evening=fields.Float(string="Evening")
    night= fields.Float(string="Night")
    units= fields.Many2one('uom.uom',string="units")
    potency = fields.Char(string="Potency")
    anupana = fields.Char(string="Notes")
    bf_af=fields.Selection([('before','Before Food'),('after','After Food')])

class document_type_upload(models.Model):
    _name = 'document.type.line'

    name = fields.Char(string="Patient Name")
    patient_id = fields.Many2one('res.partner',string='Name')
    document_detail=fields.Binary(string="Upload Documents")
    doc_types=fields.Selection([('voice','Voice Recording'),('ebook','Ebook'),('Video','Video'),('photo','Photo'),('green','Green Document'),('gov','Gov ID'),
        ('original','Original'),('lab','Lab Document'),('scan','Scan Document')],string="Document Type")
    
    document_line = fields.One2many('document.add.line','Documents',string='Document Lines')
    attach_types = fields.Selection([('voice','Voice Recording'),('Video','Video'),('ebook','Ebook'),('photo','Photo'),('green','Green Document'),('gov','Gov ID'),
        ('original','Original'),('lab','Lab Document'),('scan','Scan Document')],string='Attachment Type')

    
    @api.constrains('document_line')
    def pat_stat(self):
        if self.attach_types == 'lab':
            orm_1 = self.env['lab.scan.form'].search([('patient_id','=',self.name)])
            orm_1.write({'patient_activity':'labs'})
            
            orm = self.env['medical.patient'].search([('patient_id','=',self.name)])
            orm.write({'patient_activity':'labs'})
            
            orm1 = self.env['medical.doctor'].search([('patient','=',self.name)])
            orm1.write({'patient_activity':'labs'})
            
            orm_3 = self.env['res.partner'].search([('name','=',self.name)])
            orm_3.write({'patient_activity':'labs'})
            
            orm_4 = self.env['patient.bills'].search([('patient_name','=',self.name)])
            orm_4.write({'patient_activity':'labs'})
            
        if self.attach_types == 'scan':
            orm_2 = self.env['scan.test'].search([('patient_id','=',self.name)])
            orm_2.write({'patient_activity':'scans'})
            
            orm = self.env['medical.patient'].search([('patient_id','=',self.name)])
            orm.write({'patient_activity':'scans'})
            
            orm1 = self.env['medical.doctor'].search([('patient','=',self.name)])
            orm1.write({'patient_activity':'scans'})
            
            orm_3 = self.env['res.partner'].search([('name','=',self.name)])
            orm_3.update({'patient_activity':'scans'})
        
            orm_4 = self.env['patient.bills'].search([('patient_name','=',self.name)])
            orm_4.write({'patient_activity':'scans'})


    @api.model
    def create(self, vals):
        result = super(document_type_upload,self).create(vals)
        orm_i = self.env['medical.doctor'].search([('patient', '=',result.name)])
        
        lines=[]
        for i in result.document_line:
            values={
                'report_name':i.attach_types,
                'attachment':i.attachment,
            }
            lines.append((0,0,values))
            
        orm_i.write({'documents':lines})
        return result


    
class documentAddLine(models.Model):
    _name = 'document.add.line'
    
    Documents = fields.Many2one('document.type.line',string='Document')
    name = fields.Char(string='Patient Document')
    attachment = fields.Many2many('ir.attachment',string='Attach')
    attach_types = fields.Selection([('voice','Voice Recording'),('Video','Video'),('photo','Photo'),('green','Green Document'),('gov','Gov ID'),
        ('original','Original'),('lab','Lab Document'),('scan','Scan Document')])

    date_write = fields.Date(string='Date')

class ir_sequence_master(models.Model):
    _inherit = 'ir.sequence'

    def _get_prefix_suffix(self):
        def _interpolate(s, d):
            return (s % d) if s else ''

        def _interpolation_dict():
            now = range_date = effective_date = datetime.now(pytz.timezone(self._context.get('tz') or 'UTC'))
            if self._context.get('ir_sequence_date'):
                effective_date = fields.Datetime.from_string(self._context.get('ir_sequence_date'))
            if self._context.get('ir_sequence_date_range'):
                range_date = fields.Datetime.from_string(self._context.get('ir_sequence_date_range'))

            sequences = {
                'year': '%Y', 'month': '%m', 'day': '%d', 'y': '%y', 'doy': '%j', 'woy': '%W',
                'weekday': '%w', 'h24': '%H', 'h12': '%I', 'min': '%M', 'sec': '%S'
            }
            if range_date:
                ay = str(range_date.year)[2:] + '-' + \
                    str(range_date.year + 1)[2:]
                sequences.update({'ay': ay, 'month_text': '%b'})
            res = {}
            for key, format in sequences.items():
                res[key] = effective_date.strftime(format)
                res['range_' + key] = range_date.strftime(format)
                res['current_' + key] = now.strftime(format)

            return res

        d = _interpolation_dict()
        try:
            interpolated_prefix = _interpolate(self.prefix, d)
            interpolated_suffix = _interpolate(self.suffix, d)
        except ValueError:
            raise ValidationError(_('Invalid prefix or suffix for sequence \'%s\'') % (self.get('name')))
        return interpolated_prefix, interpolated_suffix
