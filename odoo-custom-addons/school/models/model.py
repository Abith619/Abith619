from odoo import models, fields, api
from odoo.exceptions import ValidationError

                    # model & Records for the student
class StudentRecord(models.Model):
    _name = "student.student"  
    name = fields.Char(string='Name', required=True)    
    middle_name = fields.Char(string='Middle Name', required=True)    
    last_name = fields.Char(string='Last Name', required=True)    
    
    photo = fields.Binary(string='Photo')    
    student_age = fields.Integer(string='Age')    
    student_dob = fields.Date(string="Date of Birth")    
    student_gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')    
    student_blood_group = fields.Selection([('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
    ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')], string='Blood Group')    

    nationality = fields.Many2one('res.country', string='Nationality')
        # Kanban View create Stages from 'service.stages' Model
    stage_ids = fields.Many2one("service.stages", string="Stage", group_expand="_read_group_stage_ids",track_visibility='onchange')
        # Add & Create Stages from Kanban View
    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        stage_idx = self.env['service.stages'].search([])
        return stage_idx

#       For Kanban-view State_Lock_Condition
    def write(self, values):
        if 'stage_id' in values.keys():
            if self.stage_id == 'completed':
                raise ValidationError(("After Completed  You can't move !"))
        return super(StudentRecord, self).write(values)

#   Model for Stages in Kanban View
class Stages(models.Model):
    _name = 'service.stages'
    _rec_name = 'name'
    name = fields.Char(string="Name")