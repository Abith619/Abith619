# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

{
    "name": "Project Workflow Transition by Project",
    "summary": "This module extends ``project_workflow_management``"
               "in order to provide transition constraints based on project.",
    "category": "Project",
    "version": "11.0.1.0.0",
    "license": "LGPL-3",
    "author": "Modoolar",
    "website": "https://www.modoolar.com/",
    "images": ["static/description/banner.png"],
    "depends": [
        "project_workflow_management",
    ],
    "data": [
        "views/project_workflow_views.xml",
    ],

    "demo": [],
    "qweb": [

    ],
    "application": False,
}
