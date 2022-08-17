# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).
{
    "name": "Project Workflow Actions",
    "summary": "Module extends workflow with server actions.",
    "category": "Project",
    "version": "11.0.1.0.0",
    "license": "LGPL-3",
    "author": "Modoolar",
    "website": "https://www.modoolar.com/",
    "images": ["static/description/banner.png"],
    "depends": [
        "project_workflow_management",
        "server_action_sudo",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/project_workflow_transition_view.xml",
        "views/project_workflow_state_view.xml",
        "views/menu.xml",
    ],
    "installable": True,
}
