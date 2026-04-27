from odoo import models, fields


class ResPartnerCustomInherit(models.Model):
    _inherit = 'res.partner'

    # ── GST / Compliance ──────────────────────────────────────────────────────
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
