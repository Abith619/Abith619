from odoo import api, fields, models


class medical_test_units(models.Model):
    _name = 'test.units'
    _rec_name='unit'


    unit=fields.Char(string='Unit')