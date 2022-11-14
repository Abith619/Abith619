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
    _rec_name = 'patient_id'
    
    name = fields.Char(string='Name')
    company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company']._company_default_get('in.patient'))
    patient_id = fields.Many2one('res.partner',string='Patient Name',domain=[('is_patient','=',True)],required=True)
    reg_no = fields.Char(string='Reg.No')
    file_num = fields.Char(string='File Number')
    gender = fields.Selection([('m','Male'),('f','Female'),('o','Others')],string='Gender')
    conditions = fields.Many2many('medical.pathology',string='Complaints')
    dob = fields.Date(string="Date of Birth")
    age = fields.Char(string='Age')
    contact_num = fields.Char(string='Contact Number')
    address = fields.Text(string='Address')
    doctor_in = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor InCharge')
    attend_num = fields.Char(string='Attender Contact.No')
    nurse_name = fields.Many2one('res.partner',string='Nurse Name')
    time = fields.Char(string='Time')
    diet_id_diet = fields.Many2one('prescribe.diet',string='Diet')
    medicine_id = fields.Many2one('medical.prescription.order', string='Medicine')
    history_complaint = fields.Char(string='History of Present Illness')
    bp = fields.Char(string='BP in mmHg')
    
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
            
    # def create(self):

    in_pat_line = fields.One2many('in.patient.dayone','name',string='Doctor Rounds')
    diet_line = fields.One2many('diet.line.old','name',string='Diet')
    sister_line = fields.One2many('sister.round','name',string='Sister')
    therapy_line = fields.One2many('ip.therapy','name',string='Therapy')
    medicine_line = fields.One2many('patient.prescription','ip_name',string='Medicine')
    lab_line = fields.One2many('lab.test.line','ip_name',string='Lab')
    scan_line = fields.One2many('scan.line','ip_name',string='Scan')
    
# day 2 Line

    in_pat_line_two = fields.One2many('line.two','name',string='Doctor Rounds')
    diet_line_two = fields.One2many('diet.line.one','name',string='Diet')
    sister_line_two = fields.One2many('sister.line','name',string='Sister')
    therapy_line_two = fields.One2many('therapy.line','name',string='Therapy')
    medicine_line_two = fields.One2many('medicine.line.one','ip_name',string='Medicine')
    lab_line_two = fields.One2many('lab.line.one','ip_name',string='Lab')
    scan_line_two = fields.One2many('scan.line.one','ip_name',string='Scan')
    
# day 3 Line

    in_pat_line_three = fields.One2many('line.three','name',string='Doctor Rounds')
    diet_line_three = fields.One2many('diet.line.two','name',string='Diet')
    sister_line_three = fields.One2many('sister.line.three','name',string='Sister')
    therapy_line_three = fields.One2many('therapy.line.three','name',string='Therapy')
    medicine_line_three = fields.One2many('medicine.line.two','ip_name',string='Medicine')
    lab_line_three = fields.One2many('lab.line.two','ip_name',string='Lab')
    scan_line_three = fields.One2many('scan.line.two','ip_name',string='Scan')
    
# day 4 Line

    in_pat_line_four = fields.One2many('line.four','name',string='Doctor Rounds')
    diet_line_four = fields.One2many('diet.line.three','name',string='Diet')
    sister_line_four = fields.One2many('sister.line.four','name',string='Sister')
    therapy_line_four = fields.One2many('therapy.line.four','name',string='Therapy')
    medicine_line_four = fields.One2many('medicine.line.three','ip_name',string='Medicine')
    lab_line_four = fields.One2many('lab.line.three','ip_name',string='Lab')
    scan_line_four = fields.One2many('scan.line.three','ip_name',string='Scan')
    
# day 5 Line

    in_pat_line_five = fields.One2many('line.five','name',string='Doctor Rounds')
    diet_line_five = fields.One2many('diet.line.four','name',string='Diet')
    sister_line_five = fields.One2many('sister.line.five','name',string='Sister')
    therapy_line_five = fields.One2many('therapy.line.five','name',string='Therapy')
    medicine_line_five = fields.One2many('medicine.line.four','ip_name',string='Medicine')
    lab_line_five = fields.One2many('lab.line.four','ip_name',string='Lab')
    scan_line_five = fields.One2many('scan.line.four','ip_name',string='Scan')
    
# day 6 Line

    in_pat_line_six = fields.One2many('line.six','name',string='Doctor Rounds')
    diet_line_six = fields.One2many('diet.line.five','name',string='Diet')
    sister_line_six = fields.One2many('sister.line.six','name',string='Sister')
    therapy_line_six = fields.One2many('therapy.line.six','name',string='Therapy')
    medicine_line_six = fields.One2many('medicine.line.five','ip_name',string='Medicine')
    lab_line_six = fields.One2many('lab.line.five','ip_name',string='Lab')
    scan_line_six = fields.One2many('scan.line.five','ip_name',string='Scan')
    
# day 7 Line

    in_pat_line_seven = fields.One2many('line.seven','name',string='Doctor Rounds')
    diet_line_seven = fields.One2many('diet.line.six','name',string='Diet')
    sister_line_seven = fields.One2many('sister.line.seven','name',string='Sister')
    therapy_line_seven = fields.One2many('therapy.line.seven','name',string='Therapy')
    medicine_line_seven = fields.One2many('medicine.line.six','ip_name',string='Medicine')
    lab_line_seven = fields.One2many('lab.line.six','ip_name',string='Lab')
    scan_line_seven = fields.One2many('scan.line.six','ip_name',string='Scan')
    
# day 8 Line

    in_pat_line_eight = fields.One2many('line.eight','name',string='Doctor Rounds')
    diet_line_eight = fields.One2many('diet.line.seven','name',string='Diet')
    sister_line_eight = fields.One2many('sister.line.eight','name',string='Sister')
    therapy_line_eight = fields.One2many('therapy.line.eight','name',string='Therapy')
    medicine_line_eight = fields.One2many('medicine.line.seven','ip_name',string='Medicine')
    lab_line_eight = fields.One2many('lab.line.seven','ip_name',string='Lab')
    scan_line_eight = fields.One2many('scan.line.seven','ip_name',string='Scan')
    
# day 9 Line

    in_pat_line_nine = fields.One2many('line.nine','name',string='Doctor Rounds')
    diet_line_nine = fields.One2many('diet.line.eight','name',string='Diet')
    sister_line_nine = fields.One2many('sister.line.nine','name',string='Sister')
    therapy_line_nine = fields.One2many('therapy.line.nine','name',string='Therapy')
    medicine_line_nine = fields.One2many('medicine.line.eight','ip_name',string='Medicine')
    lab_line_nine = fields.One2many('lab.line.eight','ip_name',string='Lab')
    scan_line_nine = fields.One2many('scan.line.eight','ip_name',string='Scan')
    
