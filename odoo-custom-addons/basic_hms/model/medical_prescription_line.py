# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
from odoo.exceptions import  ValidationError

class medical_prescription_line(models.Model):
    _name = "medical.prescription.line"

    name = fields.Many2one('medical.prescription.order','Prescription ID',ondelete='cascade')
    medicament_id = fields.Many2one('medical.medicament','Medicament')
    ip_name = fields.Many2one('in.patient',string='In-Patient')
    indication = fields.Char('Indication')
    allow_substitution = fields.Boolean('Allow Substitution')
    form = fields.Char('Form')
    prnt = fields.Boolean('Print')
    route = fields.Char('Administration Route')
    end_treatement  = fields.Datetime('Administration Route')
    dose = fields.Float('Dose')
    dose_unit_id = fields.Many2one('medical.dose.unit', 'Dose Unit')
    qty = fields.Integer('x')
    medication_dosage_id = fields.Many2one('medical.medication.dosage','Frequency')
    admin_times = fields.Char('Admin Hours', size = 128)
    frequency = fields.Integer('Frequency')
    frequency_unit = fields.Selection([('seconds','Seconds'),('minutes','Minutes'),('hours','hours'),('days','Days'),('weeks','Weeks'),('wr','When Required')], 'Unit')
    duration = fields.Integer('Treatment Duration')
    duration_period = fields.Selection([('minutes','Minutes'),('hours','hours'),('days','Days'),('months','Months'),('years','Years'),('indefine','Indefine')],'Treatment Period')
    quantity = fields.Integer('Quantity')
    review = fields.Datetime('Review')
    refills = fields.Integer('Refills#')
    short_comment = fields.Char('Comment', size=128 )
    end_treatment = fields.Datetime('End of treatment')
    start_treatment = fields.Datetime('Start of treatment')
    company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company']._company_default_get('medical.prescription.order'))

    # names = fields.Many2one('medical.prescription.order','Prescription ID')
    prescribed_quantity = fields.Float(string="Prescribed Quantity")
    medicine_name = fields.Many2one('product.product',string='Medicine Name')
    quantity = fields.Float(related='medicine_name.qty_available', string="Quantity Available")
    morning= fields.Float('Morning')
    noon= fields.Float('After Noon')
    evening= fields.Integer('Evening')
    night= fields.Float('Night')
    before_after = fields.Selection([('bf',"Before Food"),('af',"After food")],'Before Food')
    comment= fields.Char('Comment')
    days1= fields.Integer('Days')
    units= fields.Many2one('uom.uom',string="units")
    potency = fields.Char(string="Potency")
    anupana = fields.Char(string="Notes")
    price = fields.Float(string="Price/unit",related='medicine_name.lst_price')
    total_price = fields.Float(string="Total Price")
    all_day=fields.Char(string="Dose")

    @api.onchange('prescribed_quantity','medicine_name')
    def compute_price(self):
        val=self.price*self.prescribed_quantity
        self.total_price=val

    bf_af=fields.Selection([('before','Before Food'),('after','After Food')])

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

    @api.onchange('medicine_name')
    def prescribe_medicine(self):
        rec= self.env['product.product'].search([('id', '=', self.medicine_name.id)])
        for res in rec.medicine_details:
            self.all_day=res.all_day
            self.units = res.units
            self.anupana = res.anupana
    sequence_ref = fields.Integer('SL.NO', compute="_sequence_ref")
    
    # @api.constrains('medicine_name')
    # def write_list(self):
    #     # orm = self.env['patient.bills'].search([('patient_name','=',self.patient_id.id)])
    #     orm_update = self.env['prescription.bills'].search([('prescription_id', '=', self.name.name)])
    #     # raise ValidationError(orm_update)
    #     billing_lines=[]
    #     for i in self.name:
    #         billing_value = {
    #             'date':i.write_date,
    #             'medicine_name':self.medicine_name.id,
    #             'prescription_id':i.name,
    #             'pre_amount':i.total,
    #             'delivery_mode':i.courier_option,
    #         }
    #         billing_lines.append(0,0,0,billing_value)
    #         orm_update.update(billing_lines)
    #         # orm.write({'pres_bill':billing_lines})

    @api.depends('name.prescription_line_ids', 'name.prescription_line_ids.medicine_name')
    def _sequence_ref(self):
        for line in self:
            no = 0
            line.sequence_ref = no
            for l in line.name.prescription_line_ids:
                no += 1
                l.sequence_ref = no
