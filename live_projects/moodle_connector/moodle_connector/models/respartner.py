from odoo import models,fields,api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    dob = fields.Date(string="Date of Birth")
    gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Others')], string="Gender")
    institution_name = fields.Char(string="Institution Name")
    institution_address = fields.Char(string="Institution Address")
    qualification = fields.Char(string="Qualification")

