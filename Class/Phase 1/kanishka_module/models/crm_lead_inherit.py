from odoo import models, fields
from odoo.exceptions import ValidationError
class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    custom_field = fields.Char(
        string="Custom Field",
        help="This field is added from custom module"
    )
    def action_custom_module(self):
        raise ValidationError("This field is added from custom module in button")