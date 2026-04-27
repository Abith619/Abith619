from odoo import models, fields

class CrmEnquiryType(models.Model):
    _name = 'crm.enquiry.type'
    _description = 'Enquiry Type'
    _order = 'name'

    name = fields.Char(string="Enquiry Type", required=True)
    active = fields.Boolean(default=True)
