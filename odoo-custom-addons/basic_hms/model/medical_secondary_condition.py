# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_secondary_condition(models.Model):
    _name = 'medical.secondary_condition'
    _rec_name = 'pathology_id'

    patient_evaluation_id = fields.Many2one('medical.patient.evaluation','Patient Evaluation')
    pathology_id = fields.Many2one('medical.pathology','Pathology')
    comments = fields.Char('Comments')