# day 10 Line

    in_pat_line_ten = fields.One2many('line.ten','name',string='Doctor Rounds')
    diet_line_ten = fields.One2many('diet.line.nine','name',string='Diet')
    sister_line_ten = fields.One2many('sister.line.ten','name',string='Sister')
    therapy_line_ten = fields.One2many('therapy.line.ten','name',string='Therapy')
    medicine_line_ten = fields.One2many('medicine.line.nine','ip_name',string='Medicine')
    lab_line_ten = fields.One2many('lab.line.nine','ip_name',string='Lab')
    scan_line_ten = fields.One2many('scan.line.nine','ip_name',string='Scan')
    
    def discharge(self):
        return{
            'name': "Discharge Summary",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'discharge.summary',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_doctor_incharge':self.doctor_in.id,
                'default_name':self.reg_no,
                'default_file_num':self.file_num,
                'default_chief_complaint':[[6,0,[i.id for i in self.conditions]]],
                'default_history_complaint':self.history_complaint,
                'default_admission_date':self.write_date,
                'default_write_date':datetime.now(),
                'default_address':self.address,
                'default_age':self.age,
                'default_bp':self.bp,
                },
            'target': 'new'
        }
    
    def scan_one(self):
        return{
            'name': "Scan Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'scan.test',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '1'
                },
            'target': 'new'
            }
        
    def scan_two(self):
        return{
            'name': "Scan Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'scan.test',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '2'
                },
            'target': 'new'
            }
    def scan_three(self):
        return{
            'name': "Scan Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'scan.test',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '3'
                },
            'target': 'new'
            }
        
    def scan_four(self):
        return{
            'name': "Scan Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'scan.test',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '4'
                },
            'target': 'new'
            }
        
    def scan_five(self):
        return{
            'name': "Scan Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'scan.test',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '5'
                },
            'target': 'new'
            }
        
    def scan_six(self):
        return{
            'name': "Scan Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'scan.test',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '6'
                },
            'target': 'new'
            }
        
    def scan_seven(self):
        return{
            'name': "Scan Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'scan.test',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '7'
                },
            'target': 'new'
            }
        
    def scan_eight(self):
        return{
            'name': "Scan Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'scan.test',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '8'
                },
            'target': 'new'
            }
        
    def scan_nine(self):
        return{
            'name': "Scan Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'scan.test',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '9'
                },
            'target': 'new'
            }
        
    def scan_ten(self):
        return{
            'name': "Scan Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'scan.test',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '10'
                },
            'target': 'new'
            }
        
    def lab_button(self):
        return{
            'name': "Lab Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'lab.scan.form',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '1'
                },
            'target': 'new'
            }
    
    def lab_one(self):
        return{
            'name': "Lab Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'lab.scan.form',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '2'
                },
            'target': 'new'
            }
    def lab_two(self):
        return{
            'name': "Lab Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'lab.scan.form',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '3'
                },
            'target': 'new'
            }
    def lab_three(self):
        return{
            'name': "Lab Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'lab.scan.form',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '4'
                },
            'target': 'new'
            }
    def lab_four(self):
        return{
            'name': "Lab Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'lab.scan.form',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '5'
                },
            'target': 'new'
            }
    def lab_five(self):
        return{
            'name': "Lab Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'lab.scan.form',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '6'
                },
            'target': 'new'
            }
    def lab_six(self):
        return{
            'name': "Lab Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'lab.scan.form',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '7'
                },
            'target': 'new'
            }
    def lab_seven(self):
        return{
            'name': "Lab Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'lab.scan.form',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '8'
                },
            'target': 'new'
            }
    def lab_eight(self):
        return{
            'name': "Lab Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'lab.scan.form',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '9'
                },
            'target': 'new'
            }
    def lab_nine(self):
        return{
            'name': "Lab Tests",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'lab.scan.form',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '10'
                },
            'target': 'new'
            }
        
        
    def diet_for(self):
        return{
            'name': "Prescribe Diet",
            'type': 'ir.actions.act_window', 
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'prescribe.diet',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '1'
                },
            'target': 'new'
        }
        
    def diet_one(self):
        return{
            'name': "Prescribe Diet",
            'type': 'ir.actions.act_window', 
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'prescribe.diet',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '2'
                },
            'target': 'new'
        }
        
    def diet_two(self):
        return{
            'name': "Prescribe Diet",
            'type': 'ir.actions.act_window', 
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'prescribe.diet',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '3'
                },
            'target': 'new'
        }
        
    def diet_three(self):
        return{
            'name': "Prescribe Diet",
            'type': 'ir.actions.act_window', 
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'prescribe.diet',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '4'
                },
            'target': 'new'
        }
        
    def diet_four(self):
        return{
            'name': "Prescribe Diet",
            'type': 'ir.actions.act_window', 
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'prescribe.diet',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '5'
                },
            'target': 'new'
        }
        
    def diet_five(self):
        return{
            'name': "Prescribe Diet",
            'type': 'ir.actions.act_window', 
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'prescribe.diet',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '6'
                },
            'target': 'new'
        }
        
    def diet_six(self):
        return{
            'name': "Prescribe Diet",
            'type': 'ir.actions.act_window', 
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'prescribe.diet',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '7'
                },
            'target': 'new'
        }
        
    def diet_seven(self):
        return{
            'name': "Prescribe Diet",
            'type': 'ir.actions.act_window', 
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'prescribe.diet',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '8'
                },
            'target': 'new'
        }
        
    def diet_eight(self):
        return{
            'name': "Prescribe Diet",
            'type': 'ir.actions.act_window', 
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'prescribe.diet',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '9'
                },
            'target': 'new'
        }
        
    def diet_nine(self):
        return{
            'name': "Prescribe Diet",
            'type': 'ir.actions.act_window', 
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'prescribe.diet',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_num_days': '10'
                },
            'target': 'new'
        }
    
        
    def prescription_button(self):
        
        return{
            'name': "Prescription",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'medical.prescription.order',
            'view_id': self.env.ref('basic_hms.medical_prescription_order_form_view').id,
            'context': {
                'default_doctor_id': self.doctor_in.id,
                'default_sex': self.gender,
                'default_patient_id': self.patient_id.id,
                'default_prescription_date': datetime.now(),
                'default_num_days': '1',
                },
                'target': 'new'
            }
        
    def prescription_one(self):
        return{
            'name': "Prescription",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'medical.prescription.order',
            'view_id': self.env.ref('basic_hms.medical_prescription_order_form_view').id,
            'context': {
                'default_doctor_id': self.doctor_in.id,
                'default_sex': self.gender,
                'default_patient_id': self.patient_id.id,
                'default_prescription_date': datetime.now(),
                'default_num_days': '2',
                },
                'target': 'new'
            }
    def prescription_two(self):
        return{
            'name': "Prescription",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'medical.prescription.order',
            'view_id': self.env.ref('basic_hms.medical_prescription_order_form_view').id,
            'context': {
                'default_doctor_id': self.doctor_in.id,
                'default_sex': self.gender,
                'default_patient_id': self.patient_id.id,
                'default_prescription_date': datetime.now(),
                'default_num_days': '3',
                },
                'target': 'new'
            }
    def prescription_three(self):
        return{
            'name': "Prescription",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'medical.prescription.order',
            'view_id': self.env.ref('basic_hms.medical_prescription_order_form_view').id,
            'context': {
                'default_doctor_id': self.doctor_in.id,
                'default_sex': self.gender,
                'default_patient_id': self.patient_id.id,
                'default_prescription_date': datetime.now(),
                'default_num_days': '4',
                },
                'target': 'new'
            }
    def prescription_four(self):
        return{
            'name': "Prescription",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'medical.prescription.order',
            'view_id': self.env.ref('basic_hms.medical_prescription_order_form_view').id,
            'context': {
                'default_doctor_id': self.doctor_in.id,
                'default_sex': self.gender,
                'default_patient_id': self.patient_id.id,
                'default_prescription_date': datetime.now(),
                'default_num_days': '5',
                },
                'target': 'new'
            }
    def prescription_five(self):
        return{
            'name': "Prescription",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'medical.prescription.order',
            'view_id': self.env.ref('basic_hms.medical_prescription_order_form_view').id,
            'context': {
                'default_doctor_id': self.doctor_in.id,
                'default_sex': self.gender,
                'default_patient_id': self.patient_id.id,
                'default_prescription_date': datetime.now(),
                'default_num_days': '6',
                },
                'target': 'new'
            }
    def prescription_six(self):
        return{
            'name': "Prescription",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'medical.prescription.order',
            'view_id': self.env.ref('basic_hms.medical_prescription_order_form_view').id,
            'context': {
                'default_doctor_id': self.doctor_in.id,
                'default_sex': self.gender,
                'default_patient_id': self.patient_id.id,
                'default_prescription_date': datetime.now(),
                'default_num_days': '7',
                },
                'target': 'new'
            }
    def prescription_seven(self):
        return{
            'name': "Prescription",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'medical.prescription.order',
            'view_id': self.env.ref('basic_hms.medical_prescription_order_form_view').id,
            'context': {
                'default_doctor_id': self.doctor_in.id,
                'default_sex': self.gender,
                'default_patient_id': self.patient_id.id,
                'default_prescription_date': datetime.now(),
                'default_num_days': '8',
                },
                'target': 'new'
            }
    def prescription_eight(self):
        return{
            'name': "Prescription",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'medical.prescription.order',
            'view_id': self.env.ref('basic_hms.medical_prescription_order_form_view').id,
            'context': {
                'default_doctor_id': self.doctor_in.id,
                'default_sex': self.gender,
                'default_patient_id': self.patient_id.id,
                'default_prescription_date': datetime.now(),
                'default_num_days': '9',
                },
                'target': 'new'
            }
    def prescription_nine(self):
        return{
            'name': "Prescription",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'medical.prescription.order',
            'view_id': self.env.ref('basic_hms.medical_prescription_order_form_view').id,
            'context': {
                'default_doctor_id': self.doctor_in.id,
                'default_sex': self.gender,
                'default_patient_id': self.patient_id.id,
                'default_prescription_date': datetime.now(),
                'default_num_days': '10',
                },
                'target': 'new'
            }
    
        
