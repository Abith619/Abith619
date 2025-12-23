from odoo import models, fields, api
from odoo.exceptions import ValidationError,UserError
class Student(models.Model):
    _name = "student.demo"
    _description = "Student Demo"

    first_name = fields.Char("First Name")
    last_name = fields.Char("Last Name")
    country = fields.Selection([
        ('india', 'India'),
        ('usa', 'USA'),
    ], string="Country")
    phone_code = fields.Char("Phone Code")
    age = fields.Integer("Age")

    full_name = fields.Char("Full Name", compute="compute_full_name")

    # -----------------------------------
    # @api.depends
    # -----------------------------------
    @api.depends('first_name', 'last_name')
    def compute_full_name(self):
        for record in self:
            record.full_name = f"{record.first_name or ''} {record.last_name or ''}"

    # -----------------------------------
    # @api.onchange
    # -----------------------------------
    @api.onchange('country')
    def set_phone_code(self):
        if self.country == 'india':
            self.phone_code = "+91"
        elif self.country == 'usa':
            self.phone_code = "+1"
        else:
            self.phone_code = ""

    # -----------------------------------
    # @api.constrains
    # -----------------------------------
    @api.constrains('age')
    def validate_age(self):
        if self.age and self.age < 5:
            raise ValidationError("Age must be 5 or above!")

    # -----------------------------------
    # @api.model
    # -----------------------------------
    @api.model
    def welcome_message(self):
        message = "Welcome to Student System!"
        print("🔥 Terminal Output:", message)  # This prints in terminal
        return message

    def action_show_welcome(self):
        msg = self.welcome_message()
        raise UserError(msg)   # This shows popup
