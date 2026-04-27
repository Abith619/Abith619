from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    enquiry_type_id = fields.Many2one('crm.enquiry.type', string="Enquiry Type")
    expected_quantity = fields.Integer(string="Expected Quantity")
    expected_delivery_date = fields.Date(string="Expected Delivery Timeline")
    enquiry_date = fields.Datetime(string="Enquiry Date",related='create_date',store=True)
    product_line_ids = fields.One2many('crm.lead.line','lead_id',string="Products")

    has_confirmed_sale = fields.Boolean(
        string="Has Confirmed Sale",
        compute="_compute_has_confirmed_sale"
    )

    def _compute_has_confirmed_sale(self):
        for rec in self:
            count = self.env['sale.order'].search_count([
                ('opportunity_id', '=', rec.id),
                ('state', '=', 'sale')
            ])
            rec.has_confirmed_sale = count > 0

    @api.constrains('product_line_ids')
    def _check_product_lines(self):
        for rec in self:
            if not rec.product_line_ids:
                raise ValidationError("At least one product line is required.")

    def action_sale_quotations_new(self):
        self.ensure_one()

        # ✅ CHECK PRODUCT LINES HERE
        if not self.product_line_ids:
            raise ValidationError("Please add at least one product before creating quotation.")

        for line in self.product_line_ids:
            if not line.product_id or not line.quantity or not line.uom_id:
                raise ValidationError("All product line fields are required.")

        action = super().action_sale_quotations_new()

        action['context'] = {
            'default_opportunity_id': self.id,
            'default_partner_id': self.partner_id.id,
            'default_enquiry_type_id': self.enquiry_type_id.id if self.enquiry_type_id else False,
            'default_expected_quantity': self.expected_quantity,
            'default_expected_delivery_date': self.expected_delivery_date,
            'default_order_line': [
                (0, 0, {
                    'product_id': line.product_id.id,
                    'product_uom_qty': line.quantity,
                })
                for line in self.product_line_ids
            ]
        }

        return action

    def _get_action_view_sale_quotation_domain(self):
        return [('state', 'in', ('sent', 'submitted_lvl2', 'cancel'))]

    def _get_lead_quotation_domain(self):
        return [('state', 'in', ('sent', 'submitted_lvl2'))]

    def _get_lead_sale_order_domain(self):
        return [('state', 'not in', ('draft', 'sent', 'submitted_lvl1', 'rejected_lvl1', 'submitted_lvl2', 'cancel'))]
