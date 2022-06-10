from odoo import models, api, fields
import datetime
import base64


class WhatsappSendMessage(models.TransientModel):
    _name = 'whatsapp.wizard'

    user_id = fields.Many2one('res.partner', string="Recipient")
    mobile = fields.Char(required=True,readonly=True)
    message = fields.Text(string="message", required=True)
    doc_prescription=fields.Binary(string="Attach Prescription")
    doc_invoice=fields.Binary(string="Attach Invoice")

    prescription=fields.Many2one('medical.prescription.order',string="Prescription")
    attachment_ids = fields.Many2many(
    'ir.attachment',string='Attachment')
    # default_values = self.with_context(default_model='medical.prescription.order', default_res_id=res_id).default_get(['model', 'res_id', 'partner_ids', 'message', 'attachment_ids'])
    # values = dict((key, default_values[key]) for key in ['subject', 'body', 'partner_ids', 'email_from', 'reply_to', 'attachment_ids', 'mail_server_id'] if key in default_values)

    def send_message(self):
        if self.message and self.mobile:
            message_string = ''
            message = self.message.split(' ')
            for msg in message:
                message_string = message_string + msg + '%20'
            message_string = message_string[:(len(message_string) - 3)]
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        template_id = ir_model_data.get_object_reference('report_print_prescription', 'prescription_demo_report_template')[1]

        report_template_id = self.env.ref(
            'basic_hms.prescription_whatsapp_report').render_qweb_pdf(self.patient_id.id)
        data_record = base64.b64encode(report_template_id[0])
        ir_values = {
            'name': "Customer Report",
            'type': 'binary',
            'datas': data_record,
            'store_fname': data_record,
            # 'datas_fname': ATTACHMENT_NAME + '.pdf',
            'res_model': self.whatsapp.wizard,
            'res_id': self.id,
            'mimetype': 'application/x-pdf',
        }
        data_id = self.env['ir.attachment'].create(ir_values)
        template = self.template_id
        template.attachment_ids = [(6, 0, [data_id.id])]
        ir_model_data = self.env['ir.model.data']
        template_id = ir_model_data.get_object_reference('report_print_prescription', 'prescription_demo_report_template')[1]
        ctx = {
        'default_model': 'medical.prescription.order',
        'default_res_id': self.ids[0],
        'default_use_template': template_id,
        'default_template_id': template_id,
        'default_body': 'Inspection Report',
        'default_attachment_ids': template_id,
        'default_composition_mode': 'comment',
        }
        return self.env['ir.attachment'].create({
                'type': 'ir.actions.act_url',
                'url': "https://api.whatsapp.com/send?phone="+self.mobile+"&text=" + message_string,
                'target': 'self',
                'default_model': 'medical.prescription.order',
                'default_res_id': self.ids[0],
                'default_use_template': template_id,
                'default_template_id': template_id,
                'default_body': 'Inspection Report',
                'default_attachment_ids': template_id,
                'default_composition_mode': 'comment',
                'res_id': self.id,
                'datas': data_record,
                'store_fname': data_record,
                'attachment_ids': self.attachment_ids and [(6, 0, self.attachment_ids.ids)],
                # 'datas_fname': ATTACHMENT_NAME + '.pdf',
                'res_model': self.whatsapp.wizard,
                # 'res_id': self.id,
                'mimetype': 'application/x-pdf',
                'context': ctx,
                })

    # @api.model
    # def create(self , vals):
    #     vals['name'] = self.env['ir.sequence'].next_by_code('medical.prescription.order') or '/'   
    #     res = super(WhatsappSendMessage, self).create(vals)
    #     orm = self.env['medical.doctor'].search([('patient','=',res.patient_id.id)])
    #     lines=[]
    #     value={
    #         'prescription_alot':res.id,
    #         'date':datetime.now()
    #         }
    #     lines.append((0,0,value))
    #     orm.write({'prescription_patient':lines})
    #     return res

# class CustomerReport(models.Model):
#     _name = 'customer.report'
#     _description = "Customer Report"
#     partner_id = fields.Many2one('res.partner', string="Customer")
#     template_id = fields.Many2one('mail.template', string='Email Template', domain="[('model','=','customer.report')]",
#                                     required=True)
#     line_ids = fields.One2many('account.move', 'report_id', string="Invoice")

#     def send_email_with_attachment(self):
#         report_template_id = self.env.ref(
#             'basic_hms.prescription_order_sequence').render_qweb_pdf(self.id)
#         data_record = base64.b64encode(report_template_id[0])
#         ir_values = {
#             'name': "Customer Report",
#             'type': 'binary',
#             'datas': data_record,
#             'store_fname': data_record,
#             'mimetype': 'application/x-pdf',
#         }
#         data_id = self.env['ir.attachment'].create(ir_values)
#         template = self.template_id
#         template.attachment_ids = [(6, 0, [data_id.id])]
#         email_values = {'email_to': self.partner_id.email,
#                         'email_from': self.env.user.email}
#         template.send_mail(self.id, email_values=email_values, force_send=True)
#         template.attachment_ids = [(3, data_id.id)]
#         return True