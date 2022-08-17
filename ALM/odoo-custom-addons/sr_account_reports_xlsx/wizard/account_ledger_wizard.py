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

from odoo import fields, models, api
import time

class AccountLedgerWizard(models.TransientModel):
    
    _name = 'account.ledger.wizard'
    _description = 'Account Ledger Wizard'

    account_ids = fields.Many2many('account.account',
                                    'account_ledger_wizard_rel',
                                    'account',
                                    'wizard_id',
                                    string='Accounts')
    from_date = fields.Date(string='From Date', default=time.strftime('%Y-01-01'))
    to_date = fields.Date(string='To Date', default=fields.Date.today)
    include_opening_balance = fields.Boolean(string='Include Opening Balances', default=True)
    show_zero_balance = fields.Boolean(string='Show Zero Balance', default=False)
    posted_entries_only = fields.Boolean(string='Posted Entries Only', default=True)
    summary_format = fields.Boolean(string='Summary Format')
    
    partner_ids = fields.Many2many('res.partner',
                                   'partner_filter_ledger_wizard_rel',
                                   'partner_id',
                                   'wizard_id',
                                   string='Partners')

    include_movement_filter = fields.Boolean(string="Include Movement Filter",default=True)
    account_filter = fields.Selection([('receivable','Receivable'),('payable','Payable'),('receivable_payable','Receivable and Payable')],string="Account Filter")

    
    @api.multi
    def print_report(self, data):
        return self.env.ref('sr_account_reports_xlsx.account_ledger_report_id').report_action(self, 
                                                                                       data=data)

