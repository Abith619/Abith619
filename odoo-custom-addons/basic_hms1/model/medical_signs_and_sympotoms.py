# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_signs_and_sympotoms(models.Model):
    _name = 'medical.signs.and.sympotoms'
    _rec_name = 'pathology_id'

    patient_evaluation_id = fields.Many2one('medical.patient.evaluation','Patient Evaluation')
    pathology_id = fields.Many2one('medical.pathology','Sign or Symptom')
    sign_or_symptom = fields.Selection([
            ('sign', 'Sign'),
            ('symptom', 'Symptom'),
        ], string='Subjective / Objective')
    comments = fields.Char('Comments')


