# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

{
    "name": "Project Agile Analytic",
    "summary": "This module provides analytics for project tasks",
    "category": "Project",
    "version": "11.0.1.0.0",
    "license": "LGPL-3",
    "author": "Modoolar",
    "website": "https://www.modoolar.com/",
    "images": ["static/description/banner.png"],
    "depends": ["project_agile"],
    "data": [

        # security
        "security/ir.model.access.csv",

        # View
        "views/project_agile_analytic_view.xml",
    ],
    "qweb": [],
    "installable": True,
}
