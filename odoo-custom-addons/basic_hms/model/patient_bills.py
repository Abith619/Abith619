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
    gst_total_tax = fields.Float(string='Medicine Amount With GST', compute="depend_fun_gst")
    total_tax = fields.Float(String='Total Taxes',compute='depend_fun_gst' )
    billed_amount = fields.Float(string='Total Amount',compute='onchan_func_gst',store=True)
    total_tree=fields.Float(compute='total_func_rec',string ='total tree',store=True)
    billed_by=fields.Many2one('res.users',string='Billed By',default=lambda self: self.env.user,readonly='1')
    patient_activity = fields.Selection([('wait',"Doctor Assigned"),('doc','Diet Assigned'),
                                         ('lab','Lab Assigned'),('pres','Prescription'),('scan','Scan Assigned'),
                                         ('bill',"Pharmacy Bill Assigned"),('completed',"Completed")],default='wait')
    discounted = fields.Float(string='Discount',readonly=False)
    discounted_total = fields.Float(string='Total With Discount')
    payment_type = fields.Selection([('cash','Cash'),('card','Card'),('upi','Upi')], string='Payment Type')
    payment_id = fields.Char(string='Payment ID')



    @api.onchange('discounted')
    def onchan_func_gst(self):
        for rec in self:
            for k in rec.pres_bill:
                for j in k.gst_tax:
                    percentage = self.env['account.tax'].search([('id','=',j._origin.id)])
                    rec.discounted_total = (rec.total1 - rec.discounted)
                    rec.total_tax = ((rec.discounted_total / 100) * (percentage.amount))

    @api.depends('discounted_total','total_tax','total2','total_scan','total','gst_total_tax')
    def depend_fun_gst(self):
        for rec in self:
            for tax_id in self.pres_bill:
                tax = tax_id.gst_tax.amount
            # percentage = self.env['account.tax'].search([('id','=',76)])
                rec.discounted_total = (rec.total1 - rec.discounted)
                rec.total_tax = ((rec.discounted_total / 100) * tax)
        # raise ValidationError((percentage.amount))
        rec.gst_total_tax = (rec.discounted_total)+(rec.total_tax)
        a =(rec.total2 + rec.total_scan + rec.total) 
        j = rec.gst_total_tax
        self.billed_amount = (a+j)

    @api.model
    def _default_gst(self):
        company_id = self.env.company.id
        gst = self.env['account.journal'].search([('company_id', '=', company_id)])
        if gst:
            return gst[0]
        return self.env['account.journal']

    journal_id = fields.Many2one('account.journal', string='GST',  default=_default_gst, check_company=True)
                                     
    def invoice_button(self):        
        context ={
                'partner_id':self.patient_name.id,
                'bill_no':self.id,
                'name':self.id,
                'amount':self.billed_amount
                }
        orm = self.env['account.payment'].create(context)
    
    def create(self, vals):
        obj = super(PatientBills, self).create(vals)
        if obj.bill_no == '/':
            number = self.env['ir.sequence'].get('bill.sequence') or '/'
            obj.write({'bill_no': number})
            
        # context ={
        #         'partner_id':obj.patient_name.id,
        #         'bill_no':obj.id,
        #         'amount':self.billed_amount
        #         }
        # orm = self.env['account.payment'].create(context)

        return obj
        
        
        # return{
        #     'name': "Patient Invoice",
        #     'type': 'ir.actions.act_window',
        #     'view_type': 'form',
        #     'view_mode': 'form',
        #     'res_model': 'account.payment',
        #     'context': {
        #         'default_partner_id':self.patient_name.id,
        #         'default_bill_no':self.id
        #         },
        #     }

    @api.onchange('paid_status')
    def paid_not(self):
        if self.paid_status == True:
            self.total_amount = 0.00
            orm = self.env['medical.patient'].search([('patient_id','=',self.patient_name.id)])
            orm.write({'patient_activity':'completed'})

        

    # @api.depends('total_amount','total','gst_total_tax','total2','total_scan',)
    # def on_total_func(self):
    #     for rec_sum in self:
    #         k =(rec_sum.total2 + rec_sum.total_scan)+(rec_sum.total + rec_sum.gst_total_tax )
    #     self.billed_amount = k


    # @api.depends('total_amount','total','gst_total_tax','total_tree','total_scan',)
    # def on_total_func(self):
    #     for rec_sum in self:
    #         k =(rec_sum.total_tree + rec_sum.total_scan)+(rec_sum.total + rec_sum.gst_total_tax )
    #     self.billed_amount = k


    @api.depends('reception_bills')
    def total_func_rec(self):
        sums = []
        for i in self:
            for k in i.reception_bills:
                # if k.payment_status == False:
                sums.append(k.bill_amount)
            i.total_tree = sum(sums)

    @api.depends('reception_bills')
    def onchan_func_rec(self):
        sums = []
        for i in self:
            for k in i.reception_bills:
                # if k.payment_status == False:
                sums.append(k.bill_amount)
            i.total2 = sum(sums)

    @api.depends('lab_bill')
    def onchan_func_lab(self):
        sums = []
        for i in self:
            for k in i.lab_bill:
                # if k.payment_status == False:
                sums.append(k.bill_amount)
            i.total = sum(sums)

    @api.depends('scan_bill')
    def onchan_func_scan(self):
        sums = []
        for i in self:
            for k in i.scan_bill:
                # if k.payment_status == False:
                sums.append(k.bill_amount)
            i.total_scan = sum(sums)

    @api.depends('pres_bill')
    def onchan_func_pres(self):
        sums = []
        for i in self:
            for k in i.pres_bill:
                # if k.payment_status == False:
                sums.append(k.pre_amount)
            i.total1 = sum(sums)

    # @api.depends('pres_bill')
    # def onchan_func_gst(self):
    #     for rec in self:
    #         taxed_amount = 0
    #         for k in rec.pres_bill:
    #             if k.payment_status == False:
    #                 total_tax = 0
    #                 for gst_id in k.gst_tax:
    #                     percentage = self.env['account.tax'].search([('id','=',gst_id.id)])
    #                     total_tax += percentage.amount
    #                 taxed_amount += (k.pre_amount / 100) * total_tax 
    #         rec.total_tax = taxed_amount
    #         rec.gst_total_tax = rec.total1 + taxed_amount 


