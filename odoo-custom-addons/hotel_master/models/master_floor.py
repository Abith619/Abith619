from odoo import models, fields, api

class Floor(models.Model):
    _name="floor.floor"
    _rec_name ="name"
    _inherit = ['mail.thread', 'mail.activity.mixin',]

    name = fields.Char(string='Floor Name',track_visibility = 'always',required=True)

    floor_incharge = fields.Many2one('res.partner',string='Floor Incharge')
    rooms = fields.Integer(compute='room_count',string="Rooms")
    booked_room = fields.Integer(compute='booked_count', string="Booked Rooms")
    available_room = fields.Integer(compute='available_count', string="Available Rooms")

    @api.multi
    def button_rooms(self, cr,  context=None):
        return {
    'name': "Rooms",
    'view_mode': 'form',
    'res_model': 'floor.room',
    'view_type': 'form',
    'context': {
    'default_floor':self.id,
    # 'default_salary_structure':self.plans_offered.id,
    # 'default_contacts':self.contact.id,
    } ,
    'type': 'ir.actions.act_window',
    }

    @api.multi
    def button_room(self, cr,  context=None):
        return {
    'name': "Floor Room",
    'domain':[('floor', '=', self.id)],
    'view_mode': 'tree,form',
    'res_model': 'floor.room',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }

    @api.multi
    def booked_rooms(self, cr,  context=None):
        return {
    'name': "Floor Room",
    'domain':[('status', '=', 'booked')],
    'view_mode': 'tree,form,graph',
    'res_model': 'floor.room',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }
    
    @api.multi
    def available_rooms(self, cr,  context=None):
        return {
    'name': "Floor Room",
    'domain':[('status', '=', 'available')],
    'view_mode': 'tree,form,graph',
    'res_model': 'floor.room',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }
    @api.depends('rooms')
    def room_count(self):
        for i in self:
            count2 = self.env['floor.room'].search_count([('floor', '=', i.id)])
            self.rooms= count2
    @api.depends('available_room')
    def available_count(self):
        for i in self:
            count1 = self.env['floor.room'].search_count([('floor', '=', i.id),('status', '=', 'available')])
            self.available_room = count1
    @api.depends('booked_room')
    def booked_count(self):
        for i in self:
            count = self.env['floor.room'].search_count([('floor', '=', i.id),('status', '=', 'booked')])
            self.booked_room = count
