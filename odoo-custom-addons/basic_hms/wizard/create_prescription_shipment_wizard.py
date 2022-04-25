# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
from odoo.exceptions import Warning

class create_prescription_shipment(models.TransientModel):
    _name = 'create.prescription.shipment'

    @api.multi
    def create_prescription_shipment(self):
        active_id = self._context.get('active_id')
        prescription_obj = self.env['medical.prescription.order']
        sale_order_obj  = self.env['sale.order']
        sale_order_line_obj = self.env['sale.order.line']
        
        priscription_record = prescription_obj.browse(active_id)
        if priscription_record.is_shipped == True:
            raise Warning('All ready shipped.')
        
        res = sale_order_obj.create({'partner_id':priscription_record.patient_id.patient_id.id ,
                                     'date_invoice': date.today(),
                                      'account_id':priscription_record.patient_id.patient_id.property_account_receivable_id.id,
                                             })
        if priscription_record.prescription_line_ids:
            for p_line in priscription_record.prescription_line_ids:
                 
                res1 = sale_order_line_obj.create({'product_id':p_line.medicament_id.product_id.id ,
                                                 'product_uom': p_line.medicament_id.product_id.uom_id.id,
                                                 'name': p_line.medicament_id.product_id.name,
                                                 'product_uom_qty':1,
                                                 'price_unit':p_line.medicament_id.product_id.lst_price, 
                                                 #'account_id': priscription_record.patient_id.patient_id.property_account_receivable_id.id,
                                                 'order_id': res.id})
        else:
            raise Warning('There is no shipment line.')
        priscription_record.write({'is_shipped': True})
        res.action_confirm()
        result = res.action_view_delivery()
        return result


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
