from freezegun import freeze_time

from odoo import Command, release
from odoo.tests import tagged
from odoo.addons.l10n_cz_reports_2025.tests.test_l10n_cz_reports_2025_common import CzechReportsCommon


@tagged('post_install_l10n', 'post_install', '-at_install')
class CzechVIESReportTest(CzechReportsCommon):
    @freeze_time('2019-12-31')
    def setUp(self):
        super().setUp()
        self.env['account.move'].create({
            'invoice_date': '2019-11-12',
            'taxable_supply_date': '2019-11-12',
            'move_type': 'in_invoice',
            'partner_id': self.partner_eu_1.id,
            'invoice_line_ids': [Command.create(line_data) for line_data in [
                {'quantity': 1, 'price_unit': 100, 'l10n_cz_transaction_code': '0'},
                {'quantity': 3, 'price_unit': 10, 'l10n_cz_transaction_code': '0'},
                {'quantity': 2, 'price_unit': 30, 'l10n_cz_transaction_code': '1'},
            ]],
        }).action_post()
        self.env['account.move'].create({
            'invoice_date': '2019-11-12',
            'taxable_supply_date': '2019-11-12',
            'move_type': 'in_invoice',
            'partner_id': self.partner_eu_1.id,
            'invoice_line_ids': [Command.create(line_data) for line_data in [
                {'quantity': 2, 'price_unit': 90, 'l10n_cz_transaction_code': '1'},
                {'quantity': 3, 'price_unit': 20, 'l10n_cz_transaction_code': '2'},
                {'quantity': 1, 'price_unit': 80, 'l10n_cz_transaction_code': '3'},
            ]],
        }).action_post()
        self.env['account.move'].create({
            'invoice_date': '2019-11-12',
            'taxable_supply_date': '2019-11-12',
            'move_type': 'in_invoice',
            'partner_id': self.partner_eu_2.id,
            'invoice_line_ids': [Command.create(line_data) for line_data in [
                {'quantity': 3, 'price_unit': 20, 'l10n_cz_transaction_code': '1'},
                {'quantity': 2, 'price_unit': 90, 'l10n_cz_transaction_code': '1'},
                {'quantity': 1, 'price_unit': 80, 'l10n_cz_transaction_code': '3'},
            ]],
        }).action_post()
        self.env['account.move'].create({
            'invoice_date': '2019-11-12',
            'taxable_supply_date': '2019-11-12',
            'move_type': 'in_invoice',
            'partner_id': self.partner_eu_3.id,
            'invoice_line_ids': [Command.create({'quantity': 3, 'price_unit': 20, 'l10n_cz_transaction_code': '2'})],
        }).action_post()
        self.env['account.move'].create({
            'invoice_date': '2019-11-12',
            'taxable_supply_date': '2019-11-12',
            'move_type': 'in_invoice',
            'partner_id': self.partner_non_eu.id,
            'invoice_line_ids': [Command.create(line_data) for line_data in [
                {'quantity': 3, 'price_unit': 20, 'l10n_cz_transaction_code': '0'},
                {'quantity': 2, 'price_unit': 90, 'l10n_cz_transaction_code': '1'},
                {'quantity': 1, 'price_unit': 80, 'l10n_cz_transaction_code': '2'},
                {'quantity': 4, 'price_unit': 50, 'l10n_cz_transaction_code': '3'},
            ]],
        }).action_post()
        self.env.flush_all()

    @freeze_time('2019-12-31')
    def test_cz_vies_report(self):
        report = self.env.ref('l10n_cz_reports_2025.vies_summary_report')
        options = report.get_options({})

        # Excluding journal items lines from the test
        lines = [line for line in report._get_lines({**options, 'unfold_all': True}) if line['level'] != 6]

        self.assertLinesValues(
            lines,
            # Name                   county code        vat number            supplies code         supplies number                total
            [0,                          1,                 2,                      3,                     4,                        5],
            [
                ('B. SECTION',          '',                '',                      '',                    21,                       890),
                ('Partner EU 1',        'FR',              'FR23334175221',         '',                    12,                        510),
                ('0 Goods',             'FR',              'FR23334175221',         '0',                   4,                        130),
                ('1 Business asset',    'FR',              'FR23334175221',         '1',                   4,                        240),
                ('2 Triangular',        'FR',              'FR23334175221',         '2',                   3,                        60),
                ('3 Service',           'FR',              'FR23334175221',         '3',                   1,                        80),
                ('Partner EU 2',        'DE',              'DE123456788',           '',                    6,                        320),
                ('1 Business asset',    'DE',              'DE123456788',           '1',                   5,                        240),
                ('3 Service',           'DE',              'DE123456788',           '3',                   1,                        80),
                ('Partner EU 3',        'BE',              'BE0477472701',          '',                    3,                        60),
                ('2 Triangular',        'BE',              'BE0477472701',          '2',                   3,                        60),
            ],
            options,
        )

    @freeze_time('2019-12-31')
    def test_cz_vies_report_default_options_export(self):
        report = self.env.ref('l10n_cz_reports_2025.vies_summary_report')
        options = report.get_options({})

        generated_xml = self.env['l10n_cz.vies.summary.report.handler'].export_to_xml(options)['file_content']
        expected_xml = f"""
            <Pisemnost nazevSW="Odoo SA" verzeSW="{release.version}">
            <DPHSHV verzePis="02.01">
                <VetaD shvies_forma="N" dokument="SHV" k_uladis="DPH" mesic="11" rok="2019"/>
                <VetaP typ_ds="P" zkrobchjm="company_1_data" c_pracufo="2001" c_ufo="451" dic="12345679" email="info@company.czexample.com"/>
                <VetaR k_stat="FR" c_vat="FR23334175221" k_pln_eu="0" pln_pocet="4" pln_hodnota="130.0"/>
                <VetaR k_stat="FR" c_vat="FR23334175221" k_pln_eu="1" pln_pocet="4" pln_hodnota="240.0"/>
                <VetaR k_stat="FR" c_vat="FR23334175221" k_pln_eu="2" pln_pocet="3" pln_hodnota="60.0"/>
                <VetaR k_stat="FR" c_vat="FR23334175221" k_pln_eu="3" pln_pocet="1" pln_hodnota="80.0"/>
                <VetaR k_stat="DE" c_vat="DE123456788"   k_pln_eu="1" pln_pocet="5" pln_hodnota="240.0"/>
                <VetaR k_stat="DE" c_vat="DE123456788"   k_pln_eu="3" pln_pocet="1" pln_hodnota="80.0"/>
                <VetaR k_stat="BE" c_vat="BE0477472701"  k_pln_eu="2" pln_pocet="3" pln_hodnota="60.0"/>
            </DPHSHV>
            </Pisemnost>
        """
        self.assertXmlTreeEqual(
            self.get_xml_tree_from_string(generated_xml),
            self.get_xml_tree_from_string(expected_xml),
        )

    @freeze_time('2019-12-31')
    def test_cz_vies_report_custom_options_export(self):
        report = self.env.ref('l10n_cz_reports_2025.vies_summary_report')
        options = self._generate_options(report, date_from='2018-07-01', date_to='2018-09-30')
        self.env.company.partner_id.company_type = 'person'

        generated_xml = self.env['l10n_cz.vies.summary.report.handler'].export_to_xml(options)['file_content']
        expected_xml = f"""
            <Pisemnost nazevSW="Odoo SA" verzeSW="{release.version}">
            <DPHSHV verzePis="02.01">
                <VetaD shvies_forma="N" dokument="SHV" k_uladis="DPH" ctvrt="3" rok="2018"/>
                <VetaP typ_ds="F" zkrobchjm="company_1_data" c_pracufo="2001" c_ufo="451" dic="12345679" email="info@company.czexample.com"/>
            </DPHSHV>
            </Pisemnost>
        """
        self.assertXmlTreeEqual(
            self.get_xml_tree_from_string(generated_xml),
            self.get_xml_tree_from_string(expected_xml),
        )

    def test_cz_vies_report_with_miscellaneous_entry(self):
        self.env['account.move'].create({
            'invoice_date': '2025-01-01',
            'taxable_supply_date': '2025-01-01',
            'move_type': 'in_invoice',
            'partner_id': self.partner_eu_1.id,
            'invoice_line_ids': [Command.create(line_data) for line_data in [
                {
                    'price_unit': 20,
                    'deferred_start_date': '2025-01-01',
                    # Create deferred entries --> not an invoice/refund (with a transaction code set)
                    'deferred_end_date': '2025-12-31',
                    'l10n_cz_transaction_code': '0',
                },
            ]],
        }).action_post()
        report = self.env.ref('l10n_cz_reports_2025.vies_summary_report')
        options = self._generate_options(report, date_from='2025-01-01', date_to='2025-12-31')

        self.assertLinesValues(
            report._get_lines({**options, 'unfold_all': True}), [0, 5],
            #        name              total
            [
                ('B. SECTION',          20),
                ('Partner EU 1',        20),
                ('0 Goods',             20),
                ('BILL/2025/01/0001',   20),
            ],
            options,
        )
