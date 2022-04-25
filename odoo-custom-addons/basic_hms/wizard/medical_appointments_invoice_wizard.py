# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import Warning,UserError
from datetime import date,datetime

class medical_appointments_invoice_wizard(models.TransientModel):
    _name = "medical.appointments.invoice.wizard"

    @api.multi
    def create_invoice(self):
        active_ids = self._context.get('active_ids')
        list_of_ids  = []
        lab_req_obj = self.env['medical.appointment']
        account_invoice_obj  = self.env['account.invoice']
        account_invoice_line_obj = self.env['account.invoice.line']
        ir_property_obj = self.env['ir.property']
        for active_id in active_ids: 
            lab_req = lab_req_obj.browse(active_id)
            if lab_req.is_invoiced  == True:
                raise Warning('All ready Invoiced.')
            if lab_req.no_invoice == False:
                sale_journals = self.env['account.journal'].search([('type','=','sale')])
                invoice_vals = {
                'name': "Customer Invoice",
                'origin': lab_req.name or '',
                'type': 'out_invoice',
                'reference': False,
                'account_id': lab_req.patient_id.patient_id.property_account_receivable_id.id or False,
                'journal_id':sale_journals and sale_journals[0].id or False,
                'partner_id': lab_req.patient_id.patient_id.id or False,
                'partner_shipping_id':lab_req.patient_id.patient_id.id,
                'currency_id':lab_req.patient_id.patient_id.currency_id.id ,
                'payment_term_id': False,
                'fiscal_position_id': lab_req.patient_id.patient_id.property_account_position_id.id,
                'team_id': False,
                'comment': "Invoice Created from Medical Appointment",
                'date_invoice': date.today(),
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

                res1 = account_invoice_line_obj.create({
                                            'origin': lab_req.name or '',
                                            'product_id':lab_req.consultations_id.id ,
                                             'uom_id': lab_req.consultations_id.uom_id.id,
                                             'name': lab_req.consultations_id.name or '',
                                             'quantity':1,
                                             'price_unit':lab_req.consultations_id.lst_price,
                                             'account_id': invoice_line_account_id,
                                             'invoice_id': res.id,
                                             'invoice_line_tax_ids': [(6, 0, tax_ids)],
                                             })
                list_of_ids.append(res.id)
                if list_of_ids:
                        imd = self.env['ir.model.data']
                        lab_req_obj_brw = lab_req_obj.browse(self._context.get('active_id'))
                        lab_req_obj_brw.write({'is_invoiced': True})
                        action = imd.xmlid_to_object('account.action_invoice_tree1')
                        list_view_id = imd.xmlid_to_res_id('account.invoice_tree')
                        form_view_id = imd.xmlid_to_res_id('account.invoice_form')
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