class InPatientNotebook(models.Model):
    _name = 'in.patient.dayone'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    doctor = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor')
    review = fields.Text(string='Review')
    medicine = fields.Char(string='Medicines')
    drounds = fields.Char(string='Round', default='Round ')
    
class DietOne(models.Model):
    _name = 'diet.line.old'
    
    diet2 = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade', index=True, copy=False)
    diet_for = fields.Many2one('set.diets',string="Diet Name")
    diet_seq = fields.Many2one('prescribe.diet',string='Diet S.No')
    dates = fields.Datetime(string='Date')
    name = fields.Many2one('in.patient',string='Name')
    patient_id = fields.Many2one('res.partner', string='Patient Name')
    diet_id = fields.Many2one('prescribe.diet',string='Diet')
    
class DietOnet(models.Model):
    _name = 'diet.line.in'
    
    diet2 = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade', index=True, copy=False)
    diet_for = fields.Many2one('set.diets',string="Diet Name")
    diet_seq = fields.Many2one('prescribe.diet',string='Diet S.No')
    dates = fields.Datetime(string='Date')
    name = fields.Many2one('in.patient',string='Name')
    patient_id = fields.Many2one('res.partner', string='Patient Name')
    diet_id = fields.Many2one('prescribe.diet',string='Diet')
    
class SisterRound(models.Model):
    _name='sister.round'
    
    
    name = fields.Many2one('in.patient',string='IN Details')
    nurse_name = fields.Many2one('res.partner',string='Nurse Name')
    time = fields.Char(string='Time', default='02:30 After Noon')
    cbg = fields.Selection([('rbs','RBS'),('fbs','FBS'),('ppbs','PPBS')],string='CBG')
    bp = fields.Char(string='BP', default='BP-mm/Hg')
    temp = fields.Char(string='TEMP', default='*F')
    spo2 = fields.Char(string='SPO2', default='%')
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
    
    @api.model
    def create(self,vals):
        result = super(TherapyIP, self).create(vals)
        patient_id = result.name.patient_id.id
        orm = self.env['patient.bills'].search([('patient_name','=',patient_id)],order='id desc', limit=1)
        lines=[]
        # orm1 = self.env['']
        for rec in result:
            valuez={
                    'therapy':rec.therapy,
                    'time':rec.time,
                    'amount': rec.amount,
                }
            lines.append((0, 0, valuez))
        orm.write({'ip_therapy':lines})
        return result
    
class DoctorLine(models.Model):
    _name = 'line.two'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    doctor = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor')
    review = fields.Text(string='Review')
    medicine = fields.Char(string='Medicines')
    drounds = fields.Char(string='Round', default='Round ')
    
