from odoo import models, fields, api

class ApiDemo(models.Model):
    _name = 'api.demo'
    _description = 'API Demo Model'

    name = fields.Char("Name")
    age = fields.Integer("Age")

    @api.model
    def create(self, vals):
        print("🔥 CREATE called with:", vals)
        return super().create(vals)

    def write(self, vals):
        print("🔥 WRITE called with:", vals)
        return super().write(vals)

    def unlink(self):
        print("🔥 UNLINK called for IDs:", self.ids)
        return super().unlink()
