# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).
from odoo import models, fields


class BoardCreateWizard(models.TransientModel):
    _inherit = 'project.agile.board.create.wizard'

    type = fields.Selection(
        selection=[('kanban', 'Kanban')],
        default='kanban',
        required=True
    )
