from odoo import models, fields, api

class Roomtype(models.Model):
    _name="room.type"
    _rec_name = 'type_name'
    _inherit = ['mail.thread', 'mail.activity.mixin',]

    type_name = fields.Char(string='Type Name',track_visibility = 'always',required= True)