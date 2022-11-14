# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
from odoo.exceptions import  ValidationError

class medical_prescription_order(models.Model):
    _name = "medical.prescription.order"
    
    company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company']._company_default_get('medical.patient.lab.test'))
    name = fields.Char('Prescription ID')
    age = fields.Char('Age')
    sex = fields.Selection([('m', 'Male'),('f', 'Female')], string ="Sex", required= True)
    height= fields.Float(string="Height")
    weight=fields.Float(string="Weight")
    stages= fields.Selection([('new',"New"),('draft','Draft'),('done',"Done")])
    treatments_for = fields.Many2many('treatment.for',string="Treatment For")
    write_date=fields.Date(string='Date')
    ebook_id = fields.Char(string='Patient ID')
    prescribed_by=fields.Many2one('res.users',string='Appointment By',default=lambda self: self.env.user,readonly='1')

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
    medicine_name = fields.Many2one('product.product',string='Medicine Name')
    bf_af=fields.Selection([('before','Before Food'),('after','After Food')],string='BF - AF')
    delivery_option= fields.Selection([('dir','Direct'),('on',"Online")],string="Delivery Option",default='dir')
    courier_option = fields.Selection([('domestic','Domestic'),('international',"International")],string='Courier')
    num_days = fields.Selection([('ed','edit'),('e','ebook'),('1','Day1'),('2','Day2'),('3','Day3'),('4','Day4'),('5','Day5'),
                                ('6','Day6'),('7','Day7'),('8','Day8'),('9','Day9'),('10','Day10')])

    @api.onchange('prescription_line_ids')
    def onchan_func(self):
        sums = []
        for i in self:
            for k in i.prescription_line_ids:
                sums.append(k.total_price)
            i.total = sum(sums)
            
    @api.constrains('patient_id')
    def write_lab(self):
        orm_e = self.env['medical.doctor'].search([('patient','=',self.patient_id.id)])
        orm_e.write({'patient_activity' : 'pres'})
        
        orm = self.env['medical.patient'].search([('patient_id','=',self.patient_id.id)])
        orm.write({'patient_activity' : 'pres'})
        
        # self.patient_a
            
    # @api.constrains('prescription_line_ids.medicine_name')
    def write(self, vals):
        orm = self.env['patient.bills'].search([('pres_bill.prescription_id','=',self.name)]).write({'pres_bill':[(5, 0, 0)]})
        return orm
        # orm_med = self.env['patient.bills'].browse([(orm.pres_bill.medicine_name)])
        # orm_id = self.env['patient.bills'].browse([(orm)])
        # med_id = self.prescription_line_ids.medicine_name
        # raise ValidationError(type(med_id))
        
        # for line in orm_med:
        #     if line not in med_id:
        #         return orm_id.unlink()
        #     else:
        #         pass
                # self.orm_id = [(5,0,0)]
                
        # orm_update = self.env['prescription.bills'].search([('prescription_id', '=', self.name)])
        # orm__med = self.env['patient.bills'].search([('pres_bill.medicine_name', '=', self.prescription_line_ids.medicine_name.id)])
        # billing_lines=[]
        # for i in self.prescription_line_ids:
        #     billing_value ={
        #         'date':self.write_date,
        #         'medicine_name':i.medicine_name.id,
        #         'prescription_id':self.name,
        #         'pre_amount':self.total,
        #         'delivery_mode':self.courier_option,
        #     }
            # orm_update.write(0,0,{
            #     'date':self.write_date,
            #     'medicine_name':i.medicine_name.id,
            #     'prescription_id':self.name,
            #     'pre_amount':self.total,
            #     'delivery_mode':self.courier_option,
            # })
        #     billing_lines.append((2,0,billing_value))
        # orm.update({'pres_bill':billing_lines})
        # orm_update.update({billing_data})
        

    @api.model
    def create(self , vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('medical.prescription.order') or '/'   
        res = super(medical_prescription_order, self).create(vals)
        if res.num_days == 'e':
            billing = self.env['patient.bills'].search([('patient_name','=',res.patient_id.id)], order='id desc', limit=1)
            for rec in billing:
                billing_lines=[]
                for rez in res.prescription_line_ids:
                    billing_value = {
                        'date':datetime.now(),
                        'medicine_name':rez.medicine_name.id,
                        'prescription_id':res.name,
                        'pre_amount':res.total,
                        'delivery_mode':res.courier_option,                
                            }
                    billing_lines.append((0,0,billing_value))
                rec.write({'pres_bill':billing_lines})
                
            orm = self.env['medical.doctor'].search([('patient','=',res.patient_id.id)])
            lines=[]
            value={
                'prescription_alot':res.id,
                'date':datetime.now(),
                'patient_name':res.patient_id.id,
                'delivery_option':res.delivery_option,
                'delivery_mode':res.courier_option,
                }
            lines.append((0,0,value))
            orm.write({'prescription_patient':lines,
                    'medicine_id':res.id})

        if res.num_days == '1':
            billing = self.env['patient.bills'].search([('patient_name','=',res.patient_id.id)], order='id desc', limit=1)
            orm_id = self.env['in.patient'].search([('patient_id','=',res.patient_id.id)])
            
            for rec in billing:
                billing_lines=[]
                for rez in res.prescription_line_ids:
                    billing_value={
                        'date':datetime.now(),
                        'medicine_name':rez.medicine_name.id,
                        'prescription_id':res.name,
                        'pre_amount':res.total,
                        'delivery_mode':res.courier_option,                
                        }
                    billing_lines.append((0,0,billing_value))
                rec.write({'inpatient_tablet':billing_lines})
            lines=[]
            value={
                'prescription_alot':res.id,
                'date':datetime.now(),
                'patient_name':res.patient_id.id,
                }
            lines.append((0,0,value))
            orm_id.write({'medicine_line':lines})
            
            
            
        elif res.num_days == '2':
            billing = self.env['patient.bills'].search([('patient_name','=',res.patient_id.id)], order='id desc', limit=1)
            orm_id = self.env['in.patient'].search([('patient_id','=',res.patient_id.id)])
            for rec in billing:
                billing_lines=[]
                for rez in res.prescription_line_ids:
                    billing_value={
                        'date':datetime.now(),
                        'medicine_name':rez.medicine_name.id,
                        'prescription_id':res.name,
                        'pre_amount':res.total,
                        'delivery_mode':res.courier_option,                
                        }
                    billing_lines.append((0,0,billing_value))
                rec.write({'inpatient_tablet':billing_lines})            
            lines=[]
            value={
                'prescription_alot':res.id,
                'date':datetime.now(),
                'patient_name':res.patient_id.id,
                }
            lines.append((0,0,value))
            orm_id.write({'medicine_line_two':lines})
            
        elif res.num_days == '3':
            billing = self.env['patient.bills'].search([('patient_name','=',res.patient_id.id)], order='id desc', limit=1)
            orm_id = self.env['in.patient'].search([('patient_id','=',res.patient_id.id)])
            for rec in billing:
                billing_lines=[]
                for rez in res.prescription_line_ids:
                    billing_value={
                        'date':datetime.now(),
                        'medicine_name':rez.medicine_name.id,
                        'prescription_id':res.name,
                        'pre_amount':res.total,
                        'delivery_mode':res.courier_option,                
                        }
                    billing_lines.append((0,0,billing_value))
                rec.write({'inpatient_tablet':billing_lines})            
            lines=[]
            value={
                'prescription_alot':res.id,
                'date':datetime.now(),
                'patient_name':res.patient_id.id,
                }
            lines.append((0,0,value))
            orm_id.write({'medicine_line_three':lines})
            
        elif res.num_days == '4':
            billing = self.env['patient.bills'].search([('patient_name','=',res.patient_id.id)], order='id desc', limit=1)
            orm_id = self.env['in.patient'].search([('patient_id','=',res.patient_id.id)])
            for rec in billing:
                billing_lines=[]
                for rez in res.prescription_line_ids:
                    billing_value={
                        'date':datetime.now(),
                        'medicine_name':rez.medicine_name.id,
                        'prescription_id':res.name,
                        'pre_amount':res.total,
                        'delivery_mode':res.courier_option,                
                        }
                    billing_lines.append((0,0,billing_value))
                rec.write({'inpatient_tablet':billing_lines})            
            lines=[]
            value={
                'prescription_alot':res.id,
                'date':datetime.now(),
                'patient_name':res.patient_id.id,
                }
            lines.append((0,0,value))
            orm_id.write({'medicine_line_four':lines})
            
        elif res.num_days == '5':
            billing = self.env['patient.bills'].search([('patient_name','=',res.patient_id.id)], order='id desc', limit=1)
            orm_id = self.env['in.patient'].search([('patient_id','=',res.patient_id.id)])
            for rec in billing:
                billing_lines=[]
                for rez in res.prescription_line_ids:
                    billing_value={
                        'date':datetime.now(),
                        'medicine_name':rez.medicine_name.id,
                        'prescription_id':res.name,
                        'pre_amount':res.total,
                        'delivery_mode':res.courier_option,                
                        }
                    billing_lines.append((0,0,billing_value))
                rec.write({'inpatient_tablet':billing_lines})            
            lines=[]
            value={
                'prescription_alot':res.id,
                'date':datetime.now(),
                'patient_name':res.patient_id.id,
                }
            lines.append((0,0,value))
            orm_id.write({'medicine_line_five':lines})
            
        elif res.num_days == '6':
            billing = self.env['patient.bills'].search([('patient_name','=',res.patient_id.id)], order='id desc', limit=1)
            orm_id = self.env['in.patient'].search([('patient_id','=',res.patient_id.id)])
            for rec in billing:
                billing_lines=[]
                for rez in res.prescription_line_ids:
                    billing_value={
                        'date':datetime.now(),
                        'medicine_name':rez.medicine_name.id,
                        'prescription_id':res.name,
                        'pre_amount':res.total,
                        'delivery_mode':res.courier_option,                
                        }
                    billing_lines.append((0,0,billing_value))
                rec.write({'inpatient_tablet':billing_lines})            
            lines=[]
            value={
                'prescription_alot':res.id,
                'date':datetime.now(),
                'patient_name':res.patient_id.id,
                }
            lines.append((0,0,value))
            orm_id.write({'medicine_line_six':lines})
            
        elif res.num_days == '7':
            billing = self.env['patient.bills'].search([('patient_name','=',res.patient_id.id)], order='id desc', limit=1)
            orm_id = self.env['in.patient'].search([('patient_id','=',res.patient_id.id)])
            for rec in billing:
                billing_lines=[]
                for rez in res.prescription_line_ids:
                    billing_value={
                        'date':datetime.now(),
                        'medicine_name':rez.medicine_name.id,
                        'prescription_id':res.name,
                        'pre_amount':res.total,
                        'delivery_mode':res.courier_option,                
                        }
                    billing_lines.append((0,0,billing_value))
                rec.write({'inpatient_tablet':billing_lines})            
            lines=[]
            value={
                'prescription_alot':res.id,
                'date':datetime.now(),
                'patient_name':res.patient_id.id,
                }
            lines.append((0,0,value))
            orm_id.write({'medicine_line_seven':lines})
            
        elif res.num_days == '8':
            billing = self.env['patient.bills'].search([('patient_name','=',res.patient_id.id)], order='id desc', limit=1)
            orm_id = self.env['in.patient'].search([('patient_id','=',res.patient_id.id)])
            for rec in billing:
                billing_lines=[]
                for rez in res.prescription_line_ids:
                    billing_value={
                        'date':datetime.now(),
                        'medicine_name':rez.medicine_name.id,
                        'prescription_id':res.name,
                        'pre_amount':res.total,
                        'delivery_mode':res.courier_option,                
                        }
                    billing_lines.append((0,0,billing_value))
                rec.write({'inpatient_tablet':billing_lines})            
            lines=[]
            value={
                'prescription_alot':res.id,
                'date':datetime.now(),
                'patient_name':res.patient_id.id,
                }
            lines.append((0,0,value))
            orm_id.write({'medicine_line_eight':lines})
            
        elif res.num_days == '9':
            billing = self.env['patient.bills'].search([('patient_name','=',res.patient_id.id)], order='id desc', limit=1)
            orm_id = self.env['in.patient'].search([('patient_id','=',res.patient_id.id)])
            for rec in billing:
                billing_lines=[]
                for rez in res.prescription_line_ids:
                    billing_value={
                        'date':datetime.now(),
                        'medicine_name':rez.medicine_name.id,
                        'prescription_id':res.name,
                        'pre_amount':res.total,
                        'delivery_mode':res.courier_option,                
                        }
                    billing_lines.append((0,0,billing_value))
                rec.write({'inpatient_tablet':billing_lines})            
            lines=[]
            value={
                'prescription_alot':res.id,
                'date':datetime.now(),
                'patient_name':res.patient_id.id,
                }
            lines.append((0,0,value))
            orm_id.write({'medicine_line_nine':lines})
            
        elif res.num_days == '10':
            billing = self.env['patient.bills'].search([('patient_name','=',res.patient_id.id)], order='id desc', limit=1)
            orm_id = self.env['in.patient'].search([('patient_id','=',res.patient_id.id)])
            for rec in billing:
                billing_lines=[]
                for rez in res.prescription_line_ids:
                    billing_value={
                        'date':datetime.now(),
                        'medicine_name':rez.medicine_name.id,
                        'prescription_id':res.name,
                        'pre_amount':res.total,
                        'delivery_mode':res.courier_option,                
                        }
                    billing_lines.append((0,0,billing_value))
                rec.write({'inpatient_tablet':billing_lines})            
            lines=[]
            value={
                'prescription_alot':res.id,
                'date':datetime.now(),
                'patient_name':res.patient_id.id,
                }
            lines.append((0,0,value))
            orm_id.write({'medicine_line_ten':lines})
        
        
        

        picking_list=[]
        for rec in res.prescription_line_ids:
            for data in rec:
                datas={
                    'name':'Prescribed Medicine',
                    'product_id':data.medicine_name,
                    'product_uom_qty':data.prescribed_quantity,
                    'product_uom':data.units
                }
            picking_list.append((0,0,datas))
        company_orm = self.env['stock.picking.type'].search([('company_id','=',res.company_id.id),('sequence_code','=','OUT')])
        company_orm_id=company_orm[0]['id']

        company_orm_1 = self.env['stock.location'].search([('company_id','=',res.company_id.id),('usage','=','internal')])
        company_orm_id_1=company_orm_1[0]['id']

        company_orm_2 = self.env['stock.location'].search([('usage','=','customer')])
        company_orm_id_2=company_orm_2[0]['id']
        
        picking_data={
            'partner_id':res.patient_id.id,
            'picking_type_id':company_orm_id,
            'location_id':company_orm_id_1,
            'location_dest_id':company_orm_id_2,
            'prescerption_ids':res.id,
            'move_ids_without_package':picking_list          
        } 

        picking_orm = self.env['stock.picking'].create(picking_data)
        return res


    @api.model
    def prescription_report(self):
        return self.env.ref('basic_hms.report_print_prescription').report_action(self)



class Pickinginherit(models.Model):
    _inherit='stock.picking'

    prescerption_ids=fields.Many2one('medical.prescription.order',string="Prescription Id")
    partner_ids = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Delivery Contact")



class Pickingline_inherit(models.Model):
    _inherit='stock.move'


    user_id = fields.Many2one('res.users',string="User Name",readonly=True,store=True)
    pin_num = fields.Char(string="Pin Number",default="")


    @api.onchange('pin_num')
    def get_user(self):
        if self.pin_num != "":
            user_orm = self.env['res.users'].search([('otp_num','=',self.pin_num)])
            if user_orm:
                for rec in user_orm:
                    self.user_id = rec.id
            else:
                raise ValidationError('Invalid Pin')

                
            

