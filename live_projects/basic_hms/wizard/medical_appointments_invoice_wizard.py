# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import Warning,UserError
from datetime import date,datetime

class medical_appointments_invoice_wizard(models.TransientModel):
    _name = "medical.appointments.invoice.wizard"

    def create_invoice(self):
        active_ids = self._context.get('active_ids')
        list_of_ids  = []
        lab_req_obj = self.env['medical.appointment']
        account_invoice_obj  = self.env['account.move']
        account_invoice_line_obj = self.env['account.move.line']
        ir_property_obj = self.env['ir.property']
        for active_id in active_ids: 
            lab_req = lab_req_obj.browse(active_id)
            lab_req.validity_status = 'invoice'
            if lab_req.is_invoiced  == True:
                raise Warning('All ready Invoiced.')
            if lab_req.no_invoice == False:
                sale_journals = self.env['account.journal'].search([('type','=','sale')])
                invoice_vals = {
                'name': self.env['ir.sequence'].next_by_code('medical_app_inv_seq'),
                'invoice_origin': lab_req.name or '',
                'move_type': 'out_invoice',
                'ref': False,
                'partner_id': lab_req.patient_id.patient_id.id or False,
                'partner_shipping_id':lab_req.patient_id.patient_id.id,
                'currency_id':lab_req.patient_id.patient_id.currency_id.id ,
                'invoice_payment_term_id': False,
                'fiscal_position_id': lab_req.patient_id.patient_id.property_account_position_id.id,
                'team_id': False,
                'invoice_date': date.today(),
                'company_id':lab_req.patient_id.patient_id.company_id.id or False ,
                }
                res = account_invoice_obj.create(invoice_vals)
                invoice_line_account_id = False
                if lab_req.consultations_id.id:
                    invoice_line_account_id = lab_req.consultations_id.property_account_income_id.id or lab_req.consultations_id.categ_id.property_account_income_categ_id.id or False 
                if not invoice_line_account_id:
                    inc_acc = ir_property_obj.get('property_account_income_categ_id', 'product.category')
                if not invoice_line_account_id:
                    raise UserError(
                        _('There is no income account defined for this product: "%s". You may have to install a chart of account from Accounting app, settings menu.') %
                        (lab_req.consultations_id.name,))

                tax_ids = []
                taxes = lab_req.consultations_id.taxes_id.filtered(lambda r: not lab_req.consultations_id.company_id or r.company_id == lab_req.consultations_id.company_id)
                tax_ids = taxes.ids
                invoice_line_vals = {
                    'name': lab_req.consultations_id.name or '',
                    'account_id': invoice_line_account_id,
                    'price_unit':lab_req.consultations_id.lst_price,
                    'product_uom_id':lab_req.consultations_id.uom_id.id,
                    'quantity': 1,
                    'product_id':lab_req.consultations_id.id,
                }

                res1 = res.write({'invoice_line_ids' :([(0,0,invoice_line_vals)]) })

                list_of_ids.append(res.id)
                if list_of_ids:
                        imd = self.env['ir.model.data']
                        lab_req_obj_brw = lab_req_obj.browse(self._context.get('active_id'))
                        lab_req_obj_brw.write({'is_invoiced': True})
                        action = imd.sudo().xmlid_to_object('account.action_move_out_invoice_type')
                        list_view_id = imd.sudo().xmlid_to_res_id('account.view_invoice_tree')
                        form_view_id = imd.sudo().xmlid_to_res_id('account.view_move_form')
                        result = {
                                    'name': action.name,
                                    'help': action.help,
                                    'type': action.type,
                                    'views': [ [list_view_id,'tree' ],[form_view_id,'form' ]],
                                    'target': action.target,
                                    'context': action.context,
                                    'res_model': action.res_model,

                                    }
                        if list_of_ids:
                            result['domain'] = "[('id','in',%s)]" % list_of_ids
            else:
                raise UserError(_(' The Appointment is invoice exempt   '))
            return result


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
