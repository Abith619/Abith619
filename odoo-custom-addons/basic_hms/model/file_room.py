from odoo import api, fields, models, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta 
import qrcode
import base64
from io import BytesIO
from odoo.exceptions import ValidationError

class FileRoom(models.Model):
    _name='file.room'
    
    patient_id = fields.Many2one('res.partner', string='Patient Name')
    attachment = fields.Many2many('ir.attachment',string="Attachment")
    name = fields.Char(string='Exercise')
    
class InPatientDept(models.Model):
    _name='in.patient'
    
    name = fields.Char(string='Name')
    patient_id = fields.Many2one('res.partner',string='Patient Name',domain=[('is_patient','=',True)])
    reg_no = fields.Char(string='Reg.No')
    file_num = fields.Char(string='File Number')
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Others')],string='Gender')
    conditions = fields.Text(string='Conditions')
    dob = fields.Date(string="Date of Birth")
    contact_num = fields.Char(string='Contact Number')
    address = fields.Text(string='Address')
    doctor_in = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor InCharge')
    attend_num = fields.Char(string='Attender Contact.No')
    nurse_name = fields.Many2one('res.partner',string='Nurse Name')
    time = fields.Char(string='Time')
    
    qr_code = fields.Binary("QR Code", attachment=True, compute='generate_qr_code')
    
    def generate_qr_code(self):
        for rec in self:
            p_details={
                'Patient Id':rec.name,
                'Patient Name':rec.patient_id.name,
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

    in_pat_line = fields.One2many('in.patient.dayone','name',string='Doctor Rounds')
    diet_line = fields.One2many('diet.field.for','name',string='Diet')
    sister_line = fields.One2many('sister.round','name',string='Sister')
    therapy_line = fields.One2many('ip.therapy','name',string='Therapy')
    
class InPatientNotebook(models.Model):
    _name = 'in.patient.dayone'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    doctor = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor')
    review = fields.Text(string='Review')
    medicine = fields.Char(string='Medicines')
    
class SisterRound(models.Model):
    _name='sister.round'
    
    name = fields.Many2one('in.patient',string='IN Details')
    nurse_name = fields.Many2one('res.partner',string='Nurse Name')
    time = fields.Char(string='Time')
    lbg = fields.Char(string='LBG')
    bp = fields.Char(string='BP')
    temp = fields.Char(string='TEMP')
    spo2 = fields.Char(string='SPO2')
    motion = fields.Char(string='Motion')
    urine = fields.Char(string='Urine')
    sleep = fields.Char(string='Sleep')
    digestion = fields.Char(string='Digestion')
    pain = fields.Char(string='Pain')
    notes = fields.Char(string='Notes')

class TherapyIP(models.Model):
    _name = 'ip.therapy'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    therapy = fields.Char(string='Therapy')
    amount = fields.Char(string='Amount')