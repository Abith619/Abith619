# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class NetfarmSalConfig(models.TransientModel):
    _inherit = 'res.config.settings'

    enabled_module_selection = fields.Many2many(
        string="Sal Enabled Module",
        comodel_name="ir.model"
    )

    @api.model
    def _get_selection(self):
        value = self.env['ir.config_parameter'].sudo().get_param('netfarm_sal_12.enabled_module_selection')
        if value == '[]':
            value = False
        if not value:
            return []
        value = value.strip('][').split(',')
        value = [int(i) for i in value]
        selection = []
        for v in value:
            model = self.env['ir.model'].sudo().browse(v)
            selection.append((model.id, model.name))
        return selection

    module_selection = fields.Selection(
        string="Default module",
        selection="_get_selection"
    )

    @api.multi
    def set_values(self):
        super(NetfarmSalConfig, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('netfarm_sal_12.enabled_module_selection', self.enabled_module_selection.ids)
        self.env['ir.config_parameter'].sudo().set_param('netfarm_sal_12.module_selection',self.module_selection)

    @api.model
    def get_values(self):
        res = super(NetfarmSalConfig, self).get_values()
        value = self.env['ir.config_parameter'].sudo().get_param('netfarm_sal_12.enabled_module_selection')
        if not value:
            return res
        value = value.strip('][').split(',')
        try:
            value = [int(i) for i in value]
        except:
            value = []

        value_module_selection = self.env['ir.config_parameter'].sudo().get_param('netfarm_sal_12.module_selection')
        res.update(
            enabled_module_selection=[(6, False, value)],
            module_selection=int(value_module_selection)
        )
        return res

    @api.model
    def get_sal_config(self):
        enabled_module_selection = self.env['ir.config_parameter'].sudo().get_param('netfarm_sal_12.enabled_module_selection')
        if enabled_module_selection == '[]':
            enabled_module_selection = False
        if not enabled_module_selection:
            return {'models_allowed': [], 'model_selected': ''}
        enabled_module_selection = enabled_module_selection.strip('][').split(',')
        enabled_module_selection = [int(i) for i in enabled_module_selection]
        selection = []
        for v in enabled_module_selection:
            model = self.env['ir.model'].sudo().browse(v)
            selection.append((model.model, model.display_name))

        value_module_selection = self.env['ir.config_parameter'].sudo().get_param('netfarm_sal_12.module_selection')
        module_selection = self.env['ir.model'].sudo().browse(int(value_module_selection))
        return {'models_allowed': selection, 'model_selected': module_selection.model}