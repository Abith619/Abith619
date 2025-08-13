# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_pathology(models.Model):
    _name = 'medical.pathology'

    name = fields.Char(string="Name",required=True)
    code = fields.Char(string="Code")
    info = fields.Text(string="Extra Info")
    # category_id = fields.Many2one('medical.pathology.category',string="Disease Category")
    # line_ids = fields.One2many('medical.pathology.group.member','disease_group_id',string="Group")
    # chromosome = fields.Char(string="Affected Chromosome")
    # gene = fields.Char(string="Gene")
    # protein = fields.Char(string="Protein")


    
    def symptoms_button(self):
       return{
        'name': "Symptoms",
        'type': 'ir.actions.act_window',
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'medical.symptoms',
        'context': {

            'default_diseases': self.id,

        },
        'target': 'new'
    }



    def symptom_types(self):
        return {
    'name': "Symptoms",
    'domain':[('diseases', '=', self.id)],
    'view_mode': 'tree,form',
    'res_model': 'medical.symptoms',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }
#      Count in Smart Button
    def symptoms_count(self):
        count_s = self.env['medical.symptoms'].search_count([('diseases', '=', self.id)])
        self.diseases_symptoms= count_s

    diseases_symptoms = fields.Integer(compute='symptoms_count',string="Symptoms Count")




