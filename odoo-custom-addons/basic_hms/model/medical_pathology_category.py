# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_pathology_category(models.Model):
    _name = 'medical.pathology.category'
    
    name = fields.Char(string="Category Name",required=True)
    active = fields.Boolean(string="Active" , default = True)
    parent_id = fields.Many2one('medical.pathology.category', string="Parent Category")

