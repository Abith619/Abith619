from odoo import models, fields

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

    def action_confirm(self):
        for rec in self:
            rec.state='confirm'

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

    techer_line=fields.One2many('teacher.teacher.line','teach')

    state=fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirm'),('inpayment','Inpayment'),
        ('paid','Paid'),('cancelled','Cancelled')
        ],string='Status',track_visibility='always', default='draft')

class TeacherLine(models.Model):
    _name="teacher.teacher.line"
    student_field_1 = fields.Many2one('res.users',string="Users")
    teach = fields.Many2one('teacher.teacher',string="Teacher")