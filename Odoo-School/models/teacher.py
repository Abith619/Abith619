from odoo import models, fields

class TeacherRecord(models.Model):
    _name = "teacher.teacher"    
    name = fields.Char(string='Name', required=True) 
    teacher_age = fields.Integer(string='Age')    
    teacher_dob = fields.Date(string="Date of Birth")    
    gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')    
    teacher_blood_group = fields.Selection([('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'), ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')], string='Blood Group')
    nationality = fields.Many2one('res.country', string='Nationality')

    techer_line=fields.One2many('teacher.teacher.line','teach')


class TeacherLine(models.Model):
    _name="teacher.teacher.line"
    student_field_1 = fields.Many2one('res.users',string="Users")
    teach = fields.Many2one('teacher.teacher',string="Teacher")