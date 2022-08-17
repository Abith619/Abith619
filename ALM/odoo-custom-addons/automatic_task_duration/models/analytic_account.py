# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')
