# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_mammography_history(models.Model):

    _name = 'medical.patient.mammography.history'
    
    patient_id = fields.Many2one('medical.patient', 'Patient')
    evolution_id = fields.Many2one('medical.patient.evaluation','Evaluation')
    evolution_date = fields.Date('Date')
    last_mamography_date = fields.Date('Date')
    result = fields.Selection([('normal','Normal'),('abnormal','Abnormal')])
    remark = fields.Char('Comments')


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
