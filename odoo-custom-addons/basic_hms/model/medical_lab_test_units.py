# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
# classes under cofigration menu of laboratry 

class medical_lab_test_units(models.Model):

    _name = 'medical.lab.test.units'
    
    name = fields.Char('Name', required = True)
    test = fields.Many2one('medical.test_type',string="Test")
    code  =  fields.Float('Price')
    test_line= fields.One2many('lab_test.lines','test',string='Test Lines')
    units = fields.Many2one('test.units',string="Units")
    normal_range= fields.Float(string="Normal Range")


class Units_range(models.Model):
    _name='lab_test.lines'

    test=fields.Many2one('medical.lab.test.units')
    normal_range= fields.Float(string="Normal Range")
    unit = fields.Many2one('test.units',string="Units")



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:    
