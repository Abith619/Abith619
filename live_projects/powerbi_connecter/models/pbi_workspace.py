# -*- coding: utf-8 -*-
import logging
from odoo import fields, models
from odoo.exceptions import UserError, ValidationError
import requests

_logger = logging.getLogger(__name__)


class PbiWorkspace(models.Model):
    _name = 'pbi.workspace'
    _description = "power bi workspace"
    connection_id : fields.Many2one = fields.Many2one('pbi.connect', string='Connection')
    workspace_id = fields.Char(string="workspace ID")
    name = fields.Char(string="Name")
    reports_ids : fields.One2many = fields.One2many('pbi.report', 'workspace_id', string='Reports', copy=True, readonly=True)
    _sql_constraints = [
        ('unique_workspace_id', 'unique(workspace_id)', 'workspace_id. should be unique.'),
    ]


    def get_reports(self):
        # if self.id==False:
        #     self = self.search([('is_connect','=',True)])[0]
        # if self.id==False:
        #     _logger.exception('do not have connected config')
        #     return

        endpoint = 'https://api.powerbi.com/v1.0/myorg/groups/'+self.workspace_id+'/reports'
        headers = {
            'Authorization': f'Bearer ' + str(self.connection_id.access_id)
        }

        try:
            report = self.env['pbi.report']
            dashboard = self.env['pbi.dashboard']
            response_request = requests.get(endpoint,headers=headers)
            if response_request.status_code==200:
                result = response_request.json()
                for item in result['value']:
                    try:
                        dup = report.search([('report_id','=',item['id'])])
                        if len(dup)==0:
                            if item['reportType']=='PowerBIReport':
                                dashboard.create({
                                'name':item['name'],
                                'report_id':item['id'],
                                'workspace_id':self.id,
                                'embedurl':item['embedUrl'],
                                'report_type':item['reportType'],
                                })
                            else:
                                report.create({
                                    'name':item['name'],
                                    'report_id':item['id'],
                                    'workspace_id':self.id,
                                    'embedurl':item['embedUrl'],
                                    'report_type':item['reportType'],
                                })
                    except Exception as e:
                        _logger.info(e)

        except (UserError, ValidationError):
            _logger.exception(UserError)
