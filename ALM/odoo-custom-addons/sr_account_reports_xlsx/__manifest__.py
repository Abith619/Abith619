# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016 SEEROO IT SOLUTIONS PVT.LTD(<https://www.seeroo.com/>)
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
##############################################################################

{
    'name': 'Accounting Reports XLSX',
    'version': '1.0.0',
    'summary': 'Partner ledger and General ledger Reports in XLSX Format',
    'description': """
        Helps you to print accounting reports (Partner ledger and General ledger Reports) in xlsx Format.
        """,
    'category': 'Account',
    'author': 'Seeroo IT Solutions',
    'company': 'Seeroo IT Solutions',
    'maintainer': 'Seeroo IT Solutions',
    'website': "http://www.seeroo.com",
    'depends': [
        'account','report_xlsx',
    ],
    'data': [
        'wizard/partner_ledger_wizard_view.xml',
        'wizard/account_ledger_wizard_view.xml',
        
        'views/report.xml',
        
        'views/menu.xml'
    ],
    'demo': [],
    'images': ['static/description/banner.jpg'],
    'auto_install': False,
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
