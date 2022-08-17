# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
import requests
import json

# class ticket_odoo(models.Model):
#     _name = 'ticket_odoo.ticket_odoo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Ticket(models.Model):
    _name = 'ticket.ticket'
    _inherit = ['mail.thread', 'mail.activity.mixin',]

    name = fields.Char(string="Subject", required=True, track_visibility='onchange')
    names = fields.Char(string="Ticket No", readonly=True, required=True, copy=False, default='New',track_visibility='onchange',)
    state = fields.Selection([
        ('yet', 'Not started'),
        ('started', 'In progress'),
        ('done', 'Completed'),
        ('cancel', 'Cancelled'),
        ], string='Status',  track_visibility='onchange', track_sequence=3, default='yet')

    description = fields.Text(help="Describe your problem ." , track_visibility='onchange',)
    reporter_id = fields.Many2one('res.users', ondelete='set null', readonly=True, string="Reporter", index=True, default=lambda self: self.env.user)
    reported_id = fields.Many2one('hr.employee', string='Reported Employee', track_visibility='onchange',domain=[('department_id','=',13)])
    date = fields.Datetime(string="Date", required=True, default=fields.Datetime.now, help="Date of the problem occurred.", track_visibility='onchange',)

    @api.multi
    def action_start(self):
        self.state = 'started'

    @api.multi
    def action_complete(self):
        self.state = 'done'

    @api.model   
    def create(self, vals):
        if vals.get('names', 'New') == 'New':
                vals['names'] = self.env['ir.sequence'].next_by_code('ticket.ticket.sequence') or 'New'
        val = vals.get('names')
        var = vals.get('name')
        con = (str(val) +'-' + var)
        s = requests.Session()
        s.headers.update({"Authorization": "Bearer " + "8o8w8wexxpgjtmqorq4eahemxc"})
        channel_id = 'qqcssyrme3dbfcr9mankj4npna'
        message = 'Hey dude New Service Ticket' +'-'+con
        p = s.post('https://chat.xmedia.in/api/v4/posts', data=json.dumps({
        "channel_id": channel_id,
        "message": message,
        }))


        result = super(Ticket, self).create(vals)       
        return result


