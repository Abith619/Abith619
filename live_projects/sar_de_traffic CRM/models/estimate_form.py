from odoo import models, fields, api
from odoo.exceptions import ValidationError

class QuotationEstimate(models.Model):
    _name = 'quotation.estimate'
    _description = 'Quotation Estimate'
    _rec_name = 'name'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string='Ref no')
    date_from = fields.Date(string='Date', default=fields.Date.context_today)
    customer_id : fields.Many2one = fields.Many2one('res.partner', string='Customer', required=True)
    project_id : fields.Many2one = fields.Many2one('project.project', string='Project')
    lead_id : fields.Many2one = fields.Many2one('crm.lead', string='Lead')
    taxes_id : fields.Many2one = fields.Many2one('account.tax', string='Taxes')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')
    sale_order_id : fields.Many2one = fields.Many2one('sale.order', string='Sale Order')
    currency_id : fields.Many2one = fields.Many2one(
        comodel_name='res.currency',
        default=lambda self: self.env.company.currency_id,
    )

    item_product : fields.Many2one = fields.Many2one('product.template', string='Item', context={"default_purchase_ok": False}, domain=[('purchase_ok', '=', False),('sale_ok', '=', True)])

    item_category : fields.Many2one = fields.Many2one('product.category', string='Category', related='item_product.categ_id')
    estimate_qty = fields.Float(string="Quantity", default=1.0)
    # shape_id : fields.Many2one = fields.Many2one('product.shape', string='Shape')
    # size_id : fields.Many2one = fields.Many2one('custom.size', string='Size')
    measure = fields.Selection([
        ('meter', '(m)'),
        ('msq', '(m2)'),
    ])

    form_type = fields.Selection([
        ('post', 'Post'),
        ('frame', 'Frame'),
        ('sign', 'Sign')
    ], string='Estimation Type', default='post', required=True)

    stage_one_sign : fields.One2many = fields.One2many('stage.one.sign', 'estimate_id', string='Stage One Sign Details')
    # stage_two_frame : fields.One2many = fields.One2many('stage.two.frame', 'estimate_id', string='Stage Two Frame Details')
    # stage_three_pack : fields.One2many = fields.One2many('stage.three.pack', 'estimate_id', string='Stage Three Rivet & Packing Details')
    # stage_four_post : fields.One2many = fields.One2many('stage.four.post', 'estimate_id', string='Stage Four Post Details')

    sign_sub_total = fields.Float(string='Sub Total', readonly=True)
    sign_over_head_expense = fields.Float(string="Over Head Expenses (%)")
    sign_expense_rate = fields.Float(string="Net Amount", readonly=True, compute='_compute_totals')
    sign_profit = fields.Float(string="Profit (%)")
    sign_profit_rate = fields.Float(string="Profit Amount", readonly=True, compute='_compute_totals')
    sign_grand_total = fields.Float(string="Grand Total", readonly=True)

    # frame_sub_total = fields.Float(string='Frame Sub Total', readonly=True)
    # frame_over_head_expense = fields.Float(string="Frame Over Head Expenses (%)")
    # frame_expense_rate = fields.Float(string="Frame Net Amount", readonly=True, compute='_compute_totals')
    # frame_profit = fields.Float(string="Frame Profit (%)")
    # frame_profit_rate = fields.Float(string="Frame Profit Amount", readonly=True, compute='_compute_totals')
    # frame_grand_total = fields.Float(string="Frame Grand Total", readonly=True)

    # pack_sub_total = fields.Float(string='Pack Sub Total', readonly=True)
    # pack_over_head_expense = fields.Float(string="Pack Over Head Expenses (%)")
    # pack_expense_rate = fields.Float(string="Pack Net Amount", readonly=True, compute='_compute_totals')
    # pack_profit = fields.Float(string="Pack Profit (%)")
    # pack_profit_rate = fields.Float(string="Pack Profit Amount", readonly=True, compute='_compute_totals')
    # pack_grand_total = fields.Float(string="Pack Grand Total", readonly=True)

    # post_sub_total = fields.Float(string='Sub Total', readonly=True)
    # post_over_head_expense = fields.Float(string="Over Head Expenses (%)")
    # post_expense_rate = fields.Float(string="Net Amount", readonly=True, compute='_compute_totals')
    # post_profit = fields.Float(string="Profit (%)")
    # post_profit_rate = fields.Float(string="Profit Amount", readonly=True, compute='_compute_totals')
    # post_grand_total = fields.Monetary(string="Grand Total", currency_field='currency_id', readonly=True)

    corporate_oh = fields.Float(string='Corporate O/H (%)')
    corporate_oh_rate = fields.Float(string='Corporate O/H', compute='_compute_totals')
    corporate_profit = fields.Float(string='Corporate Profit (%)')
    corporate_profit_rate = fields.Float(string='Corporate Profit', compute='_compute_totals')

    subtotal = fields.Monetary(string='Subtotal', currency_field='currency_id')
    net_amount = fields.Monetary(string='Net Amount', currency_field='currency_id', compute='_compute_totals')
    amount_total = fields.Monetary(string='Total Amount', currency_field='currency_id', compute='_compute_totals')
    rate_per_quantity = fields.Float(string='Rate Per Quantity', store=True, compute='_compute_rate_per_quantity')

    def action_create_quotation(self):
        active_ids = self.env.context.get('active_ids', [])
        if not active_ids:
            raise ValidationError("No estimates selected.")

        estimates = self.browse(active_ids)

        customers = estimates.mapped('customer_id')
        if len(customers) != 1:
            raise ValidationError("All selected estimates must belong to the same customer.")
        customer = customers[0]

        sale_order = self.env['sale.order'].create({
            'partner_id': customer.id,
            'origin': ', '.join(estimates.mapped('name')),
            'date_order': fields.Datetime.now(),
            'currency_id': self.env.company.currency_id.id,
        })

        for rec in estimates:
            sale_order_line_vals = {
                'order_id': sale_order.id,
                'product_id': rec.item_product.product_variant_id.id,
                'product_uom_qty': rec.estimate_qty,
                'price_unit': rec.rate_per_quantity,
                'name': rec.item_product.name or rec.name,
            }
            self.env['sale.order.line'].create(sale_order_line_vals)

            rec.sale_order_id = sale_order.id
            rec.status = 'confirmed'

        return {
            'type': 'ir.actions.act_window',
            'name': 'Sale Order',
            'res_model': 'sale.order',
            'view_mode': 'form',
            'res_id': sale_order.id,
            'target': 'current',
        }

    @api.onchange('item_product')
    def _onchange_item_product(self):
            for rec in self:
                if rec.item_product:
                    bom=self.env['mrp.bom'].search([('product_tmpl_id','=',rec.item_product.id)], limit=1)
                    if bom:
                        rec.stage_one_sign = False
                        for line in bom.bom_line_ids:
                            rec.stage_one_sign += self.env['stage.one.sign'].new({
                                'resource_name': line.product_id.product_tmpl_id.id,
                            })

    @api.onchange('estimate_qty')
    @api.depends('estimate_qty','amount_total')
    def _compute_rate_per_quantity(self):
        for rec in self:
            rec.rate_per_quantity = (rec.amount_total / rec.estimate_qty)

    def _compute_currency_id(self):
        currency_default_id = self.env.ref('base.INR')
        for order in self:
            order.currency_id = currency_default_id

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['name'] = self.env['ir.sequence'].next_by_code('quotation.estimate')
        res = super().create(vals_list)
        return res

    def action_confirm(self):
        mo_line_values=[]
        so_line_values=[]
    #                                              Create Manufacturing Order
        for rec in self:
            for line in rec.stage_one_sign:
                mo_line_values.append((0, 0, {
                    'product_id': line.resource_name.product_variant_id.id,
                    'product_uom_qty': line.calc_qty,
                    'product_uom': line.unit_id.id,
                }))
        mo = self.env['mrp.production'].create({
            'product_id': self.item_product.product_variant_id.id,
            'product_qty': self.estimate_qty,
            'move_raw_ids': mo_line_values,
        })
        #                                                  Create Bill of Materials
        for rec in self:
            if rec.item_product and rec.stage_one_sign:
                bom_vals = {
                    'product_tmpl_id': rec.item_product.id,
                    'product_id': False,
                    'product_qty': rec.estimate_qty,
                    'type': 'normal',
                    'code': rec.name,
                    'company_id': self.env.company.id,
                }
                bom = self.env['mrp.bom'].create(bom_vals)

                # Create BoM Lines
                for line in rec.stage_one_sign:
                    if line.resource_name == rec.item_product:
                        continue

                    self.env['mrp.bom.line'].create({
                        'bom_id': bom.id,
                        'product_id': line.resource_name.product_variant_id.id,
                        'product_qty': line.calc_qty * rec.estimate_qty,
                        'product_uom_id': line.resource_name.uom_id.id,
                        'company_id': self.env.company.id,
                    })

    #                                               Create Sales Order Quotation
        for rec in self:
            so_line_values.append((0, 0, {
                'product_id': rec.item_product.product_variant_id.id,
                'product_uom_qty': rec.estimate_qty,
                'price_unit': rec.amount_total,
            }))
        self.env['sale.order'].create({
            'partner_id': self.customer_id.id,
            'partner_invoice_id': self.customer_id.id,
            'partner_shipping_id': self.customer_id.id,
            'opportunity_id': self.lead_id.id,
            'order_line': so_line_values,
        })
        self.status = 'confirmed'
        user_id = self.env.user
        self.message_post(
            body=f"Estimate {self.name} has been confirmed by {user_id.name} ✅",
            message_type="notification"
        )

    def action_cancel(self):
        self.status = 'cancelled'
        user_id = self.env.user
        self.message_post(
            body=f"Estimate {self.name} has been cancelled by {user_id.name} ❌",
            message_type="notification"
        )

    @api.depends(
        'stage_one_sign.net_amount', 'sign_over_head_expense', 'sign_profit','net_amount', 'amount_total',
        'corporate_oh_rate', 'corporate_profit_rate','corporate_oh', 'corporate_profit',
    )
    def _compute_totals(self):
        for rec in self:
            # Stage 1 (Sign)
            sign_net_total = self.env['stage.one.sign'].read_group([('estimate_id', '=', rec.id)], ['net_amount:sum'], groupby=[])
            rec.sign_sub_total = sign_net_total and sign_net_total[0].get('net_amount', 0.0) if sign_net_total else 0.0
            # rec.sign_sub_total = sum(rec.stage_one_sign.mapped("net_amount"))
            rec.sign_profit_rate = rec.sign_sub_total * (rec.sign_profit or 0) / 100.0
            rec.sign_expense_rate = rec.sign_sub_total * (rec.sign_over_head_expense or 0) / 100.0
            rec.sign_grand_total = rec.sign_sub_total + rec.sign_profit_rate + rec.sign_expense_rate

            # Corporate OH & Profit
            rec.net_amount = rec.sign_grand_total
            rec.corporate_oh_rate = rec.net_amount * (rec.corporate_oh or 0) / 100.0
            rec.corporate_profit_rate = rec.net_amount * (rec.corporate_profit or 0) / 100.0

            # Overall totals
            rec.subtotal = rec.sign_sub_total
            rec.amount_total = rec.net_amount + rec.corporate_oh_rate + rec.corporate_profit_rate

