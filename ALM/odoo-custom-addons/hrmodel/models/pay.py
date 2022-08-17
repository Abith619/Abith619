# -*- coding: utf-8 -*-


from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
import re
from num2words import num2words

from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import string
# from datetime import date
from num2words import num2words
import datetime



class hrpayslip(models.Model):
    _inherit = 'hr.payslip'



    Employeecodes  = fields.Char(related='employee_id.employee_code',string='Employee Code')

    dateofjoin  = fields.Date(related='employee_id.joining_date',string='Date of joining')    
    
    noofdayspresent  = fields.Char(string='No Of Days Present')    
        
    lop  = fields.Float(string='LOP')    
            
    branchname  = fields.Char(related='employee_id.bank_account_id.branch_name' , string='Branch Name')    
            
    bankname  = fields.Many2one('res.bank',string='Bank Name',related='employee_id.bank_account_id.bank_id')        
            
    leaveavail  = fields.Float(string='Leave Availed')    

    department  = fields.Many2one('hr.department',string='Department Name',related='employee_id.department_id')
    
    deductions = fields.Char(string='Deduction')    
    currency_id = fields.Many2one('res.currency', string='Currency' , )
    num_word = fields.Char(string="Amount In Words:", compute='_compute_amount_in_word')
    salary_advances = fields.Monetary(string="Salary Advance")
    reamining_leave = fields.Float(string='Remaining Leaves')

    leave_earned = fields.Float(string='Leave Earned')

    @api.one
    def _compute_amount_in_word(self):
        for rec in self:
            # rec.num_word = str(rec.currency_id.amount_to_text(rec.amount_total)) + ' only'
            rec.num_word = 'Rupees '+str(num2words(rec.amount_total)).title() + ' Only'

    no_of_days_month = fields.Char('No Of Days In Month') 
    deduction_amount = fields.Monetary('Deduction Amount',store=True,compute='_compute_deduction_amount')  
    eb_deduction = fields.Monetary(string="EB & Motor Charge")
    total_deductions = fields.Monetary(string="Total Dedctions",compute='_compute_total_deduction')
    loan_deduction = fields.Monetary(string="Loan Deduction",compute='_compute_loan_deduction')
    netearnings = fields.Monetary('Gross Earnings')  
    gross_earnings = fields.Monetary(related='contract_id.wage',string='Gross Earnings') 

    amount_total = fields.Monetary(compute="_compute_amount_total",string="Amount Total")
    

    @api.depends('gross_earnings', 'deduction_amount','eb_deduction','loan_deduction','date_from','salary_advances','employee_id')
    def _compute_amount_total(self):
        date1 = datetime.datetime.strptime(str(self.date_from), "%Y-%m-%d").date()
        self.name = f'Salary Slip of {str(datetime.datetime.strptime(str(date1.month), "%m").strftime("%B"))} {str(datetime.datetime.strftime(date1, "%Y"))}'
        present = self.env['salary.advance'].search([('employee_id','=',self.employee_id.id),('paid','=',False)],order='date desc', limit=1)
        self.salary_advances = present.advance
        for record in self:
            if record.eb_deduction:
                record.amount_total = round(record.gross_earnings - record.deduction_amount - record.eb_deduction)
            else:
                record.amount_total = round(record.gross_earnings - record.deduction_amount)
            if record.salary_advances:
                # self.salary_advances = record.salary_advance
                record.amount_total = round(record.amount_total - self.salary_advances)
            if record.loan_deduction:
                record.amount_total = round(record.amount_total - self.loan_deduction)
    @api.depends('deduction_amount','eb_deduction','loan_deduction','salary_advances')
    def _compute_total_deduction(self):
        for rec in self:
            if rec.deduction_amount:
                rec.total_deductions = round(rec.deduction_amount)
            if rec.eb_deduction:
                rec.total_deductions = round(rec.total_deductions + rec.eb_deduction)
            if rec.loan_deduction:
                 rec.total_deductions = round(rec.total_deductions + rec.loan_deduction)
            if rec.salary_advances:
                rec.total_deductions = round(rec.total_deductions + rec.salary_advances)
#   Jegan
    @api.depends('date_from','date_to','employee_id','contract_id')
    def _compute_deduction_amount(self):
        date_format = "%Y-%m-%d"
        a = datetime.datetime.strptime(str(self.date_from), date_format)
        b = datetime.datetime.strptime(str(self.date_to), date_format)
        delta = b - a
        days = delta.days+1
        lstt = []        
        data_request = self.env['hr.leave'].search([('holiday_status_id','=',10),('date_from','>=',self.date_from),('date_from','<=',self.date_to),('employee_id','=',self.employee_id.id),('state','=','validate')])
        # above id refers to without pay leave type id
        for u in data_request:
            leavesss = u.number_of_days_display
            lstt.append(leavesss)    
        sdf =sum(lstt)    
        result = self.contract_id.wage/int(days)        
        dk =(result*sdf)
        # raise ValidationError(dk)
        self.deduction_amount = round(dk)



##############################################################################################################################################################
    @api.onchange('employee_id','contract_id','struct_id','date_from','date_to')
    def leaveofpay(self):
        self.deductions = "Leave Deduction"
        self.currency_id = 20
        # above mentioned INR currency id 
########################################################################################################################################################
        ch = []
        c = 1
        date1 = datetime.datetime.strptime(str(self.date_from), "%Y-%m-%d").date()
        self.name = f'Salary Slip For {str(datetime.datetime.strptime(str(date1.month), "%m").strftime("%B"))} {str(datetime.datetime.strftime(date1, "%Y"))}'
        date2 = datetime.datetime.strptime(str(self.date_to), "%Y-%m-%d").date()
        day = datetime.timedelta(days=1)
        while date1 <= date2:
            ch.append(c)
            c+=1
            date1 = date1 + day
        self.no_of_days_month = len(ch)
