# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import base64
import io

from collections import defaultdict

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools.misc import xlsxwriter


class L10nChMonthlySummaryWizard(models.Model):
    _inherit = 'l10n.ch.monthly.summary'

    def _get_valid_payslips(self):
        domain = [
            ('state', 'in', ['paid', 'done']),
            ('company_id', 'in', self.company_ids.ids),
            ('date_from', '>=', self.date_start),
            ('date_to', '<=', self.date_end),
            ('struct_id.code', '=', 'CHMONTHLYELM')
        ]
        payslips = self.env['hr.payslip'].search(domain)
        if not payslips:
            raise UserError(_("There is no paid or done payslips over the selected period."))
        return payslips

    def _get_line_values(self):
        self.ensure_one()
        payslips = self._get_valid_payslips()

        lines = payslips.line_ids.filtered(lambda l: l.salary_rule_id.l10n_ch_code)
        is_lines = payslips.l10n_ch_is_log_line_ids
        rules_company = defaultdict(lambda: defaultdict(float))
        for line in lines:
            if line.salary_rule_id.l10n_ch_code == "9041":
                rules_company["9041"][f'LAAC Salary - Code {line.slip_id.l10n_ch_additional_accident_insurance_line_ids[0].solution_code}'] += line.total
            elif line.salary_rule_id.l10n_ch_code == "9043":
                rules_company["9041"][f'LAAC Salary - Code {line.slip_id.l10n_ch_additional_accident_insurance_line_ids[1].solution_code}'] += line.total
            elif line.salary_rule_id.l10n_ch_code == "5041":
                rules_company["5041"][f'{line.name[:-2]} - Code {line.slip_id.l10n_ch_additional_accident_insurance_line_ids[0].solution_code}'] += line.total
            elif line.salary_rule_id.l10n_ch_code == "5043":
                rules_company["5041"][f'{line.name[:-2]} - Code {line.slip_id.l10n_ch_additional_accident_insurance_line_ids[1].solution_code}'] += line.total
            elif line.salary_rule_id.l10n_ch_code == "5045":
                rules_company["5045"][f'{line.name[:-2]} - Code {line.slip_id.l10n_ch_sickness_insurance_line_ids[0].solution_code}'] += line.total
            elif line.salary_rule_id.l10n_ch_code == "5047":
                rules_company["5045"][f'{line.name[:-2]} - Code {line.slip_id.l10n_ch_sickness_insurance_line_ids[1].solution_code}'] += line.total

            elif line.salary_rule_id.l10n_ch_code == "9051":
                rules_company["9051"][f'IJM Salary - Code {line.slip_id.l10n_ch_sickness_insurance_line_ids[0].solution_code}'] += line.total
            elif line.salary_rule_id.l10n_ch_code == "9053":
                rules_company["9051"][f'IJM Salary - Code {line.slip_id.l10n_ch_sickness_insurance_line_ids[1].solution_code}'] += line.total
            else:
                if line.salary_rule_id.l10n_ch_code not in ["9070", "9072", "9071", "9073", "9075", "5061", "5062", "5060"]:
                    rules_company[line.salary_rule_id.l10n_ch_code][line.name] += line.total

        for line in is_lines:
            if line.code == "ISSALARY":
                rules_company["9070"][f'Source-Tax Salary - {line.source_tax_canton}-{line.is_code}'] += line.amount
            if line.code == "ISDTSALARY":
                rules_company["9073"][f'Source-Tax Rate Determinant Salary - {line.source_tax_canton}'] += line.amount
            if line.code == "IS":
                rules_company["5060"][f'Source-Tax Amount - {line.source_tax_canton}-{line.is_code}'] += -line.amount

        rules = sorted(
            [
                {"code": code, "name": name, "value": round(value, 2)}
                for code, names in rules_company.items()
                for name, value in names.items()
            ], key=lambda rule: rule['code']
        )

        return rules

    def action_generate_pdf(self):
        self.ensure_one()
        report_data = {
            'date_start': self.date_start.strftime("%d/%m/%Y"),
            'date_end': self.date_end.strftime("%d/%m/%Y"),
            'line_values': self._get_line_values(),
            "company": self.env.company
        }

        filename = '%s-%s-monthly-summary.pdf' % (self.date_start.strftime("%d%B%Y"), self.date_end.strftime("%d%B%Y"))
        monthly_summary, _ = self.env["ir.actions.report"].sudo()._render_qweb_pdf(
            self.env.ref('l10n_ch_hr_payroll.action_report_monthly_summary'),
            res_ids=self.ids, data=report_data)

        self.monthly_summary_pdf_filename = filename
        self.monthly_summary_pdf_file = base64.encodebytes(monthly_summary)

    def action_generate_xls(self):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})

        line_values = self._get_line_values()

        for aggregate_record, rules_data in line_values.items():
            worksheet = workbook.add_worksheet(aggregate_record.name)
            style_highlight = workbook.add_format({'bold': True, 'pattern': 1, 'bg_color': '#E0E0E0', 'align': 'center'})
            style_normal = workbook.add_format({'align': 'center'})
            row = 0
            col = 0

            headers = ["Code", "Name", "Amount"]
            rows = [(rule.l10n_ch_code, rule.name, total) for rule, total in rules_data.items()]

            for header in headers:
                worksheet.write(row, col, header, style_highlight)
                worksheet.set_column(col, col, 30)
                col += 1

            row = 1
            for employee_row in rows:
                col = 0
                for employee_data in employee_row:
                    worksheet.write(row, col, employee_data, style_normal)
                    col += 1
                row += 1

        workbook.close()
        xlsx_data = output.getvalue()

        self.monthly_summary_xls_file = base64.encodebytes(xlsx_data)
        self.monthly_summary_xls_filename = '%s-%s-monthly-summary.xlsx' % (self.date_start.strftime("%d%B%Y"), self.date_end.strftime("%d%B%Y"))
