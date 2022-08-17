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
from odoo.exceptions import ValidationError

class WhatsappForms(models.Model):
    _name = 'whatsapp.form.qr'
    
    name = fields.Char(string='Whatsapp QR')
    number = fields.Char(string='Mobile Number')
    
    qr_code = fields.Binary("QR Code", attachment=True )
    random_number = fields.Integer('Rand Num')
    
    def generate_number(self):
        rand = random.randint(0,9)
        orm = self.env['whatsapp.form.qr'].search([('id', '=', 4)])   
        orm.random_number=rand
        p_details={
            'Patient_Id':rand,
            'Patient_Name':orm.name,
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