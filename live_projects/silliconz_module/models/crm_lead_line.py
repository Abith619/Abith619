from odoo import models, fields

class CrmLeadLine(models.Model):
    _name = 'crm.lead.line'
    _description = 'CRM Product Line'
    lead_id = fields.Many2one('crm.lead',string="Lead",ondelete='cascade')
    product_id = fields.Many2one('product.product',string="Product",required=True)
    quantity = fields.Float(string="Quantity",default=1.0)
    description = fields.Char(string="Description", related='product_id.name')
    uom_id = fields.Many2one("uom.uom",string="UoM", related='product_id.uom_id')

        

