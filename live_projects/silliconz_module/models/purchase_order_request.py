from odoo import models, fields, api
from odoo.exceptions import UserError


class PurchaseRequest(models.Model):
    _name = "purchase.request"
    _description = "Purchase Request"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _order = 'id desc'

    name = fields.Char(string="Reference", required=True, copy=False, default="New")
    material_request_id = fields.Many2one("material.request", string="Material Request")
    line_ids = fields.One2many("purchase.request.line", "request_id", string="Lines")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('done', 'Done'),
    ], string="Status", default='draft', tracking=True, copy=False)

    analytic_account_id = fields.Many2one(
    "account.analytic.account",
    string="Analytical Account",
    tracking=True,)

    mo_id = fields.Many2one("mrp.production",string="Source Document")
    expected_date = fields.Date(string="Expected Date", required=True, default=fields.Date.today, tracking=True)
    received_date = fields.Date(string="Received Date", tracking=True)

    pr_requestor_id = fields.Many2one('res.users', string="Requested By", readonly=True, copy=False)
    pr_requestor_signature = fields.Image(string="Requestor Signature", readonly=True, copy=False)
    
    pr_approver_id = fields.Many2one('res.users', string="Approved By", readonly=True, copy=False)
    pr_approver_signature = fields.Image(string="Approver Signature", readonly=True, copy=False)

    purchase_order_ids = fields.One2many("purchase.order", "purchase_request_id", string="Purchase Orders")
    purchase_order_count = fields.Integer(string="Purchase Orders", compute="_compute_purchase_order_count")

    def _compute_purchase_order_count(self):
        for rec in self:
            rec.purchase_order_count = len(rec.purchase_order_ids)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = self.env["ir.sequence"].next_by_code(
                    "purchase.request"
                ) or "New"
        return super().create(vals_list)

    def action_submit(self):
        """User submits the purchase request for manager approval."""
        for rec in self:
            if not rec.line_ids:
                raise UserError("You cannot submit a purchase request without any product lines.")
            rec.state = 'submitted'
            rec.pr_requestor_id = self.env.user.id
            rec.pr_requestor_signature = self.env.user.signature_image

    def action_approve(self):
        """Manager approves the purchase request. It goes direct to approved stage."""
        for rec in self:
            rec.state = 'approved'
            rec.pr_approver_id = self.env.user.id
            rec.pr_approver_signature = self.env.user.signature_image

    def action_open_create_po_wizard(self):
        """Opens the wizard to create a PO manually."""
        for rec in self:
            lines = [(0, 0, {
                'product_id': line.product_id.id,
                'quantity': line.quantity,
                'uom_id': line.uom_id.id,
            }) for line in rec.line_ids]
            
            return {
                'name': 'Create Purchase Order RFQ',
                'type': 'ir.actions.act_window',
                'res_model': 'create.po.wizard',
                'view_mode': 'form',
                'target': 'new',
                'context': {
                    'default_request_id': rec.id,
                    'default_line_ids': lines,
                }
            }

    def action_reset_draft(self):
        """Reset the purchase request back to draft state."""
        for rec in self:
            rec.state = 'draft'

    def action_view_purchase_orders(self):
        """Smart button action to view related purchase orders."""
        self.ensure_one()
        if self.purchase_order_count == 1:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Purchase Order',
                'res_model': 'purchase.order',
                'view_mode': 'form',
                'res_id': self.purchase_order_ids.id,
            }
        return {
            'type': 'ir.actions.act_window',
            'name': 'Purchase Orders',
            'res_model': 'purchase.order',
            'view_mode': 'list,form',
            'domain': [('purchase_request_id', '=', self.id)],
        }

    def check_all_po_done(self):
        for rec in self:
            if not rec.purchase_order_ids:
                continue
            
            non_cancel_pos = rec.purchase_order_ids.filtered(lambda p: p.state != 'cancel')
            if not non_cancel_pos:
                continue
                
            all_done = all(po.state in ['purchase', 'done'] for po in non_cancel_pos)
            
            if all_done and rec.state == 'approved':
                rec.state = 'done'
            elif not all_done and rec.state == 'done':
                rec.state = 'approved'

class PurchaseRequestLine(models.Model):
    _name = "purchase.request.line"
    _description = "Purchase Request Line"

    request_id = fields.Many2one("purchase.request", ondelete="cascade")

    product_id = fields.Many2one("product.product", required=True)
    product_tmpl_id = fields.Many2one("product.template", related="product_id.product_tmpl_id", store=True)

    quantity = fields.Float()

    uom_id = fields.Many2one("uom.uom")
    description=fields.Char(string="Description")

    price_unit = fields.Float(string="Unit Price", digits='Product Price', related="product_id.standard_price", store=True)

    @api.onchange('product_id')
    def _onchange_product_id_price(self):
        for line in self:
            if line.product_id:
                line.price_unit = line.product_id.standard_price
                line.uom_id = line.product_id.uom_id
                line.description = line.product_id.name
            else:
                line.price_unit = 0.0

    allowed_manufacturer_ids = fields.Many2many("product.manufacturer", compute="_compute_allowed_manufacturers")
    allowed_part_number_ids = fields.Many2many("product.manufacturer.info", compute="_compute_allowed_manufacturers")

    @api.depends("product_id", "manufacturer_ids", "manufacturer_part_number_ids")
    def _compute_allowed_manufacturers(self):
        for rec in self:
            if rec.product_id and rec.product_id.manufacturer_line_ids:
                allowed_mfrs = rec.product_id.manufacturer_line_ids.mapped('manufacturer_id')
                if rec.manufacturer_ids:
                    allowed_mfrs |= rec.manufacturer_ids
                rec.allowed_manufacturer_ids = allowed_mfrs

                if rec.manufacturer_ids:
                    allowed_parts = rec.product_id.manufacturer_line_ids.filtered(lambda l: l.manufacturer_id == rec.manufacturer_ids)
                else:
                    allowed_parts = rec.product_id.manufacturer_line_ids
                    
                if rec.manufacturer_part_number_ids:
                    allowed_parts |= rec.manufacturer_part_number_ids
                rec.allowed_part_number_ids = allowed_parts
            else:
                rec.allowed_manufacturer_ids = rec.manufacturer_ids
                rec.allowed_part_number_ids = rec.manufacturer_part_number_ids

    @api.model_create_multi
    def create(self, vals_list):
        lines = super().create(vals_list)
        lines._sync_manufacturer_to_product()
        return lines

    def write(self, vals):
        res = super().write(vals)
        self._sync_manufacturer_to_product()
        return res

    def _sync_manufacturer_to_product(self):
        for line in self:
            if not line.product_id:
                continue
            
            tmpl = line.product_id.product_tmpl_id
            mfr = line.manufacturer_ids
            part = line.manufacturer_part_number_ids
            
            if mfr and not mfr.product_tmpl_id:
                mfr.product_tmpl_id = tmpl.id
                
            if part:
                if not part.product_tmpl_id:
                    part.product_tmpl_id = tmpl.id
                if not part.manufacturer_id and mfr:
                    part.manufacturer_id = mfr.id

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

    

    