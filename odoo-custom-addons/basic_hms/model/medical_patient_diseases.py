# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_diseases(models.Model):
    _name = 'medical.patient.diseases'
    
    pathelogh_id = fields.Many2one('medical.pathology', 'Disease')
    status_of_the_disease = fields.Selection([('chronic','Chronic'),('status quo','Status Quo'),('healed','Healed'), ('improving','Improving'), ('worsening', 'Worsening') ], 'Status of the disease')
    is_active = fields.Boolean('Active Disease')
    diagnosed_date = fields.Date('Date of Diagnosis')
    age = fields.Date('Age when diagnosed')
    disease_severity = fields.Selection([('mild','Mild'), ('moderate','Moderate'), ('severe','Severe')], 'Severity')
    is_infectious = fields.Boolean('Infectious Disease', help = 'Check if the patient has an infectious / transmissible disease')
    short_comment = fields.Char('Remarks')
    healed_date = fields.Date('Healed')
    physician_id = fields.Many2one('medical.patient','Doctor')
    is_allergy = fields.Boolean('Allergic Disease')
    is_infectious = fields.Boolean('Infectious Disease')
    allergy_type  = fields.Selection([('drug_allergy', 'Drug Allergy'),('food_allergy', 'Food Allergy'),('misc', 'Misc')], 'Allergy_type')
    pregnancy_warning = fields.Boolean('Pregnancy warning')
    weeks_of_pregnancy = fields.Integer('Contracted in pregnancy week #')
    is_on_treatment = fields.Boolean('Currently on Treatment')
    treatment_description = fields.Char('Treatment Description')
    date_start_treatment = fields.Date('Start of treatment')
    date_stop_treatment = fields.Date('End of treatment')
    psc_code_id = fields.Many2one('psc.code', 'Code')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:    