# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).


from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_project_agile_scrum = fields.Boolean(
        string="Scrum"
    )

    module_project_agile_kanban = fields.Boolean(
        string="Kanban"
    )

    module_project_agile_analytic = fields.Boolean(
        string="Analytics"
    )

    module_project_agile_timesheet_category = fields.Boolean(
        string="Timesheet Category"
    )

    module_project_agile_jira = fields.Boolean(
        string="JIRA Importer"
    )

    module_project_agile_workflow_transitions_by_task_type = fields.Boolean(
        string="Workflow Transitions by task type"
    )
