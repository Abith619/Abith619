# -*- coding: utf-8 -*-


from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import date
import re
from dateutil.relativedelta import relativedelta






class ProductProduct(models.Model):
    _inherit = 'hr.employee'


    bloodgroup = fields.Selection([('O+', 'O+'), ('O−', 'O−'),('A−', 'A−'),('A+', 'A+'),
										('B−', 'B−'),('B+', 'B+'),('AB−', 'AB−'),('AB+', 'AB+'),('A1+', 'A1+'),('AB1+', 'AB1+'),('AB-', 'AB-'),('A1-', 'A1-'),
                                        ('A2B+', 'A2B+')])


    production_active = fields.Boolean(string='Pro Active')

    Permanentaddress = fields.Text(string='Permanent Address')

    hostelwardennumber = fields.Char(string='Hostel Warden Phone')

    scoress = fields.Integer(string='Scores Earned')


    employee_status = fields.Selection([('active','Active'),('internship','Internship'),('left','Left'),
    ('resigned','Resigned'),('termination','Terminate'),('obscond','Abscond'),('notreporting','Not Reporting'),
    ('medical','Medical'),('workfromhome','Work From Home')],string = 'Employee Status')
    certificate = fields.Selection(selection_add=[('10th','10th'),('diploma','Diploma')])
    confirmation_date = fields.Date("Confirmation Date")
    left_date = fields.Date("Left Date")
    with_effect_from = fields.Date("With effect from")
    employee_code = fields.Char("Employee Code")
    job_level = fields.Many2one('joblevel.joblevel',string="Job Level")
    #job_level = fields.Selection([('l0','L0'),('l1','L1'),('l2','L2'),
    #('l3','L3'),('l4','L4'),('l5','L5')],string = 'Job Level')
    employee_personal_number = fields.Char('Employee Personal Number')



class Customize_attendance(models.Model):
    _inherit = 'hr.attendance'
        
    joining_dates = fields.Date(string='Date of joining',related ='employee_id.joining_date')
    #date = fields.Date(string='Date')
    month = fields.Selection([('jan','Jan'),('feb','Feb'),('mar','Mar'),('apr','Apr'),('may','May'),('jun','Jun'),
    ('jul','July'),('aug','Aug'),('sep','Sep'),('oct','Oct'),('nov','Nov'),('dec','Dec')])
    job_id = fields.Many2one('hr.job',string='Job Position',related = 'employee_id.job_id')
    actual_duty_hours = fields.Char("Actual Duty hours",default='9:00')
    overtime = fields.Float("OT")

    over_time_in = fields.Datetime('OT IN')
    over_time_out = fields.Datetime('OT OUT')
    
    total_hours = fields.Float(string='Total Hours', compute='_compute_total_hours', store=True, readonly=True)
    worked_hours = fields.Float(string='Worked Hours', compute='_compute_worked_hours', store=True, readonly=True)
    remarks = fields.Selection([('sunday','Sunday'),('halfday','Half Day Leave'),
    ('holiday','Holiday'),('earnedleave','Earned Leave'),
    ('sickleave','Sick Leave'),('lop','LOP'),('weekoff','Weekoff'),('absent','Absent'),
    ('leave','Leave'),('permission','Permission'),('holidayworking','Holiday / Working'),('wfh','Work From Home')
    ])

    @api.depends('check_in', 'check_out')
    def _compute_worked_hours(self):
        for attendance in self:
            if attendance.check_out:
                delta = attendance.check_out - attendance.check_in
                attendance.worked_hours = delta.total_seconds() / 3600.0

    @api.depends('worked_hours', 'overtime')
    def _compute_total_hours(self):
        for attendance in self:
          attendance.total_hours = attendance.worked_hours + attendance.overtime 


