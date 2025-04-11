from odoo import models, fields, api
from odoo.exceptions import ValidationError
import qrcode, json, base64
from io import BytesIO

class EventBooth(models.Model):
    _inherit = 'crm.lead'

    event_id: fields.Many2one = fields.Many2one('event.event', string='Event')
    booth_category: fields.Many2one = fields.Many2one('event.booth.category', string='Booth Applied', domain=[('use_sponsor', '=', True)])
    expected_revenue: fields.Monetary = fields.Monetary(compute="compute_expected_revenue", store=True, currency_field='company_currency')
    company_currency: fields.Many2one = fields.Many2one('res.currency', related='company_id.currency_id', readonly=True)

    @api.depends('booth_category')
    def compute_expected_revenue(self):
        for record in self:
            record.expected_revenue = record.booth_category.price if record.booth_category else 0

class ExhibitorQR(models.Model):
    _inherit = 'event.sponsor'

    qr_code = fields.Binary("QR Code", store=True, attachment=True, compute='_generate_qr_code')

    @api.depends('name', 'url')
    def _generate_qr_code(self):
        for record in self:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(record.url)
            qr.make(fit=True)
            img = qr.make_image(fill="black", back_color="white")
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            qr_base64 = base64.b64encode(buffered.getvalue())
            record.qr_code = qr_base64