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

class CreateTask(models.TransientModel):
    _name = "sale.create.task"
    
    project_task_id = fields.Many2one('project.project', string='Project', required=True, help='This field displays project name')
    assigned_to_id = fields.Many2one('res.users', string='Assigned To', required=True, help='Displays the assigned user name')
    deadline = fields.Datetime(string='Deadline', required=True, help='Date which display deadline of the task')
   
    # This function is used for create wizard and assign values to specific fields
    @api.multi
    def create_task(self):
        store_products = []
        for record in self:
            active_model_id = self.env.context.get('active_id')
            if active_model_id:
                order_obj=self.env['sale.order'].browse(active_model_id)
                order_name=order_obj.name
                customer_name=order_obj.partner_id.id
                confirm_date=order_obj.confirmation_date
                products = order_obj.order_line
                if products:
                    for product_store in products:
                        for products_name in product_store:
                            store_products.append(products_name.product_id.id)
                        project_dictionary = {
                                              'user_id':self.assigned_to_id.id,
                                              'project_id':self.project_task_id.id,
                                              'date_deadline':self.deadline,
                                              'sale_order_id':order_obj.id,
                                              'partner_id':customer_name,
                                              'name':order_name,
                                              'sale_order_date':confirm_date,
                                              'products_task_ids':[(6,0,store_products)]
                                             }
                        if project_dictionary:
                            store_task_id = self.env['project.task'].create(project_dictionary)
                            if store_task_id:
                                order_obj.write({'sale_order_task_field_id': store_task_id.id})
        return True
	            