########################################################################################################################################################
        lst = []
        let = self.env['hr.leave'].search([('holiday_status_id','=',10),('date_from','>=',self.date_from),('date_from','<=',self.date_to),('employee_id','=',self.employee_id.id),('state','=','validate')])
        # above id refers to without pay leave type id
        for k in let:
            leaves = k.number_of_days_display
            lst.append(leaves)
        self.lop = sum(lst)
########################################################################################################################################################
        # j = []
        # a = 1
        # present = self.env['hr.attendance'].sudo().read_group([('check_in','>=',self.date_from),('check_in','<=',self.date_to),('employee_id','=',self.employee_id.id)], fields=['check_in','id'], groupby=['check_in:day'])              
        # for i in present:
        #     avl = i['check_in:day']
        #     j.append(a)
        #     a+=1        
        # self.noofdayspresent = len(j)
        date11 = datetime.datetime.strptime(str(self.date_from), "%Y-%m-%d").date()
        date22 = datetime.datetime.strptime(str(self.date_to), "%Y-%m-%d").date()
        dayy = datetime.timedelta(days=1)
        h = []
        while date11 <= date22:
            sumss = []
            ids = self.env['hr.attendance'].search([('employee_id', '=', self.employee_id.id),('check_in', '>=', date11),('check_in', '<=', date11)])
            for i in ids:
                sumss.append(i.worked_hours)
                if sum(sumss)>=6:
                    h.append(1)
                else:
                    h.append(0.5)
            date11 = date11 + dayy
        self.noofdayspresent = sum(h)

########################################################################################################################################################
        l = []
        lets = self.env['hr.leave'].search([('holiday_status_id','!=',19),('date_from','>=',self.date_from),('date_from','<=',self.date_to),('employee_id','=',self.employee_id.id),('state','=','validate')])
        for d in lets:
            leav = d.number_of_days_display
            l.append(leav)
        self.leaveavail = sum(l)    
########################################################################################################################################################
        leave_all = []
        leave_aviled = []
        leave_earned = []
        lve_all = self.env['hr.leave'].search([('employee_id','=',self.employee_id.id),('state','=','validate'),('holiday_status_id','=',11)])
        lve_aviled = self.env['hr.leave.allocation'].search([('employee_id','=',self.employee_id.id),('state','=','validate'),('holiday_status_id','=',11)])
        lve_ern = self.env['hr.leave.allocation'].search([('employee_id','=',self.employee_id.id),('state','=','validate'),('holiday_status_id','=',11),('create_date','>=',self.date_from),('create_date','<=',self.date_to)])
        for y in lve_all:
            leave_all.append(y.number_of_days_display)
        for u in lve_aviled:
            leave_aviled.append(u.number_of_days_display)
        for r in lve_ern:
            leave_earned.append(r.number_of_days_display)
        self.leave_all = sum(leave_all)
        self.reamining_leave = sum(leave_aviled)-sum(leave_all)
        self.leave_earned = sum(leave_earned)

########################################################################################################################################################

    @api.depends('date_from','date_to','employee_id')
    def _compute_loan_deduction(self):
        date1 = datetime.datetime.strptime(str(self.date_from), "%Y-%m-%d").date()
        loan = self.env['hr.loan'].search([('employee_id','=',self.employee_id.id),('Finished','=',False)])
        # p.append(loan.loan_lines.id)
        for lo in loan:
            payment_dates = datetime.datetime.strptime(str(lo.payment_date), "%Y-%m-%d").date()
            naol = self.env['hr.loan.line'].search([('date','=',f"{str(datetime.datetime.strftime(date1,'%Y'))}-{str(datetime.datetime.now().month)}-{str(datetime.datetime.strftime(payment_dates,'%d'))}"),('paid_due_amount','=',False)])
            self.loan_deduction = naol.amount


    @api.multi
    def compute_sheet(self):
        for payslip in self:
            number = payslip.number or self.env['ir.sequence'].next_by_code('salary.slip')
            # delete old payslip lines
            payslip.line_ids.unlink()
            # set the list of contract for which the rules have to be applied
            # if we don't give the contract, then the rules to apply should be for all current contracts of the employee
            contract_ids = payslip.contract_id.ids or \
                self.get_contract(payslip.employee_id, payslip.date_from, payslip.date_to)
            lines = [(0, 0, line) for line in self._get_payslip_lines(contract_ids, payslip.id)]
            payslip.write({'line_ids': lines, 'number': number})
        return True

    @api.multi
    def action_payslip_done(self):
#   Jegan
        loan = self.env['hr.loan'].search([('employee_id','=',self.employee_id.id)])
        for lo in loan:
            payment_dates = datetime.datetime.strptime(str(lo.payment_date), "%Y-%m-%d").date()
            naol = self.env['hr.loan.line'].search([('date','=',f"{str(datetime.datetime.strftime(payment_dates,'%Y'))}-{str(datetime.datetime.now().month)}-{str(datetime.datetime.strftime(payment_dates,'%d'))}")])
            naol.write({'paid_due_amount':True})
        present = self.env['salary.advance'].search([('employee_id','=',self.employee_id.id),('paid','=',False)],order='date desc', limit=1)
        for o in present:
            o.write({'paid': True})
            
#ZZZZZZZ
        if not self.env.context.get('without_compute_sheet'):
            self.compute_sheet()
        return self.write({'state': 'done'})
