from odoo import models, fields

class TallyBillWizard(models.TransientModel):
    _name = "tally.bill.wizard"
    _description = "Bill Export Wizard"

    date_from = fields.Date("From Date")
    date_to = fields.Date("To Date")
    branch_id : fields.Many2one = fields.Many2one("res.branch", string="Branch")

    def action_export_bill_xml(self):
        bills = self.env["account.move"].search([
            ("move_type", "=", "in_invoice"),
            ("state", "=", "posted"),
            ("invoice_date", ">=", self.date_from),
            ("invoice_date", "<=", self.date_to),
        ])
        return self.env.ref("tally_connector.report_bill_xml").report_action(bills)
