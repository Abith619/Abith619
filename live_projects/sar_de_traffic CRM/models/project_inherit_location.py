from odoo import models, api

class ProjectInheritLocation(models.Model):
    _inherit='project.project'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            self.env['stock.location'].create({
                "name": vals.get("name"),
                "location_id": 3,
            })
        return super(ProjectInheritLocation, self).create(vals_list)