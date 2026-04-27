from odoo import models, fields

class ResUsers(models.Model):
    _inherit = "res.users"

    signature_image = fields.Image(string="Digital Signature")

class ResPartner(models.Model):
    _inherit = "res.partner"

    credit_limit = fields.Float(
        groups="account.group_account_invoice,account.group_account_readonly,base.group_system,base.group_erp_manager"
    )
    use_partner_credit_limit = fields.Boolean(
        groups="account.group_account_invoice,account.group_account_readonly,base.group_system,base.group_erp_manager"
    )
    show_credit_limit = fields.Boolean(
        groups="account.group_account_invoice,account.group_account_readonly,base.group_system,base.group_erp_manager"
    )