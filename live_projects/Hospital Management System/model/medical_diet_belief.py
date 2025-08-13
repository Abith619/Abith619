# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_diet_belief(models.Model):
    _name = 'medical.diet.belief'

    code = fields.Char(string='Code',required=True)
    description = fields.Text(string='Description',required=True)
    name = fields.Char(string='Belief')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
