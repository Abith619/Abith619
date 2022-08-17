# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).


from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_project_git_bitbucket = fields.Boolean(
        string="Bitbucket"
    )

    module_project_git_github = fields.Boolean(
        string="GitHub"
    )

    module_project_git_gitlab = fields.Boolean(
        string="GitLab"
    )
