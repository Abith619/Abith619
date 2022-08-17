from odoo import api, SUPERUSER_ID


def migrate(cr, installed_version):
    api.Environment(cr, SUPERUSER_ID, {})['ir.config_parameter'].set_param(
        'yodoo_client.yodoo_allow_admin_logins', True)
