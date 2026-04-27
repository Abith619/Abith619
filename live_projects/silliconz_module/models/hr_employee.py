from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    aadhaar_number = fields.Char(string="Aadhaar Number", groups="hr.group_hr_user", tracking=True)
    pan_number = fields.Char(string="PAN Number", groups="hr.group_hr_user", tracking=True)
    pf_number = fields.Char(string="PF Number", groups="hr.group_hr_user", tracking=True)
    esic_number = fields.Char(string="ESIC Number", groups="hr.group_hr_user", tracking=True)
    esi_insurance_number = fields.Char(string="ESI Insurance Number", groups="hr.group_hr_user", tracking=True)
