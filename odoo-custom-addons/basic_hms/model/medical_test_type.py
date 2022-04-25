# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
# classes under cofigration menu of laboratry 

class medical_test_type(models.Model):

    _name  = 'medical.test_type'

    name = fields.Char('Name', required = True)
    code  =  fields.Char('Code' , required = True)
    critearea_ids = fields.One2many('medical_test.critearea', 'test_id','Critearea')
    service_product_id = fields.Many2one('product.product','Service' , required = True)
    info  = fields.Text('Extra Information')
