from odoo import models, fields, api
# from odoo.exceptions import ValidationError

class QuotationEstimate(models.Model):
    _name = 'quotation.estimate'
    _description = 'Quotation Estimate'

    name = fields.Char(string='Ref no')
    date = fields.Date(string='Date', default=fields.Date.context_today)
    customer_id : fields.Many2one = fields.Many2one('res.partner', string='Customer', required=True)
    project_id : fields.Many2one = fields.Many2one('project.project', string='Project')
    taxes_id : fields.Many2one = fields.Many2one('account.tax', string='Taxes')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')
    sale_order_id : fields.Many2one = fields.Many2one('sale.order', string='Sale Order')
    currency_id : fields.Many2one = fields.Many2one(
        comodel_name='res.currency',
        compute='_compute_currency_id',
        store=True,
        precompute=True,
        ondelete='restrict'
    )
    subtotal = fields.Monetary(string='Subtotal', currency_field='currency_id', store=True)
    amount_total = fields.Monetary(string='Total Amount', currency_field='currency_id', store=True)

    item_category : fields.Many2one = fields.Many2one('product.category', string='Item Category')
    shape_id : fields.Many2one = fields.Many2one('product.shape', string='Shape')
    size_id : fields.Many2one = fields.Many2one('custom.size', string='Size')
    measure = fields.Selection([
        ('meter', '(m)'),
        ('msq', '(m2)'),
    ])

    form_type = fields.Selection([
        ('post', 'Post'),
        ('frame', 'Frame'),
        ('sign', 'Sign')
    ], string='Estimation Type', default='post', required=True)

    def _compute_currency_id(self):
        currency_default_id = self.env.ref('base.INR')
        for order in self:
            order.currency_id = currency_default_id

    def action_validate(self):
        pass

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['name'] = self.env['ir.sequence'].next_by_code('quotation.estimate')
        res = super().create(vals_list)
        return res

    #                                                                                           Sign Fields
    substrate_id : fields.Many2one = fields.Many2one('product.template', string='Substrate', domain="[('categ_id', '=', item_category)]")
    reflective_id : fields.Many2one = fields.Many2one('product.template', string='Reflective', domain="[('categ_id', '=', item_category)]")

    #                                                                                   Sign Substrate Value
    substrate_make : fields.Many2many = fields.Many2many(
        'product.attribute.value',
        relation='quotation_estimate_substrate_make_rel',
        column1='estimate_id',
        column2='attribute_value_id',
        string='Make',
        domain="[('attribute_id.name', '=', 'Make')]",
        store=True
    )
    make_many2one : fields.Many2one = fields.Many2one('product.attribute.value', string="Make", store=True, readonly=False, domain="[('id', 'in', substrate_make)]") #, domain="[('attribute_id.name', '=', 'Make')]"
    substrate_area = fields.Float(string="Area")
    substrate_waste = fields.Float(string="Wastage")
    substrate_rate_kg = fields.Float(string="Rate(Kgs)")
    substrate_rate_m2 = fields.Float(string="Rate(m2)")
    substrate_amount = fields.Float(string="Amount")
    substrate_cutting_amt = fields.Float(string="Cutting Amt")
    substrate_paint_rate = fields.Float(string="Rate")
    substrate_paint_amt = fields.Float(string="Paint Amount")
    substrate_total = fields.Float(string="Total", compute='_compute_total_amount')

    @api.onchange('substrate_id')
    def _onchange_substrate_make(self):
        for line in self.substrate_id.attribute_line_ids:
            if line.attribute_id.name == 'Make':
                ids = line.value_ids.ids
                self.substrate_make = ids
                self.make_many2one = ids[0]
        self.substrate_amount = self.substrate_id.list_price

    @api.onchange('reflective_id')
    def _onchange_reflective_make(self):
        for line in self.reflective_id.attribute_line_ids:
            if line.attribute_id.name == 'Color':
                ids = line.value_ids.ids
                self.reflective_color = ids
                self.reflective_make = ids[0]
        self.reflective_amount = self.reflective_id.list_price

    @api.depends('substrate_amount', 'substrate_cutting_amt', 'substrate_paint_amt', 'substrate_total')
    def _compute_total_amount(self):
        for rec in self:
            rec.substrate_total = (rec.substrate_amount + rec.substrate_cutting_amt + rec.substrate_paint_amt)

    @api.onchange('item_category', 'shape_id', 'size_id')
    def _get_from_master(self):
        if self.item_category and self.shape_id and self.size_id:
            master = self.env['sign.master'].search([
                ('category_id', '=', self.item_category.id),
                ('shape_id', '=', self.shape_id.id),
                ('size_id', '=', self.size_id.id),
            ], limit=1)
            if master:
                wastage = (master.substrate_area - master.common_area)
                self.write({
                    'substrate_area': master.common_area,
                    'substrate_waste': wastage,
                    'reflective_area': master.base_sheet_area,
                    'vinyl_area': master.vinyl_area,
                    'ec_flim_area': master.flim_area,
                    'screen_print_area': master.screen_print_area,
                    'process_area': master.processing_area,
                })

    #                                                                                                                  Sign Reflective Sheet
    reflective_color : fields.Many2many = fields.Many2many(
        'product.attribute.value',
        relation='quotation_estimate_reflective_color_rel',
        column1='estimate_id',
        column2='attribute_value_id',
        string='Color',
        domain="[('attribute_id.name', '=', 'Color')]",
        store=True
    )
    reflective_make : fields.Many2one = fields.Many2one("product.attribute.value", string="Color", domain="[('id', 'in', reflective_color)]")
    reflective_area = fields.Float(string="Area")
    reflective_wastage = fields.Float(string="Wastage")
    reflactive_rate = fields.Float(string="Rate")
    reflective_amount = fields.Float(string="Amount")

    # Vinyl Cost
    vinyl_type : fields.Many2one = fields.Many2one('product.category', string="Type")
    vinyl_color : fields.Many2one = fields.Many2one('product.attribute.value', string="Color")
    vinyl_make : fields.Many2one = fields.Many2one('product.attribute.value', string='Make')
    vinyl_area = fields.Float(string="Area")
    vinyl_rate = fields.Float(string="Rate(m2)")
    vinyl_amt = fields.Float(string="Amt")

    # EC Flim Cost
    ec_flim_type : fields.Many2one = fields.Many2one('product.category', string="Type")
    ec_flim_color : fields.Many2one = fields.Many2one('product.attribute.value', string="Color")
    ec_flim_make : fields.Many2one = fields.Many2one('product.attribute.value', string='Make')
    ec_flim_area = fields.Float(string="Area")
    ec_flim_rate = fields.Float(string="Rate(m2)")
    ec_flim_amt = fields.Float(string="Amt")

    # Reflective Cost
    ref_cost_type : fields.Many2one = fields.Many2one('product.category', string="Type")
    ref_cost_color : fields.Many2one = fields.Many2one('product.attribute.value', string="Color")
    ref_cost_make : fields.Many2one = fields.Many2one('product.attribute.value', string='Make')
    ref_cost_area = fields.Float(string="Area")
    ref_cost_rate = fields.Float(string="Rate(m2)")
    ref_cost_amt = fields.Float(string="Amt")

    # Screen Print
    screen_print_type : fields.Many2one = fields.Many2one('product.category', string="Type")
    screen_print_color : fields.Many2one = fields.Many2one('product.attribute.value', string="Color")
    screen_print_make : fields.Many2one = fields.Many2one('product.attribute.value', string='Make')
    screen_print_area = fields.Float(string="Area")
    screen_print_rate = fields.Float(string="Rate(m2)")
    screen_print_amt = fields.Float(string="Amt")

    # Process
    process_type : fields.Many2one = fields.Many2one('product.category', string="Type")
    process_color : fields.Many2one = fields.Many2one('product.attribute.value', string="Color")
    process_make : fields.Many2one = fields.Many2one('product.attribute.value', string='Make')
    process_area = fields.Float(string="Area")
    process_rate = fields.Float(string="Rate(m2)")
    process_amt = fields.Float(string="Amt")

    # Sign Total
    sign_sub_total = fields.Float(string="Sub Total")
    sign_oh_percent = fields.Float(string="OH %")
    sign_profit_percent = fields.Float(string="Profit %")
    sign_net_amount = fields.Float(string="Net Amt")

    #                                                               Frame Fields
    # Material Spec
    frame_material : fields.Many2one = fields.Many2one("product.template", string="Material")
    material_side_1 = fields.Float(string="Side-1 (mm)")
    material_side_2 = fields.Float(string="Side-2 (mm)")
    material_thick = fields.Float(string="Thick (mm)")
    material_rate = fields.Float(string="Rate (Kgs)")

    # Frame Size
    frame_size_len = fields.Float(string="Size L(m)")
    frame_size_width = fields.Float(string="Size W(m)")
    frame_cross_v = fields.Float(string="Cross V(nos)")
    frame_cross_h = fields.Float(string="Cross H(nos)")
    frame_total_length = fields.Float(string="Total")
    frame_weight = fields.Float(string="Weight(Kg)")
    frame_wastage = fields.Float(string="Wastage-%")
    frame_total_weight = fields.Float(string="Total")

    # Frame Accessories
    frame_items_ids : fields.One2many = fields.One2many('frame.accessories', 'estimate_id', string='Frame Accessories')

    # Frame Material
    frame_material_area = fields.Float(string="Area/Kgs")
    frame_material_rate = fields.Float(string='Rate(m2)')
    frame_material_amt = fields.Float(string="Amt")

    # Frame Labour
    frame_labour_area = fields.Float(string="Area/Kgs")
    frame_labour_rate = fields.Float(string='Rate(m2)')
    frame_labour_amt = fields.Float(string="Amt")

    # Frame Paint
    frame_paint_area = fields.Float(string="Area/Kgs")
    frame_paint_rate = fields.Float(string='Rate(m2)')
    frame_paint_amt = fields.Float(string="Amt")

    # Frame Drilling
    frame_drilling_area = fields.Float(string="Area/Kgs")
    frame_drilling_rate = fields.Float(string='Rate(m2)')
    frame_drilling_amt = fields.Float(string="Amt")

    # Frame Total
    frame_sub_total = fields.Float(string="Sub Total")
    frame_oh_percent = fields.Float(string="OH %")
    frame_profit_percent = fields.Float(string="Profit %")
    frame_total_amount = fields.Float(string="Net Amt")

    #                                                                           Post
    #       Post Material Spec
    post_material : fields.Many2one = fields.Many2one('product.template', string="Material")
    post_material_size = fields.Char(string="Size")

    #   Post Details
    post_length = fields.Float(string="L")
    post_qty = fields.Integer(string="Nos")
    post_weight  = fields.Float(string="Kg/m")
    post_area = fields.Float(string="m2/m")

    post_weight_area = fields.Float(string='Post Wgt/area')
    post_rate = fields.Float(string="Post Rate (Kgs)")
    post_amt = fields.Float(string="Post Amt")

    fabrication_amt = fields.Float(string="Fabrication Amt")

    paint_weight_area = fields.Float(string='Paint Wgt/area')
    paint_rate = fields.Float(string="Paint Rate (Kgs)")
    paint_amt = fields.Float(string="Paint Amt")

    transport_weight_area = fields.Float(string='Transport Wgt/area')
    transport_rate = fields.Float(string="Transport Rate (Kgs)")
    transport_amt = fields.Float(string="Transport Amt")

    post_sub_total = fields.Float(string="Sub Total")
    post_oh_percent = fields.Float(string="OH %")
    post_profit_percent = fields.Float(string="Profit %")
    post_total_amount = fields.Float(string="Net Amt")

class FrameAccessoriesModel(models.Model):
    _name = "frame.accessories"

    frame_items : fields.Many2one = fields.Many2one("product.template",string="Items")
    estimate_id : fields.Many2one = fields.Many2one('quotation.estimate', string="Quotation Estimate")
    frame_item_qty = fields.Float(string="Nos")
    frame_item_rate = fields.Float(string="Rate")
    frame_item_amt = fields.Float(string="Amt")
    frame_items_total = fields.Float(string="Total")
