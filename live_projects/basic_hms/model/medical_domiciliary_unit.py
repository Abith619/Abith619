# # -*- coding: utf-8 -*-
# # Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
# 
# from odoo import api, fields, models, _
# 
# class medical_domiciliary_unit(models.Model):
#     _name = "medical.domiciliary.unit"
# 
# 
#     def get_data (self):
#         res_partner_obj  = self.env['res.partner']
#         user_ids = res_partner_obj.search( [('du_id.name', '=', self.name)])
#         print user_ids
#         return [(6, 0, user_ids)]
# 
# 
#     name = fields.Char(string="Code")
#     desc = fields.Char(string="Desc")
#     address_street = fields.Char(string="Street")
#     address_street_number = fields.Integer(string="Number")
#     address_street_bis = fields.Char(string="Apartment")
#     address_district = fields.Char(string="District")
#     address_municipality = fields.Char(string="Municipality")
#     address_city = fields.Char(string="City")
#     address_zip = fields.Integer(string="Zip Code")
#     state_id = fields.Many2one('res.country.state','Province')
#     address_country = fields.Many2one('res.country','Country')
#     latitude = fields.Char(string="Latitude")
#     longitude = fields.Char(string="Longitude")
#     urladdr = fields.Char(string="OSM Map")
#     housing = fields.Selection([
#             ('0', 'Shanty, deficient sanitary conditions'),
#             ('1', 'Small, croeded but with good sanitary conditions'),
#             ('2', 'Comfortable and good sanitary conditions'),
#             ('3', 'Roomy and excellent sanitary conditions'),
#             ('4', 'Luxury and excellent sanitary conditions'),
#         ], 'Conditions', sort=False)
#     dwelling = fields.Selection([
#             ('singale_house', 'Single/Detached House'),
#             ('apartment', 'Apartment'),
#             ('townhouse', 'Townhouse'),
#             ('factory', 'Factory'),
#             ('buliding', 'Building'),
#             ('mobilehome', 'Mobile house'),
#         ], 'Type', sort=False)
#     materials = fields.Selection([
#             ('concrete', 'Concrete'),
#             ('adobe', 'Adobe'),
#             ('wood', 'Wood'),
#             ('mud', 'Mud/Straw'),
#             ('stone', 'Stone'),
#         ], 'Material', sort=False)
#     roof_type = fields.Selection([
#             ('concrete', 'Concrete'),
#             ('adobe', 'Adobe'),
#             ('wood', 'Wood'),
#             ('mud', 'Mud/Straw'),
#             ('tuatch', 'Thatched'),
#             ('stone', 'Stone'),
#         ], 'Roof', sort=False)
#     total_surface = fields.Integer(string="Surface")
#     bedrooms = fields.Integer(string="Bedrooms")
#     bathrooms = fields.Integer(string='Bathrooms')
#     water = fields.Boolean(string='Running Water')
#     sewers = fields.Boolean(string='Sanitary Sewers')
#     trash = fields.Boolean(string='Trash recollection')
#     electricity = fields.Boolean(string='Electrical supply')
#     gas = fields.Boolean(string='Gas supply')
#     telephone = fields.Boolean(string='Telephone')
#     television = fields.Boolean(string='Television')
#     internet = fields.Boolean(string='Internet')
#     operational_sector = fields.Many2one('medical.operational_sector','Operational Sector')
#     members_ids = fields.One2many('res.partner','domiciliary_id', )
# 
# 
#     info = fields.Text(string="Extra info")
# 
# 
# # vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: