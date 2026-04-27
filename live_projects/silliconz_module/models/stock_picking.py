from odoo import api, models, fields
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare

class StockPicking(models.Model):
    _inherit = "stock.picking"

    material_request_id = fields.Many2one("material.request", string="Material Requester")
    
    state = fields.Selection(selection_add=[
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('assigned', 'Ready'),
        ('done', 'Done'),
    ])

    def action_submit(self):
        for rec in self:
            if rec.state == 'draft':
                rec.state = 'submitted'

    def button_validate(self):
        for picking in self:
            if picking.state == 'submitted':
                picking.action_confirm()

            if picking.picking_type_code not in ('incoming', 'outgoing'):
                continue

            error_lines = []

            for move in picking.move_ids.filtered(
                lambda m: m.state not in ('done', 'cancel')
            ):
                demanded = move.product_uom_qty
                done = sum(move.move_line_ids.mapped('quantity'))

                if done == 0:
                    continue


                tolerance = move.product_id.product_tmpl_id.tolerance_percent or 0.0
                min_qty = demanded * (1 - tolerance / 100)
                max_qty = demanded * (1 + tolerance / 100)

                if (
                    float_compare(done, min_qty, precision_rounding=move.product_uom.rounding) < 0
                    or float_compare(done, max_qty, precision_rounding=move.product_uom.rounding) > 0
                ):
                    error_lines.append(
                        f"{move.product_id.display_name}\n"
                        f"  Entered : {done:.2f}\n"
                        f"  Allowed : {min_qty:.2f} \u2192 {max_qty:.2f}"
                    )
                else:
        
                    if float_compare(done, demanded, precision_rounding=move.product_uom.rounding) != 0:
                        move.write({'product_uom_qty': done})

            if error_lines:
                raise UserError(
                    "Quantity outside tolerance range:\n\n" + "\n\n".join(error_lines)
                )

        return super().button_validate()



    terms_id = fields.Many2one(
        'terms.and.condition',
        string="Terms & Conditions",
        domain="[('type', 'in', ['delivery', 'general']), ('active','=',True)]"
    )

    @api.onchange('terms_id')
    def _onchange_terms_id(self):
        for rec in self:
            if rec.terms_id and rec.terms_id.content:
                if rec.note:
                    rec.note = rec.note + "\n\n" + rec.terms_id.content
                else:
                    rec.note = rec.terms_id.content

    def _action_done(self):
        res = super()._action_done()
        for picking in self:
            if picking.material_request_id:
                picking.material_request_id.line_ids._update_request_state()
            if picking.purchase_id and picking.purchase_id.purchase_request_id:
                pr = picking.purchase_id.purchase_request_id.sudo()
                pr.received_date = fields.Date.today()
                pr.state = 'done'
        return res

class StockMove(models.Model):
    _inherit = "stock.move"

    manufacturing_date = fields.Date(string="Manufacturing Date")
    warranty_info = fields.Char(string="Warranty")
    expiry_date = fields.Date(string="Expiry Date")
    ex_rate = fields.Float(string="EX Rate", digits=(12, 4))
    tolerance_percent = fields.Float(
        string="Tolerance (%)",
        related="product_id.product_tmpl_id.tolerance_percent",
        store=False,
        readonly=True,
    )

    allowed_manufacturer_ids = fields.Many2many("product.manufacturer", compute="_compute_allowed_manufacturers")
    allowed_part_number_ids = fields.Many2many("product.manufacturer.info", compute="_compute_allowed_manufacturers")

    @api.depends("product_id", "manufacturer_ids", "manufacturer_part_number_ids")
    def _compute_allowed_manufacturers(self):
        for rec in self:
            if rec.product_id and rec.product_id.manufacturer_line_ids:
                rec.allowed_manufacturer_ids = rec.product_id.manufacturer_line_ids.mapped('manufacturer_id')
                if rec.manufacturer_ids:
                    rec.allowed_part_number_ids = rec.product_id.manufacturer_line_ids.filtered(lambda l: l.manufacturer_id == rec.manufacturer_ids)
                else:
                    rec.allowed_part_number_ids = rec.product_id.manufacturer_line_ids
            else:
                rec.allowed_manufacturer_ids = rec.manufacturer_ids
                rec.allowed_part_number_ids = rec.manufacturer_part_number_ids

    manufacturer_ids = fields.Many2one("product.manufacturer",string="Manufacturers", compute="_compute_uom_and_manufacturers", store=True, readonly=False)
    manufacturer_part_number_ids = fields.Many2one("product.manufacturer.info",string="Mfr Part Numbers", compute="_compute_uom_and_manufacturers", store=True, readonly=False)

    @api.depends("product_id", "manufacturer_ids")
    def _compute_uom_and_manufacturers(self):
        for rec in self:
            if not rec.product_id:
                rec.manufacturer_ids = False
                rec.manufacturer_part_number_ids = False
                continue
            if rec.product_id and rec.manufacturer_ids:
                matching_lines = rec.product_id.manufacturer_line_ids.filtered(lambda l: l.manufacturer_id == rec.manufacturer_ids)
                if matching_lines:
                    rec.manufacturer_part_number_ids = matching_lines[0].id

            lines = rec.product_id.manufacturer_line_ids

            if lines:
                if not rec.manufacturer_ids:
                    rec.manufacturer_ids = lines[0].manufacturer_id

                if not rec.manufacturer_part_number_ids or \
                rec.manufacturer_part_number_ids.manufacturer_id != rec.manufacturer_ids:
                    match = lines.filtered(lambda l: l.manufacturer_id == rec.manufacturer_ids)
                    rec.manufacturer_part_number_ids = match[:1] if match else False
            else:
                rec.manufacturer_ids = False
                rec.manufacturer_part_number_ids = False

    @api.onchange("manufacturer_ids")
    def _onchange_manufacturer_part_number(self):
        if self.product_id and self.manufacturer_ids:
            matching_lines = self.product_id.manufacturer_line_ids.filtered(lambda l: l.manufacturer_id == self.manufacturer_ids)
            if matching_lines:
                self.manufacturer_part_number_ids = matching_lines[0].id
