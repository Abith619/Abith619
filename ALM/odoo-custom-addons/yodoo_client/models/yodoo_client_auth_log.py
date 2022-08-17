from odoo import models, fields, http


class YodooClientAuthLog(models.Model):
    _name = 'yodoo.client.auth.log'
    _description = 'Yodoo Auth Log'
    _log_access = False

    login_date = fields.Datetime(required=True, readonly=True)
    login_expire = fields.Datetime(readonly=True)
    login_session = fields.Char(readonly=True)
    login_state = fields.Selection(
        [('active', 'Active'),
         ('expired', 'Expired')],
        readonly=True)
    logout_date = fields.Datetime(readonly=True)
    login_remote_uuid = fields.Char(readonly=True)
    login_user_id = fields.Integer(readonly=True)

    def action_expire(self):
        for record in self:
            if record.login_state != 'expired':
                session = http.root.session_store.get(record.login_session)
                http.root.session_store.delete(session)
                record.login_state = 'expired'
                record.logout_date = fields.Datetime.now()

    def scheduler_logout_expired(self):
        self.search([
            ('login_expire', '<', fields.Datetime.now()),
        ]).action_expire()

    def unlink(self):
        self.action_expire()
        return super(YodooClientAuthLog, self).unlink()
