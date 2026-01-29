from odoo import models, fields


class SlideChannel(models.Model):
    _inherit = 'slide.channel'

    # -----------------------------------
    # Website progress
    # -----------------------------------
    website_show_results = fields.Boolean(
        compute='_compute_website_progress'
    )
    website_completed_slides = fields.Integer(compute='_compute_website_progress')
    website_total_slides = fields.Integer(compute='_compute_website_progress')
    website_course_xp = fields.Integer(compute='_compute_website_progress')

    # -----------------------------------
    # Website results
    # -----------------------------------
    website_quiz_marks = fields.Integer(compute='_compute_website_progress')
    website_quiz_out_of = fields.Integer(compute='_compute_website_progress')
    website_total_lesson_marks=fields.Integer(compute='_compute_website_progress')

    website_assignment_marks = fields.Integer(compute='_compute_website_progress')

    website_user_total_marks = fields.Integer(compute='_compute_website_progress')
    website_overall_total_marks = fields.Integer(compute='_compute_website_progress')
    website_overall_percentage = fields.Float(compute='_compute_website_progress')

    # ✅ NEW – GRADE FROM MASTER
    website_grade_id = fields.Many2one(
        'course.grade',
        compute='_compute_website_progress',
        string="Grade"
    )

    # Optional: easy display for QWeb
    website_grade_name = fields.Char(
        compute='_compute_website_progress',
        string="Grade Value"
    )

    faculty_ids = fields.Many2many(
        'faculty.master',
        'faculty_course_rel',
        'channel_id',
        'faculty_id',
        string="Faculty"
    )

    # -----------------------------------
    # MAIN WEBSITE COMPUTE
    # -----------------------------------
    def _compute_website_progress(self):
        SlidePartner = self.env['slide.slide.partner'].sudo()
        Slide = self.env['slide.slide'].sudo()
        ChannelPartner = self.env['slide.channel.partner'].sudo()

        partner = self.env.user.partner_id

        for channel in self:
            # ---------- DEFAULTS ----------

            channel.website_completed_slides = 0
            channel.website_total_slides = 0
            channel.website_course_xp = 0
            channel.website_total_lesson_marks=0

            channel.website_quiz_marks = 0
            channel.website_quiz_out_of = 0
            channel.website_assignment_marks = 0

            channel.website_user_total_marks = 0
            channel.website_overall_total_marks = 0
            channel.website_overall_percentage = 0.0

            channel.website_grade_id = False
            channel.website_grade_name = False
            channel.website_show_results = False


            if not partner:
                continue

            # ---------- LESSON PROGRESS ----------
            completed = SlidePartner.search_count([
                ('channel_id', '=', channel.id),
                ('partner_id', '=', partner.id),
                ('completed', '=', True),
                ('slide_id.is_category', '=', False),
            ])

            total = Slide.search_count([
                ('channel_id', '=', channel.id),
                ('is_category', '=', False),
            ])

            channel.website_completed_slides = completed
            channel.website_total_slides = total
            channel.website_course_xp = completed * 10

            # ---------- COURSE ENROLLMENT ----------
            channel_partner = ChannelPartner.search([
                ('channel_id', '=', channel.id),
                ('partner_id', '=', partner.id),
            ], limit=1)

            if not channel_partner:
                continue

            # ---------- TOTALS (FROM BACKEND LOGIC) ----------
            channel.website_total_lesson_marks = channel_partner.total_lesson_marks
            channel.website_show_results = channel_partner.show_results_on_website


            channel.website_quiz_marks = channel_partner.total_quiz_xp
            channel.website_quiz_out_of = channel_partner.total_quiz_out_of
            channel.website_total_lesson_marks = channel_partner.total_lesson_marks

            channel.website_user_total_marks = channel_partner.user_total_marks
            channel.website_overall_total_marks = channel_partner.overall_total_marks
            channel.website_overall_percentage = channel_partner.overall_percentage

            # ✅ GRADE (MASTER)
            channel.website_grade_id = channel_partner.grade_id
            channel.website_grade_name = channel_partner.grade_id.name if channel_partner.grade_id else False

            # ---------- ASSIGNMENTS ----------
            assignment_lines = SlidePartner.search([
                ('channel_id', '=', channel.id),
                ('partner_id', '=', partner.id),
                ('slide_id.is_assignment', '=', True),
            ])

            channel.website_assignment_marks = sum(
                assignment_lines.mapped('assignment_marks')
            )