#                                               Stage One : Sign

class Stage1Sign(models.Model):
    _name='stage.one.sign'
    _description="Stage One Sign Details"

    estimate_id : fields.Many2one = fields.Many2one('quotation.estimate', string='Estimate Reference', required=True, ondelete='cascade')
    resource_type = fields.Selection([
        ('direct', 'Direct Material Cost'),
        ('labour', 'Labour Work Item'),
        ('others', 'Others'),
    ], string='Type', required=True, default='direct')
    acc_group = fields.Selection([
        ('direct', 'Direct Cost'),
        ('labour', 'Labour'),
        ('others', 'Others'),
    ], string='Account', required=True, default='direct')
    resource_for = fields.Selection([
        ('production', 'Production'),
        ('manufacturing', 'Manufacturing'),
    ], string="Resource", default='production')
    resource_name : fields.Many2one = fields.Many2one('product.template', string='Component', required=True, domain=[('purchase_ok', '=', True),('sale_ok', '=', False)], context={"default_sale_ok": False})
    make_id : fields.Many2one = fields.Many2one('product.attribute.value', string='Make', domain=[('attribute_id.name', '=', 'Make')])
    supplier_id : fields.Many2one = fields.Many2one('res.partner', string='Supplier')
    unit_id : fields.Many2one = fields.Many2one('uom.uom', string='Unit', required=True, related='resource_name.uom_id')
    co_efficient = fields.Float(string='Co-Efficient')
    rate_factor = fields.Float(string='Rate Factor')
    calc_qty = fields.Float(string='Quantity', store=True, compute='_calc_stage1_fields')
    unit_rate = fields.Integer(string='Unit Rate',readonly=False, store=True, compute='_compute_purchase_price')
    delivery_charges = fields.Float(string='Delivery Charges')
    wastage = fields.Float(string='Wastage (%)')
    wastage_amount = fields.Float(string='Wastage Amount', store=True, compute='_calc_stage1_fields')
    resources_total = fields.Float(string='Resources Total', store=True, compute='_calc_stage1_fields')
    add_rate = fields.Float(string='Add Rate')
    net_amount = fields.Float(string='Net Amount', store=True, compute='_calc_stage1_fields')

    @api.depends('resource_name')
    def _compute_purchase_price(self):
        for rec in self:
            variant_seller_ids = rec.resource_name.variant_seller_ids
            if len(variant_seller_ids) > 1:
                purchase_order = variant_seller_ids[-1]
                rec.unit_rate = purchase_order.price
            else:
                purchase_order = variant_seller_ids[:1]
                rec.unit_rate = purchase_order.price


    @api.depends('co_efficient', 'rate_factor', 'calc_qty', 'unit_rate', 'wastage', 'wastage_amount', 'resources_total', 'add_rate')
    def _calc_stage1_fields(self):
        for rec in self:
            rec.calc_qty = (rec.co_efficient * rec.rate_factor)
            rec.wastage_amount = (rec.calc_qty * rec.unit_rate) * (rec.wastage / 100)
            rec.resources_total = (rec.calc_qty * rec.unit_rate) + (rec.wastage_amount + rec.add_rate)
            rec.net_amount = (rec.resources_total + rec.add_rate)

