from odoo import http
from odoo.http import request, Controller, route, Response
import requests, uuid

class ExternalAPIController(Controller):

    def get_paypal_access_token(self, client_id, client_secret):
        url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
        headers = {
            "Accept": "application/json",
            "Accept-Language": "en_US",
        }
        data = {"grant_type": "client_credentials"}
        auth = (client_id, client_secret)

        response = requests.post(url, headers=headers, data=data, auth=auth)
        response.raise_for_status()
        return response.json()['access_token']

    def create_paypal_order(self, amount, lead_id, client_id, client_secret):
        """
        Create a PayPal order and return the approval URL.
        Uses a unique temp_token for internal tracking to avoid PayPal token conflicts.
        """
        access_token = self.get_paypal_access_token(client_id, client_secret)
        url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"

        web_base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        temp_token = uuid.uuid4().hex

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }

        data = {
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "amount": {
                        "currency_code": "USD",
                        "value": str(amount)
                    },
                    "custom_id": str(lead_id),
                    "description": f"Payment for {self.env['crm.lead'].browse(lead_id).name or 'Course'}"
                }
            ],
            "application_context": {
                "return_url": f"{web_base_url}/paypal/success?lead_id={lead_id}&temp_token={temp_token}",
                "cancel_url": f"{web_base_url}/paypal/cancel?lead_id={lead_id}"
            }
        }

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()

        paypal_order_id = result.get('id')
        approval_url = next(link['href'] for link in result['links'] if link['rel'] == 'approve')

        return approval_url

