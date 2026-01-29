from odoo import models, fields

class CourseGrade(models.Model):
    _name = 'course.grade'
    _description = 'Course Grade Master'
    _order = 'min_percentage desc'

    name = fields.Char(string='Grade', required=True)   # A, B, C, F
    min_percentage = fields.Float(string='Min Percentage', required=True)
    max_percentage = fields.Float(string='Max Percentage', required=True)

    active = fields.Boolean(default=True)

    _sql_constraints = [
        (
            'percentage_range_check',
            'CHECK(min_percentage <= max_percentage)',
            'Min percentage must be less than or equal to Max percentage'
        )
    ]
