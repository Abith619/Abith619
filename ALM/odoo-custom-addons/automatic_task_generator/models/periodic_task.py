# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, exceptions
from odoo.exceptions import ValidationError, UserError
from datetime import datetime, timedelta, time

class PeriodicTask(models.Model):
    _name = "automatic_task_generator.periodic_task"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'rating.mixin']

    @api.onchange('project_id')
    def _list_states_project(self):
        self.task_state = False
        self.parent_id = False

        return {
            'domain': {
                'parent_id': [('project_id', '=', self.project_id.id)],
                'task_state': [('id', 'in', self.project_id.type_ids.ids)],
            }
        }

    @api.onchange('parent_id')
    def _list_states_parent(self):
        if self.parent_id and self.parent_id.subtask_project_id:
            return {
                'domain': {
                    'task_state': [('id', 'in', self.parent_id.subtask_project_id.type_ids.ids)],
                }
            }

    name = fields.Char(string='Title', track_visibility='always', required=True, index=True)
    project_id = fields.Many2one('project.project',
        string='Project',
        default=lambda self: self.env.context.get('default_project_id'),
        index=True,
        track_visibility='onchange',
        change_default=True,
        required=True)
    task_state = fields.Many2one('project.task.type', string='Task stage', track_visibility='always')
    parent_id = fields.Many2one('project.task', string='Parent Task', index=True, track_visibility='always')
    user_id = fields.Many2one('res.users',
        string='Assigned to',
        default=lambda self: self.env.uid,
        index=True, track_visibility='always',
        required=True)
    active = fields.Boolean(default=True, track_visibility='always')
    periodicity = fields.Integer(string="Periodicity (days)", required=True, track_visibility='always')
    write_date = fields.Date(string="Last task written", readonly=True, index=True, track_visibility='always')
    date_start = fields.Date(string='Cron Date', index=True, copy=False, required=True, track_visibility='always', help="Date used for calculating next automatic task assigment")
    generated_tasks = fields.Many2many('project.task')
    tasks_ids_nbr = fields.Integer(compute='_compute_task_ids_nbr', string='# of Tasks')

    @api.depends('generated_tasks')
    def _compute_task_ids_nbr(self):
        for task in self:
            task.tasks_ids_nbr = len(task.generated_tasks)

    @api.multi
    def action_view_tasks(self):
        action = {
            'name': _('Generated tasks'),
            'type': 'ir.actions.act_window',
            'res_model': 'project.task',
            'target': 'current',
        }

        task_ids = self.generated_tasks.ids

        if len(task_ids) == 1:
            task = task_ids[0]
            action['res_id'] = task
            action['view_mode'] = 'form'
            action['views'] = [(self.env.ref('project.view_task_form2').id, 'form')]
        else:
            action['view_mode'] = 'tree,form'
            action['domain'] = [('id', 'in', task_ids)]

        return action

    @api.multi
    def action_create_task(self):
        try:
            for periodic_task in self:
                project = self.env['project.project'].search([('id', '=', periodic_task.project_id.id)])
                today_string = datetime.now().strftime("%Y-%m-%d")

                if project.active:
                    r = self.env['project.task'].sudo().create({
                        'user_id': periodic_task.user_id.id,
                        'project_id': periodic_task.project_id.id,
                        'stage_id': periodic_task.task_state.id,
                        'parent_id': periodic_task.parent_id.id,
                        'name': periodic_task.name,
                        'date_deadline': datetime.now()
                    })

                    periodic_task.write_date = today_string
                    periodic_task.generated_tasks = [(4, r.id)]

                    self.message_post(body="<ul><li>" + _("Succesful manual task assigment") + "</li></ul>")
        except:
            self.message_post(body="<ul><li>" + _("Error while manual task assigment") + "</li></ul>")

class PeriodicTask(models.Model):
    _name = "automatic_task_generator.generate_tasks"

    @api.model
    def generate_by_date(self):
        try:
            periodic_tasks = self.env['automatic_task_generator.periodic_task'].search([('active', '=', True)])

            for periodic_task in periodic_tasks:
                project = self.env['project.project'].search([('id', '=', periodic_task.project_id.id)])
                date_task = datetime.strptime(str(periodic_task.date_start), '%Y-%m-%d')
                today_string = datetime.now().strftime("%Y-%m-%d")
                today = datetime.strptime(today_string, '%Y-%m-%d')
                number_of_days = (today - date_task).days

                if project.active:
                    if int(periodic_task.periodicity) == int(number_of_days):
                        r = self.env['project.task'].sudo().create({
                            'user_id': periodic_task.user_id.id,
                            'project_id': periodic_task.project_id.id,
                            'stage_id': periodic_task.task_state.id,
                            'parent_id': periodic_task.parent_id.id,
                            'name': periodic_task.name,
                            'date_deadline': datetime.now()
                        })

                        periodic_task.write_date = today_string
                        periodic_task.date_start = today_string
                        periodic_task.generated_tasks = [(4, r.id)]

                        periodic_task.message_post(body="<ul><li>" + _("Succesful automatic task assigment") + "</li></ul>")
                    elif periodic_task.periodicity < number_of_days:
                        periodic_task.message_post(body="<ul><li>" + _("Error while automatic task assigment") + "</li></ul>")
        except:
            periodic_task.message_post(body="<ul><li>" + _("Error while automatic task assigment") + "</li></ul>")