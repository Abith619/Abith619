from socket import SOL_CAN_RAW
from odoo import api, fields, models
from datetime import datetime, timedelta

class PatientBills(models.Model):
    _name = 'patient.bills'
    _rec_name ='bill_no'

    patient_name = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name",required=True)
    date_date = fields.Datetime(string="Bill Date",default=datetime.now())
    bills_lines = fields.One2many('patient.bills.lines','bill',string="Patient Bills")
    total_amount = fields.Float(string ='Due Amount',compute='onchan_func',store=True)
    bill_no = fields.Char('Bill No.', default='/')

    company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company']._company_default_get('medical.prescription.order'))
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
    scan_bill=fields.One2many('scan.bills','bill',string='Scan-Test Bills')
    pres_bill=fields.One2many('prescription.bills','bill',string='Doctor Bills')
    total=fields.Float(string='Lab Total',compute='onchan_func_lab')
    total_scan=fields.Float(string='Lab Total',compute='onchan_func_scan')
    total1=fields.Float(string='Total',compute='onchan_func_pres')
    total2=fields.Float(string='Total',compute='onchan_func_rec')
    write_date=fields.Date(string='Date')
    ebook_id = fields.Char(string='Patient ID')
    paid_status = fields.Boolean(string='Paid')
    billed_amount = fields.Float(string='Total Amount',compute='on_total_func',store=True)
    total_tree=fields.Float(compute='total_func_rec',string ='total_tree',store=True)
    billed_by=fields.Many2one('res.users',string='Billed By',default=lambda self: self.env.user,readonly='1')

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

    @api.onchange('paid_status')
    def paid_not(self):
        if self.paid_status == True:
            self.total_amount = 0.00
        

    @api.depends('total_amount','total','total1','total2','total_scan',)
    def onchan_func(self):
        for rec_sum in self:
            k =(rec_sum.total2 + rec_sum.total_scan)+(rec_sum.total + rec_sum.total1 )
        self.total_amount = k

    @api.depends('total_amount','total','total1','total_tree','total_scan',)
    def on_total_func(self):
        for rec_sum in self:
            k =(rec_sum.total_tree + rec_sum.total_scan)+(rec_sum.total + rec_sum.total1 )
        self.billed_amount = k

    @api.depends('reception_bills')
    def total_func_rec(self):
        sums = []
        for i in self:
            for k in i.reception_bills:
                sums.append(k.bill_amount)
            i.total_tree = sum(sums)

    @api.depends('reception_bills')
    def onchan_func_rec(self):
        sums = []
        for i in self:
            for k in i.reception_bills:
                if k.payment_status == False:
                    sums.append(k.bill_amount)
            i.total2 = sum(sums)

    @api.depends('lab_bill')
    def onchan_func_lab(self):
        sums = []
        for i in self:
            for k in i.lab_bill:
                if k.payment_status == False:
                    sums.append(k.bill_amount)
            i.total = sum(sums)

    @api.depends('scan_bill')
    def onchan_func_scan(self):
        sums = []
        for i in self:
            for k in i.scan_bill:
                if k.payment_status == False:
                    sums.append(k.bill_amount)
            i.total_scan = sum(sums)

    @api.depends('pres_bill')
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
    name= fields.Char(string="Test Name")
    date= fields.Datetime(string="Bill Date")
    bill = fields.Many2one('patient.bills')
    bill_amount =fields.Float(string='Bill Amount')
    payment_status = fields.Boolean(string="Paid",readonly=True)
    test_name=fields.Char(string="Test Name")
    test_types=fields.Char(string="Test Type")
    total=fields.Float(string="Total")

class ScanBills(models.Model):
    _name='scan.bills'

    # patient_name = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name",required=True)
    name= fields.Char(string="Test Name")
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
    delivery_mode = fields.Selection([('domestic','Domestic'),('international',"International")],string='Courier Mode')


class Billingpayment(models.Model):
    _inherit='account.payment'

    bill_lines = fields.One2many('account.bills.lines','bill',string='Patient Bills')
    bill_no = fields.Many2one('patient.bills',string="Bill No")

    @api.onchange('bill_no')
    def onchange_bill(self):
        for rec in self:
            lines = []
            for line in self.bill_no.reception_bills:
                val={
                    'name': line.name,
                    'date':line.date,
                    'bill_amount':line.bill_amount,
                }
                lines.append((0,0,val))
            rec.bill_lines=lines
            self.amount = self.bill_no.total2
        
            lab = []
            for line in self.bill_no.lab_bill:
                val={
                    'name': line.name,
                    'date':line.date,
                    'bill_amount':line.bill_amount,
                }
                lab.append((0,0,val))
            rec.bill_lines=lab
            self.amount = self.bill_no.total

            scan = []
            for line in self.bill_no.scan_bill:
                val={
                    'name': line.name,
                    'date':line.date,
                    'bill_amount':line.bill_amount,
                }
                scan.append((0,0,val))
            rec.bill_lines=scan
            self.amount = self.bill_no.total_scan

            medicine = []
            for line in self.bill_no.pres_bill:
                val={
                    'name': 'medicine',
                    'date':line.date,
                    'bill_amount':line.pre_amount,
                }
                medicine.append((0,0,val))
            rec.bill_lines=medicine
            self.amount = self.bill_no.total1

class Paymentlines(models.Model):
    _name = 'account.bills.lines'

    bill = fields.Many2one('account.payment')
    name= fields.Char(string="Type of  Bill")
    date= fields.Datetime(string="Bill Date")
    bill_amount =fields.Float(string='Bill Amount')
    payment_status = fields.Boolean(string="Paid",readonly=True)


