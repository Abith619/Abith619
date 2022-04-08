from odoo.exceptions import ValidationError
from odoo import models, fields, api

#                       Teacher Field, Form
class TeacherRecord(models.Model):
    _name = "teacher.teacher"   
    _inherit=('mail.thread')
    _description= "School teacher"
    name = fields.Char(string='Name', required=True) 
    teacher_age = fields.Integer(string='Age')    
    teacher_dob = fields.Date(string="Date of Birth")    
    gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')    
    teacher_blood_group = fields.Selection([('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'), ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')], string='Blood Group')
    nationality = fields.Many2one('res.country', string='Nationality')

#           E-Mail 
    def action_send_email(self):
        self.ensure_one()
        compose_form_id = False
        return {
        'name': 'Compose Email',
        'type': 'ir.actions.act_window',
        'view_mode': 'form',
        'res_model': 'mail.compose.message',
        'views': [(compose_form_id, 'form')],
        'view_id': compose_form_id,
        'target': 'new',
    }
#       Set Age Condition
    @api.constrains('teacher_age')
    def age(self):
        if self.teacher_age <= 18:
            raise ValidationError("Please provide valid age  ?")
#   Print Report & PDF
    @api.multi
    def print_report(self):
        data={
            'from_date':self.from_date,
            'to_date':self.to_date
        }
        return self.env.ref('teacher.action_student_id_card').report_action(None, data=data)

#       State-Confirm
    def action_confirm(self):
        for rec in self:
            rec.state='confirm'

#       State-Paid
    def action_paid(self):
        for i in self:
            i.state='paid'

    def invoices_button(self):
        return{
        'name': "Paid ",
        'type': 'ir.actions.act_window',
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'teacher.teacher',
        'view_id': self.env.ref('school.view_teacher_form').id,
        'target': 'new'
    }

#           One2many 
    techer_line=fields.One2many('teacher.teacher.line','teach')

#       Condition_for add_line
    @api.constrains('techer_line')
    def val(self):
        if not self.techer_line:
            raise ValidationError('Please Select Your Product')

#       States
    state=fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirm'),('inpayment','Inpayment'),
        ('paid','Paid'),('cancelled','Cancelled')
        ],string='Status',track_visibility='always', default='draft')

class TeacherLine(models.Model):
    _name="teacher.teacher.line"
    student_field_1 = fields.Many2one('res.users',string="Users")
    teach = fields.Many2one('teacher.teacher',string="Teacher")