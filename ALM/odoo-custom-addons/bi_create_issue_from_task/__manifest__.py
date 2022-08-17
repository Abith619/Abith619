# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Create Issue from Project Task',
    'version': '12.0.0.0',
    'author': 'BrowseInfo',
    'category':'Project',
    'website': 'www.browseinfo.in',
    'description':""" This module allow to create issue directly from task and it will show how many issues in a particular task.Create Issue from Task, Add Issue from Task, Create Issue from Project Task, Add Issue from Project Task """,
    'license':'OPL-1',
    'summary': 'This apps helps to create multiple issue from the project task',
    'depends':['base','project'],
    'data':[
        'views/project_issues.xml',
        'wizard/project_issue_wizard.xml',
        ],
    'installable': True,
    'auto_install': False,
    'live_test_url':'https://youtu.be/ioWRSQsEL-Y',
    "images":['static/description/Banner.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
