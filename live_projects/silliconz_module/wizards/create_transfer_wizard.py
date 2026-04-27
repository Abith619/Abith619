from odoo import models, fields, api
from odoo.exceptions import ValidationError
from collections import defaultdict


class CreateTransferWizard(models.TransientModel):
    _name = "create.transfer.wizard"
    _description = "Create Transfer Wizard"

    material_request_id = fields.Many2one(
        "material.request", required=True, readonly=True
    )

    source_location_id = fields.Many2one(
        "stock.location", required=True
    )


    line_ids = fields.One2many(

        "create.transfer.wizard.line", "wizard_id"
    )

    # ---------------------------------------------------
    # ✅ MAIN ACTION
    # ---------------------------------------------------
    def action_confirm_transfer(self):
        self.ensure_one()
        request = self.material_request_id

        if not self.line_ids:
            raise ValidationError("No lines to transfer.")

        # ✅ INTERNAL PICKING TYPE
        picking_type = self.env["stock.picking.type"].search([
            ("code", "=", "internal"),
            ("warehouse_id.company_id", "=", self.env.company.id)
        ], limit=1)

        if not picking_type:
            raise ValidationError("Internal picking type not found.")

        grouped_lines = defaultdict(list)

        # ✅ GROUP BY DESTINATION
        for line in self.line_ids:
            if line.approved_qty > 0:
                grouped_lines[line.destination_location_id].append(line)

        if not grouped_lines:
            raise ValidationError("No approved quantities to transfer.")

        created_pickings = self.env["stock.picking"]

        # ---------------------------------------------------
        # ✅ CREATE PICKINGS
        # ---------------------------------------------------
        for dest_location, lines in grouped_lines.items():

            picking = self.env["stock.picking"].create({
                "partner_id": self.env.user.partner_id.id,
                "picking_type_id": picking_type.id,
                "location_id": self.source_location_id.id,
                "location_dest_id": dest_location.id,
                "origin": request.name,
                "material_request_id": request.id,
            })

            created_pickings |= picking

            # ---------------------------------------------------
            # ✅ CREATE MOVES
            # ---------------------------------------------------
            for line in lines:

                # ❌ skip invalid
                if line.approved_qty <= 0:
                    raise ValidationError(
                        f"Approved qty must be greater than 0 for {line.product_id.display_name}"
                    )

                # ✅ GET AVAILABLE FROM SOURCE LOCATION ONLY
                quants = self.env["stock.quant"].search([
                    ("product_id", "=", line.product_id.id),
                    ("location_id", "=", self.source_location_id.id)
                ])
                available_qty = sum(quants.mapped("quantity"))

                # ✅ VALIDATION
                if line.approved_qty > available_qty:
                    raise ValidationError(
                        f"Not enough stock for {line.product_id.display_name} "
                        f"(Available: {available_qty})"
                    )

                # ✅ CREATE MOVE
                self.env["stock.move"].create({
                    "description_picking": line.product_id.display_name,
                    "picking_id": picking.id,
                    "product_id": line.product_id.id,
                    "product_uom_qty": line.approved_qty,
                    "product_uom": line.uom_id.id,
                    "location_id": self.source_location_id.id,
                    "location_dest_id": dest_location.id,
                })




            # picking.button_validate()

        # ---------------------------------------------------
        # ✅ UPDATE REQUEST STATE
        # ---------------------------------------------------
        request.state = "approved"

        return {
            "type": "ir.actions.act_window",
            "res_model": "stock.picking",
            "view_mode": "form",
            "res_id": created_pickings[-1].id,
        }


# =========================================================
# ✅ WIZARD LINE
# =========================================================
class CreateTransferWizardLine(models.TransientModel):
    _name = "create.transfer.wizard.line"

    wizard_id = fields.Many2one(
        "create.transfer.wizard",
        ondelete="cascade"
    )

    product_id = fields.Many2one("product.product")
    description = fields.Text()

    requested_qty = fields.Float()
    approved_qty = fields.Float()

    uom_id = fields.Many2one("uom.uom")

    destination_location_id = fields.Many2one(
        "stock.location",
        domain="[('usage', 'in', ('internal', 'customer'))]"
    )

    available_qty = fields.Float(
        compute="_compute_available_qty",
    )


    @api.depends("product_id", "wizard_id.source_location_id")
    def _compute_available_qty(self):
        for line in self:
            source = line.wizard_id.source_location_id

            if not source or not source.is_material_source:
                line.available_qty = 0.0
                continue

            if line.product_id:
                quants = self.env["stock.quant"].search([
                    ("product_id", "=", line.product_id.id),
                    ("location_id", "=", source.id)
                ])
                line.available_qty = sum(quants.mapped("quantity"))
            else:
                line.available_qty = 0.0