class sisterLine(models.Model):
    _name = 'sister.line'
    
    name = fields.Many2one('in.patient',string='IN Details')
    nurse_name = fields.Many2one('res.partner',string='Nurse Name')
    time = fields.Char(string='Time', default='02:30 After Noon')
    cbg = fields.Selection([('rbs','RBS'),('fbs','FBS'),('ppbs','PPBS')],string='CBG')
    bp = fields.Char(string='BP', default='BP-mm/Hg')
    temp = fields.Char(string='TEMP', default='*F')
    spo2 = fields.Char(string='SPO2', default='%')
    motion = fields.Char(string='Motion')
    urine = fields.Char(string='Urine')
    sleep = fields.Char(string='Sleep')
    digestion = fields.Char(string='Digestion')
    pain = fields.Char(string='Pain')
    notes = fields.Char(string='Notes')
    
class TherapyLineOne(models.Model):
    _name = 'therapy.line'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    therapy = fields.Char(string='Therapy')
    amount = fields.Char(string='Amount')
    
    @api.model
    def create(self, vals):
        res = super(TherapyLineOne, self).create(vals)
        patient_id = res.name.patient_id.id
        orm = self.env['patient.bills'].search([('patient_name','=',patient_id)],order='id desc', limit=1)
        lines=[]
        # orm1 = self.env['']
        for rec in res:
            valuez={
                    'therapy':rec.therapy,
                    'time':rec.time,
                    'amount': rec.amount,
                }
            lines.append((0, 0, valuez))
        orm.write({'ip_therapy':lines})
        return res
    
class DoctorLineOne(models.Model):
    _name = 'line.three'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    doctor = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor')
    review = fields.Text(string='Review')
    medicine = fields.Char(string='Medicines')
    drounds = fields.Char(string='Round', default='Round ')
    
class sisterLine(models.Model):
    _name = 'sister.line.three'
    
    name = fields.Many2one('in.patient',string='IN Details')
    nurse_name = fields.Many2one('res.partner',string='Nurse Name')
    time = fields.Char(string='Time', default='02:30 After Noon')
    cbg = fields.Selection([('rbs','RBS'),('fbs','FBS'),('ppbs','PPBS')],string='CBG')
    bp = fields.Char(string='BP', default='BP-mm/Hg')
    temp = fields.Char(string='TEMP', default='*F')
    spo2 = fields.Char(string='SPO2', default='%')
    motion = fields.Char(string='Motion')
    urine = fields.Char(string='Urine')
    sleep = fields.Char(string='Sleep')
    digestion = fields.Char(string='Digestion')
    pain = fields.Char(string='Pain')
    notes = fields.Char(string='Notes')
    
class TherapyLineThree(models.Model):
    _name = 'therapy.line.three'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    therapy = fields.Char(string='Therapy')
    amount = fields.Char(string='Amount')
    
    @api.model
    def create(self, vals):
        res = super(TherapyLineThree, self).create(vals)
        patient_id = res.name.patient_id.id
        orm = self.env['patient.bills'].search([('patient_name','=',patient_id)],order='id desc', limit=1)
        lines=[]
        # orm1 = self.env['']
        for rec in res:
            valuez={
                    'therapy':rec.therapy,
                    'time':rec.time,
                    'amount': rec.amount,
                }
            lines.append((0, 0, valuez))
        orm.write({'ip_therapy':lines})
        return res
    
class DoctorLine(models.Model):
    _name = 'line.four'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    doctor = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor')
    review = fields.Text(string='Review')
    medicine = fields.Char(string='Medicines')
    drounds = fields.Char(string='Round', default='Round ')
    
class sisterLine(models.Model):
    _name = 'sister.line.four'
    
    name = fields.Many2one('in.patient',string='IN Details')
    nurse_name = fields.Many2one('res.partner',string='Nurse Name')
    time = fields.Char(string='Time', default='02:30 After Noon')
    cbg = fields.Selection([('rbs','RBS'),('fbs','FBS'),('ppbs','PPBS')],string='CBG')
    bp = fields.Char(string='BP', default='BP-mm/Hg')
    temp = fields.Char(string='TEMP', default='*F')
    spo2 = fields.Char(string='SPO2', default='%')
    motion = fields.Char(string='Motion')
    urine = fields.Char(string='Urine')
    sleep = fields.Char(string='Sleep')
    digestion = fields.Char(string='Digestion')
    pain = fields.Char(string='Pain')
    notes = fields.Char(string='Notes')
    
class TherapyLineFour(models.Model):
    _name = 'therapy.line.four'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    therapy = fields.Char(string='Therapy')
    amount = fields.Char(string='Amount')
    
    @api.model
    def create(self, vals):
        res = super(TherapyLineFour, self).create(vals)
        patient_id = res.name.patient_id.id
        orm = self.env['patient.bills'].search([('patient_name','=',patient_id)],order='id desc', limit=1)
        lines=[]
        # orm1 = self.env['']
        for rec in res:
            valuez={
                    'therapy':rec.therapy,
                    'time':rec.time,
                    'amount': rec.amount,
                }
            lines.append((0, 0, valuez))
        orm.write({'ip_therapy':lines})
        return res
    
# class DoctorLine(models.Model):
#     _name = 'line.four'
    
#     name = fields.Many2one('in.patient',string='IN Details')
#     time = fields.Char(string='Time')
#     doctor = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor')
#     review = fields.Text(string='Review')
#     medicine = fields.Char(string='Medicines')
#     rounds = fields.Selection([('1','Round 1'),('2','Round 2'),('3','Round 3')], string='Round')
    
# class sisterLine(models.Model):
#     _name = 'sister.line.four'
    
#     name = fields.Many2one('in.patient',string='IN Details')
#     nurse_name = fields.Many2one('res.partner',string='Nurse Name')
#     time = fields.Char(string='Time')
#     lbg = fields.Char(string='LBG')
#     bp = fields.Char(string='BP')
#     temp = fields.Char(string='TEMP')
#     spo2 = fields.Char(string='SPO2')
#     motion = fields.Char(string='Motion')
#     urine = fields.Char(string='Urine')
#     sleep = fields.Char(string='Sleep')
#     digestion = fields.Char(string='Digestion')
#     pain = fields.Char(string='Pain')
#     notes = fields.Char(string='Notes')
    
# class TherapyLine(models.Model):
#     _name = 'therapy.line.four'
    
#     name = fields.Many2one('in.patient',string='IN Details')
#     time = fields.Char(string='Time')
#     therapy = fields.Char(string='Therapy')
#     amount = fields.Char(string='Amount')
    
class DoctorLine(models.Model):
    _name = 'line.five'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    doctor = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor')
    review = fields.Text(string='Review')
    medicine = fields.Char(string='Medicines')
    drounds = fields.Char(string='Round', default='Round ')
    
