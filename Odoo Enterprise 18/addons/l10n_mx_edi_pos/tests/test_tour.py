# -*- coding: utf-8 -*-
from .common import TestMxEdiPosCommon
import odoo
from odoo.tests import tagged
from odoo.addons.point_of_sale.tests.test_frontend import TestPointOfSaleHttpCommon


@tagged('post_install_l10n', 'post_install', '-at_install')
class TestUi(TestMxEdiPosCommon, TestPointOfSaleHttpCommon):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner_mx.write({
            "name": "Arturo Garcia",
            "l10n_mx_edi_usage": "I01",
        })

    def test_mx_pos_invoice_order(self):
        self.start_tour("/odoo", "l10n_mx_edi_pos.tour_invoice_order", login=self.env.user.login)

    def test_mx_pos_invoice_order_default_usage(self):
        self.start_tour("/odoo", "l10n_mx_edi_pos.tour_invoice_order_default_usage", login=self.env.user.login)

    def test_mx_pos_invoice_previous_order(self):
        self.start_tour("/odoo", "l10n_mx_edi_pos.tour_invoice_previous_order", login=self.env.user.login)
        invoice = self.env['account.move'].search([('move_type', '=', 'out_invoice')], order='id desc', limit=1)
        self.assertRecordValues(invoice, [{
            'partner_id': self.partner_mx.id,
            'l10n_mx_edi_usage': "G03",
            'l10n_mx_edi_cfdi_to_public': False,
        }])

    def test_mx_pos_invoice_previous_order_default_usage(self):
        self.start_tour("/odoo", "l10n_mx_edi_pos.tour_invoice_previous_order_default_usage", login=self.env.user.login)
        invoice = self.env['account.move'].search([('move_type', '=', 'out_invoice')], order='id desc', limit=1)
        self.assertRecordValues(invoice, [{
            'partner_id': self.partner_mx.id,
            'l10n_mx_edi_usage': "I01",
            'l10n_mx_edi_cfdi_to_public': True,
        }])

    def test_qr_code_receipt_mx(self):
        """This test make sure that no user is created when a partner is set on the PoS order.
            It also makes sure that the invoice is correctly created.
        """
        self.authenticate(None, None)
        self.new_partner = self.env['res.partner'].create({
            'name': 'AAA Partner',
            'zip': '12345',
            'country_id': self.env.company.country_id.id,
        })
        self.product1 = self.env['product.product'].create({
            'name': 'Test Product 1',
            'is_storable': True,
            'list_price': 10.0,
            'taxes_id': False,
        })
        self.main_pos_config.open_ui()
        self.pos_order = self.env['pos.order'].create({
            'company_id': self.env.company.id,
            'session_id': self.main_pos_config.current_session_id.id,
            'partner_id': self.new_partner.id,
            'access_token': '1234567890',
            'lines': [(0, 0, {
                'name': "OL/0001",
                'product_id': self.product1.id,
                'price_unit': 10,
                'discount': 0.0,
                'qty': 1.0,
                'tax_ids': False,
                'price_subtotal': 10,
                'price_subtotal_incl': 10,
            })],
            'amount_tax': 10,
            'amount_total': 10,
            'amount_paid': 10.0,
            'amount_return': 10.0,
        })
        self.main_pos_config.current_session_id.close_session_from_ui()
        get_invoice_data = {
            'access_token': self.pos_order.access_token,
            'name': self.new_partner.name,
            'email': "test@test.com",
            'company_name': self.new_partner.company_name,
            'street': "Test street",
            'city': "Test City",
            'zipcode': self.new_partner.zip,
            'country_id': self.new_partner.country_id.id,
            'state_id': self.new_partner.state_id,
            'phone': "123456789",
            'vat': 'GODE561231GR8',
            'invoice_l10n_mx_edi_usage': 'D10',
            'partner_l10n_mx_edi_fiscal_regime': '624',
            'csrf_token': odoo.http.Request.csrf_token(self)
        }
        self.url_open(f'/pos/ticket/validate?access_token={self.pos_order.access_token}', data=get_invoice_data)
        self.assertEqual(self.env['res.partner'].sudo().search_count([('name', '=', 'AAA Partner')]), 1)
        self.assertTrue(self.pos_order.is_invoiced, "The pos order should have an invoice")
        self.assertEqual(self.pos_order.account_move.l10n_mx_edi_usage, 'D10', 'Invoice values not saved')
        self.assertEqual(self.new_partner.l10n_mx_edi_fiscal_regime, '624', 'Partner values not saved')

    def test_settle_account_mx(self):
        if self.env['ir.module.module']._get('pos_settle_due').state != 'installed':
            self.skipTest("pos_settle_due needs to be installed")

        self.partner_test_1.country_id = self.env.ref('base.mx').id
        self.partner_test_1.is_company = True

        # create customer account payment method
        self.customer_account_payment_method = self.env['pos.payment.method'].create({
            'name': 'Customer Account',
            'split_transactions': True,
        })
        # add customer account payment method to pos config
        self.main_pos_config.write({
            'payment_method_ids': [(4, self.customer_account_payment_method.id, 0)],
        })

        self.assertEqual(self.partner_test_1.total_due, 0)

        self.main_pos_config.with_user(self.pos_admin).open_ui()
        current_session = self.main_pos_config.current_session_id

        order = self.env['pos.order'].create({
            'company_id': self.company.id,
            'session_id': current_session.id,
            'partner_id': self.partner_test_1.id,
            'lines': [odoo.Command.create({
                'product_id': self.product.id,
                'price_unit': 10,
                'discount': 0,
                'qty': 1,
                'price_subtotal': 10,
                'price_subtotal_incl': 10,
            })],
            'amount_paid': 10.0,
            'amount_total': 10.0,
            'amount_tax': 0.0,
            'amount_return': 0.0,
            'to_invoice': True,
            'last_order_preparation_change': '{}'
        })

        self.make_payment(order, self.customer_account_payment_method, 10.0)

        self.assertEqual(self.partner_test_1.total_due, 10)
        current_session.action_pos_session_closing_control()

        self.main_pos_config.with_user(self.user).open_ui()
        self.start_tour("/pos/ui?config_id=%d" % self.main_pos_config.id, 'pos_settle_account_due', login="accountman")
        self.assertEqual(self.partner_test_1.total_due, 0)
