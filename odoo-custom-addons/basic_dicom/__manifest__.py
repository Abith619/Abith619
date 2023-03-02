# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name": "Hospital Management System with Dicom",
    "version": "14.0.0.1",
    "currency": 'INR',
    "summary": "Apps Hospital, Healthcare Management system ",
    "category": "Industries",
    "description": """
        Dicom Integration
""",

    # 'external_dependencies': {'python': ['slicer']},

    "depends": ["base", "web", "contacts"],
    "data": [
        'security/ir.model.access.csv',
        'views/view_dicom.xml',
    ],
    'demo': [
    ],
    'css': [],
    "author": "Abith",
    "website": "https://www.scopex.in",
    "installable": True,
    "application": True,
    "auto_install": False,
    "images": ['static/description/Banner.png'],
    "live_test_url": 'https://pydicom.mo.vc/',
}
