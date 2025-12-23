from odoo import models, fields,api
from odoo.exceptions import ValidationError


class CustomModel(models.Model):
    _name = 'custom.model'
    _description = 'Custom Model Description'

    name = fields.Char(string='Name', required=True)
    phone=fields.Char(string='Phone',groups='custom_module.group_custom_event_user') 
    email = fields.Char(string='Email')
    age = fields.Integer(string='Age')
    active = fields.Boolean(string='Active', default=True)
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection(
    [('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
    string='Gender')
    reference = fields.Many2one('res.partner', string='Reference')
    address = fields.Text(string='Address')
    resume = fields.Binary(string='Resume')
    profile = fields.Image(string='Profile', max_width=800, max_height=800)
    fees = fields.Float(string='Fees')
    joinDate = fields.Datetime(string='JoinDate')
    is_active = fields.Boolean(string='Active', default=True)
    totalcost = fields.Monetary(string='Cost', currency_field="currency_id")
    currency_id = fields.Many2one('res.currency', string='Currency')
    description = fields.Html(string='Description')
    busfees=fields.Float(string='Bus Fees')
    totalfees=fields.Float(string="Total Fees",compute='_compute_my_field')
    grand_total=fields.Float(string="Grand Total",compute='_compute_grand_total')
    custom_model_related_ids = fields.One2many('custom.model.related', 'custom_model_id', string="Related Records")
    serial_number = fields.Char(string="Serial Number", readonly=True)
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['serial_number'] = self.env['ir.sequence'].next_by_code('custom.model')
        res = super(CustomModel, self).create(vals_list)
        return res
    def _compute_grand_total(self):
        for rec in self:
            rec.grand_total=sum(rec.custom_model_related_ids.mapped('total'))
    payment_status = fields.Selection([
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    ], string="Payment Status", default='unpaid')
    def action_test_method(self):
        partner_list=[]
        partners=self.env['res.partner'].search([])
        for part in partners:
            partner_list.append(part.name)
        raise ValidationError(partner_list)
    @api.model
    def send_mail(self):
        for model in self:
            template = self.env['mail.template'].browse(self.env.ref('custom_module.mail_template_sale_order').id)
            template.send_mail(model.id, force_send=True)
    def write(self, vals):
        
        
        if 'name' in vals:
            raise ValidationError("You are not allowed to change the name.")

        return super(CustomModel, self).write(vals)
    

    def unlink(self):
        for rec in self:
            if rec.name == "fero":
                raise ValidationError("Cannot delete this record.")
        return super(CustomModel, self).unlink()
    def open_wizard(self):
   
        return {'type': 'ir.actions.act_window',
           'name':'Custom Wizard',
           'res_model': 'custom.wizard',
           'target': 'new',
           'context': {
                'default_name': self.name,
                'default_custom_model_id': self.id,
            },
           'view_mode': 'form',
           'view_type': 'form',
           }
    @api.onchange('age')
    def change_age(self):
        if self.age and self.age <= 18:
            raise ValidationError("Age should be greater than 18")
    @api.constrains('fees')
    def _check_price_quantity(self):
        for record in self:
            if record.fees < 0 :
                raise ValidationError("Fees  must be positive.") 
    @api.model
    def my_model_method(self): 
        return "This model api method can be called without records"   
    
    def call_test(self):
        result = self.my_model_method()
        return {
        'effect': {
            'fadeout': 'slow',
            'message': result,
            'type': 'rainbow_man',
        }
    }
    @api.depends('busfees','fees')
    def _compute_my_field(self):
        for record in self:
            record.totalfees = record.busfees + record.fees
    @api.returns('self')
    def copy(self, default=None):
        default = dict(default or {})
        default['name'] = "Copy of " + (self.name or "")
        return super(CustomModel, self).copy(default)
class CustomModelRelated(models.Model):
    _name = 'custom.model.related'
    _description = 'Custom Model Related Description'

    custom_model_id = fields.Many2one('custom.model', string="Custom Model")
    product = fields.Many2one('product.template', string='Product')
    purchase_date = fields.Date(string="Date")
    quantity = fields.Integer(string="Quantity",default=1)
    
    detail = fields.Char(string="Detail")
    price = fields.Float(string="Price")
    total = fields.Float(string="Total", compute='_compute_total_amount') 
    @api. onchange('product')
    def _onchange_product(self):
        if self.product:
            self.price = self.product.list_price
    @api.depends('price','quantity')
    def _compute_total_amount(self):
        for record in self:
            record.total = (record.price or 0) * (record.quantity or 0)
            serial_number = fields.Char(string="Serial Number", readonly=True)
    
