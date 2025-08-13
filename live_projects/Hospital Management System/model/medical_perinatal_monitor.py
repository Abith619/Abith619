# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_perinatal_monitor(models.Model):
    
    _name = 'medical.perinatal.monitor'
    
    medical_perinatal_id = fields.Many2one('medical.perinatal.monitor')
    date  = fields.Date('Date')
    systolic = fields.Integer('Systolic Pressure')
    diastolic = fields.Integer('Diastolic Pressure')
    mothers_heart_freq = fields.Integer('Mothers Heart Freq')
    consentration = fields.Integer('Consentration')
    cervix_dilation = fields.Integer('Cervix Dilation')  
    fundel_height = fields.Integer('Fundel Height')
    fetus_presentation = fields.Selection([('n','Correct'),
                                         ('o','Occiput /Cephalic Postrior'),
                                         ('fb','Frank Breech'),
                                         ('cb','Complete Breech'),
                                         ('tl','Transverse Lie'),
                                         ('fu','Footling Lie')], 'Fetus Presentation')
    f_freq = fields.Integer('Fetus Heart Frequency')
    bleeding = fields.Boolean('Bleeding')
    meconium = fields.Boolean('Meconium')
    notes = fields.Char('Notes')


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
