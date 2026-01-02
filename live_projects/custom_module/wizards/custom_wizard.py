from odoo import models, fields
from odoo.exceptions import ValidationError
from datetime import date

class CustomWizard(models.TransientModel):
    _name = 'custom.wizard'
    _description = "Custom Wizard"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')

    custom_model_id = fields.Many2one('custom.model', string='Related Custom Model')

    payment = fields.Boolean(string='Payment')

    def action_save(self):
        # related_model = self.custom_model_id

        related_orm = self.env['custom.model'].search([('name', '=', self.name)])
        related_orm.payment_status = 'paid' if self.payment else 'unpaid'

        self.env['custom.model'].create({
            'name': 'Test from Wizard',
            'age': 30,
            'email': 'test@odoo.com',
            'contact': self.env['res.partner'].search([], limit=1).id,
            'payment_status': 'paid' if self.payment else 'unpaid',
            'date': date.today(),
        })