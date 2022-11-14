from odoo import api, fields, models, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta 
import qrcode
import base64
from io import BytesIO
from odoo.exceptions import ValidationError

class DischargeSummary(models.Model):
    _name = 'discharge.summary'
    _rec_name = 'patient_id'
    
    name = fields.Char(string='Name')
    patient_id = fields.Many2one('res.partner', string='Patient Name',
                                 domain=[('is_patient','=',True)], required=True)
    chief_complaint = fields.Many2many('medical.pathology',string='Chief Complaints')
    associated_complaint = fields.Char(string='Associated Complaints')
    history_complaint = fields.Char(string='History of Present Illness')
    treat_history = fields.Char(string='Treatment History')
    vitals = fields.Char(string='Vitals')
    apperance = fields.Char(string='General Apperance')
    ip_summary = fields.Char(string='Summary of Key Investigation')
    treatment_given = fields.Char(string='Treatment Given')
    therapy_given = fields.Char(string='Therapy Given')
    discharge_condition = fields.Char(string="Discharge Condition")
    pres_discharge = fields.Char(string='Prescription on Discharge')
    advice_discharge = fields.Char(string='Discharge Advice')
    diet_discharge = fields.Many2one('set.diets', string='Discharge Diet')
    file_num = fields.Char(string='File Number')
    doctor_incharge = fields.Many2one('res.partner', string='Doctor',
                                      domain=[('is_doctor','=',True)], required=True)
    admission_date = fields.Datetime(string='Admission Date')
    address = fields.Text(string='Address')
    age = fields.Char(string='Age')
    acknowledgement = fields.Boolean(string='I\we have Understood the Instruction given about the Medicine Dosage and Discharge after Case')
    signature = fields.Char(string='Signature', readonly=True)
    bp = fields.Char(string='BP in mmHg')
    
    company_id = fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company']._company_default_get('discharge.summary'))