from odoo import models, fields

class StockQuantityInherit(models.Model):
    _inherit = 'stock.quant'

    area = fields.Float(string='Area', help="Area in square meters")
    measure = fields.Selection([('m', 'Meter'), ('sqm', 'Sq Meter')], string='Measure',
                               help="Unit of measurement for the area")

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        res = super(StockPicking, self).button_validate()

        for picking in self:
            for move_line in picking.move_line_ids_without_package:
                product = move_line.product_id
                lot = move_line.lot_id
                area = move_line.area or 1.0
                measure = move_line.measure or 1.0

                domain = [
                    ('product_id', '=', product.id),
                    ('location_id.usage', '=', 'internal'),
                ]

                if lot:
                    domain.append(('lot_id', '=', lot.id))

                quants = self.env['stock.quant'].sudo().search(domain)

                for quant in quants:
                    quant.area = area
                    quant.measure = measure

        return res
