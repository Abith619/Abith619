from odoo import models, fields, api

class ProductManufacturerInfo(models.Model):
    _name = 'product.manufacturer.info'
    _description = 'Product Manufacturer Information'
    _rec_name = 'part_number'

    product_tmpl_id = fields.Many2one('product.template', string='Product', index=True, ondelete='cascade')
    manufacturer_id = fields.Many2one('product.manufacturer', string='Manufacturer')
    part_number = fields.Char(string='Part Number')

    @api.onchange('manufacturer_id')
    def _onchange_manufacturer_id(self):
        if self.manufacturer_id and self.manufacturer_id.part_number:
            self.part_number = self.manufacturer_id.part_number.part_number
        else:
            self.part_number = False

class ProductManufacturer(models.Model):
    _name = 'product.manufacturer'
    _description = 'Product Manufacturer'
    _rec_name = 'manufacturer'

    manufacturer = fields.Char(string='Manufacturer')
    product_tmpl_id = fields.Many2one('product.template', string='Product', index=True, ondelete='cascade')
    part_number = fields.Many2one('product.manufacturer.info', string='Part Number')

class ProductTemplate(models.Model):
    _inherit = "product.template"

    tolerance_percent = fields.Float(
        string="Tolerance (%)",
        help="Allowed deviation from demanded quantity. E.g. 10 = ±10%.",
    )
    
    manufacturer_line_ids = fields.One2many(
        'product.manufacturer.info', 'product_tmpl_id', string='Manufacturers'
    )

    approval_state = fields.Selection([ 
        ('draft', 'Draft'), 
        ('submitted', 'Submitted for Approval'), 
        ('approved', 'Approved'), 
        ('rejected', 'Rejected') ], default='draft', string='Approval State') 
    
    def action_submit(self): 
        self.write({
                'approval_state': 'submitted', 
                'active': False 
        }) 
    
    def action_approve(self): 
        self.write({
             'approval_state': 'approved', 
             'active': True 
        }) 
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['active'] = False
            vals['approval_state'] = 'draft'
        return super().create(vals_list)
    
    def action_reject(self): 
        self.write({
             'approval_state': 'rejected', 
             'active': False 
        })

class ProductSupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'

    min_qty = fields.Float(string="Minimum Quantity", default=1.0)


