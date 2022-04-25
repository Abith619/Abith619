from odoo import fields, models

#       Inherit Contacts to add a Field in contacts
class inheritance(models.Model):
    _inherit='res.partner'
    demo = fields.Char(string="Demo")

#       Inherit Sales Module to add a Field in Sales
class inherit_sale(models.Model):
    _inherit="sale.order"
    value = fields.Char(string="sale")

#       Inherit Sales Module to add a Field in Sales.order_line
class inherit_line(models.Model):
    _inherit="sale.order.line"
    sale_line=fields.Char(string='Line')
