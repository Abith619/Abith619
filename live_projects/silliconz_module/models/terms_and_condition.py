from odoo import models, fields
class TermsAndCondition(models.Model):
    _name = 'terms.and.condition'
    _description = 'Terms and Conditions'

    name = fields.Char(string="name", required=True)
    content = fields.Text(string="Description", required=True)
    type = fields.Selection([
        ('quotation', 'Quotation'),
        ('purchase', 'Purchase'),
        ('delivery', 'Delivery'),
        ('invoice', 'Invoice'),
        ('general', 'General'),], string="Type", default='general', required=True)
    active = fields.Boolean(default=True)