class sisterLine(models.Model):
    _name = 'sister.line.five'
    
    name = fields.Many2one('in.patient',string='IN Details')
    nurse_name = fields.Many2one('res.partner',string='Nurse Name')
    time = fields.Char(string='Time', default='02:30 After Noon')
    cbg = fields.Selection([('rbs','RBS'),('fbs','FBS'),('ppbs','PPBS')],string='CBG')
    bp = fields.Char(string='BP', default='BP-mm/Hg')
    temp = fields.Char(string='TEMP', default='*F')
    spo2 = fields.Char(string='SPO2', default='%')
    motion = fields.Char(string='Motion')
    urine = fields.Char(string='Urine')
    sleep = fields.Char(string='Sleep')
    digestion = fields.Char(string='Digestion')
    pain = fields.Char(string='Pain')
    notes = fields.Char(string='Notes')
    
class TherapyLineFive(models.Model):
    _name = 'therapy.line.five'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    therapy = fields.Char(string='Therapy')
    amount = fields.Char(string='Amount')
    
    @api.model
    def create(self, vals):
        res = super(TherapyLineFive, self).create(vals)
        patient_id = res.name.patient_id.id
        orm = self.env['patient.bills'].search([('patient_name','=',patient_id)],order='id desc', limit=1)
        lines=[]
        # orm1 = self.env['']
        for rec in res:
            valuez={
                    'therapy':rec.therapy,
                    'time':rec.time,
                    'amount': rec.amount,
                }
            lines.append((0, 0, valuez))
        orm.write({'ip_therapy':lines})
        return res
    
class DoctorLine(models.Model):
    _name = 'line.six'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    doctor = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor')
    review = fields.Text(string='Review')
    medicine = fields.Char(string='Medicines')
    drounds = fields.Char(string='Round', default='Round ')
    
class sisterLine(models.Model):
    _name = 'sister.line.six'
    
    name = fields.Many2one('in.patient',string='IN Details')
    nurse_name = fields.Many2one('res.partner',string='Nurse Name')
    time = fields.Char(string='Time', default='02:30 After Noon')
    cbg = fields.Selection([('rbs','RBS'),('fbs','FBS'),('ppbs','PPBS')],string='CBG')
    bp = fields.Char(string='BP', default='BP-mm/Hg')
    temp = fields.Char(string='TEMP', default='*F')
    spo2 = fields.Char(string='SPO2', default='%')
    motion = fields.Char(string='Motion')
    urine = fields.Char(string='Urine')
    sleep = fields.Char(string='Sleep')
    digestion = fields.Char(string='Digestion')
    pain = fields.Char(string='Pain')
    notes = fields.Char(string='Notes')
    
class TherapyLineSix(models.Model):
    _name = 'therapy.line.six'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    therapy = fields.Char(string='Therapy')
    amount = fields.Char(string='Amount')
    
    @api.model
    def create(self, vals):
        res = super(TherapyLineSix, self).create(vals)
        patient_id = res.name.patient_id.id
        orm = self.env['patient.bills'].search([('patient_name','=',patient_id)],order='id desc', limit=1)
        lines=[]
        # orm1 = self.env['']
        for rec in res:
            valuez={
                    'therapy':rec.therapy,
                    'time':rec.time,
                    'amount': rec.amount,
                }
            lines.append((0, 0, valuez))
        orm.write({'ip_therapy':lines})
        return res
    
class DoctorLine(models.Model):
    _name = 'line.seven'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    doctor = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor')
    review = fields.Text(string='Review')
    medicine = fields.Char(string='Medicines')
    drounds = fields.Char(string='Round', default='Round ')
    
class sisterLine(models.Model):
    _name = 'sister.line.seven'
    
    name = fields.Many2one('in.patient',string='IN Details')
    nurse_name = fields.Many2one('res.partner',string='Nurse Name')
    time = fields.Char(string='Time', default='02:30 After Noon')
    cbg = fields.Selection([('rbs','RBS'),('fbs','FBS'),('ppbs','PPBS')],string='CBG')
    bp = fields.Char(string='BP', default='BP-mm/Hg')
    temp = fields.Char(string='TEMP', default='*F')
    spo2 = fields.Char(string='SPO2', default='%')
    motion = fields.Char(string='Motion')
    urine = fields.Char(string='Urine')
    sleep = fields.Char(string='Sleep')
    digestion = fields.Char(string='Digestion')
    pain = fields.Char(string='Pain')
    notes = fields.Char(string='Notes')
    
class TherapyLineSeven(models.Model):
    _name = 'therapy.line.seven'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    therapy = fields.Char(string='Therapy')
    amount = fields.Char(string='Amount')
    
    @api.model
    def create(self, vals):
        res = super(TherapyLineSeven, self).create(vals)
        patient_id = res.name.patient_id.id
        orm = self.env['patient.bills'].search([('patient_name','=',patient_id)],order='id desc', limit=1)
        lines=[]
        # orm1 = self.env['']
        for rec in res:
            valuez={
                    'therapy':rec.therapy,
                    'time':rec.time,
                    'amount': rec.amount,
                }
            lines.append((0, 0, valuez))
        orm.write({'ip_therapy':lines})
        return res
    
class DoctorLine(models.Model):
    _name = 'line.eight'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    doctor = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor')
    review = fields.Text(string='Review')
    medicine = fields.Char(string='Medicines')
    drounds = fields.Char(string='Round', default='Round ')
    
class sisterLine(models.Model):
    _name = 'sister.line.eight'
    
    name = fields.Many2one('in.patient',string='IN Details')
    nurse_name = fields.Many2one('res.partner',string='Nurse Name')
    time = fields.Char(string='Time', default='02:30 After Noon')
    cbg = fields.Selection([('rbs','RBS'),('fbs','FBS'),('ppbs','PPBS')],string='CBG')
    bp = fields.Char(string='BP', default='BP-mm/Hg')
    temp = fields.Char(string='TEMP', default='*F')
    spo2 = fields.Char(string='SPO2', default='%')
    motion = fields.Char(string='Motion')
    urine = fields.Char(string='Urine')
    sleep = fields.Char(string='Sleep')
    digestion = fields.Char(string='Digestion')
    pain = fields.Char(string='Pain')
    notes = fields.Char(string='Notes')
    
class TherapyLineEight(models.Model):
    _name = 'therapy.line.eight'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    therapy = fields.Char(string='Therapy')
    amount = fields.Char(string='Amount')
    
    @api.model
    def create(self, vals):
        res = super(TherapyLineEight, self).create(vals)
        patient_id = res.name.patient_id.id
        orm = self.env['patient.bills'].search([('patient_name','=',patient_id)],order='id desc', limit=1)
        lines=[]
        # orm1 = self.env['']
        for rec in res:
            valuez={
                    'therapy':rec.therapy,
                    'time':rec.time,
                    'amount': rec.amount,
                }
            lines.append((0, 0, valuez))
        orm.write({'ip_therapy':lines})
        return res
    
