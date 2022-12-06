from odoo import api, fields, models
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError

class PatientBills(models.Model):
    _name = 'patient.bills'
    _rec_name ='bill_no'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_name = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name",required=True)
    date_date = fields.Datetime(string="Bill Date",default=datetime.now())
    bills_lines = fields.One2many('patient.bills.lines','bill',string="Patient Bills")
    total_amount = fields.Float(string ='Reg.Due Amount',store=True, compute='onchan_func_due')
    bill_no = fields.Char('Bill No.', default='/')

    company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company']._company_default_get('medical.prescription.order'))
    insurance = fields.Boolean(string="Insurance if any")
    type_of_insurance= fields.Text(string='Insurance Details')
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
    
    gst_total_tax = fields.Float(string='Medicine Amount With GST', compute='depend_fun_gst')
    total_tax = fields.Float(String='Total Taxes')
    billed_amount = fields.Float(string='Total Amount',compute='onchan_func_gst',store=True)
    total_tree=fields.Float(compute='total_func_rec',string ='total tree',store=True)
    billed_by=fields.Many2one('res.users',string='Billed By',default=lambda self: self.env.user,readonly='1')
    patient_activity = fields.Selection([('wait',"Waiting"),('doctor',"Doctor Assigned"),('doc','Diet Assigned'),
                                         ('lab','Lab Bill Assigned'),('pres','Pharmacy Bill Assigned'),('scan','Scan Bill Assigned'),
                                         ('labs','Lab Test Completed'),('scans','Scan Test Completed'),
                                         ('bill',"Pharmacy Bill Assigned"),('discontinued','Discontinued'),('completed',"Completed")],default='wait',track_visibility='onchange')
    
    discounted = fields.Float(string='Discount',readonly=False)
    discounted_total = fields.Float(string='Total With Discount', readonly=True)
    payment_type = fields.Selection([('cash','Cash'),('card','Card'),('upi','Upi')], string='Payment Type')
    payment_id = fields.Char(string='Payment ID')
    bed_charge = fields.Float(string='Bed Charges')
    diet_charge = fields.Float(string='Diet Charges')
    total_ip_lab = fields.Float(string='Total', compute='onchan_func_lab_ip')
    total_ip_scan = fields.Float(string='Total', compute='onchan_func_lab_scan')
    total_ip_tab = fields.Float(string='Medicine Amount', compute='onchan_func_lab_tab')
    total_ip_lab_bill = fields.Float(string='Lab Amount', compute='func_lab_patient')  
    total_ip_scan_bill = fields.Float(string='Scan Amount', compute='func_scan_patient')  
    total_ip_tab_bill = fields.Float(string='Medicine Amount')  
    reg_due = fields.Float(string='Registration Due', compute='reg_dues')
    
    amount_paid = fields.Float(string='Amount Paid', compute='due_calculate')
    therapy_charge = fields.Float(string='Therapy Charges', compute='therapy_chage_ap')
    total_paid = fields.Float(string='Total Paid')
    total_bal = fields.Float(string='Total Due',compute='total_due_fun',store=True)
    med_amt_paid = fields.Float(string='Medicine Amount Paid')
    med_amt_due = fields.Float(string='Medicine Amount Due With Tax')
    med_cancell = fields.Selection([('cancell','Cancelled'),('Completed','Purchased')], string='Medicine Details')
    file_charges = fields.Float(string='File Charges')
    med_package = fields.Selection([('2','2 Months'),('3','3 Months'),('4','4 Months'),('5','5 Months'),('6','6 Months')],string='Medicine Package')
    discount_reason = fields.Char(string='Discount Reason')
    discount_by = fields.Many2one('res.partner',string='Discounted By',domain=[('is_billing','=',True)],)
    total_tax_ip = fields.Float(string='Medicine Tax')
    total_tax_ip_tab = fields.Float(string='IP Total ', compute='gst_ip')        
    totals_ip = fields.Float(string='Total', compute='total_ip_tab_compute')
    total12=fields.Float(string='Medicine Total',compute='onchan_func_med')
    total_tax_med = fields.Float(String='IP Total Taxes',compute='new_med_calc')
    total_med_tax = fields.Float(string='IP Total',compute='new_med_calc')
    sub_total = fields.Float(string='Sub Total', compute='sub_totals')
    
    sex = fields.Selection([('m', 'Male'),('f', 'Female')], string ="Sex",required= True)
    contact_no = fields.Char(string="Contact No", required= True)
    total_due_amt = fields.Float(string='Total Due Amount', compute='due_cal_fun')
    mrd_charge = fields.Float(string='MRD Charge')
    
    @api.depends('paid_status','billed_amount','total_paid','total_due_amt')
    def due_cal_fun(self):
        for rec in self:
            if rec.paid_status == False:
                rec.total_due_amt = (rec.billed_amount - rec.total_paid)
            if rec.paid_status == True:
                rec.total_due_amt = 0.00
    
    @api.onchange('paid_status')
    def medicine_bill(self):
        if self.pres_bill:
            if self.paid_status == True:
                self.med_cancell = 'Completed'
    
    @api.constrains('paid_status')
    def paid_not(self):
        if self.paid_status == True:
            self.total_bal = 0.00
            self.total_due_amt = 0.00
            self.total_paid = self.billed_amount
            self.patient_activity = 'completed'
            
            orm = self.env['medical.patient'].search([('patient_id','=',self.patient_name.id)])
            orm.write({'patient_activity':'completed'})
            orm1 = self.env['medical.doctor'].search([('patient','=',self.patient_name.id)])
            orm1.write({'patient_activity':'completed'})
            orm_3 = self.env['res.partner'].search([('name', '=', self.patient_name.name)])
            orm_3.write({'patient_activity':'completed'})  
            
            med_assign = self.env['medical.prescription.order'].search([('patient_id','=',self.patient_name.id)])
            med_assign.write({'patient_activity' : 'completed'})
            
            orm = self.env['account.payment'].search([('partner_id','=',self.patient_name.id)])
            types = []
            
            for i in self.reception_bills:
                vals={
                    'name':i.name,
                    'bill_amount':i.bill_amount,
                    'date':i.date,
                }
                types.append((0,0,vals))
            for i in self.lab_bill:
                lab={
                    'name':i.name,
                    'bill_amount':i.bill_amount,
                    'date':i.date,
                }
                types.append((0,0,lab))
            for i in self.scan_bill:
                scan={
                    'name':i.name,
                    'bill_amount':i.bill_amount,
                    'date':i.date,
                }
                types.append((0,0,scan))
            for i in self.pres_bill:
                pres={
                    'name':i.medicine_name.name,
                    'bill_amount':i.pre_amount,
                    'date':i.date,
                }
                types.append((0,0,pres))
            for i in self.inpatient_lab:
                in_lab={
                    'name':i.name,
                    'bill_amount':i.bill_amount,
                    'date':i.date,
                }
                types.append((0,0,in_lab))
            for i in self.inpatient_scan:
                in_scan={
                    'name':i.name,
                    'bill_amount':i.bill_amount,
                    'date':i.date,
                    }
                types.append((0,0,in_scan))
            for i in self.inpatient_tablet:
                in_tab={
                    'name':i.medicine_name.name,
                    'bill_amount':i.pre_amount,
                    'date':i.date,
                }
                types.append((0,0,in_tab))
            for i in self.ip_therapy:
                in_therapy={
                    'name':i.therapy,
                    'bill_amount':i.amount,
                    'date':i.write_date,
                }
                types.append((0,0,in_therapy))
            context= {
                    'partner_id':self.patient_name.id,
                    'bill_no':self.id,
                    'payment_type':'inbound',
                    'doctor_id':self.doctor_id.id,
                    'amount':self.billed_amount,
                    'bill_lines':types,
                    'reg_bill':self.total2,
                    'lab_bill':self.total,
                    'scan_bill':self.total_scan,
                    'pres_bill':self.gst_total_tax,
                    'therapy_bill':self.therapy_charge,
                    'bed_bill':self.bed_charge,
                    'file_charges':self.file_charges,
                    }
            orm_move = self.env['account.move'].search([('line_ids.partner_id','=',self.patient_name.id)])
            acc_move = orm_move.line_ids
            # raise ValidationError(acc_move)
            if orm:
                orm.write(context)
                acc_move.update({'tax_ids':self.pres_bill.gst_tax.id})
            else:
                orm.create(context)
                acc_move.update({'tax_ids':self.pres_bill.gst_tax.id})
            
    def med_cancell_fun(self):
        self.med_cancell = 'cancell'
        self.total1 = 0.00
        self.total_tax = 0.00
        self.gst_total_tax = 0.00
        self.mrd_charge = 0.00
        self.pres_bill = [(5,0,0)]
        self.patient_activity = 'discontinued'
        orm = self.env['medical.patient'].search([('patient_id', '=', self.patient_name.id)])
        orm.write({'patient_activity':'discontinued'})
        doc = self.env['medical.doctor'].search([('patient', '=', self.patient_name.id)])
        doc.write({'patient_activity':'discontinued'})
        orm_3 = self.env['res.partner'].search([('name', '=', self.patient_name.name)])
        orm_3.write({'patient_activity':'discontinued'})
        
        med_cancel = self.env['medical.prescription.order'].search([('patient_id','=',self.patient_name.id)])
        med_cancel.write({'patient_activity' : 'discontinued'})
        
    
    @api.depends('total_paid','billed_amount')
    def total_due_fun(self):
        for i in self:
            i.total_bal = (i.billed_amount) - (i.total_paid)
                
    @api.depends('sub_total','total2','total_ip_lab_bill','total_ip_scan_bill','total1','therapy_charge','bed_charge','file_charges')
    def sub_totals(self):
        for rec in self:
            rec.sub_total = (rec.total1 + rec.total2  + rec.bed_charge) + (rec.total_ip_lab_bill + rec.total_ip_scan_bill + rec.therapy_charge + rec.file_charges)
    
    @api.depends('pres_bill','total12')
    def onchan_func_med(self):
        sums = []
        for i in self:
            for k in i.pres_bill:
                # if k.payment_status == False:
                sums.append(k.pre_amount)
            i.total12 = sum(sums)
    
    @api.depends('total_ip_tab','total_tax_ip')
    def total_ip_tab_compute(self):
        for rec in self:
            rec.totals_ip = (rec.total_ip_tab) + (rec.total_tax_ip)
            
    @api.depends('total12','total_tax_med','total_med_tax')
    def new_med_calc(self):
        for rec in self:
            for tax_id in rec.pres_bill:
                for k in tax_id.gst_tax:
                    tax = k.amount
                    rec.total_tax_med = ((rec.total12 / 100) * tax)
            rec.total_med_tax = (rec.total12) + (rec.total_tax_med)
            
    @api.depends('total_ip_tab','total_tax_ip','total_tax_ip_tab','total_ip_lab','total_ip_scan','bed_charge','therapy_charge')
    def gst_ip(self):
        for rec in self:
            for tax_id in rec.inpatient_tablet:
                for k in tax_id.gst_tax:
                    tax = k.amount
                    rec.total_tax_ip = ((rec.total_ip_tab / 100) * tax)
            rec.total_tax_ip_tab = (rec.total_tax_ip + rec.total_ip_lab + rec.total_ip_scan) + (rec.total_ip_tab + rec.bed_charge + rec.therapy_charge)
            
    @api.depends('pres_bill','med_package','total1')
    def onchan_func_pres(self):
        sums = []
        for i in self:
            for k in i.pres_bill:
                # if k.payment_status == False:
                sums.append(k.pre_amount)
            i.total1 = sum(sums)
            
            i.total1 = (i.total1 + i.total_ip_tab)
            
            if i.med_package == '2':
                i.total1 = (i.total1 * 2)
            if i.med_package == '3':
                i.total1 = (i.total1 * 3)
            if i.med_package == '4':
                i.total1 = (i.total1 * 4)
            if i.med_package == '5':
                i.total1 = (i.total1 * 5)
            if i.med_package == '6':
                i.total1 = (i.total1 * 6)
    
    

    
    @api.onchange('med_amt_paid')
    def cal_med_due_amt(self):
        for i in self:
            i.med_amt_due = (i.gst_total_tax - i.med_amt_paid)
    
    
    
    @api.depends('ip_therapy')
    def therapy_chage_ap(self):
        therapys = []
        for i in self:
            for k in i.ip_therapy:
                therapys.append(k.amount)
            i.therapy_charge = sum(therapys)
    
    @api.depends('total2','reg_due')
    def due_calculate(self):
        for i in self:
            i.amount_paid = (i.total2 - i.reg_due)
    
    @api.depends('reception_bills')
    def onchan_func_due(self):
        dues=[]
        for i in self:
            for k in i.reception_bills:
                dues.append(k.due_rec)
            # raise ValidationError(k.due_rec)
            i.total_amount = sum(dues)
    
    @api.depends('reception_bills')
    def reg_dues(self):
        dues=[]
        for i in self:
            for   k in i.reception_bills:
                dues.append(k.due_rec)
            i.reg_due = sum(dues)

    @api.onchange('discounted')
    def onchan_func_gst(self):
        for rec in self:
            for k in rec.pres_bill:
                for j in k.gst_tax:
                    percentage = self.env['account.tax'].search([('id','=',j._origin.id)])
                    rec.total_tax = ((rec.discounted_total / 100) * (percentage.amount))
            rec.discounted_total = (rec.total1 - rec.discounted)
            
    @api.depends('mrd_charge','discounted','med_package','total1','discounted_total','billed_amount','file_charges','bed_charge','therapy_charge','total_tax','total2','total_ip_scan_bill','total_ip_lab_bill','gst_total_tax')
    # @api.onchange('pres_bill')
    def depend_fun_gst(self):
        for rec in self:
            for tax_id in rec.pres_bill:
                for k in tax_id.gst_tax:
                    tax = k.amount
                    # raise ValidationError(tax)
                    rec.discounted_total = (rec.total1 - rec.discounted)
                    rec.total_tax = ((rec.discounted_total / 100) * tax)
            rec.discounted_total = (rec.total1 - rec.discounted)
            rec.gst_total_tax = (rec.discounted_total)+(rec.total_tax)
            a =(rec.total2 + rec.total_ip_scan_bill + rec.total_ip_lab_bill + rec.file_charges)
            j = (rec.gst_total_tax + rec.bed_charge + rec.therapy_charge + rec.mrd_charge)
            rec.billed_amount = (a+j)
            
    @api.model
    def _default_gst(self):
        company_id = self.env.company.id
        gst = self.env['account.journal'].search([('company_id', '=', company_id)])
        if gst:
            return gst[0]
        return self.env['account.journal']

    journal_id = fields.Many2one('account.journal', string='GST',  default=_default_gst, check_company=True)
                                     
    def invoice_button(self):            
        orm = self.env['account.payment'].search([('partner_id','=',self.patient_name.id)])
        types = []
        
        for i in self.reception_bills:
            vals={
                'name':i.name,
                'bill_amount':i.bill_amount,
                'date':i.date,
            }
            types.append((0,0,vals))
        for i in self.lab_bill:
            lab={
                'name':i.name,
                'bill_amount':i.bill_amount,
                'date':i.date,
            }
            types.append((0,0,lab))
        for i in self.scan_bill:
            scan={
                'name':i.name,
                'bill_amount':i.bill_amount,
                'date':i.date,
            }
            types.append((0,0,scan))
        for i in self.pres_bill:
            pres={
                'name':i.medicine_name.name,
                'bill_amount':i.pre_amount,
                'date':i.date,
            }
            types.append((0,0,pres))
        for i in self.inpatient_lab:
            in_lab={
                'name':i.name,
                'bill_amount':i.bill_amount,
                'date':i.date,
            }
            types.append((0,0,in_lab))
        for i in self.inpatient_scan:
            in_scan={
                'name':i.name,
                'bill_amount':i.bill_amount,
                'date':i.date,
                }
            types.append((0,0,in_scan))
        for i in self.inpatient_tablet:
            in_tab={
                'name':i.medicine_name.name,
                'bill_amount':i.pre_amount,
                'date':i.date,
            }
            types.append((0,0,in_tab))
        for i in self.ip_therapy:
            in_therapy={
                'name':i.therapy,
                'bill_amount':i.amount,
                'date':i.write_date,
            }
            types.append((0,0,in_therapy))
        context= {
                'partner_id':self.patient_name.id,
                'bill_no':self.id,
                'bill_lines':types,
                }
        if orm:
            orm.write(context)   
        else:    
            orm.create(context)
     
    def create(self, vals):
        obj = super(PatientBills, self).create(vals)
        if obj.bill_no == '/':
            number = self.env['ir.sequence'].get('bill.sequence') or '/'
            obj.write({'bill_no': number})
        return obj

    @api.depends('inpatient_lab')
    def onchan_func_lab_ip(self):
        sums = []
        # for i in self:
        for k in self.inpatient_lab:
            sums.append(k.bill_amount)
        self.total_ip_lab = sum(sums)
        
    @api.depends('inpatient_scan')
    def onchan_func_lab_scan(self):
        sums = []
        # for i in self:
        for k in self.inpatient_scan:
            sums.append(k.bill_amount)
        self.total_ip_scan = sum(sums)
        
    @api.depends('inpatient_tablet')
    def onchan_func_lab_tab(self):
        sums = []
        # for i in self:
        for k in self.inpatient_tablet:
            sums.append(k.pre_amount)
        self.total_ip_tab = sum(sums)

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
    
    @api.depends('total_ip_lab')
    def func_lab_patient(self):
        for i in self:
            i.total_ip_lab_bill = (i.total + i.total_ip_lab)
    
    @api.depends('total_ip_scan')
    def func_scan_patient(self):
        for i in self:
            i.total_ip_scan_bill = (i.total_scan + i.total_ip_scan)
            
    @api.depends('scan_bill')
    def onchan_func_scan(self):
        sums = []
        for i in self:
            for k in i.scan_bill:
                # if k.payment_status == False:
                sums.append(k.bill_amount)
            i.total_scan = sum(sums)


    
    inpatient_lab = fields.One2many('billing.inpatient.lab', 'bill', string='Lab')
    inpatient_scan = fields.One2many('billing.inpatient.scan','bill', string='Scan')
    inpatient_tablet = fields.One2many('billing.inpatient.medicine', 'bill', string='Medicines')
    ip_therapy = fields.One2many('bill.ip.therapy','name',string='Therapy')
    
