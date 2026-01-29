from odoo import models, fields, api
import logging
from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)
class SlideChannelInherit(models.Model):
    _inherit = 'slide.channel'

    application_product_id = fields.Many2one(
        'product.product',
        string="Application Product"
    )
    moodle_course_id = fields.Integer(string='Moodle Course ID')
    application_product_id : fields.Many2one = fields.Many2one('product.product', string="Application Product", help="Product used for charging application fee")
    course_description = fields.Html(string="Course Description",sanitize=True,translate=False)
    is_assignment = fields.Boolean(string="Is Assignment")
    is_lesson = fields.Boolean(
        string='Is Lesson'
    )

    lesson_marks = fields.Integer(
        string='Lesson Marks',
        default=0
    )
    assignment_total_marks=fields.Integer(string='Assignment Marks', default=0)



    show_register = fields.Boolean(compute="_compute_access")
    show_add_to_cart = fields.Boolean(compute="_compute_access")
    show_register_again = fields.Boolean(compute="_compute_access")


    @api.depends_context('uid')
    def _compute_access(self):
        SaleOrderLine = self.env['sale.order.line']
        Lead = self.env['crm.lead']
        Stage = self.env['crm.stage']
        approved_stage = Stage.sudo().search([('name', 'in', ['Approved', 'Won'])])
        user = self.env.user
        for channel in self:
            channel.show_register = False
            channel.show_add_to_cart = False
            channel.show_register_again = False
            if user._is_public():
                channel.show_register = True
                _logger.info(  "[ACCESS] PUBLIC USER → Register | Course=%s",channel.name)
                continue
            partner = user.partner_id
            email = partner.email
            if not email or not channel.application_product_id:
                channel.show_register = True
                _logger.info(  "[ACCESS] Missing email/app product → Register | Course=%s",channel.name)
                continue
            paid_application = SaleOrderLine.search([
                ('order_id.partner_id', '=', partner.id),
                ('product_id', '=', channel.application_product_id.id),
                ('order_id.state', 'in', ['sale', 'done']),
            ], limit=1)
            latest_lead = Lead.sudo().search(
                [('email_from', '=', email)],
                order='create_date desc',
                limit=1
            )
            latest_stage = latest_lead.stage_id.name if latest_lead else 'NO LEAD'
            _logger.info("[ACCESS CHECK] Email=%s | Course=%s | Product=%s | Paid=%s | LatestStage=%s",
                email,channel.name,channel.application_product_id.name,  bool(paid_application),latest_stage)
            if not latest_lead and not paid_application:
                channel.show_register = True
                _logger.info("[RESULT] FIRST TIME → Register | Course=%s",channel.name)
                continue
            if latest_lead and not paid_application:
                channel.show_register_again = True
                _logger.info("[RESULT] REGISTER AGAIN → Course=%s",channel.name)
                continue
            if paid_application and latest_lead.stage_id.id not in approved_stage.ids:
                _logger.info("[RESULT] PAID BUT STAGE=%s → NO BUTTON | Course=%s",latest_stage,channel.name)
                continue
            if paid_application and latest_lead.stage_id.id in approved_stage.ids:
                channel.show_add_to_cart = True
                _logger.info("[RESULT] ADD TO CART → Course=%s",channel.name)
                continue
            channel.show_register = True
        

class SlideInherit(models.Model):
    _inherit = 'slide.slide'

    course_description = fields.Html(
        string="Course Description",
        sanitize=True,
        translate=False
    )


    is_lesson = fields.Boolean(string='Is Lesson')
    is_assignment = fields.Boolean(string='Is Assignment')

    is_quiz = fields.Boolean(
        string='Is Quiz',
        compute='_compute_is_quiz',
        store=True
    )

    lesson_marks = fields.Integer(string='Lesson Marks', default=0)
    assignment_total_marks=fields.Integer(string='Assignment total Marks', default=0)

    @api.depends('is_lesson', 'is_assignment')
    def _compute_is_quiz(self):
        for rec in self:
            rec.is_quiz = not rec.is_lesson and not rec.is_assignment

    @api.constrains('is_lesson', 'is_assignment')
    def _check_slide_type(self):
        for rec in self:
            if rec.is_lesson and rec.is_assignment:
                raise ValidationError(
                    "A slide can be Lesson OR Assignment OR Quiz, not multiple."
                )

class SlideChannelTagGroupInherit(models.Model):
    _inherit = 'slide.channel.tag.group'
    moodle_id = fields.Integer(string='Moodle Category ID')

class SlideChannelTagInherit(models.Model):
    _inherit = 'slide.channel.tag'
    moodle_id = fields.Integer(string="Moodle ID")

    price = fields.Monetary(string="Price", help="Price associated with this course tag", currency_field="currency_id", store=True)
    currency_id : fields.Many2one = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    product_id : fields.Many2one = fields.Many2one('product.template', string="Product", help="Product associated with this course tag")

    @api.depends('product_id')
    def _compute_price(self):
        for rec in self:
            rec.price = rec.product_id.product_variant_id.lst_price if rec.product_id else 0.0