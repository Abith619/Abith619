from odoo import models, fields, api
from odoo.exceptions import ValidationError

# =========================================================
# SLIDE SLIDE PARTNER
# =========================================================
class SlideSlidePartner(models.Model):
    _inherit = 'slide.slide.partner'

    # ---------------- COURSE LINK ----------------
    channel_partner_id = fields.Many2one(
        'slide.channel.partner',
        string='Course Enrollment',
        index=True,
        ondelete='cascade'
    )

    # ---------------- TYPE FLAGS ----------------
    is_lesson = fields.Boolean(related='slide_id.is_lesson', store=True)
    is_assignment = fields.Boolean(related='slide_id.is_assignment', store=True)
    is_quiz = fields.Boolean(related='slide_id.is_quiz', store=True)

    # ---------------- SECTION ----------------
    section_id = fields.Many2one(
        'slide.slide',
        related='slide_id.category_id',
        store=True
    )

    # ---------------- LESSON ----------------
    lesson_marks = fields.Integer(
        related='slide_id.lesson_marks',
        store=True
    )
    is_lesson_custom_marks = fields.Boolean(
        string='Use Custom Marks'
    )

    lesson_custom_marks = fields.Integer(
        string='Custom Lesson Marks',
        default=0
    )

    @api.constrains('lesson_custom_marks')
    def _check_lesson_custom_marks(self):
        for rec in self:
            if rec.lesson_custom_marks < 0:
                raise ValidationError("Lesson marks cannot be negative")

    # ---------------- ASSIGNMENT ----------------
    assignment_attachment_ids = fields.Many2many(
        'ir.attachment',
        'slide_slide_partner_assignment_rel',
        'slide_partner_id',
        'attachment_id',
        string='Assignment Upload'
    )

    assignment_marks = fields.Integer(default=0)

    assignment_total_marks = fields.Integer(
        related='slide_id.assignment_total_marks',
        store=True
    )

    # ---------------- QUIZ ----------------
    quiz_xp = fields.Integer(default=0)

    quiz_out_of_marks = fields.Integer(
        related='slide_id.quiz_first_attempt_reward',
        store=True
    )

    

    # ---------------- AUTO COURSE LINK ----------------
    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)

        for record in records:
            if not record.channel_partner_id and record.channel_id and record.partner_id:
                channel_partner = self.env['slide.channel.partner'].search([
                    ('channel_id', '=', record.channel_id.id),
                    ('partner_id', '=', record.partner_id.id),
                ], limit=1)

                if channel_partner:
                    record.channel_partner_id = channel_partner.id

        return records



# =========================================================
# SLIDE CHANNEL PARTNER
# =========================================================
class SlideChannelPartner(models.Model):
    _inherit = 'slide.channel.partner'

    # ---------------- LINES ----------------
    lesson_line_ids = fields.One2many(
        'slide.slide.partner',
        'channel_partner_id',
        domain=[('is_lesson', '=', True)]
    )

    assignment_line_ids = fields.One2many(
        'slide.slide.partner',
        'channel_partner_id',
        domain=[('is_assignment', '=', True)]
    )

    quiz_line_ids = fields.One2many(
        'slide.slide.partner',
        'channel_partner_id',
        domain=[('is_quiz', '=', True)]
    )
    show_results_on_website = fields.Boolean(
        string="Show Results on Website",
        default=False
    )

    # ---------------- TOTALS ----------------
    total_lesson_marks = fields.Integer(compute='_compute_totals', store=True, compute_sudo=True)
    total_assignment_marks = fields.Integer(compute='_compute_totals', store=True)
    total_assignment_out_of = fields.Integer(compute='_compute_totals', store=True)
    total_quiz_xp = fields.Integer(compute='_compute_totals', store=True)
    total_quiz_out_of = fields.Integer(compute='_compute_totals', store=True)
    user_total_marks = fields.Integer(compute='_compute_totals', store=True)
    overall_total_marks = fields.Integer(compute='_compute_totals', store=True)

    overall_percentage = fields.Float(
        compute='_compute_percentage',
        store=False
    )

    grade_id = fields.Many2one(
        'course.grade',
        string='Overall Grade',
        store=True
    )

    # ---------------- COMPUTE LOGIC ----------------
    @api.depends(
        'lesson_line_ids.lesson_marks',
        'lesson_line_ids.lesson_custom_marks',
        'lesson_line_ids.is_lesson_custom_marks',
        'assignment_line_ids.assignment_marks',
        'assignment_line_ids.assignment_total_marks',
        'quiz_line_ids.quiz_xp',
        'quiz_line_ids.quiz_out_of_marks',
        'quiz_line_ids.completed'
    )
    def _compute_totals(self):
        Grade = self.env['course.grade']

        for rec in self:
            lesson_total = sum(
                line.lesson_custom_marks if line.is_lesson_custom_marks else line.lesson_marks
                for line in rec.lesson_line_ids
            )

            assignment_user = sum(rec.assignment_line_ids.mapped('assignment_marks'))
            assignment_out_of = sum(rec.assignment_line_ids.mapped('assignment_total_marks'))

            quizzes = rec.quiz_line_ids.filtered('completed')
            quiz_user = sum(quizzes.mapped('quiz_xp'))
            quiz_out_of = sum(quizzes.mapped('quiz_out_of_marks'))

            rec.total_lesson_marks = lesson_total
            rec.total_assignment_marks = assignment_user
            rec.total_assignment_out_of = assignment_out_of
            rec.total_quiz_xp = quiz_user
            rec.total_quiz_out_of = quiz_out_of

            rec.user_total_marks = lesson_total + assignment_user + quiz_user
            rec.overall_total_marks = lesson_total + assignment_out_of + quiz_out_of
            percentage = (
                (rec.user_total_marks / rec.overall_total_marks) * 100
                if rec.overall_total_marks else 0.0
            )

            grade = Grade.search([
                ('min_percentage', '<=', percentage),
                ('max_percentage', '>=', percentage),
                ('active', '=', True)
            ], limit=1)

            rec.grade_id = grade.id if grade else False

    @api.depends('user_total_marks', 'overall_total_marks')
    def _compute_percentage(self):
        for rec in self:
            rec.overall_percentage = (
                (rec.user_total_marks / rec.overall_total_marks) * 100
                if rec.overall_total_marks else 0.0
            )

