from odoo import models, fields
from odoo.exceptions import ValidationError

class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    custom_field = fields.Char(string='Custom Field')
    another_field = fields.Char(string='Another Field')

    def action_custom_method(self):
        raise ValidationError("Good Evening From Custom Button!")
