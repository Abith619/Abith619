from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StockLocation(models.Model):
    _inherit = "stock.location"

    is_material_source = fields.Boolean(string="Material Source Location")

    @api.constrains("is_material_source")
    def _check_only_one_source(self):
        for rec in self:
            if rec.is_material_source:
                other = self.search([
                    ("id", "!=", rec.id),
                    ("is_material_source", "=", True)
                ], limit=1)

                if other:
                    raise ValidationError(
                        "Only one location can be set as Material Source Location."
                    )