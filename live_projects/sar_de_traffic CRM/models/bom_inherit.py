from odoo import models, fields

class BomInheritCustom(models.Model):
    _inherit = 'mrp.bom'

    area = fields.Float(string='Area', help="Area in square meters")
    measure = fields.Selection([('m', 'Meter'), ('sqm', 'Sq Meter')], string='Measure', default='sqm',
                               help="Unit of measurement for the area")

    area_bool = fields.Boolean(string="Calculate by Area")

class BomLineInheritCustom(models.Model):
    _inherit = 'mrp.bom.line'

    area = fields.Float(string='Area', help="Area in square meters")
    measure = fields.Selection([('m', 'Meter'), ('sqm', 'Sq Meter')], string='Measure', default='sqm',
                               help="Unit of measurement for the area")
    area_bool = fields.Boolean(string='Area Required', help="Check if area is required for this production order")

