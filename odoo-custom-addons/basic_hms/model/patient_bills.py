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
            

    @api.onchange('bills_lines')
    def onchan_func(self):
        sums = []
        for i in self:
            for k in i.bills_lines:
                if k.payment_status == False:
                    sums.append(k.bill_amount)
            i.total_amount = sum(sums)

class Billlines(models.Model):
    _name = 'patient.bills.lines'


    bill = fields.Many2one('patient.bills')
    name= fields.Char(string="Type of  Bill")
    date= fields.Datetime(string="Bill Date")
    bill_amount =fields.Float(string='Bill Amount')
    payment_status = fields.Boolean(string="Paid",readonly=True)


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


