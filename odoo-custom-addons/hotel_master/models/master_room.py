from odoo import models, fields, api

class Room(models.Model):
    _name="floor.room"
    _rec_name = 'room_name'
    _inherit = ['mail.thread', 'mail.activity.mixin',]

    room_name = fields.Char(string='Room Name',track_visibility = 'always',required=True)
    floor = fields.Many2one('floor.floor',string= "Floor",track_visibility = 'always',required=True)
    room_type = fields.Many2one('room.type',name="Type")
    status = fields.Selection([('available','Available'),('booked','Booked')] ,default="available",track_visibility = 'always')
    seat = fields.Integer(string="Seats to Book", default=100)
    booked_seats = fields.Integer(string="Seats Booked")
    available_seats = fields.Integer(string="Seats Available")
    
    # @api.onchange('status')
    # def state_change(self):
    #     if self.status == 'available':
    #         self.room_state ='done'

    #     elif self.status == 'booked':
    #          self.room_state ='blocked'
    #     else:
    #         self.room_state ='normal'
