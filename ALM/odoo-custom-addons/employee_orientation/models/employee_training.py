# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta
from datetime import datetime,timedelta
from odoo import api, fields, models, _


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    certificates = fields.Boolean(default=True, string="Certificates")


class EmployeeTraining(models.Model):
    _name = 'employee.training'
    _rec_name = 'program_name'
    _description = "Employee Training"
    _inherit = 'mail.thread'

    program_name = fields.Char(string='Training Program', required=True)
    program_department = fields.Many2one('hr.department', string='Department', required=True)
    program_convener = fields.Many2one('res.users', string='Responsible User', size=32, required=True)
    training_id = fields.One2many('hr.employee', string='Employee Details', compute="employee_details")
    note_id = fields.Text('Description')
    date_from = fields.Datetime(string="Date From")
    date_to = fields.Datetime(string="Date To")
    user_id = fields.Many2one('res.users', string='users', default=lambda self: self.env.user)
    company_id = fields.Many2one('res.company', string='Company', required=True,
                                 default=lambda self: self.env.user.company_id)
    # product_updatable = fields.Boolean(compute='_compute_product_updatable', string='Can Edit Product', readonly=True, default=True)
    # @api.depends('training_id')
    # def _compute_product_updatable(self):
        # for line in self:
        #     if line.state in ['done', 'cancel'] or (line.state == 'sale' and (line.qty_invoiced > 0 or line.qty_delivered > 0)):
        #         line.product_updatable = False
        #     else:
        #         line.product_updatable = True

    state = fields.Selection([
        ('new', 'New'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Canceled'),
        ('complete', 'Completed'),
        ('print', 'Print'),
    ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='new')

    @api.onchange('program_department')
    def employee_details(self):
        datas = self.env['hr.employee'].search([('department_id', '=', self.program_department.id)])
        self.training_id = datas

    @api.multi
    def print_event(self):
        self.ensure_one()
        started_date = datetime.strftime(self.create_date, "%Y-%m-%d ")
        duration = (self.write_date - self.create_date).days
        pause = relativedelta(hours=0)
        difference = relativedelta(self.write_date, self.create_date) - pause
        hours = difference.hours
        minutes = difference.minutes
        data = {
            'dept_id': self.program_department.id,
            'program_name': self.program_name,
            'company_name': self.company_id.name,
            'date_to': started_date,
            'duration': duration,
            'hours': hours,
            'minutes': minutes,
            'program_convener': self.program_convener.name,

        }
        return self.env.ref('employee_orientation.print_pack_certificates').report_action(self, data=data)

    @api.multi
    def complete_event(self):
        self.write({'state': 'complete'})

    @api.multi
    def confirm_event(self):
        self.write({'state': 'confirm'})

    @api.multi
    def cancel_event(self):
        self.write({'state': 'cancel'})

    @api.multi
    def confirm_send_mail(self):
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('employee_orientation', 'orientation_training_mailer')[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        ctx = dict(self.env.context or {})
        ctx.update({
            'default_model': 'employee.training',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
        })

        return {
            'name': _('Compose Email'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }
