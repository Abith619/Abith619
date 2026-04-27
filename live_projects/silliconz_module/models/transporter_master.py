from odoo import models, fields


class TransporterMaster(models.Model):
    _name = 'transporter.master'
    _description = 'Transporter Master'
    _rec_name = 'name'
    _order = 'name asc'

    name = fields.Char(string='Transporter Name', required=True, tracking=True)
    contact_person = fields.Char(string='Contact Person')
    phone = fields.Char(string='Phone')
    mobile = fields.Char(string='Mobile')
    email = fields.Char(string='Email')
    gstin = fields.Char(string='GSTIN')
    address = fields.Text(string='Address')
    active = fields.Boolean(string='Active', default=True)
    notes = fields.Text(string='Notes')
