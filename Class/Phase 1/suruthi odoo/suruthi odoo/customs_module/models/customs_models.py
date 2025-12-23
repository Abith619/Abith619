from odoo import models, fields,api
from odoo.exceptions import ValidationError

class CustomsModels(models.Model):
    _name = 'customs.models'
    _description = 'Customs Model Description'

    name = fields.Char(string="Name", required=True)
    contact = fields.Many2one('res.partner', string="Contact")
    phone = fields.Char(string="Phone Number")
    age = fields.Integer(string="Age")
    email = fields.Char(string="Email")
    date = fields.Date(string="Date")

    payment_status = fields.Selection([
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    ], string="Payment Status", default='unpaid')

    custom_related_ids = fields.One2many(
    'customs.related',
    'custom_id',
    string="Related Records")

    grand_total = fields.Float(string="Grand Total", compute="_compute_grand_total")

    serial_number = fields.Char(string="Serial Number", readonly=True)

    @api.model
    def send_mail(self):
        for model in self.search([]):
            template = self.env['mail.template'].browse(
                self.env.ref('custom_module.mail_template_sale_order').id
            )
            template.send_mail(model.id, force_send=True)


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['serial_number'] = self.env['ir.sequence'].next_by_code('customs.models')
        return super(CustomsModels, self).create(vals_list)

    @api.depends('custom_related_ids.total')
    def _compute_grand_total(self):
        for rec in self:
            rec.grand_total = sum(rec.custom_related_ids.mapped('total'))


    # 1️⃣ SEARCH - Show all Partner Names
    def action_test_method(self):
        partner_list = []
        partners = self.env['res.partner'].search([])
        for partner in partners:
            partner_list.append(partner.name)
        raise ValidationError(partner_list)

    # 2️⃣ BROWSE - Open ID 5
    def action_browse_record(self):
        partner = self.env['res.partner'].browse(5)
        if partner:
            raise ValidationError("Browsed Partner: " + partner.name)
        else:
            raise ValidationError("No record found for ID 5")

    # 3️⃣ CREATE - Create a New Partner
    def action_create_record(self):
        new_partner = self.env['res.partner'].create({
            'name': 'New Partner Created',
            'email': 'newpartner@gmail.com',
        })
        raise ValidationError("Created Partner: " + new_partner.name)

    # 4️⃣ DELETE - Unlink
    def action_unlink_record(self):
        partner = self.env['res.partner'].search([('name', '=', 'New Partner Created')], limit=1)
        if partner:
            partner.unlink()
            raise ValidationError("Deleted Successfully")
        else:
            raise ValidationError("No matching record to delete")

    # 5️⃣ COPY - Duplicate a record
    def action_copy_record(self):
        partner = self.env['res.partner'].search([], limit=1)
        if partner:
            partner.copy()
            raise ValidationError("Record Copied: " + partner.name)
        else:
            raise ValidationError("No record available to copy")
        

class CustomsRelated(models.Model):
    _name = 'customs.related'
    _description = 'Custom Related description'

    custom_id = fields.Many2one('customs.models', string="Custom Record")

    
    serial_number = fields.Char(string="Serial Number", readonly=True)

    name = fields.Char(string="Name")
    purchase_date = fields.Date(string="Date")
    quantity = fields.Integer(string="Quantity")
    price = fields.Float(string="Price")
    total = fields.Float (string="Total",compute="_compute_total", store=True)

    @api.depends('quantity', 'price')
    def _compute_total(self):
        for rec in self:
            rec.total = (rec.quantity or 0) * (rec.price or 0)

    
        


