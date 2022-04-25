# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date,datetime

class medical_icu_glasgow(models.Model):
    _name = 'medical.icu.glasgow'
    _rec_name = 'medical_inpatient_registration_id'

    medical_inpatient_registration_id = fields.Many2one('medical.inpatient.registration',string="Registration Code",required=True)
    evaluation_date = fields.Datetime(string="Date",required=True)
    glasgow_eyes = fields.Selection([('1','1 : Does not Open Eyes'),
                                     ('2','2 : Opens eyes in response to painful Stimuli'),
                                     ('3','3 : Open eyes to response to voice'),
                                     ('4','4 : Open eyes spontaneously')],
                                    string="Eyes")
    glasgow_verbal = fields.Selection([('1','1 : Makes no sounds'),
                                       ('2','2 : Incomprehensible Sounds'),
                                       ('3','3 : Utters inapporopriate words'),
                                       ('4','4 : Confused disoriented'),
                                       ('5','5 : Oriented converses normally')],
                                      string="Verbal")
    glasgow_motor = fields.Selection([('1','1 : Makes no movement'),
                                      ('2','2 : Extension to painful stimuli -decerabrate response'),
                                      ('3','3 : Abnormal flexion to painful stimuli (decorticate response)'),
                                      ('4','4 : Flexion/Withdrawal to painful stimuli'),
                                      ('5','5 : Localizes painful stimuli'),
                                      ('6','6 : Obeys commands')],
                                     string="Motor")
    glasgow = fields.Integer(string="Glasgow", compute='get_glas_score')

    @api.one
    @api.depends('glasgow_motor', 'glasgow_verbal', 'glasgow_eyes' )
    def get_glas_score(self):
        """ Calculates Sub total"""
        count = int(self.glasgow_eyes) + int(self.glasgow_motor)+ int(self.glasgow_verbal)
        self.glasgow = count

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
