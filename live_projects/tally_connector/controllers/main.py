from odoo.addons.web.controllers.report import ReportController
from odoo.http import content_disposition, request, route, Response

class CustomReportController(ReportController):
    @route(['/report/tally_connector/<string:report_name>/<string:docids>'], type='http', auth='user')
    def report_download_xml(self, report_name, docids=None, **data):
        report = request.env.ref("tally_connector.report_ledger_xml")
        xml_content, _ = report.sudo()._render_qweb_text([int(d) for d in docids.split(",")])
        return Response(
            xml_content,
            headers=[
                ('Content-Type', 'application/xml'),
                ('Content-Disposition', content_disposition(report_name + ".xml"))
            ]
        )
