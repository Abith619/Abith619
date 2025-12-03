from odoo import models, fields
from odoo.exceptions import ValidationError

class CrmLeadInherit(models.Model):
    _inherit='crm.lead'

    custom_field = fields.Char(string='Custom Field', help='A custom field added to CRM Lead')

    def action_custom_method(self):
        raise ValidationError("Good Evening")