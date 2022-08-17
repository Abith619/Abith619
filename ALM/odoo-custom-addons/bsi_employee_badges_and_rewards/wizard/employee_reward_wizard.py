# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2021-today Botspot Infoware Pvt. Ltd. <www.botspotinfoware.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################
from odoo import api, fields, models, _
from datetime import timedelta, datetime
from datetime import date
from odoo.tools import float_compare
from odoo.exceptions import AccessError, UserError, ValidationError


class EmployeeRewardWizard(models.TransientModel):
    _name = 'employee.reward.wizard'
    _description = "Employee Reward Wizard"

    date = fields.Date(string="Date", default= lambda self: fields.Date.today())
    badge_id = fields.Many2one('employee_badge.configuration', string="Badge")
    task_id = fields.Many2one('project.task', string="Task")
    employee_id = fields.Many2one('hr.employee', string="Employee")

    def confirm_employee_reward(self):
        if not self.badge_id:
            raise ValidationError(("Please Select Reward for Employee"))

        if self.badge_id and self.task_id and self.employee_id:
            badge_line_dict = {
                               'date': self.date,
                               'badge_id': self.badge_id.id,
                               'task_id': self.task_id.id,
                               'employee_id': self.employee_id.id,
                              }
            if badge_line_dict:
                badge_line_id = self.env['employee.badge.line'].create(badge_line_dict)
                if badge_line_id:
                    self.task_id.write({'is_task_reward_done':True})


