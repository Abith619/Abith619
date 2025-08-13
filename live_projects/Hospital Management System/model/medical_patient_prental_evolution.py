# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_prental_evolution(models.Model):   
    
    _name = 'medical.patient.prental.evoultion'

    pregnency_id = fields.Many2one('medical.patient.pregnency', )
    evoultion_date = fields.Date('Date', required = True) 
    gestational_weeks = fields.Integer('Gestational Weeks', required = True)
    hypertansion = fields.Boolean('Hypertension')
    preclampsia = fields.Boolean('Prclampsia') 
    overweight = fields.Boolean('Overweight')
    diabetes= fields.Boolean('Diabetes') 
    placenta_previa = fields.Boolean('Placenta Previa')
    invasive_placentation = fields.Selection([('normal_decidua','Normal Decidua'),
                                              ('accreta','Accreta'),
                                              ('increta','Increta'),
                                              ('percreta','Precreta')])
    vasa_previa = fields.Boolean('Vasa Previa') 
    fundel_weight = fields.Integer('Fundel Weight')
    fetus_heart_rate = fields.Integer('Fetus Heart Rate')
    efw = fields.Integer('EFW')
    bpd = fields.Integer('BPD')
    hc = fields.Integer('HC')
    ac = fields.Integer('AC')
    fl = fields.Integer('FL')


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
