import io
import json
import csv
from odoo import models
from odoo.tools import json_default


class SlideChannelPartner(models.Model):
    _inherit = 'slide.channel.partner'

    def action_bulk_grade_csv(self):
        records = self
        if not records:
            records = self.search([])  

        data = {
            'ids': records.ids,
        }

        return {
            'type': 'ir.actions.report',
            'data': {
                'model': 'slide.channel.partner',
                'options': json.dumps(data, default=json_default),
                'output_format': 'csv',
                'report_name': 'Bulk_Student_Grades',
            },
            'report_type': 'csv',
        }

    def action_bulk_grade_xlsx(self):
        return self.action_bulk_grade_csv()
    def get_csv_report(self, data, response):
        records = self.browse(data.get('ids', []))

        output = io.StringIO()
        writer = csv.writer(output)

    
        writer.writerow([
            'Student Name',
            'Course',
            'Email',
            'Lesson Marks',
            'Assignment Marks',
            'Quiz Marks',
            'User Total Marks',
            'Total Marks',
            'Percentage',
            'Grade',
        ])
        for rec in records:
            writer.writerow([
                rec.partner_id.name or '',
                rec.channel_id.name or '',
                rec.partner_email or '',
                rec.total_lesson_marks or 0,
                rec.total_assignment_marks or 0,
                rec.total_quiz_xp or 0,
                rec.user_total_marks or 0,
                rec.overall_total_marks or 0,
                round(rec.overall_percentage or 0.0, 2),
                rec.grade_id.name if rec.grade_id else '',
            ])

        response.stream.write(output.getvalue().encode('utf-8'))
        output.close()
