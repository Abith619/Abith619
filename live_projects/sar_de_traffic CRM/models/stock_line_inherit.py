from odoo import models, fields, _
from collections import defaultdict

_move_lot_counters : defaultdict = defaultdict(int)

class StockPickingInheritCustom(models.Model):
    _inherit= 'stock.move'

    area = fields.Float(string='Area')
    measure = fields.Selection([('m', 'Meter'), ('sqm', 'Sq Meter')], string='Measure', default='m')

    def _prepare_move_line_vals(self, quantity=None, reserved_quant=None):
        vals = super()._prepare_move_line_vals(quantity=quantity, reserved_quant=reserved_quant)

        line_qty = quantity or 1.0

        total_qty = self.product_uom_qty or 1.0
        total_area = self.area or 0.0

        proportional_area = (total_area * line_qty) / total_qty

        vals['area'] = proportional_area
        vals['measure'] = self.measure

        picking = self.picking_id
        origin = picking.origin or picking.name or 'AUTO'

        _move_lot_counters[self.id] += 1
        counter = _move_lot_counters[self.id]

        lot_number = f"{origin}-{counter}"
        vals['lot_name'] = lot_number

        return vals

class StockMoveLineInheritCustom(models.Model):
    _inherit = 'stock.move.line'

    area = fields.Float(string='Area')
    measure = fields.Selection([('m', 'Meter'), ('sqm', 'Sq Meter')], string='Measure', default='m')
