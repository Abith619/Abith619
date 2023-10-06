from odoo import api, fields, models

class CityMaster(models.Model):
    _name='res.city'


    name=fields.Char(string="City Name")