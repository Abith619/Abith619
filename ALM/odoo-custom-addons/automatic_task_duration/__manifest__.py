# -*- coding: utf-8 -*-
# Part of AktivSoftware See LICENSE file for full
# copyright and licensing details.
{
    'name': 'Automatic Task Duration',
    'version': '12.0.1.0.0',
    'category': 'Project',
    'summary': '''
        Calculates project task duration automatically.
        ''',
    'website': 'http://www.aktivsoftware.com',
    'author': 'Aktiv Software',
    'license': "AGPL-3",
    'depends': [
        'hr_timesheet'
    ],
    'website': 'www.aktivsoftware.com',
    'data': [
        'views/project_timesheet_view.xml',
        'wizards/task_entry_view.xml'
    ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
}
