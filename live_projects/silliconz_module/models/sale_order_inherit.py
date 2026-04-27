from odoo import models, fields, api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[
        ('draft', 'draft'),
        ('submitted_lvl1', 'Submitted Level 1'),
        ('rejected_lvl1', 'Rejected Level 1'),
        ('sent', 'Quotation'),
        ('submitted_lvl2', 'Submitted for Approval L2'),
        ('sale', 'Sales Order'),
    ])

    terms_id = fields.Many2one(
        'terms.and.condition',
        string="Terms & Conditions",
        domain="[('type', 'in', ['quotation', 'general']), ('active', '=', True)]"
    )

    @api.onchange('terms_id')
    def _onchange_terms_id(self):
        for rec in self:
            if rec.terms_id and rec.terms_id.content:
                if rec.note:
                    rec.note = rec.note + "\n\n" + rec.terms_id.content
                else:
                    rec.note = rec.terms_id.content

    lead_id = fields.Many2one('crm.lead', string="Lead")
    enquiry_type_id = fields.Many2one('crm.enquiry.type', string="Enquiry Type")
    expected_quantity = fields.Integer(string="Expected Quantity")
    expected_delivery_date = fields.Date(string="Expected Delivery Timeline")
    rejection_reason = fields.Text(string="Rejection Reason (L1)")
    quotation_validity_date = fields.Date(string="Quotation Validity Date")
    quotation_type = fields.Selection([
        ('assembly', 'Assembly'),
        ('component', 'Component'),
    ], string="Quotation Type", required=True)

    customer_po_reference = fields.Char(string="Customer PO Reference")
    customer_po_date = fields.Date(string="Customer PO Date")
    customer_po_attachment = fields.Binary(string="Customer PO Attachment")
    customer_po_filename = fields.Char(string="Attachment Filename")
    amendment_origin_id = fields.Many2one('sale.order', string="Amendment Of")
    amendment_ids = fields.One2many('sale.order', 'amendment_origin_id', string="Amendments")
    amendment_count = fields.Integer(compute="_compute_amendment_count")
    production_count = fields.Integer(string="Manufacturing Orders", compute="_compute_production_count")
    production_ids = fields.One2many('mrp.production', 'sale_order_id', string="Manufacturing Orders")
    transporter_id = fields.Many2one(
        'transporter.master',
        string='Transporter',
        tracking=True,
        help='Select the transporter responsible for delivery.',
    )

    def _compute_production_count(self):
        for rec in self:
            rec.production_count = self.env['mrp.production'].search_count([
                ('sale_order_id', '=', rec.id)
            ])

    def _compute_amendment_count(self):
        for rec in self:
            root = rec._get_root_order()
            amendments = self.env['sale.order'].search([
                ('amendment_origin_id', '=', root.id)
            ])
            rec.amendment_count = len(amendments) + 1

    # =========================================================
    # EMAIL NOTIFICATION HELPER
    # =========================================================

    def _send_notification_email(self, template_xml_id):
        """
        Send an email using a mail.template.

        :param template_xml_id: fully-qualified XML ID of the mail.template record,
                                e.g. 'silliconz_module.email_template_submit_lvl1'
        """
        self.ensure_one()
        template = self.env.ref(template_xml_id, raise_if_not_found=False)
        if template:
            template.send_mail(self.id, force_send=True)

    # =========================================================
    # WORKFLOW ACTIONS
    # =========================================================

    def action_submit_lvl1(self):
        for rec in self:
            if rec.state != 'draft':
                raise UserError("Only Quotation stage can be submitted.")
            rec.state = 'submitted_lvl1'
            # Notify L1 approvers (group_sale_order_manager)
            rec._send_notification_email(
                'silliconz_module.email_template_submit_lvl1'
            )

    def action_approve_lvl1(self):
        for rec in self:
            if rec.state != 'submitted_lvl1':
                raise UserError("Order must be Submitted Level 1.")
            rec.state = 'sent'
            # Notify the salesperson that L1 was approved
            rec._send_notification_email(
                'silliconz_module.email_template_approve_lvl1'
            )

    def action_reject_lvl1(self):
        for rec in self:
            if rec.state != 'submitted_lvl1':
                raise UserError("Order must be Submitted Level 1.")

        # NOTE: The actual state change + rejection_reason write happens inside
        # reject.lvl1.wizard.  Call  rec._send_notification_email(
        #   'silliconz_module.email_template_reject_lvl1') at the END of that
        # wizard's action_reject() method (after writing state/reason).
        return {
            'type': 'ir.actions.act_window',
            'name': 'Reject Level 1',
            'res_model': 'reject.lvl1.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_sale_id': self.id}
        }

    def reset_to_draft(self):
        for rec in self:
            if rec.state not in ['rejected_lvl1']:
                raise UserError("Only Rejected Level 1 can be reset.")
            rec.state = 'draft'

    def action_submit_lvl2(self):
        for rec in self:
            if rec.state != 'sent':
                raise UserError("Order must be in Quotation Sent stage.")

        # NOTE: The actual state change happens inside submit.level2.wizard.
        # Call  rec._send_notification_email(
        #   'silliconz_module.email_template_submit_lvl2') at the END of that
        # wizard's confirm action (after writing state/PO details).
        return {
            'type': 'ir.actions.act_window',
            'name': 'Submit Level 2',
            'res_model': 'submit.level2.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_sale_id': self.id}
        }

    def action_confirm(self):
        """L2 Approval — called via 'Approve Level 2' button."""
        for rec in self:
            if rec.state != 'submitted_lvl2':
                raise UserError("Order must be Submitted for Approval L2.")

        self.write({'state': 'draft'})
        res = super().action_confirm()

        for order in self:
            if order.production_ids:
                continue

            for line in order.order_line:
                bom = self.env['mrp.bom'].search([
                    ('product_tmpl_id', '=', line.product_template_id.id)
                ], limit=1)

                production_vals = {
                    'product_id': line.product_id.id,
                    'product_qty': line.product_uom_qty,
                    'origin': order.name,
                    'sale_order_id': order.id,
                    'customer_po_reference': order.customer_po_reference,
                }
                if bom:
                    production_vals['bom_id'] = bom.id

                self.env['mrp.production'].create(production_vals)

        for order in self:
            outgoing_pickings = order.picking_ids.filtered(
                lambda p: p.picking_type_code == 'outgoing' and p.state not in ('done', 'cancel')
            )
            for picking in outgoing_pickings:
                picking.move_ids.filtered(
                    lambda m: m.state not in ('done', 'cancel')
                ).write({'state': 'draft'})
                picking.write({'state': 'draft'})

        for rec in self:
            if rec.opportunity_id:
                rec.opportunity_id.action_set_won()

            # Notify the salesperson that L2 was approved
            rec._send_notification_email(
                'silliconz_module.email_template_approve_lvl2'
            )

        return res

    def action_cancel(self):
        """Also used as L2 Reject when state is submitted_lvl2."""
        is_l2_rejection = any(rec.state == 'submitted_lvl2' for rec in self)

        res = super(SaleOrder, self).action_cancel()

        proposition_stage = self.env['crm.stage'].search([('id', '=', 3)], limit=1)

        for rec in self:
            if rec.opportunity_id:
                rec.opportunity_id.write({'stage_id': proposition_stage.id})
                rec.opportunity_id.action_set_lost()

            # Notify the salesperson that L2 was rejected
            if is_l2_rejection:
                rec._send_notification_email(
                    'silliconz_module.email_template_reject_lvl2'
                )

        return res

    # =========================================================
    # GET ROOT ORDER
    # =========================================================

    def _get_root_order(self):
        self.ensure_one()
        order = self
        while order.amendment_origin_id:
            order = order.amendment_origin_id
        return order

    # =========================================================
    # AMENDMENT ACTION
    # =========================================================

    def action_amend_order(self):
        self.ensure_one()

        if self.state not in ['sale', 'sent']:
            raise UserError("Only Quotation or Sale Orders can be amended.")

        root = self._get_root_order()
        amendment_number = len(root.amendment_ids) + 1
        base_name = root.name.split('-A')[0]
        new_name = "%s-A%s" % (base_name, amendment_number)

        new_order = self.copy({
            'name': new_name,
            'state': 'draft',
            'amendment_origin_id': root.id,
            'customer_po_reference': False,
            'customer_po_attachment': False,
            'customer_po_filename': False,
        })

        if self.state in ['sale']:
            self.action_unlock()
            self.action_cancel()
        elif self.state in ['sent']:
            self.action_cancel()

        for rec in self:
            if rec.opportunity_id:
                stage = self.env['crm.stage'].search([], limit=1)
                if stage:
                    rec.opportunity_id.stage_id = stage.id
                rec.opportunity_id.action_set_lost()

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'view_mode': 'form',
            'res_id': new_order.id,
        }

    # =========================================================
    # VIEW AMENDMENTS
    # =========================================================

    def action_view_amendments(self):
        self.ensure_one()
        root = self._get_root_order()
        domain = ['|', ('id', '=', root.id), ('amendment_origin_id', '=', root.id)]
        return {
            'type': 'ir.actions.act_window',
            'name': 'Amendments',
            'res_model': 'sale.order',
            'view_mode': 'list,form',
            'domain': domain,
        }

    # =========================================================
    # VIEW MO
    # =========================================================

    def action_view_mo(self):
        self.ensure_one()
        mos = self.env['mrp.production'].search([('sale_order_id', '=', self.id)])
        action = {
            'type': 'ir.actions.act_window',
            'name': 'Manufacturing Orders',
            'res_model': 'mrp.production',
            'view_mode': 'list,form',
            'domain': [('sale_order_id', '=', self.id)],
            'context': {'default_sale_order_id': self.id},
        }
        if len(mos) == 1:
            action.update({'view_mode': 'form', 'res_id': mos.id})
        return action