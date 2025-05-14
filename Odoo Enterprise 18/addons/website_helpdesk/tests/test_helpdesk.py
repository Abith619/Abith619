import re

from odoo.tests.common import HttpCase, TransactionCase


class TestHelpdesk(HttpCase):
    def setUp(self):
        super().setUp()
        self.team_without_web_form = self.env['helpdesk.team'].create({
            'name': 'Team without Web Form',
            'is_published': True,
        })

    def test_create_ticket_portal(self):
        # Only one team has enabled the website form then Help website menu should open the Ticket Submit page
        # If that team has enabled Knowledge then it should open Knowledge page
        team = self.env['helpdesk.team'].search([('use_website_helpdesk_form', '=', True)], limit=1)
        self.env['helpdesk.team'].search([('id', '!=', team.id)]).use_website_helpdesk_form = False
        response = self.url_open('/helpdesk')
        self.assertEqual(response.status_code, 200)
        expected_string = "How can we help you?" if team.use_website_helpdesk_knowledge else "Submit a Ticket"
        search_result = re.search(expected_string.encode(), response.content).group().decode()
        self.assertEqual(search_result, expected_string)

        # multiple teams have enabled the website form then Help website menu should refere to the Team selection page
        self.team_without_web_form.use_website_helpdesk_form = True
        other_response = self.url_open('/helpdesk')
        self.assertEqual(response.status_code, 200)
        expected_string = "Select your Team for help"
        search_result = re.search(expected_string.encode(), other_response.content).group().decode()
        self.assertEqual(search_result, expected_string)


class TestHelpdeskMenu(TransactionCase):
    def test_menu_item_visibility(self):
        website = self.env['website'].create({
            'name': 'test website'
        })
        public_user = self.env.ref('base.public_user')
        non_helpdesk_menu = self.env['website.menu'].create({
            'name': 'Menu with helpdesk in URL',
            'url': '/helpdesk-123',
            'website_id': website.id,
        })
        team = self.env['helpdesk.team'].create({
            'name': 'Test team',
            'use_website_helpdesk_form': True,
            'website_id': website.id,
        })

        non_helpdesk_menu.invalidate_recordset(["is_visible"])
        self.assertTrue(non_helpdesk_menu.with_user(public_user).is_visible, "Item with helpdesk in URL should stay visible.")
        self.assertTrue(team.website_menu_id.is_visible)
        team.use_website_helpdesk_form = False
        self.assertFalse(team.website_menu_id.is_visible)
