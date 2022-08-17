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

from openerp.addons.report_xlsx.report.report_xlsx import ReportXlsxAbstract
from datetime import datetime, timedelta
from odoo import models
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
import calendar
import base64
import io
import re


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def excel_style(row, col):
    """ Convert given row and column number to an Excel-style cell name. """
    result = []
    while col:
        col, rem = divmod(col-1, 26)
        result[:0] = LETTERS[rem]
    return ''.join(result) + str(row)



class AccountLedger(models.AbstractModel):
    _name = 'report.account_ledger_report_xlsx'    
    _inherit = 'report.report_xlsx.abstract'

    
    def generate_xlsx_report(self, workbook, data, record):
        
        top_heading_left = workbook.add_format({'align': 'left',
                                              'valign': 'vcenter',
                                              'bold': True, 'size': 12})
        
        partner_heading_left = workbook.add_format({'align': 'left',
                                              'valign': 'vcenter',
                                              'bold': True, 'size': 11})
        
        op_heading_right = workbook.add_format({'align': 'right',
                                              'valign': 'vcenter',
                                              'bold': True, 'size': 11})
        
        op_bal_heading_right =  workbook.add_format({'num_format': '#,##0.00', 
                                                      'valign': 'vcenter', 'bold': True,
                                                      'align' : 'right', 'size': 11})
        
        shading_below = workbook.add_format({'bg_color': '#a8a9ad', 'size': 10})
        
        sub_heading_left = workbook.add_format({'align': 'left',
                                              'valign': 'vcenter',
                                              'bold': True, 'size': 10})
        
        summary_heading_left = workbook.add_format({'align': 'left',
                                              'valign': 'vcenter',
                                              'bold': True, 'size': 12})
        
        total_heading_left = workbook.add_format({'align': 'left',
                                              'valign': 'vcenter',
                                              'bold': True, 'size': 11})
        
        total_heading_right = workbook.add_format({'align': 'right',
                                              'num_format': '#,##0.00', 
                                              'valign': 'vcenter',
                                              'bold': True, 'size': 11})
        
        sub_heading_center = workbook.add_format({'align': 'center',
                                              'valign': 'vcenter',
                                              'bold': True, 'size': 10})
        
        sub_heading_right = workbook.add_format({'align': 'right',
                                              'valign': 'vcenter',
                                              'bold': True, 'size': 10})
        
        summary_heading_right = workbook.add_format({'align': 'right',
                                              'valign': 'vcenter',
                                              'bold': True, 'size': 12})
        
        sub_total_right = workbook.add_format({'num_format': '#,##0.00', 
                                              'valign': 'vcenter', 'bold': True,
                                              'align' : 'right', 'size': 11})

        date_format_left = workbook.add_format({'num_format':  'dd/mm/yyyy',
                                           'align': 'left',
                                           'valign': 'vcenter',
                                           'size': 10})
        
        period_format = workbook.add_format({'num_format':  'dd/mm/yyyy',
                                           'align': 'left',
                                           'valign': 'vcenter',
                                           'bold': True,
                                           'size': 11})
        
        column_details_left = workbook.add_format({'align': 'left',
                                              'valign': 'vcenter',
                                              'text_wrap': True,
                                               'size': 10})
        
        column_numbers_right =  workbook.add_format({'num_format': '#,##0.00', 
                                                      'valign': 'vcenter',
                                                      'align' : 'right', 'size': 10})
        
        company_address_format = workbook.add_format({'align': 'left',
                                              'valign': 'vcenter',
                                              'font_color': '#4757c1',
                                              'bold': True, 'size': 11})
        
        worksheet = workbook.add_worksheet("Partner Ledger Report")
        
        row = 1
        worksheet.set_column('A:A', 10)
        worksheet.set_column('B:B', 25)
        worksheet.set_column('C:C', 25)
        worksheet.set_column('D:D', 15)
        worksheet.set_column('E:E', 15)
        worksheet.set_column('F:F', 12)
        worksheet.set_column('G:G', 12)
        company_address_col = 7
        
        if record.summary_format:
            worksheet.set_column('A:A', 10)
            worksheet.set_column('B:B', 25)
            worksheet.set_column('C:C', 25)
            worksheet.set_column('D:D', 15)
            worksheet.set_column('E:E', 15)
            worksheet.set_column('F:F', 12)
            worksheet.set_column('G:G', 12)
            worksheet.set_column('H:H', 15)
            company_address_col = 8
            
        user_company = self.env.user.company_id
        company_address = []
        if user_company.street:
            company_address.append(user_company.street)
        if user_company.street2:
            company_address.append(user_company.street2)
        city_state = []
        if user_company.city:
            city_state.append(user_company.city)
        if user_company.state_id:
            city_state.append(user_company.state_id.name)
        if city_state:
            city_state = city_state and ', '.join(city_state)
            company_address.append(city_state)
        if user_company.country_id:
            company_address.append(user_company.country_id.name)
                    
        company_logo = user_company.logo or False
         
        if company_logo:
            imgdata = base64.b64decode(company_logo)
            image = io.BytesIO(imgdata)
            worksheet.insert_image(1, 0, 'logo.png', {'image_data': image, 'x_scale': 0.165, 
                                                                           'y_scale': 0.175, 'positioning': 0})
        
        company_name = user_company.name or ''
        
        starting_col = excel_style(row + 1, 3)
        ending_col = excel_style(row + 1, company_address_col)
        worksheet.merge_range('%s:%s'%(starting_col, ending_col), company_name, top_heading_left)
        
        increment = 2
        for address_item in company_address:
            starting_col = excel_style(row+increment, 3)
            ending_col = excel_style(row+increment , company_address_col)
            worksheet.merge_range('%s:%s'%(starting_col, ending_col), address_item, company_address_format)
            increment += 1
        
        row += 6
        
        from_date = record.from_date or False
        to_date = record.to_date or False
        
        worksheet.write(row, 0, 'Period From', period_format)
        if from_date:
            from_date_string = from_date.strftime('%d-%m-%Y')
            worksheet.write(row, 1, from_date_string, period_format)
            
        row += 1
        worksheet.write(row, 0, 'Period To', period_format)
        account_filter = record.account_filter or False
        if to_date:
            to_date_string = to_date.strftime('%d-%m-%Y')
            worksheet.write(row, 1, to_date_string, period_format)
        all_accounts_objs = self.env['account.account'].search([],order="code asc")
        if account_filter:
            if account_filter == 'receivable':
                all_accounts_objs = self.env['account.account'].search([('user_type_id.type','=','receivable')],order="code asc")

            elif account_filter == 'payable':
                all_accounts_objs = self.env['account.account'].search([('user_type_id.type','=','payable')],order="code asc")

            else:
                all_accounts_objs = self.env['account.account'].search([('user_type_id.type','in',('payable','receivable'))],order="code asc")
            account_ids = (all_accounts_objs and all_accounts_objs.ids) or []
        # all_accounts_objs = self.env['account.account'].search([],order="code asc")
        else:
            account_ids = (record.account_ids and record.account_ids.ids) or (all_accounts_objs and all_accounts_objs.ids) or []
        include_opening_bal = record.include_opening_balance or False
        include_movement_filter = record.include_movement_filter or False
        show_zero_balance = record.show_zero_balance or False
        
        posted_entries_only = record.posted_entries_only or False
        partner_ids = record.partner_ids and record.partner_ids.ids or []
        summary_format = record.summary_format or False
        summary_added = False
        summary_grand_debit = 0.00
        summary_grand_credit = 0.00
        summary_grand_balance = 0.00
        
        if summary_format:
            row += 2
            worksheet.write(row, 0, 'Sl No', summary_heading_left)
            starting_col = excel_style(row + 1, 2)
            ending_col = excel_style(row + 1, 5)
            worksheet.merge_range('%s:%s'%(starting_col, ending_col), 'ACCOUNT DETAILS', summary_heading_left)
            worksheet.write(row, 5, 'Debit', summary_heading_right)
            worksheet.write(row, 6, 'Credit', summary_heading_right)
            worksheet.write(row, 7, 'Balance', summary_heading_right)
            row += 1
            starting_col = excel_style(row + 1, 1)
            ending_col = excel_style(row + 1, 8)
            worksheet.merge_range('%s:%s'%(starting_col, ending_col), '', shading_below)
            account_sl_no = 1
            
        cr = self.env.cr
        for account_id in account_ids:
            account_obj = self.env['account.account'].browse(account_id)
            if summary_format:
                summary_where_condition = """(aml.account_id = {0})""".format(account_id)
                if not include_opening_bal and from_date:
                    summary_where_condition += """ AND aml.date >= '{0}'""".format(from_date)

                
                if to_date:
                    summary_where_condition += """ AND aml.date <= '{0}'""".format(to_date)
                if posted_entries_only:
                    summary_where_condition += """ AND am.state = 'posted'"""
                if partner_ids:
                    if len(partner_ids) == 1:
                        summary_where_condition += ''' AND aml.partner_id = %s''' % partner_ids[0]
                    else:
                        summary_where_condition += ''' AND aml.partner_id IN {0}'''.format(tuple(partner_ids))
                
                cr.execute("""
                    Select
                        sum(aml.debit) as total_debit,
                        sum(aml.credit) as total_credit 
                    From 
                        account_move_line aml 
                    Left Join 
                        account_move am 
                    on 
                        (am.id = aml.move_id) 
                    Where 
                        %s
                    """ %summary_where_condition)
                
                dict_val = cr.dictfetchall()
                dict_val = dict_val and dict_val[0] or False
                total_debit = dict_val and dict_val.get('total_debit') is not None and [dict_val.get('total_debit')] or False
                total_credit = dict_val and dict_val.get('total_credit') is not None and [dict_val.get('total_credit')] or False
                   
                
                if total_debit or total_credit:
                    total_debit = total_debit and round(total_debit[0],2) or 0.00
                    total_credit = total_credit and round(total_credit[0],2) or 0.00
                    total_balance = total_debit - total_credit
                    if total_balance != 0.00:
                        row += 1
                        worksheet.write(row, 0, account_sl_no, column_details_left)
                        starting_col = excel_style(row + 1, 2)
                        ending_col = excel_style(row + 1, 5)
                        account_code = account_obj.code
                        account_name = account_obj.name
                        display_format = '[' + account_code + ']' + account_name
                        worksheet.merge_range('%s:%s'%(starting_col, ending_col), display_format, column_details_left)
                        worksheet.write(row, 5, total_debit, column_numbers_right)
                        worksheet.write(row, 6, total_credit, column_numbers_right)
                        worksheet.write(row, 7, total_balance, column_numbers_right)
                        summary_grand_debit += total_debit
                        summary_grand_credit += total_credit
                        summary_grand_balance += total_balance
                        summary_added = True
                        account_sl_no += 1
                        
                    elif total_balance == 0.00 and show_zero_balance:
                        row += 1
                        worksheet.write(row, 0, account_sl_no, column_details_left)
                        starting_col = excel_style(row + 1, 2)
                        ending_col = excel_style(row + 1, 5)
                        account_code = account_obj.code
                        account_name = account_obj.name
                        display_format = '[' + account_code + ']' + account_name
                        worksheet.merge_range('%s:%s'%(starting_col, ending_col), display_format, column_details_left)
                        worksheet.write(row, 5, total_debit, column_numbers_right)
                        worksheet.write(row, 6, total_credit, column_numbers_right)
                        worksheet.write(row, 7, total_balance, column_numbers_right)
                        summary_grand_debit += total_debit
                        summary_grand_credit += total_credit
                        summary_grand_balance += total_balance
                        summary_added = True
                        account_sl_no += 1
                        
                elif not include_movement_filter:
                    row += 1
                    worksheet.write(row, 0, account_sl_no, column_details_left)
                    starting_col = excel_style(row + 1, 2)
                    ending_col = excel_style(row + 1, 5)
                    account_code = account_obj.code
                    account_name = account_obj.name
                    display_format = '[' + account_code + ']' + account_name
                    worksheet.merge_range('%s:%s'%(starting_col, ending_col), display_format, column_details_left)
                    worksheet.write(row, 5, 00.00, column_numbers_right)
                    worksheet.write(row, 6, 0.00, column_numbers_right)
                    worksheet.write(row, 7, 0.00, column_numbers_right)
                    summary_grand_debit += 0.00
                    summary_grand_credit += 0.00
                    summary_grand_balance += 0.00
                    summary_added = True
                    account_sl_no += 1

            else:
                opening_balance = False
                if from_date:
                    opening_where_condition = """(aml.account_id = {0})""".format(account_id)
                    opening_where_condition += """ AND aml.date < '{0}'""".format(from_date)
                    if posted_entries_only:
                        opening_where_condition += """ AND am.state = 'posted'"""
                    if partner_ids:
                        if len(partner_ids) == 1:
                            opening_where_condition += ''' AND aml.partner_id = %s''' % partner_ids[0]
                        else:
                            opening_where_condition += ''' AND aml.partner_id IN {0}'''.format(tuple(partner_ids))
                    
                    cr.execute("""
                        Select
                            sum((aml.debit - aml.credit)) as balance 
                        From 
                            account_move_line aml 
                        Left Join 
                            account_move am 
                        on 
                            (am.id = aml.move_id) 
                        Where 
                            %s
                        """ %opening_where_condition)
                    
                    dict_val = cr.dictfetchall()
                    dict_val = dict_val and dict_val[0] or False
                    opening_balance = dict_val and dict_val.get('balance') is not None and [dict_val.get('balance')] or False
                
                where_condition = """(aml.account_id = {0})""".format(account_id)
             
                if from_date:
                    where_condition += """ AND aml.date >= '{0}'""".format(from_date)
                if to_date:
                    where_condition += """ AND aml.date <= '{0}'""".format(to_date)
                if posted_entries_only:
                    where_condition += """ AND am.state = 'posted'"""
                
                if partner_ids:
                    if len(partner_ids) == 1:
                        where_condition += ''' AND aml.partner_id = %s''' % partner_ids[0]
                    else:
                        where_condition += ''' AND aml.partner_id IN {0}'''.format(tuple(partner_ids)) 
                
                cr.execute("""
                            Select
                                aml.date as date,
                                aml.name as label,
                                Case when 
                                    aat.type In ('payable','receivable')
                                    Then
                                        Case when
                                            am.name is null 
                                        Then 
                                            aml.ref
                                        else
                                            am.name 
                                        End 
                                    else 
                                        Case when
                                            aml.ref is null 
                                        Then 
                                            am.name
                                        else
                                            aml.ref
                                        END 
                                End
                                    as ref,
                                aml.debit as debit,
                                aml.credit as credit,
                                (aml.debit - aml.credit) as balance,
                                rp.name as partner 
                            From 
                                account_move_line aml 
                            Left Join 
                                account_move am 
                            on 
                                (am.id = aml.move_id) 
                            Left Join 
                                res_partner rp 
                            on 
                                (rp.id = aml.partner_id) 
                            Left Join
                                account_account aa 
                            on 
                                (aa.id = aml.account_id)
                            Left Join 
                                account_account_type aat
                            on 
                                (aat.id = aa.user_type_id)
                            Where 
                                %s
                            Order by
                                aml.date 
                            """ %where_condition)
                 
                trnacation_details = cr.dictfetchall()
                
                if trnacation_details or (opening_balance and include_opening_bal) or not include_movement_filter:
                    account_total = 0.0
                    account_credit_total = 0.0
                    account_debit_total = 0.0
                    balance_log = 0.0
                    row += 2
                    worksheet.write(row, 0, 'Account', partner_heading_left)
                    starting_col = excel_style(row + 1, 2)
                    ending_col = excel_style(row + 1, 5)
                    account_code = account_obj.code
                    account_name = account_obj.name
                    display_format = '[' + account_code + ']' + account_name
                    worksheet.merge_range('%s:%s'%(starting_col, ending_col), display_format, partner_heading_left)
                    
                    if trnacation_details:
                        row += 2
                        worksheet.write(row, 0, 'Date', sub_heading_left)
                        worksheet.write(row, 1, 'Reference', sub_heading_center)
                        worksheet.write(row, 2, 'Description', sub_heading_center)
                        worksheet.write(row, 3, 'Partner Name', sub_heading_center)
                        worksheet.write(row, 4, 'Debit', sub_heading_right)
                        worksheet.write(row, 5, 'Credit', sub_heading_right)
                        worksheet.write(row, 6, 'Balance', sub_heading_right)

                        if opening_balance and include_opening_bal:
                            row += 1 
                            starting_col = excel_style(row + 1, 3)
                            ending_col = excel_style(row + 1, 6)
                            worksheet.merge_range('%s:%s'%(starting_col, ending_col), 'Opening Balance', op_heading_right)
                            worksheet.write(row, 6, opening_balance[0], op_bal_heading_right)
        #                     account_total += opening_balance[0]
                            balance_log = opening_balance[0]
                        
                        for items in trnacation_details:
                            row += 1
                            date_string = ''
                            if items.get('date'):
                                date_string = items.get('date').strftime('%d-%m-%Y')
                            worksheet.write(row, 0, date_string, date_format_left)
                            worksheet.write(row, 1, items.get('label'), column_details_left)
                            worksheet.write(row, 2, items.get('ref'), column_details_left)
                            worksheet.write(row, 3, items.get('partner'), column_details_left)
                            worksheet.write(row, 4, items.get('debit'), column_numbers_right)
                            worksheet.write(row, 5, items.get('credit'), column_numbers_right)
                            balance_log += (items.get('debit') - items.get('credit'))
                            worksheet.write(row, 6, balance_log, column_numbers_right)
    #                         account_total += items.get('balance')
                            account_credit_total += items.get('credit')
                            account_debit_total += items.get('debit')
                    elif not include_movement_filter:
                        row += 2
                        worksheet.write(row, 0, 'Date', sub_heading_left)
                        worksheet.write(row, 1, 'Description', sub_heading_center)
                        worksheet.write(row, 2, 'Reference', sub_heading_center)
                        worksheet.write(row, 3, 'Partner Name', sub_heading_center)
                        worksheet.write(row, 4, 'Debit', sub_heading_right)
                        worksheet.write(row, 5, 'Credit', sub_heading_right)
                        worksheet.write(row, 6, 'Balance', sub_heading_right)

                        if opening_balance and include_opening_bal:
                            row += 1 
                            starting_col = excel_style(row + 1, 3)
                            ending_col = excel_style(row + 1, 6)
                            worksheet.merge_range('%s:%s'%(starting_col, ending_col), 'Opening Balance', op_heading_right)
                            worksheet.write(row, 6, opening_balance[0], op_bal_heading_right)
        #                     account_total += opening_balance[0]
                            balance_log = opening_balance[0]

                        row += 1
                        date_string = ''
                        worksheet.write(row, 0, date_string, date_format_left)
                        worksheet.write(row, 1, '', column_details_left)
                        worksheet.write(row, 2, '', column_details_left)
                        worksheet.write(row, 3, '', column_details_left)
                        worksheet.write(row, 4, 0.00, column_numbers_right)
                        worksheet.write(row, 5, 0.00, column_numbers_right)
                        balance_log += 0.00
                        worksheet.write(row, 6, balance_log, column_numbers_right)
