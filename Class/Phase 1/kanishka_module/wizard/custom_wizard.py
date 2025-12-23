from odoo import fields, models
from datetime import date

class CustomWizard(models.TransientModel):
    _name='custom.wizard'

    name=fields.Char(string="Name",required=True)
    description=fields.Char(string="Description")
    custom_model_id = fields.Many2one('custom.model', string='Related Custom Model')
    payment = fields.Boolean(string='Payment')

    def save(self):
     related_model = self.custom_model_id
     related_model.payment_status = 'paid' if self.payment else 'unpaid'
     self.env['custom.model'].create({
            'name': 'New record',
            'age': 30,
            'email': 'test@odoo.com',
            'reference': self.env['res.partner'].search([], limit=1).id,
            'payment_status': 'paid' if self.payment else 'unpaid',
            'joinDate': date.today(),
        })