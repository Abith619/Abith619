from odoo import models, fields, api

class SlideChannelInherit(models.Model):
    _inherit = 'slide.channel'

    moodle_course_id = fields.Integer(string='Moodle Course ID')
    application_product_id : fields.Many2one = fields.Many2one('product.product', string="Application Product", help="Product used for charging application fee")

class SlideChannelTagGroupInherit(models.Model):
    _inherit = 'slide.channel.tag.group'

    moodle_id = fields.Integer(string='Moodle Category ID')

class SlideChannelTagInherit(models.Model):
    _inherit = 'slide.channel.tag'

    price = fields.Monetary(string="Price", help="Price associated with this course tag", currency_field="currency_id", store=True)
    currency_id : fields.Many2one = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    product_id : fields.Many2one = fields.Many2one('product.template', string="Product", help="Product associated with this course tag")

    @api.depends('product_id')
    def _compute_price(self):
        for rec in self:
            rec.price = rec.product_id.product_variant_id.lst_price if rec.product_id else 0.0