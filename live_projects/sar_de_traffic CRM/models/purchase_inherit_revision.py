from odoo import models, fields

class PurchaseInheritRevision(models.Model):
    _inherit = "purchase.order"

    def revise_order(self):
        return {
            'type': "ir.actions.act_window",
            'name': 'Purchase Order Revision PopUp',
            'res_model': 'purchase.revision.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_order_ref_id': self.id}
        }

class PurchaseLineInherit(models.Model):
    _inherit='purchase.order.line'

    area = fields.Float(string='Area')
    measure = fields.Selection([('m', 'Meter'), ('sqm', 'Sq Meter')], string='Measure', default='m')

    def _prepare_stock_moves(self, picking):
        moves = super()._prepare_stock_moves(picking)
        for move in moves:
            move['area'] = self.area
            move['measure'] = self.measure
        return moves