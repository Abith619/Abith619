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
from datetime import datetime, date, time, timedelta
from odoo import models, fields, api, exceptions, _, SUPERUSER_ID


class EmployeeBadgeConfiguration(models.Model):
    _name = 'employee_badge.configuration'
    _description = 'Employee Badge Configuration'
    _order='priority desc'

    name = fields.Char(string="Name")
    priority = fields.Integer(string="Priority")
    employee_id = fields.Many2one('hr.employee', string="Employee")

    badge_line_ids = fields.One2many('employee.badge.line','badge_id', string="Badge History")

    _sql_constraints = [('priority_uniq', 'unique (priority)', "The 'Priority' must be unique.")]

