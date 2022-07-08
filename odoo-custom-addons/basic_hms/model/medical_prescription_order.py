# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
from odoo.exceptions import  ValidationError

class medical_prescription_order(models.Model):
    _name = "medical.prescription.order"
    # _description = "Prescription Order"
    _rec_name = "name"
    
    name = fields.Char('Prescription ID')
    age = fields.Char('Age')
    sex = fields.Selection([('m', 'Male'),('f', 'Female')], string ="Sex", required= True)
    height= fields.Float(string="Height")
    weight=fields.Float(string="Weight")
    stages= fields.Selection([('new',"New"),('draft','Draft'),('done',"Done")])
    treatments_for = fields.Many2many('treatment.for',string="Treatment For")

    patient_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient" ,required=True)
    prescription_date = fields.Datetime('Prescription Date', default=fields.Datetime.now)
    user_id = fields.Many2one('res.users','Login User',readonly=True, default=lambda self: self.env.user)
    no_invoice = fields.Boolean('Invoice exempt')
    inv_id = fields.Many2one('account.invoice','Invoice')
    invoice_to_insurer = fields.Boolean('Invoice to Insurance')
    doctor_id = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string="Doctor" ,required=True)
    medical_appointment_id = fields.Many2one('medical.appointment','Appointment')
    state = fields.Selection([('invoiced','To Invoiced'),('tobe','To Be Invoiced')], 'Invoice Status')
    pharmacy_partner_id = fields.Many2one('res.partner',domain=[('is_pharmacy','=',True)], string='Pharmacy')
    prescription_line_ids = fields.One2many('medical.prescription.line','name','Prescription Line')
    invoice_done= fields.Boolean('Invoice Done')
    notes = fields.Text('Prescription Note')
    appointment_id = fields.Many2one('medical.appointment')
    is_invoiced = fields.Boolean(copy=False,default = False)
    insurer_id = fields.Many2one('medical.insurance', 'Insurer')
    is_shipped = fields.Boolean(default  =  False,copy=False)
    total=fields.Float(string="Total :")
    delivery_option= fields.Selection([('dir','Direct'),('on',"Courier")],string="Delivery Option",default='dir')
    # company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company'].browse(self.env['res.company']._company_default_get('medical.prescription.order')))
    medicine_name = fields.Many2one('product.product',string='Medicine Name')

    @api.onchange('prescription_line_ids')
    def onchan_func(self):
        sums = []
        for i in self:
            for k in i.prescription_line_ids:
                sums.append(k.total_price)
            i.total = sum(sums)


    @api.model
    def create(self , vals):
        
        vals['name'] = self.env['ir.sequence'].next_by_code('medical_prescription_order')   
        res = super(medical_prescription_order, self).create(vals)
        billing = self.env['patient.bills'].search([('patient_name','=',res.patient_id.id)], order='id desc', limit=1)
        for rec in billing:
            billing_lines=[]
            for rez in res.prescription_line_ids:
                billing_value={
                    'date':datetime.now(),
                    'medicine_name':rez.medicine_name.id,
                    'prescription_id':res.name,
                    'pre_amount':res.total,                
                }
                billing_lines.append((0,0,billing_value))
            rec.write({'pres_bill':billing_lines})
        
        orm = self.env['medical.doctor'].search([('patient','=',res.patient_id.id)])
        lines=[]
        value={
            'prescription_alot':res.id,
            'date':datetime.now(),
            # 'medicine_name':res.medicine_name.id,
            'delivery_option':res.delivery_option,
            }
        lines.append((0,0,value))
        orm.write({'prescription_patient':lines})
        return res


    @api.model
    def prescription_report(self):
        return self.env.ref('basic_hms.report_print_prescription').report_action(self)



