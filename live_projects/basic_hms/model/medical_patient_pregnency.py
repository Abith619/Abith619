# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class  medical_patient_pregnency(models.Model):
    _name = 'medical.patient.pregnency'

    gravida = fields.Integer('Pregnancy #')
    lmp = fields.Integer('LMP')
    pdd = fields.Date('Pregnency  Due Date')
    patient_id= fields.Many2one('medical.patient','Patient')
    current_pregnency = fields.Boolean('Current Pregnency')
    medical_patient_evolution_prental_ids = fields.One2many('medical.patient.prental.evoultion', 'pregnency_id', 'Patient Perinatal Evaluations')
    medical_perinatal_ids = fields.One2many('medical.preinatal', 'pregnency_id', 'Medical Perinatal ')
    puerperium_perental_ids = fields.One2many('medical.puerperium.monitor', 'pregnency_id', 'Puerperium Monitor')
    fetuses = fields.Boolean('Fetuses')
    monozygotic = fields.Boolean('Monozygotic')
    igur = fields.Selection([('s','Symmetric'),('a','Asymmetric')], 'IGUR')
    warn = fields.Boolean('Warning')
    result = fields.Char('Result')
    pregnancy_end_date = fields.Date('Pregnancy End Date')
    pregnancy_end_result = fields.Char('Pregnancy End Result')


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
