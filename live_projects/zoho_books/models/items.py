from odoo import models,fields

class Items(models.Model):
	_inherit = 'product.template'

	zoho_id = fields.Char("Zoho ID")
	is_zoho = fields.Boolean("Zoho ?")