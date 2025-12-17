# -*- coding: utf-8 -*-
from odoo import http

# class ZohoOdoo(http.Controller):
#     @http.route('/zoho_odoo/zoho_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zoho_odoo/zoho_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('zoho_odoo.listing', {
#             'root': '/zoho_odoo/zoho_odoo',
#             'objects': http.request.env['zoho_odoo.zoho_odoo'].search([]),
#         })

#     @http.route('/zoho_odoo/zoho_odoo/objects/<model("zoho_odoo.zoho_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zoho_odoo.object', {
#             'object': obj
#         })