class Customize_project(models.Model):
    _inherit = 'project.project'
    pstatus = fields.Many2one( 'status_type.status_type',string='Project Status')
    ptype = fields.Many2one('project_types.project_types', string='Project Type')
    challenge = fields.Many2one('project.challenge',string='Challenging of Project')
    work_order = fields.Many2one('sale.order',string='Work Order')
    businessanalyst = fields.Many2one('hr.employee',string='BA Name')
    projectcoordinator  = fields.Many2one('hr.employee',string='Project Coordinator')
    projectleader  = fields.Many2one('hr.employee',string='Project Leader')
    projectdeveloper  = fields.Many2many('hr.employee',string='Project Developer')
    tester  = fields.Many2one('hr.employee',string='QA')

    alocatedduration  = fields.Float(string='Project Allocated',compute='compute_project_duration')
    # billingtype = fields.Many2one('billingtype.billingtype', string="Billing Type")
    remaininghrs = fields.Float('Remaining Hours',compute='_computeremain')

    total_rate = fields.Char('Total Rate')
    estimated_hours = fields.Float(string='Estimated Hours',track_visibility='onchange')
    #removed related
    points_per_hour = fields.Float(related='challenge.points',string='Points Per Hour')
    description = fields.Html(string='Description')
    total_points = fields.Integer(string='Total Points', compute='_computeVar')
    #v2
    @api.multi
    def compute_project_duration(self):
        f1 = self.env['project.task'].search([('project_id','=',self.id)])

        total_duration = sum(f1.mapped('planned_hours'))
        for record in self:
            record.alocatedduration = total_duration
     

    @api.depends('estimated_hours', 'alocatedduration')
    def _computeremain(self):
        for record in self:
            record.remaininghrs = record.estimated_hours - record.alocatedduration

     

    @api.depends('estimated_hours', 'points_per_hour')
    def _computeVar(self):
        for record in self:
            record.total_points = record.estimated_hours * record.points_per_hour


class Customize_account(models.Model):
    _inherit = 'account.invoice'
    particulars = fields.Char(string='Particulars')
    service_type = fields.Char( string='Service Type')
    received_amount = fields.Monetary(String='Received Amount')
    pending_amount = fields.Monetary(String='Pending Amount' , compute='_comparpdfgar')
    department = fields.Many2one('hr.department',String='Department')   
   
    @api.depends('pending_amount')
    def _compute_pending_amount_words(self):
        for invoice in self:
            invoice.pending_amount_words = invoice.currency_id.amount_to_text(invoice.pending_amount)

    pending_amount_words = fields.Char("Total (In Words)", compute="_compute_pending_amount_words")

    @api.depends('amount_total', 'received_amount')
    def _comparpdfgar(self):
        for record in self:
            record.pending_amount = record.amount_total - record.received_amount 


class Customize_AccountBankStatementLine(models.Model):
    _inherit = "res.partner.bank"
    
    ifsc_code = fields.Char('IFSC Code')
    branch_name = fields.Char('Branch Name')
    typess = fields.Selection([('salaryaccount','Salary Account'),('savingsaccount','Savings Account')],string='Type')


class Customize_journal(models.Model):
    _inherit = 'account.journal'
    description = fields.Text(string='Description')

class Customize_task(models.Model):
    _inherit = 'project.task'
    

    task_type = fields.Many2one('task_type.task_type', string='Task Tag', )
    # allocated_hours = fields.Float(related='task_challenge.allocated',string='Allocated Hours For Task')
    
    points_per_hours = fields.Float(related='task_challenge.points',string='Points Per Hour')
    total_points = fields.Integer(string='Total Points', )
    task_challenge = fields.Many2one('challenge.challenge', string='Task Challenge',)
    # bonus = fields.Float(related='task_challenge.task_points',string='Bonus Point')
    
    hourly_rate = fields.Integer('Hourly Rate')
    project_points=fields.Integer(string='Project Points',related='project_id.total_points')
    project_duration=fields.Float(string='Project Duration',related='project_id.estimated_hours')
    total_task= fields.Integer(string='Assigned task points',compute='compute_total_task')
    total_duration= fields.Float(string='Assigned duration',compute='compute_total_duration')
    ########################3#newversion3
    stage_id = fields.Many2one('project.task.type',string='stage',group_expand='_read_group_stage_ids')
    effective_hours_display = fields.Char("Hours Spent Time",store=True, help="Computed using the sum of the task work done.")
    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        # for rec in self:
        stage_drop = self.env['project.task.type'].search([])
            # for rec in self:
        return stage_drop
         ########################3#newversion3

