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
from odoo.exceptions import ValidationError

class ProjectTask(models.Model):
    _inherit="project.task"


    task_sale_order_id = fields.Many2one('sale.order', string='Sale Order',readonly=True, help='This field displays Sales Order')

    # This function is used to check customer is selected or not if customer is selected than create a wizard
    @api.multi
    def create_warning(self,context=None):
        for recrod in self:
            store_partner_id_task = self.partner_id.id
            if store_partner_id_task:
                return {
                        'name': ('Create Quotation'),
                        'view_type': 'form',
                        'view_mode': 'form',
                        'res_model': 'task.create.quotation',
                        'view_id': False,
                        'type': 'ir.actions.act_window',
                        'target':'new'
                       }
            else:
                raise ValidationError(_('Please Select Customer'))



    
