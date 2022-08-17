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
from odoo import models, fields, api, exceptions, _, SUPERUSER_ID
from datetime import date
import base64


class EmployeeBadgeLine(models.Model):
    _name = "employee.badge.line"
    _description = "Employee Badge Lines"

    date = fields.Date(string="Date")
    badge_id = fields.Many2one('employee_badge.configuration', string="Badge")
    task_id = fields.Many2one('project.task', string="Task")
    employee_id = fields.Many2one('hr.employee', string="Employee")


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    badge_line_ids = fields.One2many('employee.badge.line','employee_id', string="Badge History")

    reward = fields.Selection([('month_best','Month Best'), ('month_worst','Month Worst'), ('year_best','Year Best'), ('year_worst','Year Worst')], string="Reward")
    reward_points = fields.Integer(string="Reward Points")
    reward_date = fields.Date(string="Reward Date")

    def call_employee_rewards_scheduler(self):
        employee_ids = self.env['hr.employee'].search([])
        if employee_ids:
            current_date = date.today()
            current_month = current_date.month
            current_year = current_date.year

            reward_result = []
            for employee_id in employee_ids:
                if employee_id:
                    month_avarage_reward_point = 0
                    year_avarage_reward_point = 0
                    total_month_task = 0
                    total_month_points = 0
                    total_year_task = 0
                    total_year_points = 0
                    if employee_id.badge_line_ids:
                        for badge_line in employee_id.badge_line_ids:
                            if badge_line.date and badge_line.date.month == current_month:
                                total_month_task += 1
                                if badge_line.badge_id and badge_line.badge_id.priority:
                                    total_month_points += badge_line.badge_id.priority
                            if badge_line.date and badge_line.date.year == current_year:
                                total_year_task += 1
                                if badge_line.badge_id and badge_line.badge_id.priority:
                                    total_year_points += badge_line.badge_id.priority
                    else:
                        employee_id.write({'reward': False})

                    if total_month_task > 0 and total_month_points > 0:
                        month_avarage_reward_point = total_month_points / total_month_task
                    if total_year_task > 0 and total_year_points > 0:
                        year_avarage_reward_point = total_year_points / total_year_task

                    reward_result.append({'emplpyee': employee_id, 'month_reward_point': month_avarage_reward_point, 'year_reward_point': year_avarage_reward_point})

            if reward_result:
                best_month_emp_points = 0
                best_month_employee = False
                worst_month_emp_points = 100
                worst_month_employee = False

                best_year_emp_points = 0
                best_year_employee = False
                worst_year_emp_points = 100
                worst_year_employee = False

                for line in reward_result:
                    if best_month_emp_points < line['month_reward_point']:
                        best_month_emp_points = line['month_reward_point']
                        best_month_employee = line['emplpyee']

                    if worst_month_emp_points > line['month_reward_point'] and 0 < worst_month_emp_points and 0 < line['month_reward_point']:
                        worst_month_emp_points = line['month_reward_point']
                        worst_month_employee = line['emplpyee']

                    if best_year_emp_points < line['year_reward_point']:
                        best_year_emp_points = line['year_reward_point']
                        best_year_employee = line['emplpyee']

                    if worst_year_emp_points > line['year_reward_point'] and 0 < worst_year_emp_points and 0 < line['year_reward_point']:
                        worst_year_emp_points = line['year_reward_point']
                        worst_year_employee = line['emplpyee']

            for employee_id in employee_ids:
                if employee_id:
                    ##### Only best month and best year functionality is enabled.
                    if best_month_employee and best_month_employee.id == employee_id.id:
                        reward_dict = {'reward': 'month_best', 'reward_points': best_month_emp_points, 'reward_date': date.today()}
                        employee_id.write(reward_dict)
                        self.create_and_attach_employee_certificate(employee_id, 'Best of the Month')
                    elif best_year_employee and best_year_employee.id == employee_id.id:
                        reward_dict = {'reward': 'year_best', 'reward_points': best_year_emp_points, 'reward_date': date.today()}
                        employee_id.write(reward_dict)
                        self.create_and_attach_employee_certificate(employee_id, 'Best of the Year')
                    elif worst_month_employee and worst_month_employee.id == employee_id.id:
                        employee_id.write({'reward': 'month_worst'})
                    elif worst_year_employee and worst_year_employee.id == employee_id.id:
                        employee_id.write({'reward': 'year_worst'})
                    else:
                        employee_id.write({'reward': False, 'reward_points': 0})

    def create_and_attach_employee_certificate(self, employee_id, reward):
        pdf = self.env.ref('bsi_employee_badges_and_rewards.action_employee_certificate_report').render_qweb_pdf(employee_id.id)
        b64_pdf = base64.b64encode(pdf[0])
        # save pdf as attachment
        name = str(employee_id.name) + ' - Certificate('+str(reward)+')'
        attachment_id = self.env['ir.attachment'].create({
        'name': name,
        'type': 'binary',
        'datas': b64_pdf,
        'store_fname': name,
        'res_model': self._name,
        'res_id': employee_id.id,
        'mimetype': 'application/x-pdf'
        })
        #print("=============attachment_id==============",attachment_id)

    def action_view_employee_certificates(self):
        return {
            'name': _('Employee Certificates'),
            'view_type': 'form',
            'view_mode': 'kanban,tree,form',
            'res_model': 'ir.attachment',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'domain': [('res_id','=',self.id), ('res_model','=',self._name)],
        }

