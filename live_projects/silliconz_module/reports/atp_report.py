from odoo import models

class AtpReportPdf(models.AbstractModel):
    _name = 'report.silliconz_module.atp_report_template'
    _description = 'ATP Report PDF Abstract Model'

    def _get_report_values(self, docids, data=None):
        """
        Called by Odoo's report engine.
        `data` is passed from action_print_pdf via report_action(data=...).
        """
        if not data:
            data = {}

        atp_data = data.get('atp_data', [])
        warehouse = data.get('warehouse', '')
        mo_state_map = {
            'draft_confirmed': 'Draft & Confirmed',
            'draft': 'Draft Only',
            'confirmed': 'Confirmed Only',
        }
        mo_state_label = mo_state_map.get(data.get('mo_state', ''), '')

        return {
            'doc_ids': docids,
            'doc_model': 'atp.report.wizard',
            'docs': self.env['atp.report.wizard'].browse(docids),
            'atp_data': atp_data,
            'warehouse': warehouse,
            'mo_state_label': mo_state_label,
            'report_date': self.env['ir.fields.converter']._str_to_date(
                None, None, str(self.env['ir.fields.date'].today())
            ) if False else __import__('datetime').date.today().strftime('%d-%m-%Y'),
            'company': self.env.company,
        }
