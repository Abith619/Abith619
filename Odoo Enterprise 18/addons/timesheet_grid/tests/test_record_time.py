# Part of Odoo. See LICENSE file for full copyright and licensing details.
# -*- coding: utf-8 -*-

from datetime import date, timedelta

from odoo.tests import HttpCase, tagged

from odoo.addons.hr_timesheet.tests.test_timesheet import TestCommonTimesheet


@tagged('-at_install', 'post_install')
class TestRecordTime(TestCommonTimesheet, HttpCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.env['project.project'].create({
            'name': 'Test Project'
        })

    def test_record_time(self):
        self.start_tour('/odoo', 'timesheet_record_time', login='admin', timeout=100)

    def test_timesheet_overtime(self):
        self.empl_employee.resource_calendar_id.flexible_hours = True
        # Get this week's Monday (or next Monday if today is Sunday)
        relevant_monday = date.today() + timedelta(
            days=-date.today().weekday() + (7 if date.today().weekday() == 6 else 0)
        )
        timesheets = self.env['account.analytic.line'].create([
            {
                'name': f"Test Timesheet {i+1}",
                'project_id': self.project_customer.id,
                'task_id': self.task1.id,
                'date': relevant_monday - timedelta(days=i),
                'unit_amount': 3.0 + i,
                'employee_id': self.empl_employee.id,
            }
            for i in range(8)
        ])

        self.start_tour('/odoo', 'timesheet_overtime_hour_encoding', login=self.user_employee.login, timeout=100)

        timesheets[6].write({'unit_amount': 0.0})

        self.env['res.config.settings'].create({'timesheet_encode_method': 'days'}).execute()
        self.start_tour('/odoo', 'timesheet_overtime_day_encoding', login=self.user_employee.login, timeout=100)
