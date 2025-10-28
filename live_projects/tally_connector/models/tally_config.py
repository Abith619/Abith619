from odoo import models, fields

class TallyConfig(models.Model):
    _name = "tally.config"
    _description = "Tally Configuration"

    name = fields.Char("Configuration Name", default="Tally Local Config")
    host = fields.Char("Tally Host", default="http://localhost")
    port = fields.Integer("Tally Port", default=9000)
    company_name = fields.Char("Tally Company Name")