class IpTherapyBill(models.Model):
    _name = 'bill.ip.therapy'
    
    name = fields.Many2one('patient.bills',ondelete='cascade')
    patient_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string='Patient Name')
    time = fields.Char(string='Time')
    therapy = fields.Char(string='Therapy')
    amount = fields.Float(string='Amount')
    

class InPatientLines(models.Model):
    _name = 'billing.inpatient.lab'
    
    name= fields.Char(string="Test Name")
    date= fields.Datetime(string="Bill Date")
    bill = fields.Many2one('patient.bills',ondelete='cascade')
    bill_amount =fields.Float(string='Bill Amount')
    payment_status = fields.Boolean(string="Paid",readonly=True)
    test_name=fields.Char(string="Test Name")
    test_types=fields.Char(string="Test Type")
    total=fields.Float(string="Total")
    
class InPatientScan(models.Model):
    _name = 'billing.inpatient.scan'
    
    name= fields.Char(string="Test Name")
    date= fields.Datetime(string="Bill Date")
    bill = fields.Many2one('patient.bills',ondelete='cascade')
    bill_amount =fields.Float(string='Bill Amount')
    payment_status = fields.Boolean(string="Paid",readonly=True)
    test_name=fields.Char(string="Test Name")
    test_types=fields.Char(string="Test Type")
    total=fields.Float(string="Total")
    
class InPatientMedicine(models.Model):
    _name = 'billing.inpatient.medicine'
    
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
    due_rec = fields.Float(string='Due Amount')
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
    doctor_id = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor Name')
    reg_bill = fields.Float(string='Registration Amount')
    lab_bill = fields.Float(string='Lab Amount')
    scan_bill = fields.Float(string='Scan Amount')
    pres_bill = fields.Float(string='Prescription Amount')
    therapy_bill = fields.Float(string='Therapy Amount')
    bed_bill = fields.Float(string='Bed Charges')
    file_charges = fields.Float(string='File Charges')

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


