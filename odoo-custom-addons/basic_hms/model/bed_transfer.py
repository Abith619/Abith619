# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date

class bed_transfer(models.Model):
    _name = 'bed.transfer'

    name = fields.Char("Name")
    date = fields.Datetime(string='Date')
    bed_from = fields.Char(string='From')
    bed_to = fields.Char(string='To')
    reason = fields.Text(string='Reason')
    inpatient_id = fields.Many2one('medical.inpatient.registration',string='Inpatient Id')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
