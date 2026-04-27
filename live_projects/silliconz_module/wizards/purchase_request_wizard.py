from odoo import models, fields, api
class PurchaseRequestWizard(models.TransientModel):
    _name = "purchase.request.wizard"
    _description = "Purchase Request Wizard"

    # vendor_id removed
    material_request_id = fields.Many2one("material.request",string="Material Request reference",required=True)
    mo_id = fields.Many2one("mrp.production",string="Source MO",required=False)
    line_ids = fields.One2many("purchase.request.wizard.line","wizard_id",string="Lines")
    def action_create_purchase_request(self):
        purchase_request = self.env["purchase.request"].create({
            "material_request_id": self.material_request_id.id,
            "mo_id":self.mo_id.id,
            "expected_date": self.material_request_id.expected_date,
            "line_ids": [(0, 0, {
                "product_id": line.product_id.id,
                "quantity": line.purchase_qty,
                "uom_id": line.uom_id.id,
                "manufacturer_ids": line.product_id.manufacturer_line_ids[0].manufacturer_id.id if line.product_id.manufacturer_line_ids else False,
                "manufacturer_part_number_ids": line.product_id.manufacturer_line_ids[0].id if line.product_id.manufacturer_line_ids else False,
            }) for line in self.line_ids]
        })

        return {
            "type": "ir.actions.act_window",
            "res_model": "purchase.request",
            "view_mode": "form",
            "res_id": purchase_request.id,
            "target": "current",
        }


class PurchaseRequestWizardLine(models.TransientModel):
    _name = "purchase.request.wizard.line"
    _description = "Purchase Request Wizard Line"

    wizard_id = fields.Many2one("purchase.request.wizard", ondelete="cascade")

    product_id = fields.Many2one("product.product")

    requested_qty = fields.Float()

    available_qty = fields.Float()

    remaining_qty = fields.Float(compute="_compute_remaining_qty",store=True)

    purchase_qty = fields.Float(string="Purchase Qty")

    uom_id = fields.Many2one("uom.uom")

    @api.depends("requested_qty", "available_qty")
    def _compute_remaining_qty(self):
        for rec in self:
            if rec.requested_qty>=rec.available_qty:
                rec.remaining_qty = 0.0
                rec.purchase_qty = rec.requested_qty - rec.available_qty
            elif rec.requested_qty==rec.available_qty:
                    rec.remaining_qty = 0.0
                    rec.purchase_qty = 0.0
            else:
                rec.remaining_qty= rec.available_qty - rec.requested_qty
                rec.purchase_qty = 0.0

