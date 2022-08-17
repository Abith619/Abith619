# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Project Issue Sequence',
    'version': '12.0.0.2',
    'author': 'BrowseInfo',
    'category':'Project',
    'website': 'https://www.browseinfo.in',
    'summary': 'This module allow to create automatic sequence of project issue',
    'description':""" This module allow to create automatic sequence of project issue.""", 
    'license':'OPL-1',
    'depends':['project'],
    'data':[
        'data/ir_sequence_data.xml',
        'views/project_issue.xml',
        ],
    'installable': True,
    'auto_install': False,
    "images":['static/description/Banner.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
