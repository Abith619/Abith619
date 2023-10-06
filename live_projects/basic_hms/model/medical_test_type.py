# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
# classes under cofigration menu of laboratry 

class medical_test_type(models.Model):

    _name  = 'medical.test_type'

    name = fields.Char('Name', required = True)  
    code  =  fields.Char('Code' , required = True)
    # critearea_ids = fields.One2many('medical_test.critearea', 'test_id','Critearea')
    # service_product_id = fields.Many2one('product.product','Service')
    info  = fields.Text('Extra Information')


    def test_type(self):
       return{
        'name': "Test types",
        'type': 'ir.actions.act_window',
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'medical.lab.test.units',
        'context': {

            # 'default_doctor_id': self.doctor.id,

            'default_test': self.id,

        },
        'target': 'new'
    }



    def test_types(self):
        return {
    'name': "tests",
    'domain':[('test', '=', self.id)],
    'view_mode': 'tree,form',
    'res_model': 'medical.lab.test.units',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }
#      Count in Smart Button
    def test_count(self):
        count1 = self.env['medical.lab.test.units'].search_count([('test', '=', self.id)])
        self.tests_tests= count1

    tests_tests = fields.Integer(compute='test_count',string="Tests Count")