#                         account_total += items.get('balance')
                        account_credit_total += 0.00
                        account_debit_total += 0.00

                    if account_credit_total > 0.0 or account_debit_total > 0.0:
                        row += 1
                        worksheet.write(row, 3, 'Total', sub_heading_right)
                        worksheet.write(row, 4, account_debit_total, sub_total_right)
                        worksheet.write(row, 6, account_credit_total, sub_total_right)
    #                     worksheet.write(row, 7, account_total, sub_total_right)
                    elif not include_movement_filter:
                        row += 1
                        worksheet.write(row, 3, 'Total', sub_heading_right)
                        worksheet.write(row, 4, 0.00, sub_total_right)
                        worksheet.write(row, 5, 0.00, sub_total_right)
                    
                    row += 1
                    starting_col = excel_style(row + 1, 1)
                    ending_col = excel_style(row + 1, 7)
                    worksheet.merge_range('%s:%s'%(starting_col, ending_col), '', shading_below)
        
        if summary_format and summary_added:
            row += 1
            starting_col = excel_style(row + 1, 1)
            ending_col = excel_style(row + 1, 5)
            worksheet.merge_range('%s:%s'%(starting_col, ending_col), 'Total', total_heading_left)
            worksheet.write(row, 5, summary_grand_debit, total_heading_right)
            worksheet.write(row, 6, summary_grand_credit, total_heading_right)
            worksheet.write(row, 7, summary_grand_balance, total_heading_right)
                    
            row += 1
            starting_col = excel_style(row + 1, 1)
            ending_col = excel_style(row + 1, 8)
            worksheet.merge_range('%s:%s'%(starting_col, ending_col), '', shading_below)  
                  
AccountLedger()

