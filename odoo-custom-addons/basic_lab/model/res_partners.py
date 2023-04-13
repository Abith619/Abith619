from odoo import api, fields, models, _

class ResPartnerLabInherit(models.Model):
    _inherit = 'res.partner'

    height = fields.Char(string='Height')
    weight = fields.Char(string='Weight')
    blood_type = fields.Selection([('A', 'A'),('B', 'B'),('AB', 'AB'),('O', 'O')], string ="Blood Type")
    rh = fields.Selection([('-+', '+'),('--', '-')], string ="Rh")
    