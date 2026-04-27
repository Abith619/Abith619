from odoo import models, fields
from odoo.exceptions import UserError

class VendorApplication(models.Model):
    _name = 'vendor.application'
    _description = 'Vendor Application'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Applicant Name',
        required=True,
        tracking=True
    )
    email = fields.Char(string='Email', tracking=True)
    phone = fields.Char(string='Phone', tracking=True)
    company_name = fields.Char(string='Company Name', tracking=True)
    street = fields.Char(string='Street')
    city = fields.Char(string='City')
    zip = fields.Char(string='ZIP')
    country_id = fields.Many2one('res.country', string='Country')
    website = fields.Char(string='Website')
    notes = fields.Text(string='Notes')

    stage = fields.Selection([
        ('draft', 'Draft'),
        ('waiting', 'Submitted for Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Stage', default='draft', tracking=True)

    partner_id = fields.Many2one(
        'res.partner',
        string='Vendor',
        readonly=True,
        help='The vendor record created after approval'
    )

    onboarding_date = fields.Date(string='Onboarding Date', tracking=True)

    def action_submit(self):
        for rec in self:
            if rec.stage != 'draft':
                raise UserError("Only draft applications can be submitted.")
            rec.stage = 'waiting'

    def action_approve(self):
        for rec in self:
            if rec.stage != 'waiting':
                raise UserError("Only submitted applications can be approved.")
            partner = rec._create_vendor_partner()
            rec.write({
                'stage': 'approved',
                'partner_id': partner.id,
                'onboarding_date': fields.Date.today(),
            })

    def action_reject(self):
        for rec in self:
            if rec.stage != 'waiting':
                raise UserError("Only submitted applications can be rejected.")
            rec.stage = 'rejected'

    def action_reset_draft(self):
        for rec in self:
            if rec.stage not in ('rejected',):
                raise UserError("Only rejected applications can be reset.")
            rec.stage = 'draft'

    def _create_vendor_partner(self):
        """Create a res.partner record marked as vendor from this application."""
        self.ensure_one()
        if self.partner_id:
            raise UserError(
                f"A vendor record already exists for this application: "
                f"{self.partner_id.name}"
            )
        partner = self.env['res.partner'].create({
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'company_name': self.company_name,
            'street': self.street,
            'city': self.city,
            'zip': self.zip,
            'country_id': self.country_id.id,
            'website': self.website,
            'supplier_rank': 1,
        })
        return partner

    def action_view_vendor(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner',
            'view_mode': 'form',
            'res_id': self.partner_id.id,
        }
