# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_icu_chest_drainage(models.Model):
    _name = 'medical.icu.chest_drainage'

    location = fields.Selection([('rl','Right Pleura'),
                                 ('ll','Left Pleura'),
                                 ('mediastinum','Mediastinum')],
                                string='Location')
    suction = fields.Boolean(string="Suction")
    suction_pressure = fields.Integer(string="cm H2O")
    fluid_volumme = fields.Integer(string="Volume")
    fluid_aspect = fields.Selection([('serous','Serous'),
                                     ('bloody','Bloody'),
                                     ('chylous','Chylous'),
                                     ('purulent','Purulent')],
                                    string="Aspect")
    oscillation = fields.Boolean(string='Oscillation')
    air_leak = fields.Boolean(string='Air Leak')
    remarks = fields.Char(string="Remarks")
    medical_patient_rounding_chest_drainage_id = fields.Many2one('medical.patient.rounding',string="Chest Drainage")

