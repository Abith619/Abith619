# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json

from odoo.tests.common import TransactionCase, new_test_user


class SaleOrderSpreadsheet(TransactionCase):

    def test_create_spreadsheet(self):
        spreadsheet = self.env["sale.order.spreadsheet"].create({"name": "spreadsheet"})
        data = spreadsheet.join_spreadsheet_session()["data"]
        self.assertTrue(data["lists"])
        self.assertTrue(data["globalFilters"])
        revision = spreadsheet.spreadsheet_revision_ids
        self.assertEqual(len(revision), 1)
        commands = json.loads(revision.commands)["commands"]
        self.assertEqual(commands[0]["type"], "RE_INSERT_ODOO_LIST")
        self.assertEqual(commands[1]["type"], "CREATE_TABLE")

    def test_sale_order_action_open(self):
        spreadsheet = self.env["sale.order.spreadsheet"].create({"name": "spreadsheet"})
        quotation_template = self.env["sale.order.template"].create({
            "name": "Test template",
            "spreadsheet_template_id": spreadsheet.id
        })
        sale_order = self.env["sale.order"].create({
            "partner_id": self.env.user.partner_id.id,
            "sale_order_template_id": quotation_template.id
        })
        self.assertFalse(sale_order.spreadsheet_ids)
        action = sale_order.action_open_sale_order_spreadsheet()
        self.assertEqual(action["tag"], "action_sale_order_spreadsheet")
        self.assertTrue(sale_order.spreadsheet_ids)
        self.assertEqual(sale_order.spreadsheet_ids.id, action["params"]["spreadsheet_id"])

    def test_sale_order_action_open_twice(self):
        spreadsheet = self.env["sale.order.spreadsheet"].create({"name": "spreadsheet"})
        quotation_template = self.env["sale.order.template"].create({
            "name": "Test template",
            "spreadsheet_template_id": spreadsheet.id
        })
        sale_order = self.env["sale.order"].create({
            "partner_id": self.env.user.partner_id.id,
            "sale_order_template_id": quotation_template.id
        })
        sale_order.action_open_sale_order_spreadsheet()
        spreadsheets = sale_order.spreadsheet_ids
        sale_order.action_open_sale_order_spreadsheet()
        self.assertEqual(sale_order.spreadsheet_ids, spreadsheets, "it should be the same spreadsheets")
        
    def test_sale_order_spreadsheet_deleted_with_related_order(self):
        spreadsheet = self.env["sale.order.spreadsheet"].create({"name": "spreadsheet"})
        quotation_template = self.env["sale.order.template"].create({
            "name": "Test template",
            "spreadsheet_template_id": spreadsheet.id
        })
        sale_order = self.env["sale.order"].create({
            "partner_id": self.env.user.partner_id.id,
            "sale_order_template_id": quotation_template.id
        })
        sale_order.action_open_sale_order_spreadsheet()
        so_spreadsheet = sale_order.spreadsheet_ids
        sale_order.unlink()
        self.assertFalse(so_spreadsheet.exists(), "spreadsheet should be deleted with the related order")
        self.assertTrue(spreadsheet.exists(), "Original spreadsheet should be unaltered")

    def test_access(self):
        salesman = new_test_user(self.env, login="Alice", groups="sales_team.group_sale_salesman")
        other_salesman = new_test_user(self.env, login="Bob", groups="sales_team.group_sale_salesman")
        template_spreadsheet = self.env["sale.order.spreadsheet"].create({"name": "spreadsheet"})
        quotation_template = self.env["sale.order.template"].create({
            "name": "Test template",
            "spreadsheet_template_id": template_spreadsheet.id
        })
        sale_order = self.env["sale.order"].with_user(salesman).create({
            "partner_id": self.env.user.partner_id.id,
            "sale_order_template_id": quotation_template.id,
            "user_id": salesman.id
        })
        sale_order.action_open_sale_order_spreadsheet()
        spreadsheet = sale_order.spreadsheet_id

        # user access for his own sale order
        self.assertTrue(sale_order.has_access("read"))
        self.assertTrue(sale_order.has_access("write"))
        self.assertFalse(sale_order.has_access("unlink"))
        self.assertTrue(spreadsheet.has_access("read"))
        self.assertTrue(spreadsheet.has_access("write"))
        self.assertFalse(spreadsheet.has_access("unlink"))

        # other users don't have access by default
        self.assertFalse(sale_order.with_user(other_salesman).has_access("read"))
        self.assertFalse(sale_order.with_user(other_salesman).has_access("write"))
        self.assertFalse(sale_order.with_user(other_salesman).has_access("unlink"))
        self.assertFalse(spreadsheet.with_user(other_salesman).has_access("read"))
        self.assertFalse(spreadsheet.with_user(other_salesman).has_access("write"))
        self.assertFalse(spreadsheet.with_user(other_salesman).has_access("unlink"))

        # add access to all orders
        other_salesman.groups_id |= self.env.ref("sales_team.group_sale_salesman_all_leads")
        self.assertTrue(sale_order.with_user(other_salesman).has_access("read"))
        self.assertTrue(sale_order.with_user(other_salesman).has_access("write"))
        self.assertFalse(sale_order.with_user(other_salesman).has_access("unlink"))
        self.assertTrue(spreadsheet.with_user(other_salesman).has_access("read"))
        self.assertTrue(spreadsheet.with_user(other_salesman).has_access("write"))
        self.assertFalse(spreadsheet.with_user(other_salesman).has_access("unlink"))
