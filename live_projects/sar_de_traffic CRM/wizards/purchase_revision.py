import re
from odoo import models, fields

class PurchaseRevisionWizard(models.TransientModel):
    _name = 'purchase.revision.wizard'

    order_ref_id : fields.Many2one = fields.Many2one('purchase.order', string='Order Refrence', readonly=True)
    rev_reason = fields.Text(string="Revision Reason", required=True)

    def purchase_revision(self):
        self.order_ref_id.state = 'cancel'
        current_serial = str(self.order_ref_id.name)

        self.order_ref_id.message_post(
            body=f"Amendment Reason: {self.rev_reason}.",
            message_type='comment',
            subtype_xmlid='mail.mt_note',
        )

        match = re.search(r'(R\d+)$', current_serial)
        if match:
            current_revision = int(match.group(1)[1:])
            new_revision = current_revision + 1
            base_name = current_serial[:match.start()]
        else:
            base_name = current_serial
            new_revision = 1

        new_name = f"{base_name}R{new_revision}"

        new_order_lines = []
        for line in self.order_ref_id.order_line:
            new_order_lines.append((0, 0, {
                'product_id': line.product_id.id,
                'name': line.name,
                'product_qty': line.product_qty,
                'price_unit': line.price_unit,
                'date_planned': line.date_planned,
                'product_uom': line.product_uom.id,
                'taxes_id': [(6, 0, line.taxes_id.ids)],
            }))

        new_po = self.env['purchase.order'].create({
            'name': new_name,
            'partner_id': self.order_ref_id.partner_id.id,
            'picking_type_id': self.order_ref_id.picking_type_id.id,
            'user_id': self.order_ref_id.user_id.id,
            'company_id': self.order_ref_id.company_id.id,
            'order_line': new_order_lines,
        })
        self.order_ref_id.button_cancel()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order',
            'res_id': new_po.id,
            'view_mode': 'form',
            'target': 'current',
        }