class DoctorLine(models.Model):
    _name = 'line.nine'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    doctor = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor')
    review = fields.Text(string='Review')
    medicine = fields.Char(string='Medicines')
    drounds = fields.Char(string='Round', default='Round ')
    
class sisterLine(models.Model):
    _name = 'sister.line.nine'
    
    name = fields.Many2one('in.patient',string='IN Details')
    nurse_name = fields.Many2one('res.partner',string='Nurse Name')
    time = fields.Char(string='Time', default='02:30 After Noon')
    cbg = fields.Selection([('rbs','RBS'),('fbs','FBS'),('ppbs','PPBS')],string='CBG')
    bp = fields.Char(string='BP', default='BP-mm/Hg')
    temp = fields.Char(string='TEMP', default='*F')
    spo2 = fields.Char(string='SPO2', default='%')
    motion = fields.Char(string='Motion')
    urine = fields.Char(string='Urine')
    sleep = fields.Char(string='Sleep')
    digestion = fields.Char(string='Digestion')
    pain = fields.Char(string='Pain')
    notes = fields.Char(string='Notes')
    
class TherapyLineNine(models.Model):
    _name = 'therapy.line.nine'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    therapy = fields.Char(string='Therapy')
    amount = fields.Char(string='Amount')
    
    @api.model
    def create(self, vals):
        res = super(TherapyLineNine, self).create(vals)
        patient_id = res.name.patient_id.id
        orm = self.env['patient.bills'].search([('patient_name','=',patient_id)],order='id desc', limit=1)
        lines=[]
        for rec in res:
            valuez={
                    'therapy':rec.therapy,
                    'time':rec.time,
                    'amount': rec.amount,
                }
            lines.append((0, 0, valuez))
        orm.write({'ip_therapy':lines})
        return res
    
class DoctorLine(models.Model):
    _name = 'line.ten'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    doctor = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor')
    review = fields.Text(string='Review')
    medicine = fields.Char(string='Medicines')
    drounds = fields.Char(string='Round', default='Round ')
    
class sisterLine(models.Model):
    _name = 'sister.line.ten'
    
    name = fields.Many2one('in.patient',string='IN Details')
    nurse_name = fields.Many2one('res.partner',string='Nurse Name')
    time = fields.Char(string='Time', default='02:30 After Noon')
    cbg = fields.Selection([('rbs','RBS'),('fbs','FBS'),('ppbs','PPBS')],string='CBG')
    bp = fields.Char(string='BP', default='BP-mm/Hg')
    temp = fields.Char(string='TEMP', default='*F')
    spo2 = fields.Char(string='SPO2', default='%')
    motion = fields.Char(string='Motion')
    urine = fields.Char(string='Urine')
    sleep = fields.Char(string='Sleep')
    digestion = fields.Char(string='Digestion')
    pain = fields.Char(string='Pain')
    notes = fields.Char(string='Notes')
    
class TherapyLineTen(models.Model):
    _name = 'therapy.line.ten'
    
    name = fields.Many2one('in.patient',string='IN Details')
    time = fields.Char(string='Time')
    therapy = fields.Char(string='Therapy')
    amount = fields.Char(string='Amount')
    
    @api.model
    def create(self, vals):
        res = super(TherapyLineTen, self).create(vals)
        patient_id = res.name.patient_id.id
        orm = self.env['patient.bills'].search([('patient_name','=',patient_id)],order='id desc', limit=1)
        lines=[]
        # orm1 = self.env['']
        for rec in res:
            valuez={
                    'therapy':rec.therapy,
                    'time':rec.time,
                    'amount': rec.amount,
                }
            lines.append((0, 0, valuez))
        orm.write({'ip_therapy':lines})
        return res
    
class Dietline(models.Model):
    _name = 'diet.line.one'
    
    diet2 = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade', index=True, copy=False)
    diet_for = fields.Many2one('set.diets',string="Diet Name")
    diet_seq = fields.Many2one('prescribe.diet',string='Diet S.No')
    dates = fields.Datetime(string='Date')
    name = fields.Many2one('in.patient',string='Name')
    patient_id = fields.Many2one('res.partner', string='Patient Name')
    
    @api.onchange('patient_id')
    def write(self,vals):
        result = super(Dietline, self).create(vals)
        if self.num_days == '1':
            diet_pages = self.env['in.patient'].search([('patient_id','=',result.patient_id.id)])
            
            diet_lines_append=[(4,0)]
            valuez={
                'diet_for':result.name.id,
                'dates':datetime.datetime.now(),
                }
            diet_lines_append.append((0,0,valuez))
            
            diet_pages.write({'diet_line':diet_lines_append})

class Dietlinetwo(models.Model):
    _name = 'diet.line.two'
    
    diet2 = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade', index=True, copy=False)
    diet_for = fields.Many2one('set.diets',string="Diet Name")
    diet_seq = fields.Many2one('prescribe.diet',string='Diet S.No')
    dates=fields.Datetime(string='Date')
    name=fields.Many2one('in.patient',string='Name')
    patient_id = fields.Many2one('res.partner', string='Patient Name')
    
class Dietlinethree(models.Model):
    _name = 'diet.line.three'
    
    diet2 = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade', index=True, copy=False)
    diet_for = fields.Many2one('set.diets',string="Diet Name")
    diet_seq = fields.Many2one('prescribe.diet',string='Diet S.No')
    dates=fields.Datetime(string='Date')
    name=fields.Many2one('in.patient',string='Name')
    
class Dietlinefour(models.Model):
    _name = 'diet.line.four'
    
    diet2 = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade', index=True, copy=False)
    diet_for = fields.Many2one('set.diets',string="Diet Name")
    diet_seq = fields.Many2one('prescribe.diet',string='Diet S.No')
    dates=fields.Datetime(string='Date')
    name=fields.Many2one('in.patient',string='Name')
    
class Dietlinefive(models.Model):
    _name = 'diet.line.five'
    
    diet2 = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade', index=True, copy=False)
    diet_for = fields.Many2one('set.diets',string="Diet Name")
    diet_seq = fields.Many2one('prescribe.diet',string='Diet S.No')
    dates=fields.Datetime(string='Date')
    name=fields.Many2one('in.patient',string='Name')
    
class Dietlinesix(models.Model):
    _name = 'diet.line.six'
    
    diet2 = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade', index=True, copy=False)
    diet_for = fields.Many2one('set.diets',string="Diet Name")
    diet_seq = fields.Many2one('prescribe.diet',string='Diet S.No')
    dates=fields.Datetime(string='Date')
    name=fields.Many2one('in.patient',string='Name')
    
