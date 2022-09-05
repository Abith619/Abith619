from odoo import api, fields, models, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta 
import qrcode
import base64
from io import BytesIO
from odoo.exceptions import ValidationError

class FileRoom(models.Model):
    _name='file.room'
    
    patient_id = fields.Many2one('res.partner', string='Patient Name')
    name = fields.Char(string='Exercise')
    attachment = fields.Many2many('ir.attachment',attachment=True,string="Attachment")
    # attachment=fields.Binary(string="Image", attachment=True, store=True,ondelete='cascade')
    # attach_ex = fields.Many2many('file.room', String='Attachment')
