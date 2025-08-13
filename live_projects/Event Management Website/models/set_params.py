from odoo import models, api

class ParameterConfig(models.Model):
   _inherit = 'ir.config_parameter'
   _description = 'System Parameter'

   @api.model
   def function(self):
         custom_value = "https://localhost:8069"
         self.env['ir.config_parameter'].set_param('web.base.url', custom_value)
         values = self.env['ir.config_parameter'].get_param('web.base.url', custom_value)
         print("values", values)