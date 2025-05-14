# Part of Odoo. See LICENSE file for full copyright and licensing details.
import base64
from odoo.exceptions import ValidationError
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from pytz import utc


class L10nCHSwissdecTransmitter(models.AbstractModel):
    _name = 'l10n.ch.swissdec.transmitter'
    _inherit = 'mail.thread'
    _description = 'Abstract Swissdec Transmitter'

    @api.model
    def default_get(self, field_list=None):
        if self.env.company.country_id.code != "CH":
            raise UserError(_('You must be logged in a Swiss company to use this feature'))
        return super().default_get(field_list)

    def _get_default_name(self):
        now = fields.Datetime.now()
        month = now.month
        year = now.year
        return _("Declaration %(month)s/%(year)s", month=month, year=year)

    active = fields.Boolean(default=True)
    name = fields.Char(required=True, default=_get_default_name)
    year = fields.Integer(string="Year", required=True, default=lambda self: fields.Date.today().year)
    month = fields.Selection(string="Month",selection=[
        ('1', 'January'),
        ('2', 'February'),
        ('3', 'March'),
        ('4', 'April'),
        ('5', 'May'),
        ('6', 'June'),
        ('7', 'July'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    ], required=True, default=lambda self: str((fields.Date.today()).month))
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company, domain=lambda self: [('country_id', '=', self.env.ref('base.ch'))])

    l10n_ch_declare_salary_data = fields.Json()
    actionable_warnings = fields.Json()

    l10n_ch_swissdec_declaration_ids = fields.One2many("l10n.ch.swissdec.declaration", "res_id")
    l10n_ch_swissdec_declaration_ids_size = fields.Integer(compute="_compute_l10n_ch_swissdec_declaration_ids_size")

    replacement_declaration = fields.Boolean()
    substituted_declaration_id = fields.Many2one("l10n.ch.swissdec.declaration", domain=lambda self: [('res_model', '=', self._name)], string="Declaration To Substitute")

    test_transmission = fields.Boolean(string="Test Transmission")
    attachment_ids = fields.One2many('ir.attachment', 'res_id', string='Attachments')

    def action_prepare_data(self):
        if self.year < fields.Date.today().year - 1 or self.year > fields.Date.today().year:
            raise ValidationError(_("You can only transmit data for the current or previous year."))

    @api.depends("l10n_ch_swissdec_declaration_ids")
    def _compute_l10n_ch_swissdec_declaration_ids_size(self):
        for job in self:
            job.l10n_ch_swissdec_declaration_ids_size = len(job.l10n_ch_swissdec_declaration_ids)

    def _get_institutions(self):
        return []

    def _get_declaration(self):
        return {}

    def action_declare_salary(self):
        self.ensure_one()
        declare_salary = self._get_declaration()

        result = self.env.company._l10n_ch_swissdec_request('declare_salary', data=declare_salary, is_test=self.test_transmission)
        response = result['soap_response']
        message_archive = result['request_xml']
        response_archive = result['response_xml']

        if response:
            job_key = response['JobKey']
            timestamp = fields.Datetime.from_string(response['ResponseContext']['TransmissionDate']).astimezone(utc).replace(tzinfo=None)
            declaration = self.env["l10n.ch.swissdec.declaration"].create({
                "name": f"{self.name} - {response['ResponseContext']['DeclarationID']}",
                "res_id": self.id,
                "res_model": self._name,
                "year": self.year,
                "month": self.month,
                "test_transmission": self.test_transmission,
                "job_key": job_key,
                "swissdec_declaration_id": response['ResponseContext']['DeclarationID'],
                "transmission_date": timestamp
            })
            attachment_request = self.env['ir.attachment'].create({
                'name': _("Declaration_%s_request.xml", response['ResponseContext']['DeclarationID']),
                'datas': base64.encodebytes(message_archive.encode()),
                'res_id': declaration.id,
                'res_model': declaration._name,
            })

            attachment_response = self.env['ir.attachment'].create({
                'name': _("Declaration_%s_response.xml", response['ResponseContext']['DeclarationID']),
                'datas': base64.encodebytes(response_archive.encode()),
                'res_id': declaration.id,
                'res_model': declaration._name,
            })
            declaration.message_post(attachment_ids=[attachment_request.id, attachment_response.id], body=_('Salary Declaration Archive'))

            return {
                'name': _('Declaration'),
                'res_model': 'l10n.ch.swissdec.declaration',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_id': declaration.id,
                'target': "current"
            }

    def action_open_swissec_declarations(self):
        self.ensure_one()
        return {
            'name': _('Declarations'),
            'res_model': 'l10n.ch.swissdec.declaration',
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'domain': [('res_model', '=', self._name), ('res_id', '=', self.id)],
        }
