from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CreatePOWizard(models.TransientModel):
    _name = "create.po.wizard"
    _description = "Create Purchase Order from PR"

    request_id = fields.Many2one("purchase.request", required=True, readonly=True)
    vendor_id = fields.Many2one("res.partner", string="Vendor", required=True)
    line_ids = fields.One2many("create.po.wizard.line", "wizard_id", string="Products")

    def action_create_po(self):
        self.ensure_one()
        if not self.line_ids:
            raise ValidationError("You must include at least one product.")
        
        purchase_order = self.env["purchase.order"].create({
            "partner_id": self.vendor_id.id,
            "purchase_request_id": self.request_id.id,
            "mo_reference": self.request_id.mo_id.id if self.request_id.mo_id else False,
            "order_line": [(0, 0, {
                "product_id": line.product_id.id,
                "product_qty": line.quantity,
                "product_uom_id": line.uom_id.id or line.product_id.uom_id.id,
                "price_unit": line.purchase_price,
                "date_planned": self.request_id.expected_date,
                "manufacturer_ids": line.product_id.manufacturer_line_ids[0].manufacturer_id.id if line.product_id.manufacturer_line_ids else False,
                "manufacturer_part_number_ids": line.product_id.manufacturer_line_ids[0].id if line.product_id.manufacturer_line_ids else False,
            }) for line in self.line_ids],
        })
        
        # Opens the created PO in draft state (RFQ)
        return {
            "type": "ir.actions.act_window",
            "res_model": "purchase.order",
            "view_mode": "form",
            "res_id": purchase_order.id,
            "target": "current",
        }

class CreatePOWizardLine(models.TransientModel):
    _name = "create.po.wizard.line"
    _description = "Create PO Wizard Line"

    wizard_id = fields.Many2one("create.po.wizard", ondelete="cascade")
    product_id = fields.Many2one("product.product", required=True, readonly=True)
    quantity = fields.Float(required=True)
    uom_id = fields.Many2one("uom.uom", readonly=True)
    purchase_price = fields.Float(string="Purchase Price", compute="_compute_purchase_price", store=True, readonly=False)

    @api.depends("product_id", "wizard_id.vendor_id", "quantity")
    def _compute_purchase_price(self):
        for rec in self:
            rec.purchase_price = 0.0
            if rec.product_id and rec.wizard_id.vendor_id:
                seller = rec.product_id._select_seller(
                    partner_id=rec.wizard_id.vendor_id,
                    quantity=rec.quantity,
                    date=None,
                    uom_id=rec.uom_id,
                )
                if seller:
                    rec.purchase_price = seller.price
