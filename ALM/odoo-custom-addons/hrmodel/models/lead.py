# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import date
import re
from dateutil.relativedelta import relativedelta

class my_customize_template_for_sale(models.Model):
     _inherit = 'crm.lead'

    # gstinno = fields.Integer(string='GSTIN No')

     mylead = fields.Selection([('ringingnoresponse', 'Ringing No Response'), ('callback', 'Call Back'), ('Interestedcouldbeanopp', 'Interested-Could be an Opportunity'),('numberdoesnot', 'Number Does Not Exist'),('Wrongnumber', 'Wrong Number'),('notinterseted', 'Not Interested '),('requirementnot', 'Requirement Not In Our  Scope '),('donotcall', 'Do Not call'),]  , string='Lead Status')
