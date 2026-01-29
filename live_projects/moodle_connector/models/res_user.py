from odoo import models, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def _signup_create_user(self, values):
        user = super()._signup_create_user(values)

        # website = self.env['website'].sudo().search([], limit=1)

        user.sudo().write({
            'is_published': True,
            # 'website_id': website.id,
        })

        return user
