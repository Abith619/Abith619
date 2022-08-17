# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

{
    "name": "Project Git",
    "summary": "Integrates your projects with git based services",
    "category": "Project",
    "version": "11.0.1.0.0",
    "license": "LGPL-3",
    "author": "Modoolar",
    "website": "https://www.modoolar.com/",
    "images": ["static/description/banner.png"],
    "depends": [
        "project_key",
        "web_widget_image_url",
    ],
    "data": [
        "data/mail_message.xml",

        "security/ir.model.access.csv",

        "views/project_git_commit_view.xml",
        "views/project_git_user_view.xml",
        "views/project_git_branch_view.xml",
        "views/project_git_repository_view.xml",
        "views/project_project_view.xml",
        "views/project_task_view.xml",
        "views/res_config_settings_views.xml",
        "views/menu.xml",
    ],

    "demo": [],
    "qweb": [
        "static/src/xml/agile_git.xml",
    ],
    "application": False,
    "installable": True,
}
