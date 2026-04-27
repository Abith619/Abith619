from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MaterialRequestLine(models.Model):
    _name = "material.request.line"
    _description = "Material Request Line"

    request_id = fields.Many2one("material.request", ondelete="cascade")

    product_id = fields.Many2one("product.product", required=True)
    product_tmpl_id = fields.Many2one("product.template", related="product_id.product_tmpl_id", store=True)
    description = fields.Text()

    requested_qty = fields.Float(required=True)
    approved_qty = fields.Float()

    uom_id = fields.Many2one("uom.uom")

    destination_location_id = fields.Many2one(
        "stock.location",
        domain="[('usage', 'in', ('internal', 'customer'))]",
        required=True
    )

    state = fields.Selection(related="request_id.state", store=True)

    available_qty = fields.Float(compute="_compute_available_qty")
    issued_qty = fields.Float(compute="_compute_issued_qty")
    issued_date = fields.Date()
    line_remarks = fields.Text(string="Remarks")

    can_edit_approved_qty = fields.Boolean(
        compute="_compute_can_edit_approved_qty",
        string="Can Edit Approved Qty"
    )

    def _compute_can_edit_approved_qty(self):
        is_approver = self.env.user.has_group(
            "silliconz_module.group_material_request_approver"
        )
        for rec in self:
            rec.can_edit_approved_qty = is_approver

    # -----------------------------
    # ✅ MANUFACTURER FIELDS (NO COMPUTE)
    # -----------------------------
    manufacturer_ids = fields.Many2one(
        "product.manufacturer",
        string="Manufacturer"
    )

    manufacturer_part_number_ids = fields.Many2one(
        "product.manufacturer.info",
        string="Part Number",
    )

    # -----------------------------
    # DOMAIN HELPERS
    # -----------------------------
    allowed_manufacturer_ids = fields.Many2many(
        "product.manufacturer",
        compute="_compute_allowed_manufacturers"
    )

    allowed_part_number_ids = fields.Many2many(
        "product.manufacturer.info",
        compute="_compute_allowed_manufacturers"
    )

    # -----------------------------
    # ONCHANGE: PRODUCT
    # -----------------------------
    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.uom_id = self.product_id.uom_id
            self.description = self.product_id.name

            lines = self.product_id.product_tmpl_id.manufacturer_line_ids

            if lines:
                self.manufacturer_ids = lines[0].manufacturer_id
                self.manufacturer_part_number_ids = lines[0]
            else:
                self.manufacturer_ids = False
                self.manufacturer_part_number_ids = False

    # -----------------------------
    # ONCHANGE: MANUFACTURER
    # -----------------------------
    @api.onchange("manufacturer_ids")
    def _onchange_manufacturer(self):
        if self.product_id and self.manufacturer_ids:
            lines = self.product_id.product_tmpl_id.manufacturer_line_ids.filtered(
                lambda l: l.manufacturer_id == self.manufacturer_ids
            )

            self.manufacturer_part_number_ids = lines[:1] if lines else False

    # -----------------------------
    # COMPUTE DOMAIN
    # -----------------------------
    @api.depends("product_id", "manufacturer_ids")
    def _compute_allowed_manufacturers(self):
        for rec in self:
            if rec.product_id:
                lines = rec.product_id.product_tmpl_id.manufacturer_line_ids

                rec.allowed_manufacturer_ids = lines.mapped("manufacturer_id")

                if rec.manufacturer_ids:
                    rec.allowed_part_number_ids = lines.filtered(
                        lambda l: l.manufacturer_id == rec.manufacturer_ids
                    )
                else:
                    rec.allowed_part_number_ids = lines
            else:
                rec.allowed_manufacturer_ids = False
                rec.allowed_part_number_ids = False

    # -----------------------------
    # 🔥 CORE: SYNC TO PRODUCT MASTER
    # -----------------------------
    def _sync_to_product_master(self):
        for rec in self:
            if not rec.product_id or not rec.manufacturer_ids:
                continue

            product_tmpl = rec.product_id.product_tmpl_id
            manufacturer = rec.manufacturer_ids

            part_number = rec.manufacturer_part_number_ids.part_number if rec.manufacturer_part_number_ids else False

            existing = self.env['product.manufacturer.info'].search([
                ('product_tmpl_id', '=', product_tmpl.id),
                ('manufacturer_id', '=', manufacturer.id),
                ('part_number', '=', part_number)
            ], limit=1)

            if not existing:
                new_line = self.env['product.manufacturer.info'].create({
                    'product_tmpl_id': product_tmpl.id,
                    'manufacturer_id': manufacturer.id,
                    'part_number': part_number,
                })

                rec.manufacturer_part_number_ids = new_line

    # -----------------------------
    # CREATE / WRITE
    # -----------------------------
    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records:
            record._sync_to_product_master()
        return records

    def write(self, vals):
        if "approved_qty" in vals:
            if not self.env.user.has_group(
                "silliconz_module.group_material_request_approver"
            ):
                raise ValidationError(
                    "Only Store Approver can set Approved Quantity."
                )

        res = super().write(vals)
        self._update_request_state()
        self._sync_to_product_master()
        return res

    # -----------------------------
    # VALIDATION
    # -----------------------------
    @api.constrains("requested_qty")
    def _check_requested_qty(self):
        for rec in self:
            if rec.requested_qty <= 0:
                raise ValidationError("Requested Quantity must be greater than zero.")

    # -----------------------------
    # STOCK
    # -----------------------------
    @api.depends("product_id", "request_id.source_location_id")
    def _compute_available_qty(self):
        for line in self:
            source = line.request_id.source_location_id

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

    @api.depends("product_id", "request_id.picking_ids.state", "request_id.picking_ids.move_ids.quantity")
    def _compute_issued_qty(self):
        for line in self:
            total_qty = 0.0
            latest_date = False

            done_pickings = line.request_id.picking_ids.filtered(
                lambda p: p.state == "done"
            )

            for picking in done_pickings:
                for move in picking.move_ids.filtered(
                    lambda m: m.product_id == line.product_id and m.state == "done"
                ):
                    total_qty += move.quantity

                if picking.date_done:
                    latest_date = picking.date_done.date()

            line.issued_qty = total_qty
            line.issued_date = latest_date

        self._update_request_state()

    def _update_request_state(self):
        for line in self:
            req = line.request_id

            if not req or req.state not in ("approved", "done"):
                continue

            valid_lines = [l for l in req.line_ids if l.approved_qty > 0]
            if not valid_lines:
                continue

            all_done = all(l.issued_qty >= l.approved_qty for l in valid_lines)

            req.state = "done" if all_done else "approved"