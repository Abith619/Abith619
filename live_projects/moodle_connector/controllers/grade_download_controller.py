import json
from odoo import http
from odoo.http import request, content_disposition
from odoo.tools import html_escape


class CSVReportController(http.Controller):

    @http.route('/csv_reports', type='http', auth='user', csrf=False)
    def get_csv_report(self, model, options, output_format,
                        report_name, token=None, **kwargs):
        try:
            options = json.loads(options)
            records = request.env[model].browse(options.get('ids', []))

            if output_format == 'csv':
                response = request.make_response(
                    None,
                    headers=[
                        ('Content-Type', 'text/csv'),
                        ('Content-Disposition',
                            content_disposition(f"{report_name}.csv"))
                    ]
                )
                records.get_csv_report(options, response)
                return response

        except Exception:
            error = {
                'code': 200,
                'message': 'Odoo Server Error',
            }
            return request.make_response(html_escape(json.dumps(error)))
