# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import date
import re
from dateutil.relativedelta import relativedelta
from datetime import datetime, date, timedelta
from odoo import models, fields, api, _
from odoo.exceptions import Warning, UserError
import pytz





class ProductProduct(models.Model):
    _inherit = 'hr.applicant'


    vehicle_count = fields.Integer()

    def get_vehicles(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Candidate After Interview',
            'view_type': 'form',
			'view_mode': 'tree,form',
			#'target': 'new',
            'res_model': 'afterin.afterin',
            #'domain': [('driver_id', '=', self.id)],
            #'context': "{'create': True}"
        }	


    vehicle_counts = fields.Integer()

    def get_vehicless(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'HR Report',
            'view_type': 'form',
			'view_mode': 'tree,form',
			#'target': 'new',
            'res_model': 'hrafter.hrafter',
            #'domain': [('driver_id', '=', self.id)],
            #'context': "{'create': True}"
        }	
        
    vehicle_countss = fields.Integer()

    def get_vehiclessss(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'ShortList/Finalisation',
            'view_type': 'form',
			'view_mode': 'tree,form',
			#'target': 'new',
            'res_model': 'hrshort.hrshort',
            #'domain': [('driver_id', '=', self.id)],
            #'context': "{'create': True}"
        }	
     

    stagesss = fields.Many2one('hr.recruitment.stage',string="Application Stages")