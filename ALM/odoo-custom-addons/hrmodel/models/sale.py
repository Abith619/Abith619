# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import date
import re
from dateutil.relativedelta import relativedelta
from datetime import datetime, date, timedelta
from odoo import models, fields, api, _
from odoo.exceptions import Warning, UserError
import pytz




class mys_customize_template_for_sale(models.Model):
     _inherit = 'sale.order.line'

    # gstinno = fields.Integer(string='GSTIN No')

     product_uom_qty = fields.Integer(string='Ordered Quantity',required=True)
