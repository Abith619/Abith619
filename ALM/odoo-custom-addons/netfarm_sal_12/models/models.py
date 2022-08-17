# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime, timedelta

class Sal(models.Model):
    _name = 'netfarm.sal'
    _description = 'Sal Planning'

    @api.model
    def referencable_models(self):
        value = self.env['ir.config_parameter'].sudo().get_param('netfarm_sal_12.enabled_module_selection')
        if value == '[]':
            value = False
        
        if value:
            value = value.strip('][').split(',')
            value = [int(i) for i in value]
            models = self.env['ir.model'].search([('id', 'in', value)])
        else:
            models = self.env['ir.model'].search([])
        return [(x.model, x.name) for x in models]

    active = fields.Boolean(string="Active", default=True)
    ref_doc_id = fields.Reference(selection='referencable_models', string='Reference')
    date = fields.Date(string='Date', default=fields.Date.context_today)
    employee_id = fields.Many2one(
        string='Employee',
        comodel_name='hr.employee',
        ondelete='restrict',
    )
    sequence = fields.Integer(
        string='Priority',
        default=1,
    )
    duration = fields.Float(string='Duration')
    height = fields.Char(string="Height", compute="_compute_height")
    done = fields.Boolean(string='Done')
    description = fields.Text(string='Descrizione')
    ref_value = fields.Char(sting="Ref name", compute="_compute_ref")

    def _compute_height(self):
        for record in self:
            record.height = str(record.duration * 80)

    @api.model
    def create_ckanban(self, attrs, domain):
        employee = self.env.user.employee_ids[0].id if self.env.user.employee_ids else False
        for condition in domain:
            if condition[0] == 'employee_id':
                try:
                    employee = int(condition[2])
                except:
                    employee = self.env['hr.employee'].search([('name', 'ilike', condition[2])])
                    if employee:
                        employee = employee[0].id
                    else:
                        employee = False
        attrs['employee_id'] = employee
        attrs['duration'] = 1
        created = self.create(attrs)
        return created.id

    def _compute_ref(self):
        for record in self:
            if record.ref_doc_id:
                record.ref_value = record.ref_doc_id.display_name

    @api.multi
    def write(self, vals):
        # esiste perchè la vista kanban ha il tag default_calendar
        if 'date:day' in vals:
            vals['date'] = vals['date:day']
            del vals['date:day']
        return super(Sal, self).write(vals)

class hr_employee_inherited(models.Model):

    _inherit = ['hr.employee']

    @api.model
    def get_employees(self):
        # da aggiornare con le record rules e i permessi
        domain = [('user_id', '=', self.env.user.id)]
        if self.env.user.has_group('netfarm_sal_12.group_netfarm_sal_manager'):
            domain = []
        results = self.env['hr.employee'].search_read(domain, ['id', 'name', 'department_id'])
        employees = {}
        deps = []
        for result in results:
            result['hours'] = self.env['hr.employee'].browse(result['id']).get_all_week_hours()
            if not result['department_id']:
                result['department_id'] = (0, _('No department'))
            if result['department_id'][0] in employees.keys():
                employees[result['department_id'][0]].append(result)
            else:
                employees[result['department_id'][0]] = [result]
                deps.append(result['department_id'])

        return employees, deps

    @api.model
    def get_selected_employee_data(self, domain):
        results = self.env['hr.employee'].search_read([domain], ['id', 'name', 'department_id'])
        results = results[0]
        emp = self.browse(results['id'])
        #results['week'] = emp.get_all_week_hours()
        return {'employee': emp.id, 'department_id': emp.department_id.id}

    def get_all_week_hours(self):
        self.ensure_one()
        week = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        for line in self.resource_calendar_id.attendance_ids:
            week[int(line.dayofweek)] += line.hour_to - line.hour_from
        return week

    def dailyhour(self,day):
        for record in self:
            if not record.resource_calendar_id:
                return 'no'
            a = record
            dailyhour = 0
            for i in a.resource_calendar_id.attendance_ids:
                if int(i.dayofweek) == int(day):
                    dailyhour = dailyhour + i.hour_to - i.hour_from
            return dailyhour

class SalReallocateTransient(models.TransientModel):
    _name = "reallocate.sal"

    @api.model
    def referencable_models(self):
        value = self.env['ir.config_parameter'].sudo().get_param('netfarm_sal_12.enabled_module_selection')
        if value == '[]':
            value = False
        
        if value:
            value = value.strip('][').split(',')
            value = [int(i) for i in value]
            models = self.env['ir.model'].search([('id', 'in', value)])
        else:
            models = self.env['ir.model'].search([])
        return [(x.model, x.name) for x in models]

    ref_doc_id = fields.Reference(selection='referencable_models', string='Reference', required=True)
    date = fields.Date(string="New Date", required=True)
    duration = fields.Float(string="Duration", required=True)
    employee_id = fields.Many2one(
        string='Employee',
        comodel_name='hr.employee',
        required=True
    )

    @api.multi
    def execute(self):
        self.ensure_one()
        if self.date:
            attrs = {
                'employee_id': self.employee_id.id,
                'date': self.date,
                'duration': self.duration,
                'ref_doc_id': str(self.ref_doc_id._name) + "," + str(self.ref_doc_id.id)
            }
            self.env['netfarm.sal'].create(attrs)
        return True

class SalTransient(models.TransientModel):
    _name = "create.sal"
    _description = "create sal"

    @api.model
    def referencable_models(self):
        value = self.env['ir.config_parameter'].sudo().get_param('netfarm_sal_12.enabled_module_selection')
        if value == '[]':
            value = False
        
        if value:
            value = value.strip('][').split(',')
            value = [int(i) for i in value]
            models = self.env['ir.model'].search([('id', 'in', value)])
        else:
            models = self.env['ir.model'].search([])
        return [(x.model, x.name) for x in models]

    ref_doc_id = fields.Reference(selection='referencable_models', string='Reference', required=True)
    date_start = fields.Date(string='Date Start', default=fields.Date.context_today)
    date_end = fields.Date(string='Date End')
    employee_id = fields.Many2one(
        string='Employee',
        comodel_name='hr.employee',
        required=True
    )
    duration = fields.Float(string='Duration', default=1, required=True)

    @api.multi
    def execute(self):
        self.ensure_one()
        date_start = datetime.now().date().today()
        date_end = False
        if self.date_start:
            date_start = self.date_start
        if self.date_end:
            date_end = self.date_end
        duration = self.duration
        while duration > 0:
            # seconda condizione di uscita è che metto tutto all'ultimo giorno indipendentemente dalle ore.
            if date_end == date_start:
                # metto il residuale qua
                attrs = {
                    'employee_id': self.employee_id.id,
                    'date': date_start,
                    'duration': duration,
                    'ref_doc_id': str(self.ref_doc_id._name) + "," + str(self.ref_doc_id.id)
                }
                self.env['netfarm.sal'].create(attrs)
                break
            # 1 - prendo le ore del giorno
            hour_daily = self.employee_id.dailyhour(date_start.weekday())
            if hour_daily == 'no':
                raise Warning(_('No calendar for employee'))
            # 2 - prendo le ore assegnate nel giorno
            sal = self.env['netfarm.sal'].search([
                ('employee_id', '=', self.employee_id.id),
                ('date', '=', date_start)
            ])
            total_assigned = 0
            for s in sal:
                total_assigned += s.duration
            # 3 assegno
            free = hour_daily - total_assigned

            if free > 0:
                to_assign = free if free <= duration else duration
                attrs = {
                    'employee_id': self.employee_id.id,
                    'date': date_start,
                    'duration': to_assign,
                    'ref_doc_id': str(self.ref_doc_id._name) + "," + str(self.ref_doc_id.id)
                }
                self.env['netfarm.sal'].create(attrs)
            # 4 vado avanti
                duration -= to_assign
            date_start = date_start + timedelta(days=1)

        return True