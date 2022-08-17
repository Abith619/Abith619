# -*- coding: utf-8 -*-
import datetime

from odoo import _, api, fields, models
from odoo.exceptions import Warning


class TaskEntry(models.TransientModel):
    _name = "task.entry"

    start_date = fields.Datetime(string="Start Date", readonly=True)
    end_date = fields.Datetime(string="End Date", readonly=True)
    description = fields.Text(string="Description", required=True)
    duration = fields.Float('Duration', readonly=True)

    @api.model
    def default_get(self, default_fields):
        context = self._context
        s_date = context.get('start_date')
        e_date = context.get('end_date')
        diff = datetime.datetime.strptime(
            e_date, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(
            s_date, "%Y-%m-%d %H:%M:%S")
        duration = float(diff.days) * 24 + (float(diff.seconds) / 3600)
        final_output = round(duration, 2)
        res = super(TaskEntry, self).default_get(default_fields)
        res.update({
            'start_date': s_date,
            'end_date': e_date,
            'duration': final_output,
        })
        return res

    @api.multi
    def save_entry(self):
        context = self._context
        task_id = context.get('task_id', False)
        task_rec = self.env['project.task'].browse(task_id)
        project_id = task_rec.project_id
        if project_id:
            if self.duration == 0.0:
                raise Warning(_("You can't save entry for %s duration") % (
                    self.duration))
            vals = {'date': fields.Date.context_today(self),
                    'start_date': self.start_date,
                    'end_date': self.end_date,
                    'user_id': self.env.user.id,
                    'name': self.description,
                    'task_id': task_id,
                    'project_id': project_id.id,
                    'unit_amount': self.duration,
                    'account_id': project_id.analytic_account_id.id
                    }
            analytic_line_rec = self.env['account.analytic.line'].create(vals)
            task_rec.write({'timesheet_ids': [(4, 0, [analytic_line_rec.id])],
                            'is_start': False})
        else:
            raise Warning(_("Please link Project to this Task to save the entry"))
