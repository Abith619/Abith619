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

from odoo import api,fields,models,_

class Employee(models.Model):
    _inherit="hr.employee" 
    
    task_ids=fields.One2many('project.task','employee_id',compute='check_task',string='task') #One2many fields to get multiple taskids 
    total_spent_hours=fields.Float(string='total hours',compute='hours_get') #Count total spent hours 
    total_planned_hours=fields.Float(string='total planned hours',compute='hours_get') #Count Total planned hours
    late_time = fields.Float(string='late time',compute='hours_get')
    late_count = fields.Integer(string='late count',compute='hours_get')
    on_time_count = fields.Integer(string='On Time',compute='hours_get')


    #Define function that check task list for particular user_id	
    def check_task(self): 
        for record in self:
            if record.user_id:
                task_ids=self.env['project.task'].search([('user_id','=',record.user_id.id)])
                if task_ids:
                    record.task_ids=task_ids

    #Define function to get total planned hours of each task,total spent hours on each task
    def hours_get(self):
        t_planned=0
        t_spent=0
        on_count=0
        l_time=0
        l_count=0
        for task in self:
	        name=[]
	        if task.task_ids:
		        for record in task.task_ids:	
		            t_planned+=record.planned_hours
		            t_spent+=record.effective_hours   
		            if record.planned_hours==record.effective_hours:
		                on_count+=1
		            if record.remaining_hours<0:
		                l_time+=abs(record.remaining_hours)
		                l_count+=1
        task.total_spent_hours=t_spent
        task.total_planned_hours=t_planned
        task.late_time=l_time
        task.late_count=l_count
        task.on_time_count=on_count	
		         	
class Task(models.Model):
    _inherit="project.task"
    
    employee_id=fields.Many2one('hr.employee', compute="get_emp_id", string='employee') #Define employee_id relationship to get employee task

    @api.multi
    def get_emp_id(self):
        for record in self:
            if record.user_id:
                employees = self.env['hr.employee'].search([('user_id','=',record.user_id.id)]) #Search employee exists or not
                if employees:
                    emp_id = employees[0].id
                    record.employee_id = emp_id
