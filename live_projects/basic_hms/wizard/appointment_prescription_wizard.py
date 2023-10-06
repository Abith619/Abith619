# # -*- coding: utf-8 -*-
# # Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
# 
# from odoo import api, fields, models, _
# from datetime import date,datetime
# 
# class appointment_prescription_wizard(models.TransientModel):
#     _name = "appointment.prescription.wizard"
# 
#     prescription_physician_id = fields.Many2one('medical.physician','Name Of Physician')
#     start_date = fields.Date("Start Date")
#     end_date = fields.Date('End Date')
# 
# # vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: