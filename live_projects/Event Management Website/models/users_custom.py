from odoo import models, api, fields, _
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta, timezone

class UsersInherit(models.Model):
    _inherit = 'res.users'

    x_signup_ip = fields.Char(string='Signup IP')

class DeleteFakeAccounts(models.Model):
    _name = 'custom.user.signup'
    _description = 'Automated User Delete'

    @api.model
    def auto_archive_orders(self):
        time_threshold = datetime.now(timezone.utc) - timedelta(hours=1)
        users = self.env['res.users'].search([
            ('active', '=', True), ('state', '=', 'new'), ('create_date', '<=', time_threshold)
        ])

        for user in users:
            partner = user.partner_id
            user.unlink()
            partner.write({
                'active': False,
            })