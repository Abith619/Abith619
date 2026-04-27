from odoo import models, fields, api
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    terms_id = fields.Many2one(
        'terms.and.condition',
        string="Terms & Conditions",
        domain="[('type', 'in', ['invoice', 'general']), ('active','=',True)]"
    )   

    @api.onchange('terms_id')
    def _onchange_terms_id(self):
        for rec in self:
            if rec.terms_id and rec.terms_id.content:
                if rec.narration:
                    rec.narration = rec.narration + "<br><br>" + rec.terms_id.content
                else:
                    rec.narration = rec.terms_id.content

    def action_post(self):
        for move in self:
            if move.move_type != 'in_invoice':
                continue

            mismatches = []

            for line in move.invoice_line_ids:
                po_line = line.purchase_line_id

                if not po_line:
                    continue

                if not po_line.product_qty or po_line.product_qty == 0:
                    raise UserError("Quantity is not set for the purchase order line")

                # Compare fields
                if line.product_id != po_line.product_id:
                    mismatches.append(f"{line.product_id.display_name} → Product mismatch")

                if line.quantity != po_line.product_qty:
                    mismatches.append(f"{line.product_id.display_name} → Qty mismatch")

                if line.price_unit != po_line.price_unit:
                    mismatches.append(f"{line.product_id.display_name} → Price mismatch")

                if line.product_uom_id != po_line.product_id.product_tmpl_id.uom_id:
                    mismatches.append(f"{line.product_id.display_name} → UoM mismatch")

                if set(line.tax_ids.ids) != set(po_line.tax_ids.ids):
                    mismatches.append(f"{line.product_id.display_name} → Tax mismatch")

            if mismatches and not self.env.context.get('skip_bill_validation'):
                return {
                    'type': 'ir.actions.act_window',
                    'name': 'Bill Validation',
                    'res_model': 'bill.validation.wizard',
                    'view_mode': 'form',
                    'target': 'new',
                    'context': {
                        'default_move_id': move.id,
                        'default_message': "\n".join(mismatches)
                    }
                }

        return super().action_post()
