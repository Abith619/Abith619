from odoo import models, fields, api

class dietFor(models.Model):
    _name='diet.for'

    name= fields.Char(string='Diet Name')

    hosteler=fields.Boolean(string='Hosteler')
    out_side_food=fields.Boolean(string='OutSide Food')
    control=fields.Boolean(string='Control')
    veg=fields.Boolean(string='Veg')
    non_veg=fields.Boolean(string='Non-Veg')
    not_possible=fields.Boolean(string='Not Possible')
    moderate=fields.Boolean(string='Moderate')
    ok_for_all=fields.Boolean(string='Ok for All')

    # def button_rooms(self):
    #     pass
    # def available_rooms(self):
    #     pass


    # cure=fields.Boolean(string='Cure')
    # test_dose=fields.Boolean(string='Test Dose')
    # control=fields.Boolean(string='Control')
    # paliation=fields.Boolean(string='Paliation')
    # chronic=fields.Boolean(string='Chronic')
    # ng=fields.Boolean(string='NG')
    # maintance=fields.Boolean(string='Maintance')
    # nt=fields.Boolean(string='NT')