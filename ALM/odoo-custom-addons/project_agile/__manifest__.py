# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).
{
    "name": "Project Agile",
    "summary": "Framework for development of agile methodologies",
    "version": "11.0.1.0.0",
    "category": "Project",
    "website": "https://www.modoolar.com/",
    "author": "Modoolar",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "post_init_hook": "post_init_hook",
    "images": ["static/description/banner.png"],
    "depends": [
        "web",
        "project_key",
        "project_workflow_management",
        "hr_timesheet",
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "wizards/board_create_wizard.xml",
        "wizards/project_task_worklog_wizard.xml",
        "wizards/add_subtask_wizard.xml",
        "wizards/add_task_link_wizard.xml",
        "wizards/stage_change_confirmation_wizard.xml",

        "views/project_agile.xml",
        "views/project_project_view.xml",
        "views/project_task_type2_view.xml",
        "views/project_task_link_view.xml",
        "views/project_task_priority_view.xml",
        "views/project_task_resolution_view.xml",
        "views/project_task_view.xml",
        "views/project_workflow_view.xml",
        "views/project_agile_team_view.xml",
        "views/project_agile_board_view.xml",
        "views/res_config_settings_views.xml",

        "views/menu.xml",

        "data/project_task_link_relation_data.xml",
        "data/project_task_priority_data.xml",
        "data/project_task_resolution_data.xml",
        "data/project_task_type_data.xml",
        "data/project_task_type2_data.xml",
        "data/project_project_data.xml",
    ],

    "demo": [],
    "qweb": ["static/src/xml/*.xml"],
}
