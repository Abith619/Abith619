# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_preinatal(models.Model):
    
    _name = 'medical.preinatal'
    
    pregnency_id = fields.Many2one('medical.patient.pregnency', 'Pregnancy', )
    gestational_weeks = fields.Integer('Gestational weeks')
    admission_date = fields.Date('Admission Date')
    code  = fields.Char('Code')
    labour_mode = fields.Selection([('n','Normal'),('i','Induced'),('c','C-Section')], 'Labour Mode')
    fetus_presentation = fields.Selection([('n','Correct'),
                                         ('o','Occiput /Cephalic Postrior'),
                                         ('fb','Frank Breech'),
                                         ('cb','Complete Breech'),
                                         ('tl','Transverse Lie'),
                                         ('fu','Footling Lie')], 'Fetus Presentation')
    monitor_ids = fields.One2many('medical.perinatal.monitor','medical_perinatal_id')
    dystocia = fields.Boolean('Dystocia')
    episiotomy = fields.Boolean('Episiotomy')
    lacerations = fields.Selection([('p','Perinial'),
                                      ('v','Vaginal'),
                                      ('c','Cervical'),
                                      ('bl', 'Broad Ligament'),
                                      ('vl','Vulvar'),
                                      ('r','Rectal'),
                                      ('br','Blader'),
                                      ('u','Ureteral'),  ],'Lacerations')
    
    
    hematoma = fields.Selection( [('v','Vaginal'), ('vl','Vulvar'),('r','Retroperitional')], 'Hematoma')
    plancenta_incomplete = fields.Boolean('Incomplete Placenta')
    retained_placenta = fields.Boolean('Retained Placenta')
    abruptio_placentae = fields.Boolean('Abruptio Placentae')
    
       

    notes= fields.Text('Notes')


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
