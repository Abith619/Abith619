from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BoothWebsite(models.Model):
    _inherit = 'event.booth.category'

    quantity_details = fields.Html(string='Quantity Details')