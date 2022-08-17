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

class CreateQuotation(models.TransientModel):
    _name = "task.create.quotation"
    

    task_order_date = fields.Datetime(string='Order Date', required=True, help='Date on which the sale order is confirmed')
    sale_order_products_ids = fields.Many2many('product.product',string='Products',required=True, help='This field displays products of the specific order')

    # This function is for create quotation
    @api.multi
    def create_quotation(self):
        store_products = []
        for record in self:
            if self.env.context.get('active_model') == 'project.task':
                store_id = self.env.context.get('active_id')
                if store_id:
                    task_curr_object = self.env['project.task'].browse(store_id)
                    task_partner_id = self.env['project.task'].browse(store_id).partner_id.id
                    store_task_order_date = record.task_order_date
                    store_sale_order_products = record.sale_order_products_ids
                    so_quotation = {'date_order':store_task_order_date,'partner_id':task_partner_id,'source_project_task_id':store_id}
                    quotation_id = self.env['sale.order'].create(so_quotation)
                    if quotation_id:
                        if store_sale_order_products:
                            for products in store_sale_order_products:
                                product_name = self.env['product.product'].browse(products.id).name
                                product_price = self.env['product.product'].browse(products.id).lst_price
                                order_line_dictionary = {"product_id":products.id,
				                                      "name":product_name,
				                                      "price_unit":product_price,
				                                      "order_id":quotation_id.id,
				                                     } 
                                order_line_id = self.env['sale.order.line'].create(order_line_dictionary)
                        task_curr_object.write({'task_sale_order_id':quotation_id.id})           
        return True
