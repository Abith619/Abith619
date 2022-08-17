from datetime import datetime, timedelta

from odoo import models, fields, api


def get_default_expire():
    return fields.Datetime.to_string(datetime.now() + timedelta(hours=1))


class OdooInfrasstructureClientAuth(models.Model):
    _name = 'odoo.infrastructure.client.auth'
    _description = 'Odoo Infrastructure Client Auth'

    _log_access = False

    token_user = fields.Char(index=True, readonly=True)
    token_password = fields.Char(index=True, readonly=True)
    expire = fields.Datetime(
        readonly=True,
        index=True,
        required=True,
        default=get_default_expire)
    token_temp = fields.Char(readonly=True, index=True)
    user_uuid = fields.Char(readonly=True)
    user_id = fields.Integer(readonly=True)

    @api.model
    def scheduler_cleanup_expired_entries(self):
        self.search([('expire', '<', fields.Datetime.now())]).unlink()
        return True