#    repeat_every = fields.Many2one('repeatevery.repeatevery',string='Repeat Every')
#    related = fields.Many2one('related.related',string='Related To')
    notdetectpoints = fields.Selection([('yes','Yes'),('no','No')],string='NotDetectPoints')
#Report generate in excel
    def export_data(self, fields_to_export, raw_data=False):
        records = self.browse(self.ids)
        for record in records:
            record.effective_hours_display= '{0:02.0f}:{1:02.0f}'.format(*divmod(float(record.effective_hours) * 60, 60))
        return super(Customize_task, records).export_data(fields_to_export, raw_data)

#Total
    @api.onchange('planned_hours', 'points_per_hours',)
    def onchange_function(self):
        self.total_points = self.points_per_hours * self.planned_hours 

#hoursvalidation
    @api.multi
    def compute_total_duration(self):
        f1 = self.env['project.task'].search([('project_id','=',self.project_id.id)])

        total_duration = sum(f1.mapped('planned_hours'))
        for record in self:
            record.total_duration = total_duration

    @api.constrains('planned_hours')
    def check_planned_hours(self):
        if self.planned_hours > 4:
            raise ValidationError("Cannot exceed the limit of 4 Hours")

    @api.constrains('planned_hours')
    def _onchange_tasklevel(self):
        if self.total_duration > self.project_duration:
            raise exceptions.ValidationError("You are exceeding the project time duration")

#pointsvalidation
    @api.multi
    def compute_total_task(self):
        f1 = self.env['project.task'].search([('project_id','=',self.project_id.id)])

        total_task = sum(f1.mapped('total_points'))
        for record in self:
            record.total_task = total_task


    @api.constrains('total_points')
    def _onchange_tasklevel(self):
        if self.total_task > self.project_points:
            raise exceptions.ValidationError("You are out of points to assign")

       
    assigned_by = fields.Many2one('res.users',
        string='Assigned by',
        default=lambda self: self.env.uid,
        index=True, tracking=True)
    
class Customize_sale(models.Model):
    _inherit = 'sale.order'
    is_mobile = fields.Char("Mobile")
    email = fields.Char(string='Email')
    
class project_status(models.Model):
    _name = 'project_status.project_status'

    name = fields.Char()
    
class Repeatevery(models.Model):
    _name = "related.related"
    _description = "Related"

    _rec_name = 'related_to'
    related_to = fields.Char('Related To')
    
class Billing_type(models.Model):
    _name = "billingtype.billingtype"
    _description = "Billing Type"

    _rec_name = 'bill_name'
    bill_name = fields.Char('Billing Type')
    
class Joblevel(models.Model):
    _name = "joblevel.joblevel"
    _description = "Job Level"

    _rec_name = 'joblevel_name'
    joblevel_name = fields.Char('Job Level')
    
class task_type(models.Model):
    _name = 'task_type.task_type'

    name = fields.Char()
    
class task_challenge(models.Model):
    _name = 'task_challenge.task_challenge'

    name = fields.Char()
class accountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"
    
    credit  = fields.Char('Credit')
    debit = fields.Char('Debit')
    desicrption  = fields.Char('Desicrption')
    
class project_types(models.Model):
    _name = 'project_types.project_types'

    name = fields.Char()
    
class challenge(models.Model):
    _name = 'challenge.challenge'

    name = fields.Char(string ='Task Challenge')
    # task_points = fields.Float(string ='Bonus Point For Task Challange')
    # allocated = fields.Float(string ='Allocated Hours For Task')   
    points = fields.Float(string ='Points ')  
    
class projectchallenge(models.Model):
    _name = 'project.challenge'

    name = fields.Char()
    # task_points = fields.Float(string ='Bonus Point For Project Challange')
    allocated = fields.Float(string ='Estimated Hours For Project')   
    points = fields.Float(string ='Points Per Hour')  

class status_type(models.Model):
    _name = 'status_type.status_type'

    name = fields.Char()
