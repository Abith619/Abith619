from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrderInheritCustom(models.Model):
    _inherit = 'sale.order'

    sales_person : fields.Many2one = fields.Many2one('sales.person.custom', string='Sales Person')

class ProductTemplateInheritCustom(models.Model):
    _inherit = 'product.template'

    imprint_color = fields.Char(string='Imprint color')
    imprint_line = fields.Char(string='Imprint line')
    personalization = fields.Char(string='Personalization')
    includes = fields.Text(string='Includes')
    size = fields.Html(string='Graphic Size')
    booth_des = fields.Char(string='Booth Description')
    material = fields.Text(string='Material')

class SalesPersonCustom(models.Model):
    _name = 'sales.person.custom'
    _description = 'Sales Persons'

    name = fields.Char(string='Name')
    contact_details : fields.Many2one = fields.Many2one('res.partner', string='Contact Details')