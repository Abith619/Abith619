# -*- coding: utf-8 -*-
import logging
from odoo import api,fields, models
import requests

_logger = logging.getLogger(__name__)

class PbiConnect(models.Model):
    _name = 'pbi.connect'
    _rec_name = 'username'
    _description = "power bi connection"

    app_id = fields.Char(string="APP ID")
    tenant_id = fields.Char(string="tenant id")
    username = fields.Char(string="Username")
    password = fields.Char(string="Client Secret")

    is_connect = fields.Boolean(string="Status")
    access_id = fields.Char()
    workspace_ids : fields.One2many = fields.One2many('pbi.workspace', 'connection_id', string='workspace', copy=True, readonly=True)

    @api.model
    def connect(self):
        if not self.id:
            records = self.search([('is_connect', '=', True)], limit=1)
            if records:
                self = records
            else:
                _logger.error("No connected config")
                return

        token_url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"

        data = {
            'grant_type': 'client_credentials',
            'client_id': self.app_id,
            'client_secret': self.password,
            'scope': 'https://analysis.windows.net/powerbi/api/.default'
        }

        try:
            response = requests.post(token_url, data=data)
            result = response.json()

            if 'access_token' not in result:
                _logger.error("Error acquiring token: %s", result)
                self.is_connect = False
                return

            # Save Token
            self.access_id = result['access_token']
            self.is_connect = True
            _logger.info("Power BI Connected Successfully")

        except Exception as e:
            self.is_connect = False
            _logger.exception("Power BI connection failed: %s", e)

    def connect_manual(self):
    # If record not selected, pick the connected one
        if not self.id:
            record = self.search([('is_connect', '=', True)], limit=1)
            if record:
                self = record
            else:
                _logger.error("do not have connected config")
                return

        # ---------------------------------------------------------
        # POWER BI AUTHENTICATION - CLIENT CREDENTIALS FLOW
        # ---------------------------------------------------------

        token_url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"

        data = {
            "grant_type": "client_credentials",
            "client_id": self.app_id,          # Application (client) ID
            "client_secret": self.password,  # Client Secret
            "scope": "https://analysis.windows.net/powerbi/api/.default",
        }

        try:
            response = requests.post(token_url, data=data)
            result = response.json()

            # Authentication failed
            if "access_token" not in result:
                _logger.error("Power BI Login Failed: %s", result)
                self.is_connect = False
                return

            # Authentication success
            self.access_id = result["access_token"]
            self.is_connect = True

            _logger.info("Power BI connected successfully!")
            return True

        except Exception as e:
            self.is_connect = False
            _logger.exception("Power BI connection error: %s", e)


    def get_workspaces(self):
    # ------------------------------
    # 1. Get active connection record
    # ------------------------------
        if not self.id:
            rec = self.search([('is_connect', '=', True)], limit=1)
            if rec:
                self = rec
            else:
                _logger.error("do not have connected config")
                return

        # ------------------------------
        # 2. Ensure token exists
        # ------------------------------
        if not self.access_id:
            _logger.error("Missing access token. Please connect first.")
            return

        # ------------------------------
        # 3. API endpoint & headers
        # ------------------------------
        endpoint = "https://api.powerbi.com/v1.0/myorg/groups"
        headers = {
            "Authorization": f"Bearer {self.access_id}",
            "Content-Type": "application/json",
        }

        ws = self.env["pbi.workspace"]

        # ------------------------------
        # 4. Send request
        # ------------------------------
        try:
            resp = requests.get(endpoint, headers=headers)

            # Expired token → refresh needed
            if resp.status_code == 401:
                _logger.warning("Access token expired. Please reconnect Power BI.")
                self.is_connect = False
                return

            if resp.status_code != 200:
                _logger.error("Power BI workspace fetch failed: %s", resp.text)
                return

            data = resp.json()
            values = data.get("value", [])
            _logger.warning("Workspaces returned: %s", values)
            # ------------------------------
            # 5. Save results into Odoo DB
            # ------------------------------
            for item in values:
                workspace_id = item.get("id")
                name = item.get("name")

                if not workspace_id:
                    continue

                # Check for duplicates using exists()
                if not ws.search([("workspace_id", "=", workspace_id)], limit=1):
                    ws.create({
                        "name": name,
                        "workspace_id": workspace_id,
                        "connection_id": self.id,
                    })

        except Exception as e:
            _logger.exception("Workspace sync failed: %s", e)
