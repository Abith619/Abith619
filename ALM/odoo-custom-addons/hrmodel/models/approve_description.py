# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import date
import re
from dateutil.relativedelta import relativedelta

class approvedescription(models.Model):
    _name = 'approve.description'

    description_field = fields.Char(string='Description' ,required=True)

    unauth_1 = fields.Boolean(String='Unauthorized leave')
    
    
    def addeds(self):
        if self.env.context.get('active_model') == 'hr.leave':
            active_model_id = self.env.context.get('active_id')
            hr_obj = self.env['hr.leave'].search([('id','=',active_model_id)])
            for record in hr_obj:
                record.write({
                    'report_note': self.description_field,
                    'unauth' : self.unauth_1
                })
            for record in hr_obj:
                if (record.department_id.id == 7 or record.department_id.id == 18 or record.department_id.id == 19 or record.department_id.id == 15 or record.department_id.id == 11):
                    cc = 'jagannathan@xbs.in,Manoharraj@xmediasolution.com,projects@xmediasolution.com,hr@xmediasolution.com'
                else:
                    cc = 'hr@xmediasolution.com'
                body = f'<html><h1>{record.display_name}<h1/><br><br><p>{record.employee_id.name} Leaves Approval on {record.display_name} to close for {record.request_date_to}</p></html>'
                vals = {
                    'subject': 'ALM LEAVE NOTIFICATION',
                    'body_html':body,
                    'email_to': record.employee_id.work_email,
                    'email_cc': cc,  
                    'auto_delete': False,
                    'notification': True,
                    'email_from': record.employee_id.parent_id.work_email,
                    }
                mail_id = record.env['mail.mail'].sudo().create(vals)
                mail_id.sudo().send()

    # def cancel(self):
    #     self.state = 'confirm'
    def cancel(self):
        if self.env.context.get('active_model') == 'hr.leave':
            active_model_ids = self.env.context.get('active_id')
            hr_objs = self.env['hr.leave'].search([('id','=',active_model_ids)])
            for records in hr_objs:
                records.write({
                'state' : 'confirm'
                })

class refusedescription(models.Model):
    _name = 'refuse.description'

    refuse_description_field = fields.Char(string='Description' ,required=True)

    def addedr(self):
        if self.env.context.get('active_model') == 'hr.leave':
            active_model_id = self.env.context.get('active_id')
            hr_obj = self.env['hr.leave'].search([('id','=',active_model_id)])
            for record in hr_obj:
                record.write({
                    'report_note': self.refuse_description_field
                })
            for record in hr_obj:
                if (record.department_id.id == 7 or record.department_id.id == 18  or record.department_id.id == 19 or record.department_id.id == 15 or record.department_id.id == 11):
                    cc = 'jagannathan@xbs.in,Manoharraj@xmediasolution.com,projects@xmediasolution.com,hr@xmediasolution.com'
                else:
                    cc = 'hr@xmediasolution.com'
                body = f'<html><h1>{record.display_name}<h1/><br><br><p>{record.employee_id.name} Your leave is refused .<br>{record.display_name} to close for {record.request_date_to}</p></html>'
                vals = {
                    'subject': 'ALM LEAVE NOTIFICATION',
                    'body_html':body,
                    'email_to': record.employee_id.work_email,
                    'email_cc': cc,  
                    'auto_delete': False,
                    'notification': True,
                    'email_from': record.employee_id.parent_id.work_email,
                    }
                mail_id = record.env['mail.mail'].sudo().create(vals)
                mail_id.sudo().send()              



    # def cancel(self):
    #     self.state = 'refuse'
    def cancel(self):
        if self.env.context.get('active_model') == 'hr.leave':
            active_model_ids = self.env.context.get('active_id')
            hr_objs = self.env['hr.leave'].search([('id','=',active_model_ids)])
            for records in hr_objs:
                records.write({
                'state' : 'confirm'
                })