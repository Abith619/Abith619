from odoo import models, fields


class SubmitLevel2Wizard(models.TransientModel):
    _name = 'submit.level2.wizard'
    _description = 'Submit Level 2 Wizard'

    sale_id = fields.Many2one('sale.order', required=True)
    customer_po_reference = fields.Char(required=True)
    customer_po_date = fields.Date(string="Customer PO Date", required=True)
    customer_po_attachment = fields.Binary()
    customer_po_filename = fields.Char()

    def action_confirm_submit(self):
        self.ensure_one()

        self.sale_id.write({
            'customer_po_reference': self.customer_po_reference,
            'customer_po_date': self.customer_po_date,
            'customer_po_attachment': self.customer_po_attachment,
            'customer_po_filename': self.customer_po_filename,
            'state': 'submitted_lvl2'
        })
        self.sale_id._send_notification_email('silliconz_module.email_template_submit_lvl2')

        return {'type': 'ir.actions.act_window_close'}
