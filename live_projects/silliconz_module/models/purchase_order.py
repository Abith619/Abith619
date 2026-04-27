from odoo import api, models, fields
from odoo.exceptions import UserError

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_tmpl_id = fields.Many2one("product.template", related="product_id.product_tmpl_id", store=True)
    allowed_manufacturer_ids = fields.Many2many("product.manufacturer", compute="_compute_allowed_manufacturers")
    allowed_part_number_ids = fields.Many2many("product.manufacturer.info", compute="_compute_allowed_manufacturers")
    vendor_min_qty = fields.Float(string="Vendor MOQ", readonly=True,compute="_compute_supplier_moq",store=True)

    @api.depends('product_id', 'order_id.partner_id', 'product_qty')
    def _compute_supplier_moq(self):
        for line in self:
            if not line.product_id or not line.order_id.partner_id:
                line.vendor_min_qty = 0.0
                # line.purchase_min_qty = 0.0
                continue

            suppliers = line.product_id.seller_ids.filtered(
                lambda s: s.partner_id == line.order_id.partner_id
            ).sorted(key=lambda s: s.min_qty, reverse=True)

            supplier = False
            for s in suppliers:
                if line.product_qty >= s.min_qty:
                    supplier = s
                    break

            supplier = supplier or (suppliers and suppliers[-1])

            if supplier:
                line.vendor_min_qty = supplier.min_qty
                # line.purchase_min_qty = supplier.min_qty
            else:
                line.vendor_min_qty = 0.0
                # line.purchase_min_qty = 0.0

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

    

    additional_info = fields.Text(string="Additional Info", help="Remarks or additional information for this PO line item")

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    terms_id = fields.Many2one('terms.and.condition', string="Terms & Conditions", domain="[('type', 'in', ['purchase', 'general']), ('active','=',True)]")
    
    @api.onchange('terms_id')
    def _onchange_terms_id(self):
        for rec in self:
            if rec.terms_id and rec.terms_id.content:
                if rec.note:
                    rec.note = rec.note + "<br><br>" + rec.terms_id.content
                else:
                    rec.note = rec.terms_id.content
    amendment_origin_id = fields.Many2one('purchase.order', string="Amendment Of")
    amendment_ids = fields.One2many('purchase.order', 'amendment_origin_id', string="Amendments")
    amendment_count = fields.Integer(compute="_compute_amendment_count")
    mo_reference = fields.Many2one("mrp.production",string="Manufacturing Order Reference",readonly=True,copy=False)
    po_type = fields.Selection([('raw_material', 'Raw Material'), ('finished_product', 'Finished Product')], string="Purchase Order Type")
    billing_address_id = fields.Many2one('res.partner', string="Billing Address")
    shipping_address_id = fields.Many2one('res.partner', string="Shipping Address")
    purchase_request_id = fields.Many2one("purchase.request",string="Purchase Request",readonly=True,copy=False)
    reference_date = fields.Date(string="Reference Date",required=True,default=fields.Date.today,tracking=True)

    mo_id = fields.Many2one("mrp.production", string="Source Document", readonly=True, copy=False)

    po_approver_id = fields.Many2one('res.users', string="Approved By", readonly=True, copy=False)
    po_approver_signature = fields.Image(string="Approver Signature", readonly=True, copy=False)

    po_submitted_by_id = fields.Many2one('res.users', string="Submitted By", readonly=True, copy=False)
    po_submitted_state = fields.Boolean(string="Submitted for Approval", default=False, copy=False)

    po_display_state = fields.Selection([
        ('draft',    'RFQ'),
        ('submitted','Submitted'),
        ('sent',     'RFQ Sent'),
        ('purchase', 'Purchase Order'),
        ('done',     'Locked'),
        ('cancel',   'Cancelled'),
    ], string="PO Status", compute='_compute_po_display_state', store=True)

    is_po_manager = fields.Boolean(
        string="Is PO Manager",
        compute='_compute_is_po_manager',
    )

    additional_comments = fields.Text(string="Additional Comments")
    amount_in_words = fields.Char(string="Amount In Words", compute="_compute_amount_in_words")

    @api.depends('amount_total', 'currency_id')
    def _compute_amount_in_words(self):
        for order in self:
            if order.currency_id and order.amount_total:
                order.amount_in_words = order.currency_id.amount_to_text(order.amount_total)
            else:
                order.amount_in_words = ''

    @api.depends('state', 'po_submitted_state')
    def _compute_po_display_state(self):
        for rec in self:
            if rec.state in ('draft', 'sent') and rec.po_submitted_state:
                rec.po_display_state = 'submitted'
            else:
                rec.po_display_state = rec.state or 'draft'

    def _compute_is_po_manager(self):
        is_manager = self.env.user.has_group('silliconz_module.group_purchase_order_manager')
        for rec in self:
            rec.is_po_manager = is_manager

    def action_submit_po(self):
        """User submits the RFQ for manager approval."""
        for order in self:
            if order.state not in ('draft', 'sent'):
                raise UserError("Only RFQ/Quotations can be submitted for approval.")
            order.po_submitted_state = True
            order.po_submitted_by_id = self.env.user.id

    def action_approve_po(self):
        """Manager approves submission → moves to RFQ Sent state."""
        for order in self:
            if not order.po_submitted_state:
                raise UserError("This order has not been submitted for approval.")
            order.po_submitted_state = False
            order.write({'state': 'sent'})

    def action_rfq_send(self):
        """Override to clear submitted state when manager approves via Send RFQ."""
        for order in self:
            if order.po_submitted_state:
                order.po_submitted_state = False
        return super().action_rfq_send()

    def button_approve(self, force=False):
        """Override to capture the approver and their digital signature."""
        res = super().button_approve(force=force)
        for order in self.filtered(lambda o: o.state == 'purchase'):
            order.write({
                'po_approver_id': self.env.uid,
                'po_approver_signature': self.env.user.signature_image,
            })
        return res

    def _get_root_order(self):
        self.ensure_one()
        order = self
        while order.amendment_origin_id:
            order = order.amendment_origin_id
        return order

    def _compute_amendment_count(self):
        for rec in self:
            root = rec._get_root_order()
            amendments = self.env['purchase.order'].search([
                ('amendment_origin_id', '=', root.id)
            ])
            rec.amendment_count = len(amendments) + 1

    def button_confirm(self):
        
        if self.env.context.get('skip_moq_validation'):
            return super().button_confirm()
        
        for order in self:
            for line in order.order_line:
                if not line.product_id or not order.partner_id:
                    continue
                suppliers = line.product_id.seller_ids.filtered(
                    lambda s: s.partner_id == order.partner_id
                ).sorted(key=lambda s: s.min_qty, reverse=True)

                supplier = False
                for s in suppliers:
                    if line.product_qty >= s.min_qty:
                        supplier = s
                        break
                supplier = supplier or (suppliers and suppliers[-1])

                if supplier:
                    line.vendor_min_qty = supplier.min_qty
                else:
                    line.vendor_min_qty = 0.0

            violation_lines = order.order_line.filtered(
                lambda l: l.product_id and l.vendor_min_qty > 0 and l.product_qty < l.vendor_min_qty
            )

            if violation_lines:
                wizard = self.env['po.moq.conflict.wizard'].create({
                    'po_id': order.id,
                })
                return {
                    'type': 'ir.actions.act_window',
                    'name': 'MOQ Conflict Detected',
                    'res_model': 'po.moq.conflict.wizard',
                    'res_id': wizard.id,
                    'view_mode': 'form',
                    'target': 'new',
                }
            for line in order.order_line:
                if line.product_id:
                    suppliers = self.env['product.supplierinfo'].search([
                        ('product_tmpl_id', '=', line.product_id.product_tmpl_id.id),
                        ('partner_id', '=', order.partner_id.id)
                    ], order="id desc")

                    if suppliers:
                        suppliers[0].write({
                            'price': line.price_unit,
                        })

            if order.purchase_request_id:
                order.purchase_request_id.sudo().check_all_po_done()

        return super(PurchaseOrder, self).button_confirm()

    def _create_picking(self):
        res = super(PurchaseOrder, self)._create_picking()
        for order in self:
            pickings = self.env['stock.picking'].search([('purchase_id', '=', order.id)])
            for picking in pickings:
                for move in picking.move_ids:
                    if move.state not in ['done', 'cancel']:
                        move.write({'state': 'draft'})
        return res

    def button_cancel(self):
        res = super(PurchaseOrder, self).button_cancel()
        for order in self:
            if order.purchase_request_id:
                order.purchase_request_id.sudo().check_all_po_done()
        return res

    def action_amend_order(self):
        # raise UserError(self.id)
        self.ensure_one()

        if self.state != 'purchase':
            raise UserError("Only Purchase Orders can be amended.")

        root = self._get_root_order()
        amendment_number = len(root.amendment_ids) + 1

        base_name = root.name.split('-A')[0]
        new_name = "%s-A%s" % (base_name, amendment_number)

        new_order = self.copy({
            'name': new_name,
            'state': 'draft',
            'amendment_origin_id': root.id,
        })
        if self.state == 'purchase':
            self.button_unlock()
            self.button_cancel()
        else:
            self.button_cancel()

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order',
            'view_mode': 'form',
            'res_id': new_order.id,
        }

    def action_view_amendments(self):
        self.ensure_one()
        root = self._get_root_order()
        domain = ['|',('id', '=', root.id),('amendment_origin_id', '=', root.id)]
        return {
            'type': 'ir.actions.act_window',
            'name': 'Amendments',
            'res_model': 'purchase.order',
            'view_mode': 'list,form',
            'domain': domain,
        }
    