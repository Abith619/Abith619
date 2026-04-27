from odoo import models, fields,api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)


class MaterialRequest(models.Model):
    _name = "material.request"
    _description = "Material Request"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = 'name'
    _order = 'id desc'
    product_id = fields.Many2one("product.product", string="Product",store=True, readonly=True)
    name = fields.Char(string="Reference No",required=True,copy=False,readonly=True,default="New")
    picking_ids = fields.One2many("stock.picking","material_request_id",string="Transfers")
    requester_id = fields.Many2one("res.users", default=lambda self: self.env.user, readonly=True)
    request_date = fields.Datetime(default=fields.Datetime.now)
    expected_date = fields.Datetime(string="Expected Date")
    priority = fields.Selection([('0','Very Low'),('1','Low'),('2','Medium'),('3','High'),('4','Critical')], default='1')
    project_name = fields.Char(string="Project / Code Name")
    sale_order_id = fields.Many2one("sale.order", string="Sale Order")
    mo_id = fields.Many2one("mrp.production",string="Manufacturing Order Reference")
    source_location_id = fields.Many2one(
        "stock.location",
        domain=[("usage", "=", "internal")],
        default=lambda self: self._default_source_location(),
        required=True
    )

    destination_location_id = fields.Many2one(
        "stock.location",
        string="Destination Location",
        domain="[('usage', 'in', ('internal', 'customer'))]",
        required=True
    )

    analytic_account_id = fields.Many2one(
        "account.analytic.account",
        string="Analytical Account",
        tracking=True,
    )

    remarks = fields.Text(string="Remarks")

    line_ids = fields.One2many(

        "material.request.line", "request_id"
    )

    state = fields.Selection([
        ("draft", "Draft"),
        ("submitted", "Submitted"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("done", "Done"),    
    ], default="draft", tracking=True)
    transfer_count = fields.Integer(
    string="Transfers",
    compute="_compute_transfer_count")

    purchase_request_ids = fields.One2many(
        "purchase.request",
        "material_request_id",
        string="Purchase Requests"
    )
    purchase_request_count = fields.Integer(
        string="Purchase Requests",
        compute="_compute_purchase_request_count"
    )

    # --- Signature / Workflow Capture Fields ---
    mr_requestor_id = fields.Many2one('res.users', string="Requested By", readonly=True, copy=False)
    mr_requestor_signature = fields.Image(string="Requestor Signature", readonly=True, copy=False)

    mr_approver_id = fields.Many2one('res.users', string="Approved By", readonly=True, copy=False)
    mr_approver_signature = fields.Image(string="Approver Signature", readonly=True, copy=False)

    mr_issuer_id = fields.Many2one('res.users', string="Issued By", readonly=True, copy=False)
    mr_issuer_signature = fields.Image(string="Issuer Signature", readonly=True, copy=False)
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = self.env["ir.sequence"].next_by_code(
                    "material.request"
                ) or "New"
        return super().create(vals_list)



    def _compute_transfer_count(self):
        Picking = self.env["stock.picking"]
        for rec in self:
            rec.transfer_count = Picking.search_count([
                ("material_request_id", "=", rec.id)
            ])

    def _compute_purchase_request_count(self):
        for rec in self:
            rec.purchase_request_count = self.env["purchase.request"].search_count([
                ("material_request_id", "=", rec.id)
            ])

    def action_view_purchase_requests(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Purchase Requests",
            "res_model": "purchase.request",
            "view_mode": "list,form",
            "domain": [("material_request_id", "=", self.id)],
            "context": {"default_material_request_id": self.id},
        }

    def action_view_transfers(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Transfers",
            "res_model": "stock.picking",
            "view_mode": "list,form",
            "domain": [("material_request_id", "=", self.id)],
            "context": {"create": False},
        }

    def _default_source_location(self):
        location = self.env["stock.location"].search([
            ("is_material_source", "=", True)
        ], limit=1)

        if not location:
            raise ValidationError(
                "Please configure a Material Source Location."
            )

        return location

    @api.onchange("destination_location_id")
    def _onchange_destination_location(self):
        """Auto-populate destination location in all MR lines when header value changes."""
        for line in self.line_ids:
            line.destination_location_id = self.destination_location_id


    def action_submit(self):
        for request in self:
            request.state = "submitted"
            request.mr_requestor_id = self.env.user.id
            request.mr_requestor_signature = self.env.user.signature_image
            template = self.env.ref(
                "silliconz_module.email_template_material_request_submitted",
                raise_if_not_found=True
            ) 
            if template:
                company_email = request.env.company.email

                if not company_email:
                    raise ValidationError(
                        "Your company does not have an email configured."
                    )

                requester_email = request.requester_id.partner_id.email

                if not requester_email:
                    raise ValidationError(
                        "The requester does not have a valid email address."
                    )

                if template:
                    try:
                        mail_id = template.sudo().send_mail(
                            request.id,
                            force_send=True
                        )

                        _logger.info(
                            "Material Request %s: submitted email sent successfully. "
                            "mail_id=%s, to=%s",
                            request.requester_id.name,
                            mail_id,
                            # mail_id.state,
                            request.requester_id.partner_id.email,
                        )

                    except Exception as e:
                        _logger.exception(
                            "Material Request %s: Failed to send submit email. Error: %s",
                            request.requester_id.name,
                            
                            str(e)
                        )
            


    def action_approve(self):
        for request in self:
            for line in request.line_ids:
                if not line.approved_qty:
                    line.approved_qty = line.requested_qty
                if line.approved_qty <= 0:
                    raise ValidationError(
                        f"Approved Quantity must be greater than zero for product "
                        f"{line.product_id.display_name}"
                    )
                if line.approved_qty > line.requested_qty:
                    raise ValidationError(
                        f"Approved Quantity ({line.approved_qty}) "
                        f"cannot be greater than Requested Quantity ({line.requested_qty}) "
                        f"for product {line.product_id.display_name}"
                    )
            request.state = "approved"
            request.mr_approver_id = self.env.user.id
            request.mr_approver_signature = self.env.user.signature_image

            template = self.env.ref(
                "silliconz_module.email_template_material_request_approved",
                raise_if_not_found=False
            )

            if template:
                company_email = request.env.company.email

                if not company_email:
                    raise ValidationError(
                        "Your company does not have an email configured."
                    )

                requester_email = request.requester_id.partner_id.email

                if not requester_email:
                    raise ValidationError(
                        "The requester does not have a valid email address."
                    )

                if template:
                    try:
                        mail_id = template.sudo().send_mail(
                            request.id,
                            force_send=True
                        )

                        _logger.info(
                            "Material Request %s: Approval email sent successfully. "
                            "mail_id=%s, to=%s",
                            request.requester_id.name,
                            mail_id,
                            # mail_id.state,
                            request.requester_id.partner_id.email,
                        )

                    except Exception as e:
                        _logger.exception(
                            "Material Request %s: Failed to send approval email. Error: %s",
                            request.requester_id.name,
                            
                            str(e)
                        )
    def action_reject(self):
        for request in self:
            request.state = "rejected"
            template = self.env.ref(
                "silliconz_module.email_template_material_request_rejected",
                raise_if_not_found=False
            )   
            if template:
                company_email = request.env.company.email

                if not company_email:
                    raise ValidationError(
                        "Your company does not have an email configured."
                    )

                requester_email = request.requester_id.partner_id.email

                if not requester_email:
                    raise ValidationError(
                        "The requester does not have a valid email address."
                    )

                if template:
                    try:
                        mail_id = template.sudo().send_mail(
                            request.id,
                            force_send=True
                        )

                        _logger.info(
                            "Material Request %s: Reject email sent successfully. "
                            "mail_id=%s, to=%s",
                            request.requester_id.name,
                            mail_id,
                            # mail_id.state,
                            request.requester_id.partner_id.email,
                        )

                    except Exception as e:
                        _logger.exception(
                            "Material Request %s: Failed to send Rejecy email. Error: %s",
                            request.requester_id.name,
                            
                            str(e)
                        )


    def action_reset_to_draft(self):
        for request in self:
            request.state = "draft"
            request.mr_requestor_id = False
            request.mr_requestor_signature = False
            request.mr_approver_id = False
            request.mr_approver_signature = False

    def action_create_transfer(self):
        self.ensure_one()

        if not self.line_ids:
            raise ValidationError("No lines found to create transfer.")

        # Capture issuer when the transfer wizard is opened
        self.mr_issuer_id = self.env.user.id
        self.mr_issuer_signature = self.env.user.signature_image

        return {
            "type": "ir.actions.act_window",
            "name": "Create Transfer",
            "res_model": "create.transfer.wizard",
            "view_mode": "form",
            "target": "new",
            "context": {
                "default_material_request_id": self.id,
                "default_source_location_id": self.source_location_id.id,
                "default_line_ids": [(0, 0, {
                    "product_id": line.product_id.id,
                    "description": line.description,
                    "requested_qty": line.requested_qty,
                    "approved_qty": line.approved_qty,
                    "available_qty": line.available_qty,
                    "uom_id": line.uom_id.id,
                    "destination_location_id": line.destination_location_id.id,
                }) for line in self.line_ids if line.approved_qty > 0],
            },
        }

    def action_create_purchase_request(self):

        return {
            "type": "ir.actions.act_window",
            "name": "Create Purchase Request",
            "res_model": "purchase.request.wizard",
            "view_mode": "form",
            "target": "new",
            "context": {"default_material_request_id": self.id,
                        "default_mo_id": self.mo_id.id if self.mo_id else False,
                        "default_line_ids": [(0, 0, {
                            "product_id": line.product_id.id,
                            "requested_qty": line.requested_qty,
                            "available_qty": line.available_qty,
                            "uom_id": line.uom_id.id
                        }) for line in self.line_ids
                    ],
                        },
        }