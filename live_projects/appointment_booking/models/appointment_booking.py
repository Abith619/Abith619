from odoo import models, fields

class AppointmentBooking(models.Model):
    _name = "appointment.booking"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Website Appointment Booking"

    name = fields.Char("Customer Name", required=True)
    email = fields.Char("Email")
    phone = fields.Char("Phone")
    service = fields.Selection([
        ('erp', 'ERP'),
        ('manufacturing', 'Manufacturing'),
        ('healthcare', 'HealthCare'),
    ], required=True)
    date = fields.Date("Appointment Date", required=True, tracking=True)
    slot = fields.Char("Timeslot", required=True, tracking=True)
    notes = fields.Text("Notes")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string="Status", default="draft")
