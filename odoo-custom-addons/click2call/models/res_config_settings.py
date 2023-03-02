from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    click2call_endpoint = fields.Char(
        "Click2call API URL(Endpoint)",
        config_parameter='click2call.api.endpoint'
    )