class Dietlineseven(models.Model):
    _name = 'diet.line.seven'
    
    diet2 = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade', index=True, copy=False)
    diet_for = fields.Many2one('set.diets',string="Diet Name")
    diet_seq = fields.Many2one('prescribe.diet',string='Diet S.No')
    dates=fields.Datetime(string='Date')
    name=fields.Many2one('in.patient',string='Name')
    
class Dietlineeight(models.Model):
    _name = 'diet.line.eight'
    
    diet2 = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade', index=True, copy=False)
    diet_for = fields.Many2one('set.diets',string="Diet Name")
    diet_seq = fields.Many2one('prescribe.diet',string='Diet S.No')
    dates=fields.Datetime(string='Date')
    name=fields.Many2one('in.patient',string='Name')
    
class Dietlinenine(models.Model):
    _name = 'diet.line.nine'
    
    diet2 = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade', index=True, copy=False)
    diet_for = fields.Many2one('set.diets',string="Diet Name")
    diet_seq = fields.Many2one('prescribe.diet',string='Diet S.No')
    dates=fields.Datetime(string='Date')
    name=fields.Many2one('in.patient',string='Name')
    
class MedicineLineOne(models.Model):
    _name = 'medicine.line.one'
    
    medical_doctor = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    # medicine_name = fields.Many2one('product.product',string='Medicine Name')
    patient_name = fields.Many2one('res.partner',string="Patient Name")
    ip_name = fields.Many2one('in.patient', string='Patient Name')
    
    prescription_alot= fields.Many2one('medical.prescription.order',string="Prescriptions",required=True)
    date = fields.Datetime(string="Date of Prescription")
    delivery_option= fields.Selection([('dir','Direct'),('on',"Online")],string="Delivery Option")
    delivery_mode = fields.Selection([('domestic','Domestic'),('international',"International")],string='Courier Mode')
    
class MedicineLinetwo(models.Model):
    _name = 'medicine.line.two'
    
    medical_doctor = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    # medicine_name = fields.Many2one('product.product',string='Medicine Name')
    patient_name = fields.Many2one('res.partner',string="Patient Name")
    ip_name = fields.Many2one('in.patient', string='Patient Name')
    
    prescription_alot= fields.Many2one('medical.prescription.order',string="Prescriptions",required=True)
    date = fields.Datetime(string="Date of Prescription")
    delivery_option= fields.Selection([('dir','Direct'),('on',"Online")],string="Delivery Option")
    delivery_mode = fields.Selection([('domestic','Domestic'),('international',"International")],string='Courier Mode')
    
class MedicineLinethree(models.Model):
    _name = 'medicine.line.three'
    
    medical_doctor = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    # medicine_name = fields.Many2one('product.product',string='Medicine Name')
    patient_name = fields.Many2one('res.partner',string="Patient Name")
    ip_name = fields.Many2one('in.patient', string='Patient Name')
    
    prescription_alot= fields.Many2one('medical.prescription.order',string="Prescriptions",required=True)
    date = fields.Datetime(string="Date of Prescription")
    delivery_option= fields.Selection([('dir','Direct'),('on',"Online")],string="Delivery Option")
    delivery_mode = fields.Selection([('domestic','Domestic'),('international',"International")],string='Courier Mode')
    
class MedicineLinefour(models.Model):
    _name = 'medicine.line.four'
    
    medical_doctor = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    # medicine_name = fields.Many2one('product.product',string='Medicine Name')
    patient_name = fields.Many2one('res.partner',string="Patient Name")
    ip_name = fields.Many2one('in.patient', string='Patient Name')
    
    prescription_alot= fields.Many2one('medical.prescription.order',string="Prescriptions",required=True)
    date = fields.Datetime(string="Date of Prescription")
    delivery_option= fields.Selection([('dir','Direct'),('on',"Online")],string="Delivery Option")
    delivery_mode = fields.Selection([('domestic','Domestic'),('international',"International")],string='Courier Mode')
    
class MedicineLinefive(models.Model):
    _name = 'medicine.line.five'
    
    medical_doctor = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    # medicine_name = fields.Many2one('product.product',string='Medicine Name')
    patient_name = fields.Many2one('res.partner',string="Patient Name")
    ip_name = fields.Many2one('in.patient', string='Patient Name')
    
    prescription_alot= fields.Many2one('medical.prescription.order',string="Prescriptions",required=True)
    date = fields.Datetime(string="Date of Prescription")
    delivery_option= fields.Selection([('dir','Direct'),('on',"Online")],string="Delivery Option")
    delivery_mode = fields.Selection([('domestic','Domestic'),('international',"International")],string='Courier Mode')
    
class MedicineLinesix(models.Model):
    _name = 'medicine.line.six'
    
    medical_doctor = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    # medicine_name = fields.Many2one('product.product',string='Medicine Name')
    patient_name = fields.Many2one('res.partner',string="Patient Name")
    ip_name = fields.Many2one('in.patient', string='Patient Name')
    
    prescription_alot= fields.Many2one('medical.prescription.order',string="Prescriptions",required=True)
    date = fields.Datetime(string="Date of Prescription")
    delivery_option= fields.Selection([('dir','Direct'),('on',"Online")],string="Delivery Option")
    delivery_mode = fields.Selection([('domestic','Domestic'),('international',"International")],string='Courier Mode')
    
class MedicineLineseven(models.Model):
    _name = 'medicine.line.seven'
    
    medical_doctor = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    # medicine_name = fields.Many2one('product.product',string='Medicine Name')
    patient_name = fields.Many2one('res.partner',string="Patient Name")
    ip_name = fields.Many2one('in.patient', string='Patient Name')
    
    prescription_alot= fields.Many2one('medical.prescription.order',string="Prescriptions",required=True)
    date = fields.Datetime(string="Date of Prescription")
    delivery_option= fields.Selection([('dir','Direct'),('on',"Online")],string="Delivery Option")
    delivery_mode = fields.Selection([('domestic','Domestic'),('international',"International")],string='Courier Mode')
    
class MedicineLineeight(models.Model):
    _name = 'medicine.line.eight'
    
    medical_doctor = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    # medicine_name = fields.Many2one('product.product',string='Medicine Name')
    patient_name = fields.Many2one('res.partner',string="Patient Name")
    ip_name = fields.Many2one('in.patient', string='Patient Name')
    
    prescription_alot= fields.Many2one('medical.prescription.order',string="Prescriptions",required=True)
    date = fields.Datetime(string="Date of Prescription")
    delivery_option= fields.Selection([('dir','Direct'),('on',"Online")],string="Delivery Option")
    delivery_mode = fields.Selection([('domestic','Domestic'),('international',"International")],string='Courier Mode')
    
