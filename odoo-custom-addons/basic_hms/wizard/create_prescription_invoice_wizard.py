# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
from odoo.exceptions import Warning

class create_prescription_invoice(models.TransientModel):
    _name = 'create.prescription.invoice'

    @api.multi
    def create_prescription_invoice(self):
        active_ids = self._context.get('active_ids')
        active_ids = active_ids or False
        lab_req_obj = self.env['medical.prescription.order']
        account_invoice_obj  = self.env['account.invoice']
        account_invoice_line_obj = self.env['account.invoice.line']
        ir_property_obj = self.env['ir.property']
        inv_list =[]
        lab_reqs = lab_req_obj.browse(active_ids)
        for lab_req in lab_reqs:
            if len(lab_req.prescription_line_ids) < 1:
                raise Warning('At least one prescription line is required.')

            if lab_req.is_invoiced == True:
                raise Warning('All ready Invoiced.')
            sale_journals = self.env['account.journal'].search([('type','=','sale')])
            invoice_vals = {
            'name': "Customer Invoice",
            'origin': lab_req.name or '',
            'type': 'out_invoice',
            'reference': False,
            'partner_id': lab_req.patient_id.patient_id.id,
            'date_invoice': date.today(),
            'account_id':lab_req.patient_id.patient_id.property_account_receivable_id.id,
            'journal_id':sale_journals and sale_journals[0].id or False,
            'partner_shipping_id':lab_req.patient_id.patient_id.id,
            'currency_id':lab_req.patient_id.patient_id.currency_id.id ,
            'payment_term_id': False,
            'fiscal_position_id': lab_req.patient_id.patient_id.property_account_position_id.id,
            'team_id': False,
            'comment': "Invoice Created from Medical Appointment",
            'company_id':lab_req.patient_id.patient_id.company_id.id or False ,
            }

            res = account_invoice_obj.create(invoice_vals)
            for p_line in lab_req.prescription_line_ids: 
            
                invoice_line_account_id = False
                if p_line.medicament_id.product_id.id:
                    invoice_line_account_id = p_line.medicament_id.product_id.property_account_income_id.id or p_line.medicament_id.product_id.categ_id.property_account_income_categ_id.id or False 
                if not invoice_line_account_id:
                    invoice_line_account_id = ir_property_obj.get('property_account_income_categ_id', 'product.category')
                if not invoice_line_account_id:
                    raise UserError(
                        _('There is no income account defined for this product: "%s". You may have to install a chart of account from Accounting app, settings menu.') %
                        (p_line.medicament_id.product_id.name,))

                tax_ids = []
                taxes = p_line.medicament_id.product_id.taxes_id.filtered(lambda r: not p_line.medicament_id.product_id.company_id or r.company_id == p_line.medicament_id.product_id.company_id)
                tax_ids = taxes.ids
                
                invoice_line_vals = {
                    'name': p_line.medicament_id.product_id.display_name or '',
                    'origin': p_line.name or '',
                    'account_id': invoice_line_account_id,
                    'price_unit':p_line.medicament_id.product_id.lst_price,
                    'uom_id': p_line.medicament_id.product_id.uom_id.id,
                    'quantity': 1,
                    'product_id':p_line.medicament_id.product_id.id ,
                    'invoice_id': res.id,
                    'invoice_line_tax_ids': [(6, 0, tax_ids)],
                }

                res1 = account_invoice_line_obj.create(invoice_line_vals)

            inv_list.append(res.id)
            if res:                     
                imd = self.env['ir.model.data']
                lab_reqs.write({'is_invoiced': True}) 
                action = imd.xmlid_to_object('account.action_invoice_tree1')
                list_view_id = imd.xmlid_to_res_id('account.invoice_tree')
                form_view_id = imd.xmlid_to_res_id('account.invoice_form')
                result = {      
                    
                                'name': action.name,
                                'help': action.help,
                                'type': action.type,
                                'views': [ (list_view_id ,'tree'),(form_view_id,'form')],
                                'target': action.target,
                                'context': action.context,
                                'res_model': action.res_model,
                            }
                
                if res:
                    result['domain'] = "[('id','in',%s)]" % inv_list
        return result  

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
