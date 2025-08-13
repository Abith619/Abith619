# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_menstrual_history(models.Model):

    _name = 'medical.patient.menstrual.history'
    
    patient_id = fields.Many2one('medical.patient', 'Patient')
    evolution_id = fields.Many2one('medical.patient.evaluation','Evaluation')
    evoultion_date = fields.Date('Date')
    lmp = fields.Integer('LMP', required= True)
    lmp_length = fields.Integer('LMP Length', required= True )
    is_regular = fields.Boolean('IS Regular')
    dysmenorrhea = fields.Boolean('Dysmenorrhea')
    frequency = fields.Selection([('amenorrhea','Amenorrhea'),
                                  ('oligomenorrhea','Oligomenorrhea'),
                                  ('eumenorrhea','Eumenorrhea'),
                                  ('pollymenohea','Pollymenohea')])
    volume  = fields.Selection([('hopomenorrhea','hopomenorrhea'),
                                ('normal','Normal'),
                                ('menorrhagia','Menorrhagia') ])


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
