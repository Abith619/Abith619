# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class project_issue_wizard(models.TransientModel):
    _name = 'project.issue.wizard'

    name = fields.Char(string="Name",required=True)
    
    @api.model
    def default_get(self,fields):
        res = super(project_issue_wizard, self).default_get(fields)
        if self._context.get('active_id'):
            project_task_id = self.env['project.task'].browse(self._context.get('active_id'))
            res.update({'name':project_task_id.name})
        else:
            pass
        return res

    @api.multi
    def create_issue(self):
        if self._context.get('active_id'):
            project_task_id = self.env['project.task'].browse(self._context.get('active_id'))
            vals = {
                        'user_id': project_task_id.user_id.id or False,
                        'task_id': self._context.get('active_id'),
                        'partner_id': project_task_id.partner_id.id or False,
                        'email_from': project_task_id.partner_id.email,
                        'project_id': project_task_id.project_id.id or False,
                        'name': self.name,
                        'issue_id':project_task_id.id,

                    }
            if vals:
                project_issue_id = self.env['project.task'].create(vals)
        else:
            pass
        return {
                    'name':'project.issue.form.view',
                    'res_model':'project.task',
                    'view_type':'form',
                    'view_mode':'form',
                    'res_id': project_issue_id.id,
                    'target':'current',
                    'type':'ir.actions.act_window'
                    }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
