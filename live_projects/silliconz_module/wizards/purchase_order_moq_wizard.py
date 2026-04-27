from odoo import models, fields, api
from odoo.exceptions import UserError


class PoMoqConflictWizard(models.TransientModel):
    _name = 'po.moq.conflict.wizard'
    _description = 'MOQ Conflict Wizard'

    po_id = fields.Many2one('purchase.order', required=True)

    message = fields.Text(
        string="Conflict Details",
        compute="_compute_message",
        readonly=True
    )

    @api.depends('po_id')
    def _compute_message(self):
        for wizard in self:
            if not wizard.po_id:
                wizard.message = ""
                continue

            lines = wizard.po_id.order_line.filtered(
                lambda l: l.product_id and l.product_qty < l.vendor_min_qty
            )

            if not lines:
                wizard.message = "No conflicts found."
                continue

            msg_parts = []
            for l in lines:
                msg_parts.append(
                    f"Product: {l.product_id.display_name}\n"
                    f"Ordered Qty: {l.product_qty} {l.product_id.uom_name}\n"
                    f"Vendor MOQ: {l.vendor_min_qty}\n"
                    f"-------------------------"
                )
            wizard.message = "\n".join(msg_parts)

    def action_update_pr_qty(self):
        """Update the PO line quantities to meet vendor MOQ, then confirm."""
        self.ensure_one()
        if not self.po_id.purchase_request_id:
            raise UserError("Purchase Request not found for this Order.")
        conflict_lines = self.po_id.order_line.filtered(
            lambda l: l.product_id and l.product_qty < l.vendor_min_qty
        )
        for line in conflict_lines:
            line.product_qty = line.vendor_min_qty

        # Also sync back to linked purchase request lines if any
        if self.po_id.purchase_request_id:
            for line in conflict_lines:
                pr_lines = self.po_id.purchase_request_id.line_ids.filtered(
                    lambda pl: pl.product_id == line.product_id
                )
                for pr_line in pr_lines:
                    pr_line.product_qty = line.product_qty

        return self.po_id.with_context(skip_moq_validation=True).button_confirm()

    def action_update_vendor_qty(self):
        """
        Update the vendor pricelist MOQ to match current PO qty,
        then confirm without re-raising the wizard.
        """
        self.ensure_one()
        conflict_lines = self.po_id.order_line.filtered(
            lambda l: l.product_id and l.product_qty < l.vendor_min_qty
        )
        for line in conflict_lines:
            line.product_qty = line.vendor_min_qty

        return self.po_id.with_context(skip_moq_validation=True).button_confirm()

    def action_cancel(self):
        return {'type': 'ir.actions.act_window_close'}