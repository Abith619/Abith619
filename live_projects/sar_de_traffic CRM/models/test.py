from odoo import models, fields, _, api
from odoo.exceptions import UserError

class MrpProduction(models.Model):
    _inherit = "mrp.production"

    area = fields.Float(string='Area', help="Area in square meters")
    measure = fields.Selection([('m', 'Meter'), ('sqm', 'Sq Meter')], string='Measure')

    @api.onchange('product_qty')
    def _onchange_product_qty(self):
        for production in self:
            for bom_line in production.bom_id.bom_line_ids:
                if bom_line.area_bool:

                    total_required_area = production.product_qty * bom_line.area

                    quants = self.env['stock.quant'].sudo().search([
                        ('product_id', '=', bom_line.product_id.id),
                        ('quantity', '>', 0),
                        ('location_id.usage', '=', 'internal'),
                        ('area', '>', 0),
                    ], order="id")

                    area_needed = total_required_area
                    quant_line_count = 0

                    for quant in quants:
                        if area_needed <= 0:
                            break

                        quant_area = quant.area or 0.0

                        if quant_area > 0:
                            quant_line_count += 1
                            area_needed -= quant_area

                    raw_move = production.move_raw_ids.filtered(lambda m: m.product_id == bom_line.product_id)
                    if raw_move:
                        raw_move.area = total_required_area
                        raw_move.product_uom_qty = quant_line_count
