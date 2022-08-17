# -*- coding: utf-8 -*-

{
    'name': 'Employee Skills and Qualifications',
    'category': 'Generic Modules/Human Resources',
    'version': '12.0.1.0.0',
    'summary': 'This module will adds a configuration for skills and qualification of employee.',
    'website': 'http://www.aktivsoftware.com',
    'author': 'Aktiv Software',
    'license': 'AGPL-3',
    'description': 'Manage Employee Skill and Qualifications.',

    'depends': [
        'hr_recruitment',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_skill_qualification_views.xml',
        'views/hr_applicant_skill_qualification.xml'
    ],

    'images': ['static/description/banner.jpg'],
    'auto_install': False,
    'installable': True,
    'application': False

}
