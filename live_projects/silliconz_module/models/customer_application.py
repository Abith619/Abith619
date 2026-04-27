from odoo import models, fields, api, _
from odoo.exceptions import UserError


class CustomerApplication(models.Model):
    _name = 'customer.application'
    _description = 'Customer Application'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    # ── Identity ──────────────────────────────────────────────────────────────
    company_type = fields.Selection(
        [('company', 'Company'), ('person', 'Individual')],
        string='Company Type',
        default='company',
        required=True,
        tracking=True,
    )
    name = fields.Char(string='Customer Name', required=True, tracking=True)
    parent_id = fields.Many2one(
        'customer.application',
        string='Company',
        domain=[('company_type', '=', 'company')],
    )

    # ── Contact Info ──────────────────────────────────────────────────────────
    email = fields.Char(string='Email', tracking=True)
    phone = fields.Char(string='Phone', tracking=True)
    mobile = fields.Char(string='Mobile')
    website = fields.Char(string='Website')

    # ── Address ───────────────────────────────────────────────────────────────
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street2')
    city = fields.Char(string='City')
    state_id = fields.Many2one('res.country.state', string='State', domain="[('country_id', '=', country_id)]")
    zip = fields.Char(string='ZIP')
    country_id = fields.Many2one('res.country', string='Country')

    # ── Business Info ─────────────────────────────────────────────────────────
    vat = fields.Char(string='GSTIN / Tax ID', tracking=True)
    category_id = fields.Many2many('res.partner.category', string='Tags')
    ref = fields.Char(string='Internal Reference')

    # ── GST / Compliance ─────────────────────────────────────────────────────
    msme_acknowledgement = fields.Boolean(
        string='MSME Acknowledgement',
        default=False,
        tracking=True,
        help='Check if the customer has submitted MSME registration acknowledgement.',
    )
    supply_type = fields.Selection(
        [
            ('b2b', 'B2B (Business to Business)'),
            ('b2c', 'B2C (Business to Consumer)'),
            ('export', 'Export / Zero-Rated'),
            ('sez', 'SEZ Supply'),
            ('exempt', 'Exempt Supply'),
        ],
        string='Supply Type',
        tracking=True,
        help='Nature of supply for GST classification.',
    )
    tax_applicability = fields.Selection(
        [
            ('taxable', 'Taxable'),
            ('exempt', 'Exempt'),
            ('nil_rated', 'Nil Rated'),
            ('non_gst', 'Non-GST Supply'),
            ('zero_rated', 'Zero Rated (Export/SEZ)'),
        ],
        string='Tax Applicability',
        tracking=True,
        help='GST tax applicability category for this customer.',
    )
    rcm_acknowledgement = fields.Boolean(
        string='RCM Acknowledgement',
        default=False,
        tracking=True,
        help='Check if Reverse Charge Mechanism (RCM) is applicable and acknowledged for this customer.',
    )
    onboarding_date = fields.Datetime(string='Onboarding Date', readonly=True, copy=False)

    # ── Contacts tab ─────────────────────────────────────────────────────────
    contact_ids = fields.One2many(
        'customer.application.contact',
        'application_id',
        string='Contacts',
    )

    # ── Workflow ──────────────────────────────────────────────────────────────
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('submitted', 'Waiting for Approval'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
        ],
        string='Status',
        default='draft',
        required=True,
        tracking=True,
        copy=False,
    )
    rejection_reason = fields.Text(string='Rejection Reason', tracking=True)
    partner_id = fields.Many2one('res.partner', string='Created Partner', readonly=True, copy=False)
    submitted_by = fields.Many2one('res.users', string='Submitted By', readonly=True, copy=False)
    approved_by = fields.Many2one('res.users', string='Approved By', readonly=True, copy=False)
    submitted_date = fields.Datetime(string='Submitted On', readonly=True, copy=False)
    approved_date = fields.Datetime(string='Approved On', readonly=True, copy=False)

    # ── Computed ──────────────────────────────────────────────────────────────
    is_company = fields.Boolean(compute='_compute_is_company', store=True)

    @api.depends('company_type')
    def _compute_is_company(self):
        for rec in self:
            rec.is_company = rec.company_type == 'company'

    # ── Actions ───────────────────────────────────────────────────────────────

    def action_submit(self):
        for rec in self:
            if rec.state != 'draft':
                raise UserError(_("Only draft applications can be submitted."))
            rec.write({
                'state': 'submitted',
                'submitted_by': self.env.user.id,
                'submitted_date': fields.Datetime.now(),
            })
            rec.message_post(
                body=_("Application submitted for approval by %s.", self.env.user.name),
                subtype_xmlid='mail.mt_note',
            )

    def action_approve(self):
        for rec in self:
            if rec.state != 'submitted':
                raise UserError(_("Only submitted applications can be approved."))
            partner = rec._create_customer_partner()
            rec.write({
                'state': 'approved',
                'approved_by': self.env.user.id,
                'approved_date': fields.Datetime.now(),
                'partner_id': partner.id,
                'onboarding_date': fields.Datetime.now(),
            })
            rec.message_post(
                body=_("Application approved by %s. Customer record created: %s",
                        self.env.user.name, partner.name),
                subtype_xmlid='mail.mt_note',
            )

    def action_reject(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Rejection Reason'),
            'res_model': 'customer.application.reject.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_application_id': self.id},
        }

    def action_reset_draft(self):
        for rec in self:
            if rec.state != 'rejected':
                raise UserError(_("Only rejected applications can be reset to draft."))
            rec.write({'state': 'draft', 'rejection_reason': False})
            rec.message_post(
                body=_("Application reset to draft by %s.", self.env.user.name),
                subtype_xmlid='mail.mt_note',
            )

    def action_open_partner(self):
        self.ensure_one()
        if not self.partner_id:
            raise UserError(_("No partner created yet."))
        return {
            'type': 'ir.actions.act_window',
            'name': _('Customer'),
            'res_model': 'res.partner',
            'view_mode': 'form',
            'res_id': self.partner_id.id,
        }

    # ── Internal ──────────────────────────────────────────────────────────────

    def _create_customer_partner(self):
        """Create res.partner with customer_rank=1 upon approval."""
        self.ensure_one()
        partner = self.env['res.partner'].create({
            'name': self.name,
            'company_type': self.company_type,
            'is_company': self.is_company,
            'email': self.email,
            'phone': self.phone,
            'website': self.website,
            'street': self.street,
            'street2': self.street2,
            'city': self.city,
            'state_id': self.state_id.id if self.state_id else False,
            'zip': self.zip,
            'country_id': self.country_id.id if self.country_id else False,
            'vat': self.vat,
            'category_id': [(6, 0, self.category_id.ids)],
            'ref': self.ref,
            'customer_rank': 1,
            'msme_acknowledgement': self.msme_acknowledgement,
            'supply_type': self.supply_type,
            'tax_applicability': self.tax_applicability,
            'rcm_acknowledgement': self.rcm_acknowledgement,
        })
        for contact in self.contact_ids:
            self.env['res.partner'].create({
                'name': contact.name,
                'parent_id': partner.id,
                'type': contact.contact_type,
                'email': contact.email,
                'phone': contact.phone,
                'function': contact.function,
            })
        return partner


class CustomerApplicationContact(models.Model):
    _name = 'customer.application.contact'
    _description = 'Customer Application Contact'

    application_id = fields.Many2one('customer.application', string='Application', ondelete='cascade')
    name = fields.Char(string='Contact Name', required=True)
    contact_type = fields.Selection(
        [
            ('contact', 'Contact'),
            ('invoice', 'Invoice Address'),
            ('delivery', 'Delivery Address'),
            ('other', 'Other Address'),
            ('private', 'Private Address'),
        ],
        string='Address Type',
        default='contact',
    )
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    mobile = fields.Char(string='Mobile')
    function = fields.Char(string='Job Position')
