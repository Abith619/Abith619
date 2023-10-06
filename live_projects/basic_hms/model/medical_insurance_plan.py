# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_insurance_plan(models.Model):
    _name = 'medical.insurance.plan'
    _rec_name = 'insurance_product_id'

    insurance_product_id  = fields.Many2one('product.product', 'Plan' , domain = "[('type','=','service')]")
    is_default= fields.Boolean('Default Plan')
    company_partner_id = fields.Many2one('res.partner',domain=[('is_insurance_company','=',True)],string='Company')
    notes= fields.Text('Extra Info')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
