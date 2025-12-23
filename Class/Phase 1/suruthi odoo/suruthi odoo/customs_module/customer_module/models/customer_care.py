from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class CustomerCare(models.Model):
    _name = 'customer.care'
    _description = 'Customer Care'

    # BASIC DETAILS
    customer_name = fields.Char("Customer Name", required=True)
    email = fields.Char("Email")
    phone = fields.Char(string="Phone Number")
    contact = fields.Many2one('res.partner', string="Contact", required=True)

    # ISSUE DETAILS
    issue = fields.Char("Issue Title")
    description = fields.Text("Issue Description")

    # STATUS & PRIORITY
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('waiting', 'Waiting for Customer'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ], string="Status", default='new')

    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent')
    ], string="Priority", default='medium')

    # ONE2MANY RELATED TABLE
    custom_model_related_ids = fields.One2many(
        'custom.model.related', 
        'custom_model_id', 
        string="Related Records"
    )

    # DATES
    created_date = fields.Date("Created Date", default=fields.Date.today())
    resolved_date = fields.Date("Resolved Date")
    follow_up_date = fields.Date("Follow UP Date")

    # ASSIGNED PERSON
    assigned_to = fields.Many2one('res.users', string="Assigned To")

    # ATTACHMENT
    attachment = fields.Binary("Attachment")

    # CUSTOMER RATING
    customer_rating = fields.Selection([
        ('1', '⭐'),
        ('2', '⭐⭐'),
        ('3', '⭐⭐⭐'),
        ('4', '⭐⭐⭐⭐'),
        ('5', '⭐⭐⭐⭐⭐'),
    ], string="Customer Rating")


class CustomModelRelated(models.Model):
    _name = 'custom.model.related'
    _description = 'Custom Model Related Description'

    custom_model_id = fields.Many2one('customer.care', string="Custom Model")
    name = fields.Char(string="Name")
    purchase_date = fields.Date(string="Date")
    quantity = fields.Integer(string="Quantity", default=1)
    price = fields.Float(string="Price")
    total = fields.Float(string="Total", compute="_compute_total", store=True)
    detail = fields.Char(string="Detail")

    @api.depends('quantity', 'price')
    def _compute_total(self):
        for rec in self:
            rec.total = (rec.quantity or 0) * (rec.price or 0)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['name'] = self.env['ir.sequence'].next_by_code('customer.care')
        res = super(CustomerCare,self).create(vals_list)
        return res