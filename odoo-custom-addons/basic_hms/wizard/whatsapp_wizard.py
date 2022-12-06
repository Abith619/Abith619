from odoo import models, api, fields, sql_db
from odoo.exceptions import  ValidationError
import base64
import requests, json
from odoo.tools.mimetypes import guess_mimetype
# from twilio.rest import Client


class WhatsappSendMessage(models.TransientModel):

    _name = 'whatsapp.wizard'

    user_id = fields.Many2one('res.partner', string="Recipient")
    mobile = fields.Char(required=True,readonly=True)
    message = fields.Text(string="Message", required=True)
    attachment_id = fields.Many2many('ir.attachment', string='Attachment')

    def send_message(self):
        if self.message and self.mobile:
            message_string = ''
            message = self.message.split(' ')
            for msg in message:
                message_string = message_string + msg + '%20'
            message_string = message_string[:(len(message_string) - 3)]
        attach = self.attachment_id.datas
        
        doc_base64 = base64.b64encode(attach)
        url = "https://dialer-api-sandbox-prod.doocti.com/api/v1/login"
        response = requests.request("POST","https://api.whatsapp.com/send?phone="+self.mobile+"&text=" + message_string ,data=doc_base64)
        # raise ValidationError(response.text)
        # return {
        #         'type': 'ir.actions.act_url',
        #         'url': "https://api.whatsapp.com/send?phone="+self.mobile+"&text=" + message_string,
        #         'target': 'new',
        #         'res_id': self.id,
        #         'data':doc_base64
        #     }
        return response
        
        # account_sid = 'AC920be4f28ca8783fa04f4643eb8e0bed' 
        # auth_token = '[Redacted]' 
        # client = Client(account_sid, auth_token)
        
        # message = client.messages.create( 
        #                       from_='whatsapp:+14155238886',  
        #                       body=self.message,
        #                       to='whatsapp:{}'.format(self.mobile)
        #                   )
        # return message.sid
        
        