#                                                       Stage 2 : Frame

# class Stage2Frame(models.Model):
#     _name = 'stage.two.frame'
#     _description = "Stage Two Frame Details"

#     estimate_id : fields.Many2one = fields.Many2one('quotation.estimate', string='Estimate Reference', required=True, ondelete='cascade')
#     resource_type = fields.Selection([
#         ('direct', 'Direct Material Cost'),
#         ('labour', 'Labour Work Item'),
#         ('others', 'Others'),
#     ], string='Type', required=True, default='direct')
#     acc_group = fields.Selection([
#         ('direct', 'Direct Cost'),
#         ('labour', 'Labour'),
#         ('others', 'Others'),
#     ], string='Account', required=True, default='direct')
#     resource_for = fields.Selection([
#         ('production', 'Production'),
#         ('manufacturing', 'Manufacturing'),
#     ], string="Resource", default='production')
#     resource_name : fields.Many2one = fields.Many2one('product.template', string='Component', required=True)
#     make_id : fields.Many2one = fields.Many2one('product.attribute.value', string='Make', domain=[('attribute_id.name', '=', 'Make')])
#     supplier_id : fields.Many2one = fields.Many2one('res.partner', string='Supplier')
#     unit_id : fields.Many2one = fields.Many2one('uom.uom', string='Unit', required=True, related='resource_name.uom_id')
#     co_efficient = fields.Float(string='Co-Efficient')
#     rate_factor = fields.Float(string='Rate Factor')
#     calc_qty = fields.Float(string='Quantity', store=True, compute='_calc_stage2_fields')
#     unit_rate = fields.Integer(string='Unit Rate')
#     delivery_charges = fields.Float(string='Delivery Charges')
#     wastage = fields.Float(string='Wastage (%)')
#     wastage_amount = fields.Float(string='Wastage Amount', store=True, compute='_calc_stage2_fields')
#     resources_total = fields.Float(string='Resources Total', store=True, compute='_calc_stage2_fields')
#     add_rate = fields.Float(string='Add Rate')
#     net_amount = fields.Float(string='Net Amount', store=True, compute='_calc_stage2_fields')