class Billlines(models.Model):
    _name = 'patient.bills.lines'

    bill = fields.Many2one('patient.bills',ondelete='cascade')
    name= fields.Char(string="Type of  Bill")
    date= fields.Datetime(string="Bill Date")
    bill_amount =fields.Float(string='Bill Amount')
    payment_status = fields.Boolean(string="Paid",readonly=True)

class ReceptionBills(models.Model):
    _name='reception.bills'

    # patient_name = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name",required=True)
    name= fields.Char(string="Type of  Bill")
    date= fields.Datetime(string="Bill Date")
    bill = fields.Many2one('patient.bills',ondelete='cascade')
    bill_amount =fields.Float(string='Bill Amount')
    payment_status = fields.Boolean(string="Paid",readonly=True)
    total=fields.Float(string="Total")

class DoctorBills(models.Model):
    _name='doctor.bills'

    # patient_name = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name",required=True)
    name= fields.Char(string="Type of  Bill")
    date= fields.Datetime(string="Bill Date")
    bill = fields.Many2one('patient.bills',ondelete='cascade')
    bill_amount =fields.Float(string='Bill Amount')
    payment_status = fields.Boolean(string="Paid",readonly=True)

class LabBills(models.Model):
    _name='lab.bills'

    # patient_name = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name",required=True)
    name= fields.Char(string="Test Name")
    date= fields.Datetime(string="Bill Date")
    bill = fields.Many2one('patient.bills',ondelete='cascade')
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
    bill = fields.Many2one('patient.bills',ondelete='cascade')
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
    bill = fields.Many2one('patient.bills',ondelete='cascade')
    pre_amount =fields.Float(string='Bill Amount',related='medicine_name.lst_price')
    payment_status = fields.Boolean(string="Paid",readonly=True)
    medicine_name = fields.Many2one('product.product',string='Medicine Name')
    prescription_id = fields.Char(string="Prescription ID")
    total=fields.Float(string="Total")
    gst_tax = fields.Many2many('account.tax', string='Tax',related='medicine_name.taxes_id')
    gst_calc = fields.Float(string='Total Tax Value')
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

    bill = fields.Many2one('account.payment',ondelete='cascade')
    name= fields.Char(string="Type of  Bill")
    date= fields.Datetime(string="Bill Date")
    bill_amount =fields.Float(string='Bill Amount')
    payment_status = fields.Boolean(string="Paid",readonly=True)


