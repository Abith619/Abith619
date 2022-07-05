from odoo import api, fields, models
from datetime import datetime, timedelta

class PatientBills(models.Model):
    _name = 'patient.bills'
    _rec_name ='bill_no'

    patient_name = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name",required=True)
    date_date = fields.Datetime(string="Bill Date",default=datetime.now())
    bills_lines = fields.One2many('patient.bills.lines','bill',string="Patient Bills")
    total_amount = fields.Float(string ='Total Amount',compute='onchan_func')
    bill_no = fields.Char('Bill No.', default='/')

    
    # total_val = fields.Monetary(string='Total Value')
    # currency_id = fields.Many2one('res.currency', store=True, readonly=True)
    # bill_amount_monetary= fields.Monetary(string="Bill Amount")
    insurance = fields.Boolean(string="Insurance if any")
    type_of_insurance= fields.Text(string='Insurance Details')
    # company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company'].browse(self.env['res.company']._company_default_get('medical.doctor')))
    doctor_id=fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor Name')
    reception_bills = fields.One2many('reception.bills','bill',string='Reception Bills')
    doctor_bill=fields.One2many('doctor.bills','bill',string='Doctor Bills')
    lab_bill=fields.One2many('lab.bills','bill',string='Doctor Bills')
    pres_bill=fields.One2many('prescription.bills','bill',string='Doctor Bills')
    total=fields.Float(string='Lab Total',compute='onchan_func_lab')
    total1=fields.Float(string='Total',compute='onchan_func_pres')
    total2=fields.Float(string='Total',compute='onchan_func_rec')

    def invoice_button(self):        
       return{
            'name': "Patient Invoice",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'account.payment',
            'context': {
                'default_partner_id':self.patient_name.id,
                'default_bill_no':self.id
                },
            }
     
    def create(self, vals):
        obj = super(PatientBills, self).create(vals)
        if obj.bill_no == '/':
            number = self.env['ir.sequence'].get('bill.sequence') or '/'
            obj.write({'bill_no': number})
        return obj
            

    @api.onchange('reception_bills')
    def onchan_func(self):
        sums = []
        sum1 = []
        sum2 = []
        for i in self:
            for k in i.reception_bills:
                if k.payment_status == False:
                    sums.append(k.bill_amount)
            for k in i.lab_bill:
                if k.payment_status == False:
                    sum1.append(k.bill_amount)
            for k in i.pres_bill:
                if k.payment_status == False:
                    sum2.append(k.pre_amount)
            i.total_amount = sum(sums+sum1+sum2)

    @api.onchange('reception_bills')
    def onchan_func_rec(self):
        sums = []
        for i in self:
            for k in i.reception_bills:
                # if k.payment_status == False:
                sums.append(k.bill_amount)
            i.total2 = sum(sums)

    @api.onchange('lab_bill')
    def onchan_func_lab(self):
        sums = []
        for i in self:
            for k in i.lab_bill:
                if k.payment_status == False:
                    sums.append(k.bill_amount)
            i.total = sum(sums)

    @api.onchange('pres_bill')
    def onchan_func_pres(self):
        sums = []
        for i in self:
            for k in i.pres_bill:
                if k.payment_status == False:
                    sums.append(k.pre_amount)
            i.total1 = sum(sums)

class Billlines(models.Model):
    _name = 'patient.bills.lines'


    bill = fields.Many2one('patient.bills')
    name= fields.Char(string="Type of  Bill")
    date= fields.Datetime(string="Bill Date")
    bill_amount =fields.Float(string='Bill Amount')
    payment_status = fields.Boolean(string="Paid",readonly=True)

class ReceptionBills(models.Model):
    _name='reception.bills'

    # patient_name = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name",required=True)
    name= fields.Char(string="Type of  Bill")
    date= fields.Datetime(string="Bill Date")
    bill = fields.Many2one('patient.bills')
    bill_amount =fields.Float(string='Bill Amount')
    payment_status = fields.Boolean(string="Paid",readonly=True)
    total=fields.Float(string="Total")

class DoctorBills(models.Model):
    _name='doctor.bills'

    # patient_name = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name",required=True)
    name= fields.Char(string="Type of  Bill")
    date= fields.Datetime(string="Bill Date")
    bill = fields.Many2one('patient.bills')
    bill_amount =fields.Float(string='Bill Amount')
    payment_status = fields.Boolean(string="Paid",readonly=True)

class LabBills(models.Model):
    _name='lab.bills'

    # patient_name = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name",required=True)
    name= fields.Char(string="Type of  Bill")
    date= fields.Datetime(string="Bill Date")
    bill = fields.Many2one('patient.bills')
    bill_amount =fields.Float(string='Bill Amount')
    payment_status = fields.Boolean(string="Paid",readonly=True)
    test_name=fields.Char(string="Test Name")
    test_types=fields.Char(string="Test Type")
    total=fields.Float(string="Total")

class PrescriptionBills(models.Model):
    _name='prescription.bills'

    # patient_name = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name",required=True)
    name= fields.Char(string="Type of  Bill")
    date= fields.Datetime(string="Bill Date")
    bill = fields.Many2one('patient.bills')
    pre_amount =fields.Float(string='Bill Amount',related='medicine_name.lst_price')
    payment_status = fields.Boolean(string="Paid",readonly=True)
    medicine_name = fields.Many2one('product.product',string='Medicine Name')
    prescription_id = fields.Char(string="Prescription ID")
    total=fields.Float(string="Total")


class Billingpayment(models.Model):
    _inherit='account.payment'

    bill_lines = fields.One2many('account.bills.lines','bill',string='Patient Bills')
    bill_no = fields.Many2one('patient.bills',string="Bill No")

    @api.onchange('bill_no')
    def onchange_bill(self):
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.bill_no.bills_lines:
                val={
                    'name': line.name,
                    'date':line.date,
                    'bill_amount':line.bill_amount,
                }
                lines.append((0,0,val))
            rec.bill_lines=lines
            self.amount = self.bill_no.total_amount

class Paymentlines(models.Model):
    _name = 'account.bills.lines'

    bill = fields.Many2one('account.payment')
    name= fields.Char(string="Type of  Bill")
    date= fields.Datetime(string="Bill Date")
    bill_amount =fields.Float(string='Bill Amount')
    payment_status = fields.Boolean(string="Paid",readonly=True)


