from odoo import models, api

class DeleteFakeAccounts(models.Model):
    _name = 'custom.user.signup'
    _description = 'Automated User Delete'

    @api.model
    def auto_archive_orders(self):
        users = self.env['res.users'].search([
            ('active', '=', True), ('state', '=', 'new')
        ])

        for user in users:
            partner = user.partner_id
            user.unlink()
            partner.write({
                'active': False,
            })