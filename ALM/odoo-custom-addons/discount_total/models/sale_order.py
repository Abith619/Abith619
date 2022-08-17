from odoo import models, fields, api, _
from odoo.tools import float_is_zero
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.one
    @api.depends('order_line.price_subtotal', 'order_line.price_tax',
                 'currency_id', 'company_id', 'date_order')
    def compute_discount(self):
        round_curr = self.currency_id.round
        self.amount_untaxed = sum(line.price_subtotal for line in self.order_line)
        self.amount_tax = sum(round_curr(line.price_tax) for line in self.order_line)
        self.amount_total = self.amount_untaxed + self.amount_tax
        discount = 0
        for line in self.order_line:
            discount += (line.price_unit * line.product_uom_qty * line.discount) / 100
        self.discount = discount
        amount_total_company_signed = self.amount_total
        amount_untaxed_signed = self.amount_untaxed
        if self.currency_id and self.company_id and self.currency_id != self.company_id.currency_id:
            currency_id = self.currency_id.with_context(date=self.date_order)
            amount_total_company_signed = currency_id.compute(self.amount_total, self.company_id.currency_id)
            amount_untaxed_signed = currency_id.compute(self.amount_untaxed, self.company_id.currency_id)
        self.amount_total_company_signed = amount_total_company_signed
        self.amount_total_signed = self.amount_total
        self.amount_untaxed_signed = amount_untaxed_signed

    @api.one
    @api.depends('order_line')
    def compute_total_before_discount(self):
        total = 0
        for line in self.order_line:
            total += line.price
        self.total_before_discount = total

    discount_type = fields.Selection([('percentage', 'Percentage'), ('amount', 'Amount')], string='Discount Type',
                                     readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, default='amount')
    discount_rate = fields.Float(string='Discount Rate', digits=(16, 2),
                                 readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, default=0.0)
    discount = fields.Monetary(string='Discount', digits=(16, 2), default=0.0,
                               store=True, compute='compute_discount', track_visibility='always')
    total_before_discount = fields.Monetary(string='Total Before Discount', digits=(16, 2), store=True, compute='compute_total_before_discount')

    @api.onchange('discount_type', 'discount_rate', 'order_line')
    def set_lines_discount(self):
        if self.discount_type == 'percentage':
            for line in self.order_line:
                line.discount = self.discount_rate
        else:
            total = discount = 0.0
            for line in self.order_line:
                total += (line.product_uom_qty * line.price_unit)
            if self.discount_rate != 0:
                discount = (self.discount_rate / total) * 100
            else:
                discount = self.discount_rate
            for line in self.order_line:
                line.discount = discount

    @api.multi
    def button_dummy(self):
        self.set_lines_discount()
        return True

    @api.multi
    def action_invoice_create(self, grouped=False, final=False):
        inv_obj = self.env['account.invoice']
        precision = self.env['decimal.precision'].precision_get('Product Unit of Measure')
        invoices = {}
        references = {}
        invoices_origin = {}
        invoices_name = {}

        for order in self:
            group_key = order.id if grouped else (order.partner_invoice_id.id, order.currency_id.id)
            for line in order.order_line.sorted(key=lambda l: l.qty_to_invoice < 0):
                if float_is_zero(line.qty_to_invoice, precision_digits=precision):
                    continue
                if group_key not in invoices:
                    inv_data = order._prepare_invoice()
                    invoice = inv_obj.create(inv_data)
                    references[invoice] = order
                    invoices[group_key] = invoice
                    invoices_origin[group_key] = [invoice.origin]
                    invoices_name[group_key] = [invoice.name]
                elif group_key in invoices:
                    if order.name not in invoices_origin[group_key]:
                        invoices_origin[group_key].append(order.name)
                    if order.client_order_ref and order.client_order_ref not in invoices_name[group_key]:
                        invoices_name[group_key].append(order.client_order_ref)

                if line.qty_to_invoice > 0:
                    line.invoice_line_create(invoices[group_key].id, line.qty_to_invoice)
                elif line.qty_to_invoice < 0 and final:
                    line.invoice_line_create(invoices[group_key].id, line.qty_to_invoice)

            if references.get(invoices.get(group_key)):
                if order not in references[invoices[group_key]]:
                    references[invoices[group_key]] |= order

        for group_key in invoices:
            invoices[group_key].write({'name': ', '.join(invoices_name[group_key]),
                                       'origin': ', '.join(invoices_origin[group_key])})

        if not invoices:
            raise UserError(_('There is no invoiceable line.'))

        for invoice in invoices.values():
            if not invoice.invoice_line_ids:
                raise UserError(_('There is no invoiceable line.'))
            # If invoice is negative, do a refund invoice instead
            if invoice.amount_untaxed < 0:
                invoice.type = 'out_refund'
                for line in invoice.invoice_line_ids:
                    line.quantity = -line.quantity
            # Use additional field helper function (for account extensions)
            for line in invoice.invoice_line_ids:
                line._set_additional_fields(invoice)
            # Necessary to force computation of taxes. In account_invoice, they are triggered
            # by onchanges, which are not triggered when doing a create.
            invoice.compute_taxes()
            invoice.message_post_with_view('mail.message_origin_link',
                                           values={'self': invoice, 'origin': references[invoice]},
                                           subtype_id=self.env.ref('mail.mt_note').id)

            if order.discount_rate > 0:
                invoice.discount_rate = order.discount_rate
        return [inv.id for inv in invoices.values()]


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.one
    @api.depends('product_uom_qty', 'price_unit')
    def compute_line_price(self):
        self.price = self.product_uom_qty * self.price_unit

    discount = fields.Float(string='Discount (%)', digits=(16, 2), default=0.0)
    price = fields.Float(string='Price', digits=(16, 2), store=True, compute='compute_line_price')
