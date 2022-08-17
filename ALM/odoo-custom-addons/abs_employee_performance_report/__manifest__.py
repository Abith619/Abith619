# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2019-today Ascetic Business Solution <www.asceticbs.com>
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

{
    'name': "Employee Task Performance Report",
    'author': 'Ascetic Business Solution',
    'category': 'Human Resources',
    'summary': """Employee Performance""",
    'license': 'AGPL-3',
    'website': 'http://www.asceticbs.com',
    'description': """
""",
    'version': '12.0.0.1',
    'depends': ['base','hr','project','hr_timesheet'],
    'data': ['security/ir.model.access.csv','views/employee_view.xml','report/employee_report.xml','report/employee_template_report.xml'],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
