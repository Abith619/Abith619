from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CustomModel(models.Model):
    _name = 'custom.model'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Custom Model Description'

    name = fields.Char(string="Name", required=True)
    contact = fields.Many2one('res.partner', string="Contact", required=True)
    phone = fields.Char(string="Phone Number", groups="custom_module.group_custom_event_user")
    age = fields.Integer(string="Age")
    email = fields.Char(string="Email")
    date = fields.Date(string="Date")

    user_id = fields.Many2one('res.users', string="Responsible", default=lambda self: self.env.user)

    serial_number = fields.Char(string="Serial Number", readonly=True)

    grand_total = fields.Float(string="Grand Total", compute="_compute_grand_total")

    def _compute_grand_total(self):
        for rec in self:
            rec.grand_total = sum(rec.custom_model_related_ids.mapped('total'))

    currency_id : fields.Many2one = fields.Many2one(
        comodel_name='res.currency',
        default=lambda self: self.env.company.currency_id,
    )

    custom_model_related_ids = fields.One2many('custom.model.related', 'custom_model_id', string="Related Records")

    payment_status = fields.Selection([
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    ], string="Payment Status", default='unpaid')

    @api.model
    def send_mail(self):
        for model in self:
            template = self.env['mail.template'].browse(self.env.ref('custom_module.mail_template_sale_order').id)
            template.send_mail(model.id, force_send=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['serial_number'] = self.env['ir.sequence'].next_by_code('custom.model')
        res = super(CustomModel, self).create(vals_list)
        return res

    def open_wizard(self):
        return {
            'name': 'Custom Wizard',
            'type': 'ir.actions.act_window',
            'res_model': 'custom.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_name': self.name,
                'default_custom_model_id': self.id,
            },
        }

    def action_test_method(self):
        partner_list = []
        partners = self.env['res.partner'].search([])
        for partner in partners:
            partner_list.append(partner.name)
        raise ValidationError(partner_list)


class CustomModelRelated(models.Model):
    _name = 'custom.model.related'
    _description = 'Custom Model Related Description'

    custom_model_id = fields.Many2one('custom.model', string="Custom Model")
    name = fields.Char(string="Name")
    purchase_date = fields.Date(string="Date")
    quantity = fields.Integer(string="Quantity")
    price = fields.Float(string="Price")
    total = fields.Float(string="Total")
    detail = fields.Char(string="Detail")

    # total_amount = fields.Float(string="Total Amount", compute='_compute_total_amount')