# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import date
import datetime
import re
from dateutil.relativedelta import relativedelta


class Employee_Leave(models.Model):
    _inherit = 'hr.leave'


    note_ids = fields.Char(string="Rufuse Reason")
    approve_note = fields.Char(string="Approve Reason")
    request_date_from_period = fields.Selection([('am', 'Forenoon'),
                                                 ('pm', 'Afternoon')],string="Date Period Start", default='am')
    @api.multi
    def action_approve(self):
        # self.send(1)
        # self.myfun()
        self.state = 'validate'
        approve_description = False
        return {
                'name': 'Approve description',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'approve.description',
                'views': [(approve_description, 'form')],
                'view_id':self.env.ref('hrmodel.approve_description_form').id,
                'target': 'new',
            }

    # def send(self,val):
    #     for record in self:
    #         if (record.department_id.id == 7 or record.department_id.id == 18):
    #             cc = 'jagannathan@xbs.in,Manoharraj@xmediasolution.com,projects@xmediasolution.com,hr@xmediasolution.com'
    #         else:
    #             cc = ''
    #         if val == 1:
    #             body = f'<html><h1>{record.display_name}<h1/><br><br><p>{record.employee_id.name} Leaves Approval on {record.display_name} to close for {record.request_date_to}</p></html>'
    #         if val == 2:
    #             body = f'<html><h1>{record.display_name}<h1/><br><br><p>{record.employee_id.name} Your leave is refused .<br>{record.display_name} to close for {record.request_date_to}</p></html>'
    #         vals = {
    #             'subject': 'ALM LEAVE NOTIFICATION',
    #             'body_html':body,
    #             'email_to': record.employee_id.work_email,
    #             'email_cc': cc,  
    #             'auto_delete': False,
    #             'notification': True,
    #             'email_from': record.employee_id.parent_id.work_email,
    #             }
    #         mail_id = record.env['mail.mail'].sudo().create(vals)
    #         mail_id.sudo().send()


    @api.multi
    def action_refuse(self):
        # self.send(2)
        self.state = 'refuse'
        refuse_description = False
        return {
                'name': 'Refuse description',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'refuse.description',
                'views': [(refuse_description, 'form')],
                'view_id':self.env.ref('hrmodel.refuse_description_form').id,
                'target': 'new',
            }

    # def sended(self):
    #     cc = []
    #     for record in self:
    #         if record.department_id.id == 7:
    #             id_s = self.env['hr.employee'].search([('department_id','=',8)])
    #             id_s1 = self.env['hr.employee'].search([('department_id','=',16)])
    #             for i in id_s:
    #                 mail = i.work_email
    #                 cc.append(mail)
    #             for j in id_s1:
    #                 mail_1 = j.work_email
    #                 cc.append(mail_1)
    #         else:
    #             cc = ''
  
        
    #         val_s = {
    #             'subject': 'ALM LEAVE NOTIFICATION',
    #             'body_html':f'<html><h1>{record.display_name}<h1/><br><br><p>{record.employee_id.name} Your leave is refused .<br>{record.display_name} to close for {record.request_date_to}</p></html>',
    #             'email_to': record.employee_id.work_email,
    #             'email_cc': cc,
    #             'auto_delete': False,
    #             'notification': True,
    #             'email_from': record.employee_id.parent_id.work_email,
    #             }
    #         mail_id = record.env['mail.mail'].sudo().create(val_s)
    #         mail_id.sudo().send()


    # def myfun(self):
    #     for rec in self:
    #         f1 = rec.request_date_from
    #         f2 = rec.request_date_to
    #         emp = rec.employee_id.id
    #         today = datetime.datetime.now().date()
    #         val = datetime.datetime.strptime(str(today),"%Y-%m-%d")
    #         yesterday = f1
    #         date_time_obj = datetime.datetime.strptime(str(yesterday), '%Y-%m-%d')
    #         if val > date_time_obj:
    #             t1 = "03:30:00"
    #             t2 = "12:30:00"
    #             date1 = datetime.datetime.strptime(str(f1), "%Y-%m-%d").date()
    #             date2 = datetime.datetime.strptime(str(f2), "%Y-%m-%d").date()
    #             day = datetime.timedelta(days=1)
    #             while date1 <= date2:
    #                 d1 = date1.strftime('%Y-%m-%d')
    #                 checkin = d1.replace('-','')+" "+t1
    #                 checkout = d1.replace('-','')+" "+t2
    #                 list2 = {
    #                 "employee_id" :emp,
    #                 "employee_leave":'leave',
    #                 "check_in" :datetime.datetime.strptime(checkin, "%Y%m%d %H:%M:%S"),
    #                 "check_out":datetime.datetime.strptime(checkout, "%Y%m%d %H:%M:%S"),
    #                     }
    #                 var1 = self.env['hr.attendance'].create(list2)
    #                 date1 = date1 + day
