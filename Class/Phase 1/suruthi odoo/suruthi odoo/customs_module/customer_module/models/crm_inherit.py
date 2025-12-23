from odoo import models, fields
from odoo.exceptions import UserError

class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    custom_field = fields.Char(string="Custom Field")

    def action_show_popup(self):
        raise UserError("Hello Suruthi! Button clicked successfully.")
