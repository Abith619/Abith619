from odoo import models, fields


class BomConsolidatedReportAbstract(models.AbstractModel):
    _name = 'report.silliconz_module.bom_consolidated_report_template'
    _description = 'BOM Consolidated Report Abstract'

    def _get_report_values(self, docids, data=None, **kwargs):
        data = data or {}
        company = self.env.company
        return {
            'doc_ids': docids,
            'doc_model': 'bom.consolidated.report.wizard',
            'docs': self.env['bom.consolidated.report.wizard'].browse(docids),
            'company': company,
            'warehouse': data.get('warehouse', ''),
            'mo_state_label': data.get('mo_state_label', ''),
            'report_date': data.get('report_date', fields.Date.today().strftime('%d-%m-%Y')),
            'bom_data': data.get('bom_data', []),
            'currency_symbol': data.get('currency_symbol', company.currency_id.symbol or ''),
        }