from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
class Hrloansalary(models.Model):
    _inherit = 'hr.loan.line'

    paid_due_amount = fields.Boolean("Paid Due Amont")


class Hrloan(models.Model):
    _inherit = 'hr.loan'

    Finished = fields.Boolean("Finished")
