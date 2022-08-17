# -*- coding: utf-8 -*-
from odoo import http

# class TicketOdoo(http.Controller):
#     @http.route('/ticket_odoo/ticket_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ticket_odoo/ticket_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ticket_odoo.listing', {
#             'root': '/ticket_odoo/ticket_odoo',
#             'objects': http.request.env['ticket_odoo.ticket_odoo'].search([]),
#         })

#     @http.route('/ticket_odoo/ticket_odoo/objects/<model("ticket_odoo.ticket_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ticket_odoo.object', {
#             'object': obj
#         })