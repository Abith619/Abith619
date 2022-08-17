# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2017-TODAY Cybrosys Technologies(<http://www.cybrosys.com>).
#    Author: Jesni Banu(<http://www.cybrosys.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from datetime import datetime

from odoo import api, fields, models, _

from odoo import models, fields, api
from odoo.exceptions import UserError


class ProjectTaskTimeSheet(models.Model):
    _inherit = 'account.analytic.line'

    date_start = fields.Datetime(string='Start Date')
    date_end = fields.Datetime(string='End Date')
    timer_duration = fields.Float(invisible=1, string='Time Duration (Minutes)')


class ProjectTaskTimer(models.Model):
    _inherit = 'project.task'

    task_timer = fields.Boolean()
    is_user_working = fields.Boolean(
        'Is Current User Working', compute='_compute_is_user_working',
        help="Technical field indicating whether the current user is working. ")
    duration = fields.Float(
        'Real Duration', store=True)

    def _compute_is_user_working(self):
        """ Checks whether the current user is working """
        for order in self:
            if order.timesheet_ids.filtered(lambda x: (x.user_id.id == self.env.user.id) and (not x.date_end)):
                order.is_user_working = True
            else:
                order.is_user_working = False

    def _compute_duration(self):
        self

    def set_date_end(self):
        if self.timesheet_ids:
            for data in self.timesheet_ids:
                if not data.date_end:
                    end_date = datetime.combine(data.date, datetime.min.time())
                    data.date_end = end_date

    @api.multi
    def toggle_start(self):
        for record in self:
            record.task_timer = not record.task_timer
            project_obj = self.env['project.task'].search_count(
                [('user_id', '=', record.user_id.id), ('task_timer', '=', True)])
            if project_obj > 1:
                raise UserError(_('you cannot start timer for more than one task at the same time'))
            if record.task_timer:
                self.write({'is_user_working': True,'kanban_state':'done'})
                time_line = self.env['account.analytic.line']
                for time_sheet in self:
                    time_line.create({
                        'name': self.env.user.name + ':' + time_sheet.name,
                        'task_id': time_sheet.id,
                        'stage_id' : time_sheet.write({'stage_id': 23,'kanban_state':'done'}),
                        'user_id': self.env.user.id,
                        'project_id': time_sheet.project_id.id,
                        'date_start': datetime.now(),
                    })
            else:
                self.write({'is_user_working': False,'kanban_state':'normal'})
                time_line_obj = self.env['account.analytic.line']
                domain = [('task_id', 'in', self.ids), ('date_end', '=', False)]
                for time_line in time_line_obj.search(domain):
                    time_line.write({'date_end': fields.Datetime.now()})
                    if time_line.date_end:
                        diff = fields.Datetime.from_string(time_line.date_end) - fields.Datetime.from_string(
                            time_line.date_start)
                        time_line.timer_duration = round(diff.total_seconds() / 60.0, 2)
                        time_line.unit_amount = round(diff.total_seconds() / (60.0 * 60.0), 2)
                    else:
                        time_line.unit_amount = 0.0
                        time_line.timer_duration = 0.0
