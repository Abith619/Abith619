from odoo import models, fields,api

from odoo.exceptions import ValidationError

class CustomModel(models.Model):
    _name = 'custom.model'
    _description = 'Custom Model Description'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    reference = fields.Many2one('res.partner', string='Reference')
    phone = fields.Char(string='Phone',groups='custom_module.group_custom_event_user')
    dob = fields.Date(string='DOB')
    gender = fields.Selection([('female','Female'),('male','Male')], string='Gender')
    address = fields.Text(string='Address')
    resume = fields.Binary(string='Resume')
    profile = fields.Image(string='Profile', max_width=800, max_height=800)  # optional
    age = fields.Integer(string='Age')
    fees = fields.Float(string='Fees')
    busfees=fields.Float(string='Bus Fees')
    joinDate = fields.Datetime(string='JoinDate')
    is_active = fields.Boolean(string='Active', default=True)

    totalfees=fields.Float(string="Total Fees",compute='_compute_my_field')

    custom_model_related_ids = fields.One2many('custom.model.related', 'custom_model_id', string="Related Records")
    grand_total=fields.Float(string="Grand Total",compute='_compute_grand_total')

    def _compute_grand_total(self):
        for rec in self:
            rec.grand_total=sum(rec.custom_model_related_ids.mapped('total'))

    currency_id : fields.Many2one = fields.Many2one(
        comodel_name='res.currency',
        default=lambda self: self.env.company.currency_id,
    )

    serial_number = fields.Char(string="Serial Number", readonly=True)

   
    
    description = fields.Html(string='Description')
    payment_status = fields.Selection([
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    ], string="Payment Status", default='unpaid')
    

  

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
    
    @api.model
    def send_mail(self):
        for model in self:
            template = self.env['mail.template'].browse(self.env.ref('custom_module.mail_template_sale_order').id)
            template.send_mail(model.id, force_send=True)

            
    def action_test_method(self):
        partner_list=[]
        partners=self.env['res.partner'].search([])
        # print(self)  #custom.model(1,)   here 1 is the id of current record
        for part in partners:
            partner_list.append(part.name)
        raise ValidationError("\n".join(partner_list))
        
    
    @api.onchange('age')
    def change_age(self):
        # print("onchange:",self)  #onchange custom.model(<NewId origin=2>,)  here 2 is the id of current record
        if self.age and self.age <= 18:
            raise ValidationError("Age should be greater than 18")
        

    @api.constrains('fees', 'busfees')
    def _check_price_quantity(self):
        for record in self:
            if record.fees < 0 or record.busfees < 0:
                raise ValidationError("Fees and Busfees must be positive.")
            
    #this vals contains dictionary with newly created record
    # @api.model
    # def create(self,vals):
    #     return super().create(vals) 



    # @api.model
    # def my_model_method(self): 
    #     return  "This model records"  
    
    def call_test(self):
       
        return {
        'effect': {
            'fadeout': 'slow',
            'message': "This model records",
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
    
    def create_multiple_records(self):  #button in custom_views
        vals_list = [
        {'name': 'Alice', 'email': 'alice@example.com', 'fees': 1000, 'busfees': 200},
        {'name': 'Bob', 'email': 'bob@example.com', 'fees': 1200, 'busfees': 300},
    ]
    # This calls your model_create_multi method
        records = self.env['custom.model'].create(vals_list)
        return records
    
    
    def write(self, vals):
        
        # print("write:    ",self,"vals:    ",vals)   #write:     custom.model(48,) vals:     {'name': 'AL'}  thereis ALICE ,i updated to AL.
        # Example: Prevent name change
        if 'name' in vals:
            raise ValidationError("You are not allowed to change the name.")

        return super(CustomModel, self).write(vals)
    

    def unlink(self):
        for rec in self:
            if rec.name == "Finly":
                raise ValidationError("Cannot delete this record.")
        return super(CustomModel, self).unlink()

    @api.model_create_multi
    def create(self, vals_list):
        
        for vals in vals_list:
            if 'name' in vals:
                vals['name'] = vals['name'].upper()  
        records = super(CustomModel, self).create(vals_list)
        return records
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['serial_number'] = self.env['ir.sequence'].next_by_code('custom.model')
        res = super(CustomModel, self).create(vals_list)
        return res
    
class CustomModelRelated(models.Model):
    _name = 'custom.model.related'
    _description = 'Custom Model Related Description'

    custom_model_id = fields.Many2one('custom.model', string="Custom Model")
    product = fields.Many2one('product.template', string='Product')
    purchase_date = fields.Date(string="Date")
    quantity = fields.Integer(string="Quantity",default=1)
    
    detail = fields.Char(string="Detail")

    @api.onchange('product')
    def _onchange_product(self):
        if self.product:
            self.price = self.product.list_price

    price = fields.Float(string="Price")
    total = fields.Float(string="Total", compute='_compute_total_amount')

    @api.depends('price','quantity')
    def _compute_total_amount(self):
        for record in self:
            record.total = (record.price or 0) * (record.quantity or 0)

   
    

    
    


  
   
    
    
        
    

