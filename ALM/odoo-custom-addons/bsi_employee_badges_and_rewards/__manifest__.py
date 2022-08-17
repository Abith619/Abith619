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
{
    'name'         : "Employee Badges and Rewards",
    'author'       : 'Botspot Infoware Pvt. Ltd.',
    'category'     : 'Employees',
    'summary'      : """Employees get Awarded by the badges and also get reward cerficates""",
    'website'      : 'http://www.botspotinfoware.com',
    'company'      : 'Botspot Infoware Pvt. Ltd.',
    'maintainer'   : 'Botspot Infoware Pvt. Ltd.',
    'description'  : """  """, 
    'version'      : '1.0',
    'depends'      : ['base','project','hr'],
    'data'         : [
                      'security/ir.model.access.csv',
                      'wizard/employee_reward_wizard_view.xml',
                      'views/employee_badge_configuration_view.xml',
                      'views/hr_employee_view.xml',
                      'views/project_view.xml',
                      'views/scheduler_for_employee_rewards.xml',
                      'reports/employee_certificate_report_template.xml',
                     ],
    "images"       : ['static/description/Banner.gif'],
    'license'      : 'LGPL-3',
    'installable'  : True,
    'application'  : True,
    'auto_install' : False,
}
