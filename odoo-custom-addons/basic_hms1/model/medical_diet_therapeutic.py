# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_diet_therapeutic(models.Model):
    _name = 'medical.diet.therapeutic'

    name = fields.Char(string='Diet Type',required=True)
    code = fields.Char(string='Code',required=True)
    description = fields.Text(string='Description',required=True)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
