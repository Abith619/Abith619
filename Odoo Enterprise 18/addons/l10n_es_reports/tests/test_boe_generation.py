# -*- coding: utf-8 -*-

from freezegun import freeze_time

from odoo.addons.l10n_es_reports.tests.common import TestEsAccountReportsCommon
from odoo import fields
from odoo.tests import tagged


@tagged('post_install_l10n', 'post_install', '-at_install')
class TestBOEGeneration(TestEsAccountReportsCommon):
    """ Basic tests checking the generation of BOE files is still possible.
    """

    def _check_boe_111_to_303(self, modelo_number):
        self.init_invoice('out_invoice', partner=self.spanish_partner, amounts=[10000], invoice_date=fields.Date.today(), taxes=self.spanish_test_tax, post=True)
        report = self.env.ref('l10n_es.mod_%s' % modelo_number)
        report.filter_multi_company = 'disabled'
        options = self._generate_options(report, fields.Date.from_string('2020-12-01'), fields.Date.from_string('2020-12-31'))
        self._check_boe_export(report, options, modelo_number)

    @freeze_time('2020-12-22')
    def test_boe_mod_111(self):
        self._check_boe_111_to_303('111')

    @freeze_time('2020-12-22')
    def test_boe_mod_115(self):
        self._check_boe_111_to_303('115')

    @freeze_time('2020-12-22')
    def test_boe_mod_303(self):
        self._check_boe_111_to_303('303')

    @freeze_time('2020-12-22')
    def test_boe_mod_347(self):
        invoice = self.init_invoice('out_invoice', partner=self.spanish_partner, amounts=[10000], invoice_date=fields.Date.today())
        invoice.l10n_es_reports_mod347_invoice_type = 'regular'
        invoice._post()
        report = self.env.ref('l10n_es_reports.mod_347')
        report.filter_multi_company = 'disabled'
        options = self._generate_options(report, fields.Date.from_string('2020-01-01'), fields.Date.from_string('2020-12-31'))
        self._check_boe_export(report, options, 347)

    @freeze_time('2020-12-22')
    def test_boe_mod_349(self):
        self.partner_a.write({
            'country_id': self.env.ref('base.be').id,
            'vat': "BE0477472701",
        })
        invoice = self.init_invoice('out_invoice', partner=self.partner_a, amounts=[10000], invoice_date=fields.Date.today())
        invoice.l10n_es_reports_mod349_invoice_type = 'E'
        invoice._post()
        report = self.env.ref('l10n_es_reports.mod_349')
        report.filter_multi_company = 'disabled'
        options = self._generate_options(report, fields.Date.from_string('2020-12-01'), fields.Date.from_string('2020-12-31'))
        self._check_boe_export(report, options, 349)

    @freeze_time('2020-12-22')
    def test_boe_mod_390(self):
        report = self.env.ref('l10n_es.mod_390')
        options = self._generate_options(report, '2020-01-01', '2020-12-31')
        self._check_boe_export(report, options, 390, additional_context={
            'default_physical_person_name': "Bernard Gagnant",
            'default_principal_activity': "Selling",
            'default_principal_iae_epigrafe': "EAAA",
            'default_principal_code_activity': "AAA",
            'default_judicial_person_name': "Bebert",
            'default_judicial_person_nif': "123",
            'default_judicial_person_procuration_date': '2020-01-01',
            'default_judicial_person_notary': "Maître Gagnant",
        })
