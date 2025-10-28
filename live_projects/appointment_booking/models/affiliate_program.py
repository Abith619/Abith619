from odoo import models, fields, api, _

class AffiliateProgram(models.Model):
    _name = 'affiliate.program'
    _rec_name = 'name'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Affiliate Program'

    name = fields.Char(string='Name', required=True)
    company_name = fields.Char(string='Company Name')
    designation = fields.Char(string='Designation')
    contact_number = fields.Char(string='Contact Number')
    email = fields.Char(string='Email', required=True)
    linked_in_profile = fields.Char(string='LinkedIn Profile Link')
    industry_influence_focus = fields.Text(string='Industry Influence/Focus Area')
    expected_monthly_referrals = fields.Integer(string='Expected Monthly Referrals')
    pan_gst = fields.Image(string='PAN/GST')
