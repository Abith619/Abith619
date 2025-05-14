# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.l10n_ch_hr_payroll_elm_transmission_account.tests.swissdec_common import TestSwissdecCommon
from odoo.tests.common import tagged
from freezegun import freeze_time


@tagged('post_install_l10n', 'post_install', '-at_install', 'swissdec_payroll')
class TestSwissdecTestCases(TestSwissdecCommon):
    @freeze_time("2024-01-01")
    def test_yearly_retrospective_2021_11(self):
        identifier = "yearly_retrospective_2021_11"
        generated_dict = self.yearly_retrospective_2021_11._get_declaration()
        self._compare_with_truth_base("yearly_retrospective", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_yearly_retrospective_2021_12(self):
        identifier = "yearly_retrospective_2021_12"
        generated_dict = self.yearly_retrospective_2021_12._get_declaration()
        self._compare_with_truth_base("yearly_retrospective", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_yearly_retrospective_2022_01(self):
        identifier = "yearly_retrospective_2022_01"
        generated_dict = self.yearly_retrospective_2022_01._get_declaration()
        self._compare_with_truth_base("yearly_retrospective", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_yearly_retrospective_2022_02(self):
        identifier = "yearly_retrospective_2022_02"
        generated_dict = self.yearly_retrospective_2022_02._get_declaration()
        self._compare_with_truth_base("yearly_retrospective", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_yearly_retrospective_2022_03(self):
        identifier = "yearly_retrospective_2022_03"
        generated_dict = self.yearly_retrospective_2022_03._get_declaration()
        self._compare_with_truth_base("yearly_retrospective", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_yearly_retrospective_2022_04(self):
        identifier = "yearly_retrospective_2022_04"
        generated_dict = self.yearly_retrospective_2022_04._get_declaration()
        self._compare_with_truth_base("yearly_retrospective", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_yearly_retrospective_2022_05(self):
        identifier = "yearly_retrospective_2022_05"
        generated_dict = self.yearly_retrospective_2022_05._get_declaration()
        self._compare_with_truth_base("yearly_retrospective", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_yearly_retrospective_2022_06(self):
        identifier = "yearly_retrospective_2022_06"
        generated_dict = self.yearly_retrospective_2022_06._get_declaration()
        self._compare_with_truth_base("yearly_retrospective", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_yearly_retrospective_2022_07(self):
        identifier = "yearly_retrospective_2022_07"
        generated_dict = self.yearly_retrospective_2022_07._get_declaration()
        self._compare_with_truth_base("yearly_retrospective", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_yearly_retrospective_2022_08(self):
        identifier = "yearly_retrospective_2022_08"
        generated_dict = self.yearly_retrospective_2022_08._get_declaration()
        self._compare_with_truth_base("yearly_retrospective", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_yearly_retrospective_2022_09(self):
        identifier = "yearly_retrospective_2022_09"
        generated_dict = self.yearly_retrospective_2022_09._get_declaration()
        self._compare_with_truth_base("yearly_retrospective", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_yearly_retrospective_2022_10(self):
        identifier = "yearly_retrospective_2022_10"
        generated_dict = self.yearly_retrospective_2022_10._get_declaration()
        self._compare_with_truth_base("yearly_retrospective", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_yearly_retrospective_2022_11(self):
        identifier = "yearly_retrospective_2022_11"
        generated_dict = self.yearly_retrospective_2022_11._get_declaration()
        self._compare_with_truth_base("yearly_retrospective", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_yearly_retrospective_2022_12(self):
        identifier = "yearly_retrospective_2022_12"
        generated_dict = self.yearly_retrospective_2022_12._get_declaration()
        self._compare_with_truth_base("yearly_retrospective", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_yearly_retrospective_2023_01(self):
        identifier = "yearly_retrospective_2023_01"
        generated_dict = self.yearly_retrospective_2023_01._get_declaration()
        self._compare_with_truth_base("yearly_retrospective", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_yearly_retrospective_2023_02(self):
        identifier = "yearly_retrospective_2023_02"
        generated_dict = self.yearly_retrospective_2023_02._get_declaration()
        self._compare_with_truth_base("yearly_retrospective", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_ema_declaration_2021_11(self):
        identifier = "ema_declaration_2021_11"
        generated_dict = self.ema_declaration_2021_11._get_declaration()
        self._compare_with_truth_base("ema_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_ema_declaration_2021_12(self):
        identifier = "ema_declaration_2021_12"
        generated_dict = self.ema_declaration_2021_12._get_declaration()
        self._compare_with_truth_base("ema_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_ema_declaration_2022_01(self):
        identifier = "ema_declaration_2022_01"
        generated_dict = self.ema_declaration_2022_01._get_declaration()
        self._compare_with_truth_base("ema_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_ema_declaration_2022_02(self):
        identifier = "ema_declaration_2022_02"
        generated_dict = self.ema_declaration_2022_02._get_declaration()
        self._compare_with_truth_base("ema_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_ema_declaration_2022_03(self):
        identifier = "ema_declaration_2022_03"
        generated_dict = self.ema_declaration_2022_03._get_declaration()
        self._compare_with_truth_base("ema_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_ema_declaration_2022_04(self):
        identifier = "ema_declaration_2022_04"
        generated_dict = self.ema_declaration_2022_04._get_declaration()
        self._compare_with_truth_base("ema_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_ema_declaration_2022_05(self):
        identifier = "ema_declaration_2022_05"
        generated_dict = self.ema_declaration_2022_05._get_declaration()
        self._compare_with_truth_base("ema_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_ema_declaration_2022_06(self):
        identifier = "ema_declaration_2022_06"
        generated_dict = self.ema_declaration_2022_06._get_declaration()
        self._compare_with_truth_base("ema_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_ema_declaration_2022_07(self):
        identifier = "ema_declaration_2022_07"
        generated_dict = self.ema_declaration_2022_07._get_declaration()
        self._compare_with_truth_base("ema_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_ema_declaration_2022_08(self):
        identifier = "ema_declaration_2022_08"
        generated_dict = self.ema_declaration_2022_08._get_declaration()
        self._compare_with_truth_base("ema_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_ema_declaration_2022_09(self):
        identifier = "ema_declaration_2022_09"
        generated_dict = self.ema_declaration_2022_09._get_declaration()
        self._compare_with_truth_base("ema_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_ema_declaration_2022_10(self):
        identifier = "ema_declaration_2022_10"
        generated_dict = self.ema_declaration_2022_10._get_declaration()
        self._compare_with_truth_base("ema_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_ema_declaration_2022_11(self):
        identifier = "ema_declaration_2022_11"
        generated_dict = self.ema_declaration_2022_11._get_declaration()
        self._compare_with_truth_base("ema_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_ema_declaration_2022_12(self):
        identifier = "ema_declaration_2022_12"
        generated_dict = self.ema_declaration_2022_12._get_declaration()
        self._compare_with_truth_base("ema_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_ema_declaration_2023_01(self):
        identifier = "ema_declaration_2023_01"
        generated_dict = self.ema_declaration_2023_01._get_declaration()
        self._compare_with_truth_base("ema_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_ema_declaration_2023_02(self):
        identifier = "ema_declaration_2023_02"
        generated_dict = self.ema_declaration_2023_02._get_declaration()
        self._compare_with_truth_base("ema_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_statistic_declaration_2021_11(self):
        identifier = "statistic_declaration_2021_11"
        generated_dict = self.statistic_declaration_2021_11._get_declaration()
        self._compare_with_truth_base("statistic_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_statistic_declaration_2021_12(self):
        identifier = "statistic_declaration_2021_12"
        generated_dict = self.statistic_declaration_2021_12._get_declaration()
        self._compare_with_truth_base("statistic_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_statistic_declaration_2022_01(self):
        identifier = "statistic_declaration_2022_01"
        generated_dict = self.statistic_declaration_2022_01._get_declaration()
        self._compare_with_truth_base("statistic_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_statistic_declaration_2022_02(self):
        identifier = "statistic_declaration_2022_02"
        generated_dict = self.statistic_declaration_2022_02._get_declaration()
        self._compare_with_truth_base("statistic_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_statistic_declaration_2022_03(self):
        identifier = "statistic_declaration_2022_03"
        generated_dict = self.statistic_declaration_2022_03._get_declaration()
        self._compare_with_truth_base("statistic_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_statistic_declaration_2022_04(self):
        identifier = "statistic_declaration_2022_04"
        generated_dict = self.statistic_declaration_2022_04._get_declaration()
        self._compare_with_truth_base("statistic_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_statistic_declaration_2022_05(self):
        identifier = "statistic_declaration_2022_05"
        generated_dict = self.statistic_declaration_2022_05._get_declaration()
        self._compare_with_truth_base("statistic_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_statistic_declaration_2022_06(self):
        identifier = "statistic_declaration_2022_06"
        generated_dict = self.statistic_declaration_2022_06._get_declaration()
        self._compare_with_truth_base("statistic_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_statistic_declaration_2022_07(self):
        identifier = "statistic_declaration_2022_07"
        generated_dict = self.statistic_declaration_2022_07._get_declaration()
        self._compare_with_truth_base("statistic_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_statistic_declaration_2022_08(self):
        identifier = "statistic_declaration_2022_08"
        generated_dict = self.statistic_declaration_2022_08._get_declaration()
        self._compare_with_truth_base("statistic_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_statistic_declaration_2022_09(self):
        identifier = "statistic_declaration_2022_09"
        generated_dict = self.statistic_declaration_2022_09._get_declaration()
        self._compare_with_truth_base("statistic_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_statistic_declaration_2022_10(self):
        identifier = "statistic_declaration_2022_10"
        generated_dict = self.statistic_declaration_2022_10._get_declaration()
        self._compare_with_truth_base("statistic_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_statistic_declaration_2022_11(self):
        identifier = "statistic_declaration_2022_11"
        generated_dict = self.statistic_declaration_2022_11._get_declaration()
        self._compare_with_truth_base("statistic_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_statistic_declaration_2022_12(self):
        identifier = "statistic_declaration_2022_12"
        generated_dict = self.statistic_declaration_2022_12._get_declaration()
        self._compare_with_truth_base("statistic_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_statistic_declaration_2023_01(self):
        identifier = "statistic_declaration_2023_01"
        generated_dict = self.statistic_declaration_2023_01._get_declaration()
        self._compare_with_truth_base("statistic_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_statistic_declaration_2023_02(self):
        identifier = "statistic_declaration_2023_02"
        generated_dict = self.statistic_declaration_2023_02._get_declaration()
        self._compare_with_truth_base("statistic_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_is_declaration_2021_11(self):
        identifier = "is_declaration_2021_11"
        generated_dict = self.is_declaration_2021_11._get_declaration()
        self._compare_with_truth_base("is_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_is_declaration_2021_12(self):
        identifier = "is_declaration_2021_12"
        generated_dict = self.is_declaration_2021_12._get_declaration()
        self._compare_with_truth_base("is_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_is_declaration_2022_01(self):
        identifier = "is_declaration_2022_01"
        generated_dict = self.is_declaration_2022_01._get_declaration()
        self._compare_with_truth_base("is_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_is_declaration_2022_02(self):
        identifier = "is_declaration_2022_02"
        generated_dict = self.is_declaration_2022_02._get_declaration()
        self._compare_with_truth_base("is_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_is_declaration_2022_03(self):
        identifier = "is_declaration_2022_03"
        generated_dict = self.is_declaration_2022_03._get_declaration()
        self._compare_with_truth_base("is_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_is_declaration_2022_04(self):
        identifier = "is_declaration_2022_04"
        generated_dict = self.is_declaration_2022_04._get_declaration()
        self._compare_with_truth_base("is_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_is_declaration_2022_05(self):
        identifier = "is_declaration_2022_05"
        generated_dict = self.is_declaration_2022_05._get_declaration()
        self._compare_with_truth_base("is_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_is_declaration_2022_06(self):
        identifier = "is_declaration_2022_06"
        generated_dict = self.is_declaration_2022_06._get_declaration()
        self._compare_with_truth_base("is_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_is_declaration_2022_07(self):
        identifier = "is_declaration_2022_07"
        generated_dict = self.is_declaration_2022_07._get_declaration()
        self._compare_with_truth_base("is_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_is_declaration_2022_08(self):
        identifier = "is_declaration_2022_08"
        generated_dict = self.is_declaration_2022_08._get_declaration()
        self._compare_with_truth_base("is_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_is_declaration_2022_09(self):
        identifier = "is_declaration_2022_09"
        generated_dict = self.is_declaration_2022_09._get_declaration()
        self._compare_with_truth_base("is_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_is_declaration_2022_10(self):
        identifier = "is_declaration_2022_10"
        generated_dict = self.is_declaration_2022_10._get_declaration()
        self._compare_with_truth_base("is_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_is_declaration_2022_11(self):
        identifier = "is_declaration_2022_11"
        generated_dict = self.is_declaration_2022_11._get_declaration()
        self._compare_with_truth_base("is_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_is_declaration_2022_12(self):
        identifier = "is_declaration_2022_12"
        generated_dict = self.is_declaration_2022_12._get_declaration()
        self._compare_with_truth_base("is_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_is_declaration_2023_01(self):
        identifier = "is_declaration_2023_01"
        generated_dict = self.is_declaration_2023_01._get_declaration()
        self._compare_with_truth_base("is_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_is_declaration_2023_02(self):
        identifier = "is_declaration_2023_02"
        generated_dict = self.is_declaration_2023_02._get_declaration()
        self._compare_with_truth_base("is_declaration", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_rectificate_2022_01(self):
        identifier = "rectificate_2022_01"
        generated_dict = self.rectificate_2022_01._get_declaration()
        self._compare_with_truth_base("rectificate", identifier, generated_dict)

    @freeze_time("2024-01-01")
    def test_yearly_prospective_2023_01(self):
        identifier = "yearly_prospective_2023_01"
        generated_dict = self.yearly_prospective_2023_01._get_declaration()
        self._compare_with_truth_base("yearly_prospective", identifier, generated_dict)
