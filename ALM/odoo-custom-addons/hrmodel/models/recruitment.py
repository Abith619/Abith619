# -*- coding: utf-8 -*-


from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import date
import re
from dateutil.relativedelta import relativedelta






class ProductProduct(models.Model):
    _inherit = 'hr.applicant'




    #howdoyou = fields.Text(string='How do you came to know us? ')

    interested = fields.Text(string='Interested Roles& Responsibilities')

    relocate = fields.Selection([('yes', 'Yes'), ('no', 'No')],string="Relocate")

    status = fields.Selection([('Single', 'Single'), ('married ', 'Married ')],string="Status")

    reason = fields.Text(string='Reason For Change From current Job')    

    loaction = fields.Text(string='Location')   

    background = fields.Text(string='Family BackGround')   

    nativa = fields.Char(string='Native') 

    date = fields.Datetime(string='Creating Date', required=False , readonly=False, select=True )   

    relieving = fields.Char(string='Relieving Period')   

    appointment_lines = fields.One2many('transports.item.hrlines', 'test_line_appointment', string="languages")
class newtest(models.Model):
    _name = 'transports.item.hrlines'


    types = fields.Selection([('English ', 'English '), ('Tamil ', 'Tamil '), ('Hindi', 'Hindi'), ('Telugu ', 'Telugu '), ('Malayalam', 'Malayalam'), ('Kannada', 'Kannada'), ('Marathi', 'Marathi'), ('French', 'French'), ('Sanskrit', 'Sanskrit'), ('Urdu', 'Urdu'),  ('Bengali', 'Bengali')],string="Languages")	
    test_line_appointment = fields.Many2one('hr.applicant', string="Name of Consignment")

    delivery_orders = fields.Selection([('fluency', 'Fluency'), ('medium', 'Medium'), ('poor', 'Poor')],string="Write")

    dtimess = fields.Selection([('fluency', 'Fluency'), ('medium', 'Medium'), ('poor', 'Poor')],string="Read"
                           )

    times = fields.Selection([('fluency', 'Fluency'), ('medium', 'Medium'), ('poor', 'Poor')],string="Speak")
