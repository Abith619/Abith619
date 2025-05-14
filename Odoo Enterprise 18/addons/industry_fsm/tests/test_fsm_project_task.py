# Part of Odoo. See LICENSE file for full copyright and licensing details

from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.tests import Form, tagged
from freezegun import freeze_time

from .common import TestIndustryFsmCommon

@tagged('post_install', '-at_install')
class TestAutoCreateFsmProject(TestIndustryFsmCommon):

    def test_default_project_fsm_subtasks(self):
        _, fsm_project_B = self.env['project.project'].create([
            {
                'name': 'Field Service A',
                'is_fsm': True,
                'company_id': self.env.company.id,
                'allow_timesheets': True,
                'sequence': 100,
            },
            {
                'name': 'Field Service B',
                'is_fsm': True,
                'company_id': self.env.company.id,
                'allow_timesheets': True,
                'sequence': 200,
            }
        ])
        task = self.env['project.task'].create({
            'name': 'Fsm task',
            'project_id': fsm_project_B.id,
            'partner_id': self.partner.id,
        })
        subtask = self.env['project.task'].with_context(
                fsm_mode=True,
                default_parent_id=task.id,
                default_project_id=task.project_id.id
        ).create({
            'name': 'Fsm subtask',
            'partner_id': self.partner.id,
        })
        self.assertEqual(subtask.project_id, fsm_project_B)

    @freeze_time("2025-05-12")
    def test_task_fsm_without_calendar(self):
        fsm_project = self.env['project.project'].create({
            'name': 'Field Service A',
            'is_fsm': True,
            'company_id': self.env.company.id,
        })
        employee = self.env['hr.employee'].create({
            'name': 'Test Employee', 'user_id': self.env.user.id,
        })
        employee.resource_id.write({'calendar_id': False})
        now = datetime.combine(datetime.now(), datetime.min.time())

        # first save
        task_form = Form(self.env['project.task'], view="project.view_task_form2")
        task_form.name = 'test task'
        task_form.project_id = fsm_project
        task_form.partner_id = self.partner
        task_form.user_ids = self.env.user
        task_form.planned_date_begin = False
        task_form.date_deadline = False
        task_form.save()

        # second save
        task_form.planned_date_begin = now
        task_form.date_deadline = now + relativedelta(days=1)
        task = task_form.save()
        self.assertEqual(task.allocated_hours, 8.0, "the task allocated hours should be 8.0")
