# -*- coding: utf-8 -*-
from odoo import http

# class AutomaticTaskGenerator(http.Controller):
#     @http.route('/automatic_task_generator/automatic_task_generator/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/automatic_task_generator/automatic_task_generator/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('automatic_task_generator.listing', {
#             'root': '/automatic_task_generator/automatic_task_generator',
#             'objects': http.request.env['automatic_task_generator.automatic_task_generator'].search([]),
#         })

#     @http.route('/automatic_task_generator/automatic_task_generator/objects/<model("automatic_task_generator.automatic_task_generator"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('automatic_task_generator.object', {
#             'object': obj
#         })