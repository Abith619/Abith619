# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_dose_unit(models.Model):
    _name = 'medical.dose.unit'

    name = fields.Char(string="Unit",required=True)
    description = fields.Char(string="Description")

