from email.policy import default
from imp import reload
from modulefinder import Module
from odoo import api, fields, models, _
import qrcode
import base64
from io import BytesIO
import random
import time
from time import sleep
from importlib import reload,import_module
# import schedule
import requests
from odoo.exceptions import ValidationError

class WhatsappForms(models.Model):
    _name = 'whatsapp.form.qr'
    
    name = fields.Char(string='Whatsapp QR')
    number = fields.Char(string='Mobile Number')
    
    qr_code = fields.Binary("QR Code", attachment=True )
    random_number = fields.Integer('Rand Num')
    url_link=fields.Char(string="url",default="https://sm.mo.vc/api/send.php?number=919500727093&type=text&message=goodmorning&instance_id=62D117E44E1E8&access_token=a27e1f9ca2347bb766f332b8863ebe9f")
    
    def generate_number(self):
        rand = random.randint(0,100000)
        orm = self.env['whatsapp.form.qr'].search([('id', '=', 2)])
        orm.random_number=rand
        p_details = {
            'Patient Id':rand,
            'url':self.url_link,
            'Mobile':self.number,
        }
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(p_details)
        qr.make(fit=True)
        img = qr.make_image()
        temp = BytesIO()
        img.save(temp, format="PNG")
        qr_image = base64.b64encode(temp.getvalue())
        orm.qr_code = qr_image
        
    # def create(self):
    #     url = "https://sm.mo.vc/api/send.php?number=919500727093&type=text&message=good morning&instance_id=62D117E44E1E8&access_token=a27e1f9ca2347bb766f332b8863ebe9f"

    #     payload={}
    #     headers = {}

    #     response = requests.request("GET", url, headers=headers, data=payload)

    #     print(response.text)