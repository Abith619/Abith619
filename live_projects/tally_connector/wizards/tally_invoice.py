from odoo import models, fields

class TallyInvoiceWizard(models.TransientModel):
    _name = "tally.invoice.wizard"
    _description = "Invoice Export Wizard"

    date_from = fields.Date("From Date")
    date_to = fields.Date("To Date")
    branch_id : fields.Many2one = fields.Many2one("res.branch", string="Branch")

    def action_export_invoice_xml(self):
        invoices = self.env["account.move"].search([
            ("move_type", "=", "out_invoice"),
            ("state", "=", "posted"),
            ("invoice_date", ">=", self.date_from),
            ("invoice_date", "<=", self.date_to),
        ])
        # Pass invoices to report
        return self.env.ref("tally_connector.report_invoice_xml").report_action(invoices)
