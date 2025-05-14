# -*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError

import re

avs_code_pattern = r'^[0-9]{3}\.[0-9]{3}$'


class l10nChSocialInsurance(models.Model):
    _inherit = 'l10n.ch.social.insurance'
    _description = 'Swiss: Social Insurances (AVS, AC)'

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        res.update({
            'avs_line_ids': [(0, 0, {
                'date_from': fields.Date.today().replace(month=1, day=1),
                'employer_rate': 5.3,
                'employee_rate': 5.3,
                'admin_fees': 1.2,
            })],
            'ac_line_ids': [(0, 0, {
                'date_from': fields.Date.today().replace(month=1, day=1),
                'employer_rate': 1.1,
                'employee_rate': 1.1,
                'employee_additional_rate': 0,
                'employer_additional_rate': 0,
            })],
            'l10n_ch_avs_rente_ids': [(0, 0, {
                'date_from': fields.Date.today().replace(month=1, day=1),
                'amount': 1400
            })],
            'l10n_ch_avs_ac_threshold_ids': [(0, 0, {
                'date_from': fields.Date.today().replace(month=1, day=1),
                'amount': 148200
            })],
            'l10n_ch_avs_acc_threshold_ids': [(0, 0, {
                'date_from': fields.Date.today().replace(month=1, day=1),
                'amount': 0
            })]
        })
        return res

    active = fields.Boolean(default=True)
    company_id = fields.Many2one("res.company", default=lambda self: self.env.company)
    insurance_company = fields.Char(required=False)
    no_laa_reason = fields.Char(help="If your company doesn't have a main LAA insurance, state the reason here.")
    no_lpp_reason = fields.Char(help="If your company doesn't have a main LPP insurance, state the reason here.")

    @api.constrains('insurance_code')
    def _check_insurance_code(self):
        """
        Format XXX.XXX with the first bloc greater than 0
        """
        for record in self:
            if record.insurance_code:
                if re.fullmatch(avs_code_pattern, record.insurance_code):
                    if record.insurance_code.split(".")[0] == "000":
                        raise ValidationError(_("AVS Insurance code is not plausible."))
                else:
                    raise ValidationError(_("AVS Insurance code is not plausible."))
    def _get_avs_rates(self, target):
        if not self:
            return 0, 0, 0
        for line in self.avs_line_ids:
            if line.date_from <= target and (not line.date_to or target <= line.date_to):
                return line.employee_rate, line.employer_rate, line.admin_fees
        raise UserError(_('No AVS rates found for date %s', target))



class l10nChSocialInsuranceAVSLine(models.Model):
    _inherit = 'l10n.ch.social.insurance.avs.line'
    _description = 'Swiss: Social Insurances - AVS Line'

    employee_rate = fields.Float(string="Employee Rate (%)", digits='Payroll Rate', default=5.3)
    employer_rate = fields.Float(string="Company Rate (%)", digits='Payroll Rate', default=5.3)
    admin_fees = fields.Float(string="Administrative Costs (%)", digits='Payroll Rate', default=1.2)
