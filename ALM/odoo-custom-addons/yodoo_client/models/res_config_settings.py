from odoo import models, fields, api, tools
from ..utils import prepare_db_statistic_data

STAT_FIELDS = [
    'users_total_count',
    'users_internal_count',
    'users_external_count',
    'file_storage',
    'db_storage',
]


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    users_total_count = fields.Integer(
        compute='_compute_db_statistics', readonly=True)
    users_internal_count = fields.Integer(
        compute='_compute_db_statistics', readonly=True)
    users_external_count = fields.Integer(
        compute='_compute_db_statistics', readonly=True)
    file_storage = fields.Char(
        compute='_compute_db_statistics', readonly=True)
    db_storage = fields.Char(
        compute='_compute_db_statistics', readonly=True)

    yodoo_allow_admin_logins = fields.Boolean(
        string='Allow administrative logins',
        help="Allow employees of your support company to login "
             "to database as administrator")

    @api.depends('company_id')
    def _compute_db_statistics(self):
        for rec in self:
            data = prepare_db_statistic_data(self.env.cr.dbname)
            data.update({
                'db_storage': tools.human_size(data['db_storage']),
                'file_storage': tools.human_size(data['file_storage']),
            })
            data = {f: data[f] for f in STAT_FIELDS}
            rec.update(data)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res['yodoo_allow_admin_logins'] = params.get_param(
            'yodoo_client.yodoo_allow_admin_logins', default=False)
        return res

    @api.multi
    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        params = self.env['ir.config_parameter'].sudo()
        params.set_param(
            'yodoo_client.yodoo_allow_admin_logins',
            self.yodoo_allow_admin_logins)

        if not self.yodoo_allow_admin_logins:
            self.env['yodoo.client.auth.log'].search(
                [('login_state', '=', 'active')]).action_expire()
        return res
