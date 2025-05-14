from odoo import models, fields, api
from odoo.exceptions import ValidationError
import requests, json, re

class WhatsappSettings(models.Model):
    _name = 'whatsapp.settings'
    _rec_name = 'name'
    _description = 'Whatsapp Settings'

    name = fields.Char(string='Name', required=True)
    access_token = fields.Char(string='Access Token', required=True)
    app_object_id = fields.Char(string='App Object ID', required=True)
    phone_number_id = fields.Char(string='Phone Number ID', required=True)
    app_secret = fields.Char(string='App Secret', required=True)
    business_account_id = fields.Char(string='Business Account ID', required=True)
    phone_number = fields.Char(string='Phone Number', required=True)

class WhatsappTemplate(models.Model):
    _name = 'whatsapp.template'
    _description = 'Whatsapp Template'

    name = fields.Char(string='Template Name', required=True)
    stages = fields.Selection([
        ('draft', 'Draft'),('pending','Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], string='Status', default='draft')
    template_name = fields.Char(string='Whatsapp Template Name', required=True, compute='_compute_template_name')
    api_id: fields.Many2one = fields.Many2one('whatsapp.settings', string='API', required=True)
    body = fields.Text(string='Template Body', required=True)
    header = fields.Text(string='Header', required=True)
    footer = fields.Text(string='Footer', required=True)

    def sync_template(self):
        try:
            self.refresh_access_token()
        except ValidationError:
            raise ValidationError("Access token expired. Please update manually.")

        url = f"https://graph.facebook.com/v22.0/{self.api_id.business_account_id}/message_templates"

        headers = {
            "Authorization": f"Bearer {self.api_id.access_token}",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            templates = response.json().get("data", [])

            for template in templates:
                if template.get("name") == self.template_name:
                    status = template.get("status")

                    odoo_status = {
                        "APPROVED": "approved",
                        "PENDING": "pending",
                        "REJECTED": "rejected"
                    }.get(status, "pending")

                    self.write({"stages": odoo_status})
                    return True
        else:
            raise ValidationError(f"Failed to sync template status: {response.text}")

    def approval_request(self):
        url = f"https://graph.facebook.com/v22.0/{self.api_id.business_account_id}/message_templates"

        headers = {
            "Authorization": f"Bearer {self.api_id.access_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "name": f"{self.template_name}",
            "category": "MARKETING",
            "language": "en",
            "components": [
                {
                    "type": "HEADER",
                    "format": "TEXT",
                    "text": f"{self.header}"
                },
                {
                    "type": "BODY",
                    "text": f"{self.body}"
                },
                {
                    "type": "FOOTER",
                    "text": f"{self.footer}"
                },
            ]
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response_data = response.json()

        if response.status_code == 200:
            response_data = response.json().get("data", [])
            for template in response_data:
                if template.get("name") == self.template_name:
                    status = template.get("status")

                    odoo_status = {
                        "APPROVED": "approved",
                        "PENDING": "pending",
                        "REJECTED": "rejected"
                    }.get(status, "pending")

                    self.write({"stages": odoo_status})
        else:
            raise ValidationError(f"API Error: {json.dumps(response_data, indent=2)}")

    def refresh_access_token(self):
        url = "https://graph.facebook.com/v18.0/oauth/access_token"

        params = {
            "grant_type": "fb_exchange_token",
            "client_id": self.api_id.app_object_id,
            "client_secret": self.api_id.app_secret,
            "fb_exchange_token": self.api_id.access_token
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            new_token = response.json().get("access_token")
            if new_token:
                self.api_id.write({"access_token": new_token})
                return True
        else:
            raise ValidationError(f"Failed to refresh token: {response.text}")

    def retry_approval(self):
        self.stages = 'draft'

    @api.depends('name','template_name')
    def _compute_template_name(self):
        for record in self:
            if record.name:
                record.template_name = record.name.replace(" ", "_").lower()
            else:
                record.template_name = ''

class Whatsapp(models.Model):
    _name = 'whatsapp.whatsapp'
    _rec_name = 'name'
    _description = 'Send Whatsapp Message'

    name = fields.Char(string='Reference Name', required=True)

    api: fields.Many2one = fields.Many2one('whatsapp.settings', string='API', required=True)
    api_template: fields.Many2one = fields.Many2one('whatsapp.template', string='Message Template', required=True)

    recipient_numbers: fields.Many2many = fields.Many2many('res.partner', string="Recipients")
    message = fields.Text(string='Message')

    def send_message(self):

        url = f"https://graph.facebook.com/v22.0/{self.api.phone_number_id}/messages"

        headers = {
            "Authorization": f"Bearer {self.api.access_token}",
            "Content-Type": "application/json"
        }

        responses = []

        for recipient in self.recipient_numbers:
            if recipient.phone:
                cleaned_number = re.sub(r'\D', '', recipient.phone)
                payload = {
                    "messaging_product": "whatsapp",
                    "recipient_type": "individual",
                    "to": cleaned_number,
                    "type": "template",
                    "template": {
                        "name": self.api_template.template_name,
                        "language": {"code": "en"}
                    }
                }

                response = requests.post(url, json=payload, headers=headers)
                try:
                    data = response.json()
                except ValueError:
                    data = {"error": "Invalid JSON response", "raw": response.text}
                print(f"Response for {cleaned_number}: {data}")
                if response.status_code != 200:
                    raise ValidationError(f"Failed to send message to {recipient.phone}: {response.text}")
                responses.append(data)

        return responses
