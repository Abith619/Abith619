# -*- coding: utf-8 -*-
{
    'name': 'Project and Task Report in Odoo',
    "author": "Edge Technologies",
    'version': '12.0.1.0',
    'live_test_url': "https://youtu.be/RGymMBdvNhw",
    "images":['static/description/main_screenshot.png'],
    'summary': "This app helps user to print project and task report using different filter.",
    

    'description': """This app helps user to print project and task report between start date and end date using different filter like user of project or task and task stage.
    
project task repots
Reports in Project Report on Tasks Print Project Task Report Project And Task PDF Report
print PDF report on project and task print PDF report task Project Report XLS & PDF Project task Report XLS & PDF
task pdf report, task reports Project Task Report project reports
project pdf reports project task pdf reports 




    """,
    "license" : "OPL-1",
    'depends': ['base','project','hr_timesheet'],
    'data': [
            "views/project_task_report_view.xml",
            "views/project_report_template.xml",
            "views/project_task_report_template.xml",
            ],
    'installable': True,
    'auto_install': False,
    'price': 000,
    'currency': "EUR",
    'category': 'Project',

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
