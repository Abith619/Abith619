from odoo import models, fields, api
import logging, datetime, random
from odoo.exceptions import ValidationError

class HotelBooking(models.Model):
    _name="booking.booking"
    _rec_name ="name"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Many2one('res.partner',string='Customer', required=True ,track_visibility = 'always') 
    booked_by = fields.Many2one('res.users',string="Booked by", default=lambda self: self.env.user, readonly=True)
    bill_no = fields.Char(string="Service Number", readonly=True, required=True, copy=False, default='New', track_visibility = 'always')    
    select_room=fields.One2many('booking.line','y_name')
    state =fields.Selection([
        ('draft','Draft'),('cancel','Cancelled'),
        ('confirm','Confirmed'),('closed','Closed')],string='Status',default='draft')
    total1 = fields.Float(string='Total', store=True)
#                             Print-Invoice Button
    def create_invoice(self):
            return{
        'name': "Paid ",
        'type': 'ir.actions.act_window',
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'account.invoice',
        'view_id': self.env.ref('account.invoice_form').id,
        'context': {
            'default_partner_id': self.name.id,
        },
        'target': 'new'
    }

    #                       State-Confirm
    def confirm(self):
        for rec in self:
            rec.state='confirm'

        rec=self.env['booking.line'].search([])
        for i in rec:
                val = self.env['floor.room'].search([('id','=',i.room.id)])
        for j in val:
                val.write({'status':'booked'})
#                       State-Cancell
    def cancel(self):
        for rec in self:
            rec.state='cancel'

#                               Send E-Mail 
    def action_send_email(self):
        self.ensure_one()
        compose_form_id = False
        return {
        'name': 'Compose Email',
        'type': 'ir.actions.act_window',
        'view_mode': 'form',
        'res_model': 'mail.compose.message',
        'views': [(compose_form_id, 'form')],
        'view_id': compose_form_id,
        'target': 'new',
    }

    @api.model
    def create(self, vals):
        if vals.get('bill_no', 'New') == 'New':
            vals['bill_no'] = self.env['ir.sequence'].next_by_code('self.service') or 'New'
        result = super(HotelBooking,self).create(vals)
        return result


        # for i in self:
        #     val = self.env['floor.room'].search([('id','=',i.room.id)])
        # for j in val:
        #     val.write({'status':'booked'})
    @api.multi
    def close(self):

        self.state="closed"
        
        rec=self.env['booking.line'].search([])

        for i in rec:
            val = self.env['floor.room'].search([('id','=',i.room.id)])
        for j in val:
                val.write({'status':'available'})

    @api.onchange('select_room')
    def write_fun(self):
        sums = []
        for i in self:
            for j in i.select_room:
                sums.append(j.total)
            i.total1 = sum(sums)
  

class HotelLine(models.Model):
    _name="booking.line"
    floors=fields.Many2one('floor.floor',string='Floor', required=True)
    room = fields.Many2one('floor.room',string= "room",required=True)
    y_name=fields.Many2one('booking.booking',string='Name')
    amount=fields.Float(string="Price")
    tax=fields.Many2many("account.tax",string="Tax")
    room_type=fields.Many2one('room.type',string='Room Type', required=True,related="room.room_type")
    check_in=fields.Datetime(string="Check In")
    check_out=fields.Datetime(string="Check Out")
    total = fields.Float(string='Total', store=True, compute='_get_sum', tracking=4)

    @api.depends('amount','tax')
    def _get_sum(self):
        for rec in self:
            rec.update({
                'total': rec.amount + sum(tax.amount for tax in rec.tax)
            })

    @api.onchange('floors')
    def onchange_project(self):
        for rec in self:
            return {'domain':{'room':[('floor', '=', rec.floors.id),('status','=','available')]}}


    # @api.onchange('room')
    # def onchange_fun(self):
    #     for i in self:
    #         val = self.env['floor.room'].search([('id','=',i.room.id)])
    #         for j in val:
    #             val.write({'status':'booked'})


    # @api.multi 
    # def onchange_myfun(self):
    #     for i in self:
    #         val = self.env['floor.room'].search([('id','=',i.room.id)])
    #         for j in val:
    #             val.write({'status':'available'})

        # for record in self.select_room:
        #         record.unlink()