# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class pet_type(models.Model):
    _name = 'pet.type'

    name = fields.Char('Name', required = True)
    code = fields.Char('Code')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: