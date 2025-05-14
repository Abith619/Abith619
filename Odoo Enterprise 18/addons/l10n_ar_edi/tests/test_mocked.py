# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.tests import tagged
from odoo.addons.l10n_ar_edi.tests.common import TestArEdiMockedCommon


@tagged("post_install", "post_install_l10n", "-at_install")
class TestArEdiMocked(TestArEdiMockedCommon):
    @classmethod
    @TestArEdiMockedCommon.setup_afip_ws('wsfe')
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = cls.res_partner_adhoc
        cls.journal = cls._create_journal(cls, 'wsfe')

    def test_01_invoice_a_product(self):
        # When the first record within an EDI journal is created,
        # it will try to pull the sequence from the database, and
        # if it can't find a suitable last sequence, it will query the API.
        # It does so in each onchange, which results in a large amount of these calls.
        sequence_requests = [('FECompUltimoAutorizado', 'FECompUltimoAutorizado-final', 'FECompUltimoAutorizado-final')] * 5
        with self.patch_client([
            *sequence_requests,
            ('FECAESolicitar', 'FECAESolicitar-final', 'FECAESolicitar-final'),
        ]):
            self._test_case('invoice_a', 'product')