#     @api.depends('co_efficient', 'rate_factor', 'calc_qty', 'unit_rate', 'wastage', 'wastage_amount', 'resources_total', 'add_rate')
#     def _calc_stage2_fields(self):
#         for rec in self:
#             rec.calc_qty = (rec.co_efficient * rec.rate_factor)
#             rec.wastage_amount = (rec.calc_qty * rec.unit_rate) * (rec.wastage / 100)
#             rec.resources_total = (rec.calc_qty * rec.unit_rate) + (rec.wastage_amount + rec.add_rate)
#             rec.net_amount = (rec.resources_total + rec.add_rate)

# #                                                                                                   ---------- Stage 3 : Rivet & Packing ----------

# class Stage3Pack(models.Model):
#     _name = 'stage.three.pack'
#     _description = "Stage Three Rivet & Packing Details"

#     estimate_id : fields.Many2one = fields.Many2one('quotation.estimate', string='Estimate Reference', required=True, ondelete='cascade')
#     resource_type = fields.Selection([
#         ('direct', 'Direct Material Cost'),
#         ('labour', 'Labour Work Item'),
#         ('others', 'Others'),
#     ], string='Type', required=True, default='direct')
#     acc_group = fields.Selection([
#         ('direct', 'Direct Cost'),
#         ('labour', 'Labour'),
#         ('others', 'Others'),
#     ], string='Account', required=True, default='direct')
#     resource_for = fields.Selection([
#         ('production', 'Production'),
#         ('manufacturing', 'Manufacturing'),
#     ], string="Resource", default='production')
#     resource_name : fields.Many2one = fields.Many2one('product.template', string='Component', required=True)
#     make_id : fields.Many2one = fields.Many2one('product.attribute.value', string='Make', domain=[('attribute_id.name', '=', 'Make')])
#     supplier_id : fields.Many2one = fields.Many2one('res.partner', string='Supplier')
#     unit_id : fields.Many2one = fields.Many2one('uom.uom', string='Unit', required=True, related='resource_name.uom_id')
#     co_efficient = fields.Float(string='Co-Efficient')
#     rate_factor = fields.Float(string='Rate Factor')
#     calc_qty = fields.Float(string='Quantity', store=True, compute='_calc_stage3_fields')
#     unit_rate = fields.Integer(string='Unit Rate')
#     delivery_charges = fields.Float(string='Delivery Charges')
#     wastage = fields.Float(string='Wastage (%)')
#     wastage_amount = fields.Float(string='Wastage Amount', store=True, compute='_calc_stage3_fields')
#     resources_total = fields.Float(string='Resources Total', store=True, compute='_calc_stage3_fields')
#     add_rate = fields.Float(string='Add Rate')
#     net_amount = fields.Float(string='Net Amount', store=True, compute='_calc_stage3_fields')

