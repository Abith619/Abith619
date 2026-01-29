from odoo import models, fields, api


class FacultyMaster(models.Model):
    _name = 'faculty.master'
    _description = 'Faculty / Teacher'
    _rec_name = 'name'

    # BASIC INFO
    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()
    department = fields.Char()
    qualification = fields.Char()
    active = fields.Boolean(default=True)

    # MANY FACULTY ↔ MANY COURSES
    course_ids = fields.Many2many(
        'slide.channel',
        'faculty_course_rel',   # relation table
        'faculty_id',
        'channel_id',
        string="Courses"
    )

    # SMART BUTTON COUNTS
    course_count = fields.Integer(
        compute="_compute_course_count",
        string="Courses Count"
    )

    student_count = fields.Integer(
        compute="_compute_student_count",
        string="Students"
    )


    @api.depends('course_ids')
    def _compute_course_count(self):
        for faculty in self:
            faculty.course_count = len(faculty.course_ids)


    @api.depends('course_ids')
    def _compute_student_count(self):
        Attendee = self.env['slide.channel.partner']
        for faculty in self:
            faculty.student_count = Attendee.search_count([
                ('channel_id', 'in', faculty.course_ids.ids),
            ])

    # SMART BUTTON ACTIONS
    def action_view_courses(self):
        self.ensure_one()
        return {
            'name': 'Courses',
            'type': 'ir.actions.act_window',
            'res_model': 'slide.channel',
            'view_mode': 'kanban,list,form',
            'domain': [('id', 'in', self.course_ids.ids)],
            'context': {'create': False},
        }

    def action_view_students(self):
        self.ensure_one()
        return {
            'name': 'Students',
            'type': 'ir.actions.act_window',
            'res_model': 'slide.channel.partner',
            'view_mode': 'list,form',
            'domain': [
                ('channel_id', 'in', self.course_ids.ids),
            ],
            'context': {'create': False},
        }
