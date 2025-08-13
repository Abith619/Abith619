# Part of Odoo. See LICENSE file for full copyright and licensing details.

import hashlib
import hmac
import json
import logging

from werkzeug.exceptions import Forbidden

from http import HTTPStatus
from odoo import http, _
from odoo.http import request
from odoo.tools import consteq

_logger = logging.getLogger(__name__)

class Webhook(http.Controller):

    @http.route('/whatsapp/webhook/', type='json', auth='public', methods=['POST'], csrf=False, cors="*")
    def webhookpost(self):
        try:
            data = json.loads(request.httprequest.data)
            _logger.info("Webhook data received: %s", json.dumps(data, indent=2))
            for entry in data.get('entry', []):
                account_id = entry['id']
                for change in entry.get('changes', []):
                    if change.get('field') == 'messages':
                        value = change['value']
                        phone_number_id = value.get('metadata', {}).get('phone_number_id', {})
                        if not phone_number_id:
                            phone_number_id = value.get('whatsapp_business_api_data', {}).get('phone_number_id', {})
                        if phone_number_id:
                            wa_account_id = request.env['whatsapp.account'].sudo().search([
                                ('phone_uid', '=', phone_number_id), ('account_uid', '=', account_id)])
                            if wa_account_id:
                                wa_account_id._process_messages(value)
                        request.env['whatsapp.message']._process_statuses(value)
                        contacts = value.get('contacts', [])
                        messages = value.get('messages', [])

                        for contact, message in zip(contacts, messages):
                            # wa_id = contact.get('wa_id')
                            # name = contact.get('profile', {}).get('name')
                            msg_body = message.get('text', {}).get('body')
                            msg_from = message.get('from')
                            # msg_type = message.get('type')
                            # msg_id = message.get('id')
                            # timestamp = message.get('timestamp')

                            request.env['whatsapp.incoming.message'].sudo().create({
                                # 'wa_account_id': wa_id,
                                # 'name': name,
                                'content': msg_body,
                                # 'message_id': msg_id,
                                # 'timestamp': timestamp,
                                # 'msg_type': msg_type,
                                'sender': msg_from,
                            })

            return {"status": "success"}

        except Exception as e:
            _logger.error("Error processing WhatsApp webhook: %s", str(e), exc_info=True)
            return {"status": "error", "message": str(e)}

    @http.route('/whatsapp/webhook', methods=['GET'], type="http", auth="public", csrf=False)
    def webhookget(self, **kwargs):
        """
            This controller is used to verify the webhook.
            if challenge is matched then it will make response with challenge.
            once it is verified the webhook will be activated.
        """
        token = kwargs.get('hub.verify_token')
        mode = kwargs.get('hub.mode')
        challenge = kwargs.get('hub.challenge')
        if not (token and mode and challenge):
            return Forbidden()
        wa_account = request.env['whatsapp.account'].sudo().search([('webhook_verify_token', '=', token)])
        if mode == 'subscribe' and wa_account:
            response = request.make_response(challenge)
            response.status_code = HTTPStatus.OK
            return response
        response = request.make_response({})
        response.status_code = HTTPStatus.FORBIDDEN
        return response

    def _check_signature(self, business_account):
        """Whatsapp will sign all requests it makes to our endpoint."""
        signature = request.httprequest.headers.get('X-Hub-Signature-256')
        if not signature or not signature.startswith('sha256=') or len(signature) != 71:
            # Signature must be valid SHA-256 (sha256=<64 hex digits>)
            _logger.warning('Invalid signature header %r', signature)
            return False
        if not business_account.app_secret:
            _logger.warning('App-secret is missing, can not check signature')
            return False

        expected = hmac.new(
            business_account.app_secret.encode(),
            msg=request.httprequest.data,
            digestmod=hashlib.sha256,
        ).hexdigest()

        return consteq(signature[7:], expected)
