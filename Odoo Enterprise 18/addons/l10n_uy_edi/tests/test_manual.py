from unittest.mock import patch

from odoo import Command
from odoo.tests.common import tagged
from odoo.tools import misc
from lxml import etree
import datetime

from . import common


@tagged("-at_install", "post_install", "post_install_l10n", "manual")
class TestManual(common.TestUyEdi):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company_uy.l10n_uy_edi_ucfe_env = "demo"

    def test_10_post_invoice(self):
        """ Post EDI UY invoice
        * default invoice is e-ticket,
        * default taxes auto applied on lines is 22% vat tax
        * name after post (should have * ID name)
        """
        invoice = self._create_move()
        self.assertEqual(invoice.company_id, self.company_uy, "created with wrong company")
        self.assertEqual(invoice.journal_id.l10n_uy_edi_type, "electronic", "Invoice is not created on EDI journal")
        self.assertEqual(invoice.amount_tax, 22, "invoice taxes are not properly set")
        self.assertEqual(invoice.amount_total, 122.0, "invoice taxes has not been applied to the total")
        invoice.action_post()
        self.assertEqual(invoice.state, "posted", "invoice has not been validate in Odoo")
        self.assertEqual(invoice.name, "* %s" % invoice.id, "Not expected name")

    def test_20_e_ticket_xml(self):
        """ Create/post/send an e-ticket and check that the pre-generated XML is the same as the one expected """
        invoice = self._create_move()
        self.assertEqual(invoice.l10n_latam_document_type_id.code, "101", "Not e-ticket")
        invoice.action_post()
        self._send_and_print(invoice)
        self._check_cfe(invoice, "e-TK", "20_e_ticket")

    def test_30_e_invoice_xml(self):
        """ Create e-Invoice, and check that the pre-generated xml is the same as the one expected """
        invoice = self._create_move(
            partner_id=self.partner_local.id,
            l10n_latam_document_type_id=self.env.ref("l10n_uy.dc_e_inv").id
        )
        self.assertEqual(invoice.l10n_latam_document_type_id.code, "111", "Not an e-invoice")
        invoice.action_post()
        self._send_and_print(invoice)
        self._check_cfe(invoice, "e-FC", "30_e_invoice")

    def test_40_e_expo_invoice(self):
        """ Create an Expo e-invoice, and check that the pre-generated xml is the same as the one expected """
        invoice = self._create_move(
            l10n_latam_document_type_id=self.env.ref("l10n_uy.dc_e_inv_exp").id,
            partner_id=self.foreign_partner.id,
            invoice_incoterm_id=self.env.ref("account.incoterm_FOB").id,
            l10n_uy_edi_cfe_sale_mode="1",
            l10n_uy_edi_cfe_transport_route="1",
            invoice_line_ids=[Command.create({"product_id": self.product_vat_22.id, "price_unit": 100.0})],
        )
        self.assertEqual(invoice.l10n_latam_document_type_id.code, "121", "Not Expo e-invoice")
        invoice.action_post()

        # IndFact lo cambié de 3 a 10
        self._send_and_print(invoice)
        self._check_cfe(invoice, "e-FCE", "40_e_expo_invoice")

    def test_50_e_ticket_multi_tax_xml(self):
        """ Create/post/send an e-ticket with multi tax and check that the pre-generated XML is the same as the one expected """
        invoice = self._create_move(
            invoice_line_ids=[
                Command.create({
                    "product_id": self.service_vat_22.id,
                    "price_unit": 100.0,
                }),
                Command.create({
                    "product_id": self.service_vat_10.id,
                    "quantity": 2,
                    "price_unit": 150,
                }),
            ]
        )
        self.assertEqual(invoice.l10n_latam_document_type_id.code, "101", "Not e-ticket")
        invoice.action_post()
        self._send_and_print(invoice)
        self._check_cfe(invoice, "e-TK", "50_e_ticket_multi_tax")

    def test_60_another_currency(self):
        """ create an invoice with different currency, also test that Incoterm/Transport is properly set for services """
        invoice = self._create_move(
            l10n_latam_document_type_id=self.env.ref("l10n_uy.dc_e_inv_exp").id,
            partner_id=self.foreign_partner.id,
            l10n_uy_edi_cfe_sale_mode="1",
            l10n_uy_edi_cfe_transport_route="1",
            currency_id=self.env.ref("base.USD").id,
        )
        self.assertEqual(invoice.l10n_latam_document_type_id.code, "121", "Not Expo e-invoice")
        invoice.action_post()
        self._send_and_print(invoice)
        self._check_cfe(invoice, "e-FCE", "60_e_invoice_another_currency")

    def test_70_tax_included(self):
        tax_22_included = self.tax_22.copy({"price_include_override": "tax_included", "name": "22% VAT (included)"})
        tax_10_included = self.tax_10.copy({"price_include_override": "tax_included", "name": "10% VAT (included)"})
        tax_0_included = self.tax_0.copy({"price_include_override": "tax_included", "name": "0% VAT (included)"})
        invoice = self._create_move(
            partner_id=self.partner_local.id,
            l10n_latam_document_type_id=self.env.ref("l10n_uy.dc_e_inv").id,
            invoice_line_ids=[
                Command.create({
                    "product_id": self.service_vat_22.id,
                    "price_unit": 1000,
                    "tax_ids": tax_22_included,
                }),
                Command.create({
                    "product_id": self.service_vat_22.id,
                    "quantity": 2,
                    "price_unit": 150,
                    "tax_ids": tax_10_included,
                }),
                Command.create({
                    "product_id": self.service_vat_22.id,
                    "quantity": 2,
                    "price_unit": 150,
                    "tax_ids": tax_0_included,
                }),
            ],
        )

        invoice.action_post()
        self.assertEqual(invoice.l10n_latam_document_type_id.code, "111", "Not e-invoice")
        self._send_and_print(invoice)
        self._check_cfe(invoice, "e-FC", "70_e_invoice_tax_included")

    def test_80_e_ticket_credit_note(self):
        """ Create a credit note, validate it, check that we do not get any error. """
        invoice = self._create_move()
        invoice.action_post()
        self._send_and_print(invoice)
        self._check_cfe(invoice, "e-TK", "20_e_ticket")

        refund = self._create_credit_note(invoice)
        refund.action_post()
        self.assertEqual(refund.l10n_latam_document_type_id.code, "102", "Not Credit not document type.")
        self._send_and_print(refund)
        self._check_cfe(refund, "e-NCTK", "80_e_ticket_credit_note")

    def test_90_e_ticket_debit_note(self):
        """ Create a credit note, validate it, check that we do not get any error. """
        invoice = self._create_move()
        invoice.action_post()
        self._send_and_print(invoice)
        self._check_cfe(invoice, "e-TK", "20_e_ticket")
        refund = self._create_debit_note(invoice)
        refund.action_post()
        self.assertEqual(refund.l10n_latam_document_type_id.code, "103", "Not Debit not document type.")
        self._send_and_print(refund)
        self._check_cfe(refund, "e-NDTK", "90_e_ticket_debit_note")

    def test_100_e_ticket_with_disclosures(self):
        """ Create/post/send an e-ticket with disclosures and check that the pre-generated XML is the same as the one
        expected """
        item_legend = self.env['l10n_uy_edi.addenda'].create({
            "type": 'item',
            "is_legend": True,
            "name": 'Leyenda Product/Service Detail',
            "content": 'Leyenda Product/Service Detail',
            "company_id": self.env.company.id
        })
        l10n_uy_edi_addenda_ids = self.env['l10n_uy_edi.addenda'].create({
            "type": 'cfe_doc',
            "is_legend": True,
            "name": 'CFE Legend',
            "content": 'CFE Legend',
            "company_id": self.env.company.id
        })
        invoice = self._create_move(
            l10n_uy_edi_addenda_ids=l10n_uy_edi_addenda_ids.ids,
            invoice_line_ids=[Command.create({
                "product_id": self.service_vat_22.id,
                "price_unit": 100.0,
                "l10n_uy_edi_addenda_ids": item_legend.ids,
            })],
        )
        self.assertEqual(invoice.l10n_latam_document_type_id.code, "101", "Not e-ticket")
        invoice.action_post()
        self._send_and_print(invoice)
        self._check_cfe(invoice, "e-TK", "100_e_ticket_disclosures")

    def test_120_e_ticket_final_consumer(self):
        """ Create/post/send an e-ticket and check that the pre-generated XML is the same as the one expected """
        invoice = self._create_move(partner_id=self.env.ref("l10n_uy.partner_cfu").id)
        self.assertEqual(invoice.l10n_latam_document_type_id.code, "101", "Not e-ticket")
        invoice.action_post()
        self._send_and_print(invoice)
        self._check_cfe(invoice, "e-TK", "120_e_ticket_final_consumer")

    def test_default_doc_type_by_id(self):
        dc_e_inv = self.env.ref('l10n_uy.dc_e_inv')
        move = self._create_move(partner_id=self.env.ref("l10n_uy.partner_cfu").id)
        self.assertEqual(move.l10n_latam_document_type_id, self.env.ref('l10n_uy.dc_e_ticket'), "The document type is not being set correctly.")
        move.partner_id = self.env.ref('l10n_uy.partner_dgi').id
        self.assertEqual(move.l10n_latam_document_type_id, dc_e_inv, "The expected document should be e-invoice")

    def test_130_entrega_gratuita(self):
        """ Create e-Invoice with line with discount 100% and it should work """
        invoice = self._create_move(
            partner_id=self.partner_local.id,
            l10n_latam_document_type_id=self.env.ref("l10n_uy.dc_e_inv").id,
            invoice_line_ids=[Command.create({
                "product_id": self.service_vat_22.id,
                "price_unit": 100.0,
                "discount": 100.0,
            })],
        )
        self.assertEqual(invoice.l10n_latam_document_type_id.code, "111", "Not an e-invoice")
        invoice.action_post()
        self._send_and_print(invoice)
        self._check_cfe(invoice, "e-FC", "130_entrega_gratuita")

    def test_140_global_discount(self):
        """ Create e-Invoice with line with discount 100% and it should work """
        discount = self.env["product.product"].create({
            "name": "Discount Product",
            "list_price": 10,
            "standard_price": 10,
            "type": "service",
        })
        discount_list = [
            {"product_id": discount.id, "price_unit": -5.0, "tax_ids": self.tax_22},  # w/product
            {"product_id": discount.id, "name": "", "price_unit": -2.0, "tax_ids": self.tax_22},  # w/product & wo/label
            {"name": "Discount only Label", "price_unit": -20.0, "tax_ids": self.tax_0},  # wo product but w/label
            {"price_unit": -10.0, "tax_ids": self.tax_10},  # wo product or label
        ]
        invoice = self._create_move(
            ref="test_140_global_discount",
            partner_id=self.partner_local.id,
            l10n_latam_document_type_id=self.env.ref("l10n_uy.dc_e_inv").id,
            invoice_line_ids=[
                Command.create({"product_id": self.service_vat_22.id, "price_unit": 100.0, "tax_ids": self.tax_22}),
                Command.create({"product_id": self.service_vat_22.id, "price_unit": 100.0, "tax_ids": self.tax_10}),
                Command.create({"product_id": self.service_vat_22.id, "price_unit": 100.0, "tax_ids": self.tax_0}),
                ] + [Command.create(item) for item in discount_list]  # Discounts
            )
        self.assertEqual(invoice.l10n_latam_document_type_id.code, "111", "Not an e-invoice")
        invoice.action_post()
        self._send_and_print(invoice)
        self._check_cfe(invoice, "e-FC", "140_global_discount")

    def test_150_global_donwpayment(self):
        """ Create e-Invoice that is a down payment
        invoice_ind = 6 if self._is_downpayment() else invoice_ind
        """
        down_payment = self.env["product.product"].create({
            "name": "Down Payment",
            "list_price": 10,
            "standard_price": 10,
            "type": "service",
        })
        invoice = self._create_move(
            ref="test_150_global_donwpayment",
            partner_id=self.partner_local.id,
            l10n_latam_document_type_id=self.env.ref("l10n_uy.dc_e_inv").id,
            invoice_line_ids=[
                Command.create({"product_id": down_payment.id, "price_unit": 2000.0, "tax_ids": []}),
            ])
        self.assertEqual(invoice.l10n_latam_document_type_id.code, "111", "Not an e-invoice")
        invoice.action_post()

        with patch("odoo.addons.account.models.account_move.AccountMove._is_downpayment", return_value=True), \
             patch("odoo.addons.sale.models.account_move.AccountMove._is_downpayment", return_value=True):
            self._send_and_print(invoice)
        self._check_cfe(invoice, "e-FC", "150_global_donwpayment")

    def test_160_deduct_global_donwpayment(self):
        """ Create e-Invoice that is a down payment
        invoice_ind = 7 if line.quantity < 0 else invoice_ind
        """
        down_payment = self.env["product.product"].create({
            "name": "Down Payment",
            "list_price": 10,
            "standard_price": 10,
            "type": "service",
        })
        invoice = self._create_move(
            ref="test_160_deduct_global_donwpayment",
            partner_id=self.partner_local.id,
            l10n_latam_document_type_id=self.env.ref("l10n_uy.dc_e_inv").id,
            invoice_line_ids=[
                Command.create({"product_id": self.service_vat_22.id, "price_unit": 10000.0, "tax_ids": self.tax_22}),
                Command.create({"product_id": down_payment.id, "quantity": -1.0, "price_unit": 2000.0, "tax_ids": False}),
            ])
        self.assertEqual(invoice.l10n_latam_document_type_id.code, "111", "Not an e-invoice")
        invoice.action_post()

        url = "odoo.addons.%s.models.account_move_line.AccountMoveLine._get_downpayment_lines"
        result_value = invoice.invoice_line_ids.filtered(lambda x: x.quantity < 0.0)
        with patch(url % "account", return_value=result_value), patch(url % "sale", return_value=result_value):
            self._send_and_print(invoice)
        self._check_cfe(invoice, "e-FC", "160_deduct_global_donwpayment")

    def test_170_uploaded_vendor_bill_with_global_fixed_discount(self):
        """ Simulate upload xml document with global discount fixed line on vendor bill journal and test if it was
        created correctly. """
        new_bill = self._mock_upload_document_on_journal(
            journal=self.company_data['default_journal_purchase'],
            filename='vendor_bill_with_global_fixed_discount',
        )
        self.assertEqual(new_bill.name, "e-FC A4002353")
        self.assertEqual(new_bill.invoice_date.strftime('%Y-%m-%d'), "2024-06-06")
        self.assertEqual(new_bill.invoice_date_due.strftime('%Y-%m-%d'), "2024-06-07")
        self.assertEqual(new_bill.invoice_partner_display_name, "FIERRO VIGNOLI S.A.")
        global_discount_line = new_bill.invoice_line_ids\
            .filtered(lambda line: line.name == 'descuento por forma de pago')
        self.assertEqual(global_discount_line.price_total, -431.16)

    def test_180_uploaded_vendor_bill_with_line_fixed_discount(self):
        """ Simulate upload xml document with discount fixed line on vendor bill journal and test if it was created
        correctly. """
        new_bill = self._mock_upload_document_on_journal(
            journal=self.company_data['default_journal_purchase'],
            filename='vendor_bill_with_line_fixed_discount',
        )
        self.assertEqual(new_bill.name, "e-FC F6557758")
        self.assertEqual(new_bill.invoice_date.strftime('%Y-%m-%d'), "2024-05-31")
        self.assertEqual(new_bill.invoice_date_due.strftime('%Y-%m-%d'), "2024-06-25")
        self.assertEqual(new_bill.invoice_partner_display_name, "Administración Nacional de Telecomunicaciones")