class MedicineLinenine(models.Model):
    _name = 'medicine.line.nine'
    
    medical_doctor = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    # medicine_name = fields.Many2one('product.product',string='Medicine Name')
    patient_name = fields.Many2one('res.partner',string="Patient Name")
    ip_name = fields.Many2one('in.patient', string='Patient Name')
    
    prescription_alot= fields.Many2one('medical.prescription.order',string="Prescriptions",required=True)
    date = fields.Datetime(string="Date of Prescription")
    delivery_option= fields.Selection([('dir','Direct'),('on',"Online")],string="Delivery Option")
    delivery_mode = fields.Selection([('domestic','Domestic'),('international',"International")],string='Courier Mode')
    
class LabLineOne(models.Model):
    _name = 'lab.line.one'
    
    name = fields.Char(string='Test Name')
    lab_id = fields.Many2one('medical.doctor',string="Name",ondelete='cascade')
    lab_type = fields.Many2one('lab.scan.form',string="Lab")
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    date= fields.Datetime(string="Date of Lab/Scan")
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
class LabLinetwo(models.Model):
    _name = 'lab.line.two'
    
    name = fields.Char(string='Test Name')
    lab_id = fields.Many2one('medical.doctor',string="Name",ondelete='cascade')
    lab_type = fields.Many2one('lab.scan.form',string="Lab")
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    date= fields.Datetime(string="Date of Lab/Scan")
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
class LabLinethree(models.Model):
    _name = 'lab.line.three'
    
    name = fields.Char(string='Test Name')
    lab_id = fields.Many2one('medical.doctor',string="Name",ondelete='cascade')
    lab_type = fields.Many2one('lab.scan.form',string="Lab")
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    date= fields.Datetime(string="Date of Lab/Scan")
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
class LabLinefour(models.Model):
    _name = 'lab.line.four'
    
    name = fields.Char(string='Test Name')
    lab_id = fields.Many2one('medical.doctor',string="Name",ondelete='cascade')
    lab_type = fields.Many2one('lab.scan.form',string="Lab")
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    date= fields.Datetime(string="Date of Lab/Scan")
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
class LabLinefive(models.Model):
    _name = 'lab.line.five'
    
    name = fields.Char(string='Test Name')
    lab_id = fields.Many2one('medical.doctor',string="Name",ondelete='cascade')
    lab_type = fields.Many2one('lab.scan.form',string="Lab")
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    date= fields.Datetime(string="Date of Lab/Scan")
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
class LabLinesix(models.Model):
    _name = 'lab.line.six'
    
    name = fields.Char(string='Test Name')
    lab_id = fields.Many2one('medical.doctor',string="Name",ondelete='cascade')
    lab_type = fields.Many2one('lab.scan.form',string="Lab")
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    date= fields.Datetime(string="Date of Lab/Scan")
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
class LabLineseven(models.Model):
    _name = 'lab.line.seven'
    
    name = fields.Char(string='Test Name')
    lab_id = fields.Many2one('medical.doctor',string="Name",ondelete='cascade')
    lab_type = fields.Many2one('lab.scan.form',string="Lab")
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    date= fields.Datetime(string="Date of Lab/Scan")
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
class LabLineeight(models.Model):
    _name = 'lab.line.eight'
    
    name = fields.Char(string='Test Name')
    lab_id = fields.Many2one('medical.doctor',string="Name",ondelete='cascade')
    lab_type = fields.Many2one('lab.scan.form',string="Lab")
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    date= fields.Datetime(string="Date of Lab/Scan")
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
class LabLinenine(models.Model):
    _name = 'lab.line.nine'
    
    name = fields.Char(string='Test Name')
    lab_id = fields.Many2one('medical.doctor',string="Name",ondelete='cascade')
    lab_type = fields.Many2one('lab.scan.form',string="Lab")
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    date= fields.Datetime(string="Date of Lab/Scan")
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
class scanLineOne(models.Model):
    _name = 'scan.line.one'
    
    scan = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    scan_id = fields.Many2one('scan.test',string="Scan")
    date= fields.Datetime(string="Date of Scan Test")
    name = fields.Char(string='Test Name')
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
class scanLinetwo(models.Model):
    _name = 'scan.line.two'
    
    scan = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    scan_id = fields.Many2one('scan.test',string="Scan")
    date= fields.Datetime(string="Date of Scan Test")
    name = fields.Char(string='Test Name')
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
class scanLinethree(models.Model):
    _name = 'scan.line.three'
    
    scan = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    scan_id = fields.Many2one('scan.test',string="Scan")
    date= fields.Datetime(string="Date of Scan Test")
    name = fields.Char(string='Test Name')
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
class scanLinefour(models.Model):
    _name = 'scan.line.four'
    
    scan = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    scan_id = fields.Many2one('scan.test',string="Scan")
    date= fields.Datetime(string="Date of Scan Test")
    name = fields.Char(string='Test Name')
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
class scanLinefive(models.Model):
    _name = 'scan.line.five'
    
    scan = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    scan_id = fields.Many2one('scan.test',string="Scan")
    date= fields.Datetime(string="Date of Scan Test")
    name = fields.Char(string='Test Name')
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
class scanLinesix(models.Model):
    _name = 'scan.line.six'
    
    scan = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    scan_id = fields.Many2one('scan.test',string="Scan")
    date= fields.Datetime(string="Date of Scan Test")
    name = fields.Char(string='Test Name')
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
class scanLineseven(models.Model):
    _name = 'scan.line.seven'
    
    scan = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    scan_id = fields.Many2one('scan.test',string="Scan")
    date= fields.Datetime(string="Date of Scan Test")
    name = fields.Char(string='Test Name')
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
class scanLineeight(models.Model):
    _name = 'scan.line.eight'
    
    scan = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    scan_id = fields.Many2one('scan.test',string="Scan")
    date= fields.Datetime(string="Date of Scan Test")
    name = fields.Char(string='Test Name')
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    ip_name = fields.Many2one('in.patient',string='Ip Name')
    
class scanLinenine(models.Model):
    _name = 'scan.line.nine'
    
    scan = fields.Many2one('medical.doctor',string="Patient Name",ondelete='cascade')
    scan_id = fields.Many2one('scan.test',string="Scan")
    date= fields.Datetime(string="Date of Scan Test")
    name = fields.Char(string='Test Name')
    range_test = fields.Char(string='Tested Range')
    range_normal = fields.Char(string='Normal Range')
    ip_name = fields.Many2one('in.patient',string='Ip Name')