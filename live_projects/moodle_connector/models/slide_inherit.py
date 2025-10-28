from odoo import models, fields, api

class SlideChannelInherit(models.Model):
    _inherit = 'slide.channel'

    moodle_course_id = fields.Integer(string='Moodle Course ID')

class SlideChannelTagGroupInherit(models.Model):
    _inherit = 'slide.channel.tag.group'

    moodle_id = fields.Integer(string='Moodle Category ID')
