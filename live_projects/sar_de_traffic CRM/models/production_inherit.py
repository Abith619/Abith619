from odoo import models, fields, _, api
from odoo.exceptions import UserError

class MrpProduction(models.Model):
    _inherit = "mrp.production"

    area = fields.Float(string='Area', help="Area in square meters")
    measure = fields.Selection([('m', 'Meter'), ('sqm', 'Sq Meter')], string='Measure')

    @api.onchange('product_qty')
    def _onchange_product_qty(self):
        for production in self:
            if production.bom_id.area_bool:
                for bom_line in production.bom_id.bom_line_ids:
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
        # self.pre_button_mark_done()

    @api.onchange('bom_id')
    def compute_area(self):
        for production in self:
            if production.bom_id.area_bool:
                for bom_line in production.bom_id.bom_line_ids:
                    raw_moves = production.move_raw_ids.filtered(lambda m: m.product_id == bom_line.product_id)
                    for move in raw_moves:
                        move.area = bom_line.area
                        move.measure = bom_line.measure

            elif any(b.area_bool for b in production.bom_id.bom_line_ids):
                for bom_line in production.bom_id.bom_line_ids.filtered(lambda l: l.area_bool):
                    raw_moves = production.move_raw_ids.filtered(lambda m: m.product_id == bom_line.product_id)
                    for move in raw_moves:
                        move.area = bom_line.area
                        move.measure = bom_line.measure

    def _prepare_stock_lot_values(self):
        self.ensure_one()

        product = self.product_id
        category = product.categ_id
        cat_code = category.name[:3].upper() if category else 'XXX'

        sequence_code = f'sar.{cat_code.lower()}'

        sequence = self.env['ir.sequence'].sudo().search([('code', '=', sequence_code)], limit=1)
        if not sequence:
            sequence = self.env['ir.sequence'].sudo().create({
                'name': f'SAR Sequence for {cat_code}',
                'code': sequence_code,
                'prefix': f'SAR{cat_code}',
                'padding': 5,
                'number_next': 1,
                'number_increment': 1,
            })

        name = self.env['ir.sequence'].next_by_code(sequence_code)

        exist_lot = not name or self.env['stock.lot'].search([
            ('product_id', '=', self.product_id.id),
            '|', ('company_id', '=', False), ('company_id', '=', self.company_id.id),
            ('name', '=', name),
        ], limit=1)
        if exist_lot:
            name = self.env['stock.lot']._get_next_serial(self.company_id, self.product_id)
        if not name:
            raise UserError(_("Please set the first Serial Number or a default sequence"))
        return {
            'product_id': self.product_id.id,
            'name': name,
        }

    def action_confirm(self):
        res = super(MrpProduction, self).action_confirm()

        for mo in self:
            for move in mo.move_raw_ids:
                product = move.product_id
                required_area = move.area or 0.0

                if required_area <= 0.0:
                    continue

                quants = self.env['stock.quant'].sudo().search([
                    ('product_id', '=', product.id),
                    ('quantity', '>', 0),
                    ('location_id.usage', '=', 'internal'),
                    ('area', '>', 0),
                ], order="id")

                for quant in quants:
                    if required_area <= 0.0:
                        break

                    available_area = quant.area or 0.0

                    if available_area <= 0.0:
                        continue

                    if available_area >= required_area:
                        quant.sudo().write({'area': available_area - required_area})
                        required_area = 0.0
                    else:
                        quant.sudo().write({'area': 0.0})
                        required_area -= available_area
            for move in mo.move_raw_ids:
                if move.move_line_ids:
                    move.move_line_ids.unlink()
                move._action_assign()

                lot_id = None
                if move.has_tracking != 'none':
                    lot = self.env['stock.quant'].sudo().search([
                        ('product_id', '=', move.product_id.id),
                        ('quantity', '>', 0),
                        ('location_id.usage', '=', 'internal'),
                        ('lot_id', '!=', False),
                    ], limit=1)
                    lot_id = lot.lot_id.id if lot else False
                move_line_vals = {
                    'move_id': move.id,
                    'product_id': move.product_id.id,
                    'product_uom_id': move.product_uom.id,
                    'location_id': move.location_id.id,
                    'location_dest_id': move.location_dest_id.id,
                    'quantity': move.product_uom_qty,
                    'lot_id': lot_id,
                }
                self.env['stock.move.line'].sudo().create(move_line_vals)
        return res

