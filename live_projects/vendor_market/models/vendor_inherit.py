from odoo import models, fields

class ProductTemplateVendorInherit(models.Model):
    _inherit = 'product.template'

    vendor_ids : fields.Many2one = fields.Many2one('res.partner', string='Vendors')

# class VendporUserInherit(models.Model):
#     _inherit = 'res.users'

#     is_vendor = fields.Boolean(string='Is Vendor', default=False)
