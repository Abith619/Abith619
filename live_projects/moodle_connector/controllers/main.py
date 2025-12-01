from odoo import http, fields
from odoo.http import request
import requests
import logging

_logger = logging.getLogger(__name__)

class PayPalCustomController(http.Controller):

    @http.route('/paypal/create/<int:lead_id>', type='http', auth='none', website=True, csrf=False)
    def create_paypal_order_link(self, lead_id, **kwargs):
        lead = request.env['crm.lead'].sudo().browse(lead_id)

        if not lead.exists():
            return request.redirect('/shop')

        paypal_provider = request.env['payment.provider'].sudo().search([('code', '=', 'paypal')], limit=1)
        client_id = paypal_provider.paypal_client_id
        client_secret = paypal_provider.paypal_client_secret

        # Get access token
        access_token = self._get_paypal_access_token(client_id, client_secret)
        url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"

        # Create lightweight public-safe session token
        payment_token = request.env['payment.token'].sudo().create({
            'provider_id': paypal_provider.id,
            'partner_id': lead.partner_id.id if lead.partner_id else None,
            'acquirer_ref': f"temp_{fields.Datetime.now()}",
        })

        web_base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')

        TAX_PERCENT = 15.0

        base_amount = lead.expected_revenue or 0.0
        tax_amount = base_amount * (TAX_PERCENT / 100)
        amount = round(base_amount + tax_amount, 2)

        data = {
            "intent": "CAPTURE",
            "purchase_units": [{
                "amount": {
                    "currency_code": "USD",
                    "value": str(amount),
                    "breakdown": {
                        "item_total": {"currency_code": "USD", "value": str(base_amount)},
                        "tax_total": {"currency_code": "USD", "value": str(tax_amount)},
                    },
                },
                "custom_id": str(lead.id),
                "description": f"Payment for {lead.name}",
            }],
            "application_context": {
                "return_url": f"{web_base_url}/paypal/success?lead_id={lead.id}&token_id={payment_token.id}",
                "cancel_url": f"{web_base_url}/paypal/cancel?lead_id={lead.id}",
            }
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()

        approval_url = f"{result['links'][1]['href']}&lead_id={lead.id}&temp_token={temp_token}"

        # Return redirect or message for the user
        return request.redirect(approval_url)

    @http.route(['/paypal/success'], type='http', auth='public', website=True, methods=['GET'], csrf=False)
    def paypal_success(self, **kwargs):
        """
        PayPal success callback handler.
        Captures the payment and creates related Odoo records.
        """
        _logger.info("PayPal success callback triggered.")

        lead_id = int(kwargs.get('lead_id', 0))
        paypal_order_id = kwargs.get('token')
        temp_token = kwargs.get('temp_token')
        payer_id = kwargs.get('PayerID')

        _logger.info(f"PayPal Success Params: lead_id={lead_id}, paypal_order_id={paypal_order_id}, temp_token={temp_token}, payer_id={payer_id}")

        # --- Validate incoming data
        if not lead_id or not paypal_order_id:
            _logger.error("Missing required parameters in PayPal success callback.")
            return request.redirect('/shop')

        lead = request.env['crm.lead'].sudo().browse(lead_id)
        if not lead.exists():
            _logger.error(f"Lead with ID {lead_id} does not exist.")
            return request.redirect('/shop')

        # --- Get PayPal credentials
        paypal_provider = request.env['payment.provider'].sudo().search([('code', '=', 'paypal')], limit=1)
        payment_method = request.env['payment.method'].sudo().search([('code', '=', 'paypal')], limit=1)
        client_id = paypal_provider.paypal_client_id
        client_secret = paypal_provider.paypal_client_secret
        access_token = self._get_paypal_access_token(client_id, client_secret)

        # --- Capture PayPal order
        capture_url = f"https://api-m.sandbox.paypal.com/v2/checkout/orders/{paypal_order_id}/capture"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }

        response = requests.post(capture_url, headers=headers)
        result = response.json()
        capture_amount = float(result['purchase_units'][0]['payments']['captures'][0]['amount']['value'])
        if response.status_code not in (200, 201):
            _logger.error(f"PayPal capture failed: {response.text}")
            return request.redirect('/shop')

        # --- Create Payment Transaction
        txn_vals = {
            'provider_id': paypal_provider.id,
            'payment_method_id': payment_method.id,
            'amount': capture_amount,
            'currency_id': request.env.ref('base.USD').id,
            'reference': paypal_order_id,
            'partner_id': lead.partner_id.id,
            'state': 'done',
        }
        payment_txn = request.env['payment.transaction'].sudo().create(txn_vals)
        _logger.info(f"Created Payment Transaction {payment_txn.id} for Lead {lead.name}")

        # --- Partner
        partner = lead.partner_id or request.env['res.partner'].sudo().create({
            'name': lead.partner_name or lead.name,
            'email': lead.email_from,
        })

        # --- Website / Company / Pricelist
        website = request.env['website'].sudo().search([], limit=1)
        public_user = website.user_id if website else request.env.ref('base.public_user')
        user_ctx = request.env(user=public_user)

        company = website.company_id or request.env['res.company'].sudo().search([], limit=1)
        company_id = company.id if company else False

        pricelist = request.env['product.pricelist'].sudo().search([('company_id', '=', company_id)], limit=1)
        if not pricelist:
            pricelist = request.env['product.pricelist'].sudo().search([], limit=1)
        pricelist_id = pricelist.id if pricelist else False

        # --- Disable all chatter + tracking
        ctx_no_mail = {
            'mail_create_nolog': True,
            'mail_notrack': True,
            'tracking_disable': True,
            'mail_create_nosubscribe': True,
        }

        capture_amount = float(result['purchase_units'][0]['payments']['captures'][0]['amount']['value'])
        currency = result['purchase_units'][0]['payments']['captures'][0]['amount']['currency_code']

        # --- Create Sale Order safely
        SaleOrder = user_ctx['sale.order'].sudo().with_context(**ctx_no_mail)
        sale_order = SaleOrder.create({
            'partner_id': partner.id,
            'origin': lead.name,
            'client_order_ref': paypal_order_id,
            'note': 'PayPal Payment confirmed',
            'company_id': company_id,
            'pricelist_id': pricelist_id,
        })
        _logger.info(f"Created Sale Order {sale_order.name} for Lead {lead.name}")

        # --- Add Order Line
        product = request.env['product.product'].sudo().search([], limit=1)
        sale_order.with_context(**ctx_no_mail).order_line = [(0, 0, {
            'product_id': product.id,
            'name': f"Payment for {lead.name}",
            'product_uom_qty': 1,
            'price_unit': capture_amount,
            'tax_id': [(6, 0, [])],
        })]

        # --- Confirm Order without chatter
        sale_order.with_context(**ctx_no_mail).action_confirm()
        sale_order.write({
            'website_id': website.id if website else False,
            'access_token': sale_order.access_token or sale_order._portal_ensure_token(),
        })

        # --- Link Transaction & Lead
        won_stage = request.env['crm.stage'].sudo().search([('name', '=', 'Won')], limit=1)
        if won_stage:
            lead.write({'stage_id': won_stage.id})
        payment_txn.sale_order_ids = [(4, sale_order.id)]
        _logger.info(f"Linked Payment Transaction {payment_txn.id} to Sale Order {sale_order.name}")

        tx = sale_order.get_portal_last_transaction()

        # --- Redirect to confirmation page
        return request.render("website_sale.confirmation", {
            'order': sale_order,
            'website_sale_order': sale_order,
            'tx_sudo': tx.sudo(),
        })


    @http.route(['/paypal/cancel'], type='http', auth='public', website=True)
    def paypal_cancel(self, **kwargs):
        """Handle PayPal cancellation"""
        _logger.warning("❌ User canceled PayPal payment.")
        return request.redirect('/shop')


    def _get_paypal_access_token(self, client_id, client_secret):
        """Helper for access token"""
        url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
        headers = {"Accept": "application/json", "Accept-Language": "en_US"}
        data = {"grant_type": "client_credentials"}
        auth = (client_id, client_secret)

        response = requests.post(url, headers=headers, data=data, auth=auth)
        response.raise_for_status()
        return response.json()['access_token']