#     @api.depends('co_efficient', 'rate_factor', 'calc_qty', 'unit_rate', 'wastage', 'wastage_amount', 'resources_total', 'add_rate')
#     def _calc_stage3_fields(self):
#         for rec in self:
#             rec.calc_qty = (rec.co_efficient * rec.rate_factor)
#             rec.wastage_amount = (rec.calc_qty * rec.unit_rate) * (rec.wastage / 100)
#             rec.resources_total = (rec.calc_qty * rec.unit_rate) + (rec.wastage_amount + rec.add_rate)
#             rec.net_amount = (rec.resources_total + rec.add_rate)

# #                                                               ---------- Stage 4 : Post ----------

# class Stage4Post(models.Model):
#     _name = 'stage.four.post'
#     _description = "Stage Four Post Details"

#     estimate_id : fields.Many2one = fields.Many2one('quotation.estimate', string='Estimate Reference', required=True, ondelete='cascade')
#     resource_type = fields.Selection([
#         ('direct', 'Direct Material Cost'),
#         ('labour', 'Labour Work Item'),
#         ('others', 'Others'),
#     ], string='Type', required=True, default='direct')
#     acc_group = fields.Selection([
#         ('direct', 'Direct Cost'),
#         ('labour', 'Labour'),
#         ('others', 'Others'),
#     ], string='Account', required=True, default='direct')
#     resource_for = fields.Selection([
#         ('production', 'Production'),
#         ('manufacturing', 'Manufacturing'),
#     ], string="Resource", default='production')
#     resource_name : fields.Many2one = fields.Many2one('product.template', string='Component', required=True)
#     make_id : fields.Many2one = fields.Many2one('product.attribute.value', string='Make', domain=[('attribute_id.name', '=', 'Make')])
#     supplier_id : fields.Many2one = fields.Many2one('res.partner', string='Supplier')
#     unit_id : fields.Many2one = fields.Many2one('uom.uom', string='Unit', required=True, related='resource_name.uom_id')
#     co_efficient = fields.Float(string='Co-Efficient')
#     rate_factor = fields.Float(string='Rate Factor')
#     calc_qty = fields.Float(string='Quantity', store=True, compute='_calc_stage4_fields')
#     unit_rate = fields.Integer(string='Unit Rate')
#     delivery_charges = fields.Float(string='Delivery Charges')
#     wastage = fields.Float(string='Wastage (%)')
#     wastage_amount = fields.Float(string='Wastage Amount', store=True, compute='_calc_stage4_fields')
#     resources_total = fields.Float(string='Resources Total', store=True, compute='_calc_stage4_fields')
#     add_rate = fields.Float(string='Add Rate')
#     net_amount = fields.Float(string='Net Amount', store=True, compute='_calc_stage4_fields')

#     @api.depends('co_efficient', 'rate_factor', 'calc_qty', 'unit_rate', 'wastage', 'wastage_amount', 'resources_total', 'add_rate')
#     def _calc_stage4_fields(self):
#         for rec in self:
#             rec.calc_qty = (rec.co_efficient * rec.rate_factor)
#             rec.wastage_amount = (rec.calc_qty * rec.unit_rate) * (rec.wastage / 100)
#             rec.resources_total = (rec.calc_qty * rec.unit_rate) + (rec.wastage_amount + rec.add_rate)
#             rec.net_amount = (rec.resources_total + rec.add_rate)
