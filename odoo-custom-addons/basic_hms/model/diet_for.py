from odoo import models, fields, api

class dietFor(models.Model):
    _name='diet.for'
    _rec_name='name'

    name=fields.Char('Diet Name')

    # hosteler=fields.Boolean(string='Hosteler')
    # out_side_food=fields.Boolean(string='OutSide Food')
    # control=fields.Boolean(string='Control')
    # veg=fields.Boolean(string='Veg')
    # non_veg=fields.Boolean(string='Non-Veg')
    # not_possible=fields.Boolean(string='Not Possible')
    # moderate=fields.Boolean(string='Moderate')
    # ok_for_all=fields.Boolean(string='Ok for All')

    # def button_rooms(self):
    #     pass
    # def available_rooms(self):
    #     pass

class treatmentFor(models.Model):
    _name='treatment.for'

    name =fields.Char("Treatment For")


class documentFor(models.Model):
    _name='document.for'
    _rec_name='document_name'

    document_name=fields.Char(string="Document Name")



    # gender= fields.Selection([('m', 'Male'),('f', 'Female')],string='Gender')
