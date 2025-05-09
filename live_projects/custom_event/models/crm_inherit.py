from odoo import models, fields, api
from odoo.exceptions import ValidationError
import qrcode, json, base64
import io, xlsxwriter
from io import BytesIO
from odoo.tools import json_default

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

    def sale_report_excel(self):
        products = self.mapped('order_line.product_id.name')
        data = {
            'model_id': self.id,
            'date': self.date_order,
            'customer': self.partner_id.name,
            'products': products
        }
        return {
            'type': 'ir.actions.report',
            'data': {'model': 'sale.order',
                    'options': json.dumps(data, default=json_default),
                    'output_format': 'xlsx',
                    'report_name': 'Sales Excel Report',
                    },
            'report_type': 'xlsx',
        }
    def get_xlsx_report(self, data, response):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format(
            {'font_size': '12px', 'align': 'center'})
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px'})
        txt = workbook.add_format({'font_size': '10px', 'align': 'center'})
        sheet.merge_range('B2:I3', 'EXCEL REPORT', head)
        sheet.merge_range('A4:B4', 'Customer:', cell_format)
        sheet.merge_range('C4:D4', data['customer'],txt)
        sheet.merge_range('A5:B5', 'Products', cell_format)
        for i, product in enumerate(data['products'], start=5):
            sheet.merge_range(f'C{i}:D{i}', product, txt)
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()

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