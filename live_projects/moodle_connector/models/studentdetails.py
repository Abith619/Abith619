from odoo import models, fields,api


class StudentMaster(models.Model):
    _name = 'student.master'
    _description = 'Student Master'
    _order = 'sequence asc'

    sequence = fields.Char(
        string="Student ID",
        readonly=True,
        copy=False,
        default='New'
    )
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('sequence', 'New') == 'New':
                vals['sequence'] = (
                    self.env['ir.sequence'].next_by_code('student.master')
                    or 'New'
                )
        return super().create(vals_list)
    photo = fields.Binary(string="Photo")
    photo_filename = fields.Char()


    # ---------------- BASIC ----------------
    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()
    dob = fields.Date()
    gender = fields.Selection([
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ])

    country_of_residence = fields.Char()
    nationality = fields.Char()
    time_zone = fields.Char()

    # ---------------- GUARDIAN ----------------
    underage_consent = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ])

    guardian_name = fields.Char()
    guardian_relationship = fields.Char()
    guardian_phone = fields.Char()
    guardian_email = fields.Char()

    # ---------------- SPONSOR ----------------
    has_sponsor = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ])

    sponsor_name = fields.Char()
    sponsor_relationship = fields.Char()
    sponsor_phone = fields.Char()
    sponsor_email = fields.Char()

    # ---------------- ACADEMIC ----------------
    highest_qualification = fields.Selection([
        ('high_school', 'High School Diploma'),
        ('waec', 'WAEC / NECO'),
        ('alevels', 'A-Levels'),
        ('associate', 'Associate'),
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('other', 'Other')
    ])

    last_institution = fields.Char()
    graduation_year = fields.Char()
    gpa = fields.Char()

    prior_attendance = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ])

    prior_institution_name = fields.Char()
    prior_program = fields.Char()
    prior_dates = fields.Date()
    prior_credits = fields.Char()
    prior_reason = fields.Char()

    # ---------------- RELATIONS ----------------
    partner_id = fields.Many2one('res.partner')
    lead_id = fields.Many2one('crm.lead',string="Application")
    active = fields.Boolean(default=True)
    previous_lead_id = fields.Many2one('crm.lead',string="Previous Application")
    previous_courses = fields.Text(string="Previously Applied Courses")
    application_count = fields.Integer(
        string="Applications",
        compute="_compute_application_count"
    )
    @api.depends('lead_id', 'email')
    def _compute_application_count(self):
            Lead = self.env['crm.lead']
            for rec in self:
                if rec.email:
                    rec.application_count = Lead.search_count([
                        ('email_from', '=', rec.email)
                    ])
                else:
                    rec.application_count = 0

    def action_view_applications(self):
            self.ensure_one()

            return {
                'name': 'Applications',
                'type': 'ir.actions.act_window',
                'res_model': 'crm.lead',
                'view_mode': 'list,form',
                'domain': [('email_from', '=', self.email)],
                'context': {
                    'default_email_from': self.email,
                    'default_partner_id': self.partner_id.id,
                }
            }

    enrolled_course_count = fields.Integer(
        string="Enrolled Courses",
        compute="_compute_enrolled_courses"
    )

    @api.depends('email')
    def _compute_enrolled_courses(self):
        Partner = self.env['res.partner']
        Attendee = self.env['slide.channel.partner']

        for student in self:
            student.enrolled_course_count = 0

            if not student.email:
                continue

            partner = Partner.search(
                [('email', '=', student.email)],
                limit=1
            )
            if not partner:
                continue

            student.enrolled_course_count = Attendee.search_count([
                ('partner_id', '=', partner.id),
                ('active', '=', True),
            ])

    # ---------------- SMART BUTTON ----------------
    def action_open_enrolled_courses(self):
        self.ensure_one()

        Partner = self.env['res.partner']
        partner = Partner.search(
            [('email', '=', self.email)],
            limit=1
        )

        if not partner:
            return {'type': 'ir.actions.act_window_close'}

        return {
            'name': 'Enrolled Courses',
            'type': 'ir.actions.act_window',
            'res_model': 'slide.channel.partner',
            'view_mode': 'list,form',
            'domain': [
                ('partner_id', '=', partner.id),
                ('active', '=', True),
            ],
            'context': {'create': False},
        }

    # ---------------- FACULTY (ORM ONLY) ----------------
    faculty_ids = fields.Many2many(
        'faculty.master',
        compute='_compute_faculty_from_courses',
        string="Faculty",
        store=False
    )

    @api.depends('email')
    def _compute_faculty_from_courses(self):
        Partner = self.env['res.partner']
        Attendee = self.env['slide.channel.partner']
        Faculty = self.env['faculty.master']

        for student in self:
            student.faculty_ids = [(5, 0, 0)]

            if not student.email:
                continue

            partner = Partner.search(
                [('email', '=', student.email)],
                limit=1
            )
            if not partner:
                continue

            # Step 1: get enrolled course IDs
            attendee_records = Attendee.search([
                ('partner_id', '=', partner.id),
                ('active', '=', True),
            ])

            course_ids = attendee_records.read(['channel_id'])
            course_ids = [rec['channel_id'][0] for rec in course_ids if rec['channel_id']]

            if not course_ids:
                continue

            # Step 2: get faculty via M2M relation 
            faculties = Faculty.search([
                ('course_ids', 'in', course_ids)
            ])

            student.faculty_ids = [(6, 0, faculties.ids)]
