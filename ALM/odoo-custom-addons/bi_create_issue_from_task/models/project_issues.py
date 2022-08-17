# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class project_task(models.Model):
    _inherit = 'project.task'

    @api.multi
    def tasks_issue_count(self):
        issue_lst = []
        ir_model_data = self.env['ir.model.data']
        search_view_id = ir_model_data.get_object_reference('project', 'view_project_project_filter')[1]
        search_issue_id = self.search([('issue_id', '=',self.id)])
        for i in search_issue_id:
            issue_lst.append(i.id)
            self[0].task_issue_count = len(issue_lst)
        return{
            'name':'Issues',
            'res_model':'project.task',
            'type':'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'list,kanban,form,calendar,pivot,graph',
            'domain': [('issue_id', '=',self[0].id )],
            'search_view_id':search_view_id,
         }

    task_issue_count = fields.Integer(compute=tasks_issue_count,string="Task Count")
    issue_id=fields.Many2one('project.task',string="Task Count")


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
