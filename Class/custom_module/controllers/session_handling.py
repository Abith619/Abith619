from odoo import http
from odoo.http import request, Controller, route

class SessionHandlingController(Controller):

    # http://localhost:8069/shop/cart?product_id=86&token=e8b73defa59e4e73bf0d4f046ff54919&lead_id=45

    # params = lead_id, product_id and token
    # uid = request.session.uid
    # Validated token using orm
    # get current website and sale order (quotation/cart)
    # update user cart with product id from params
    # redirect to cart page (or Checkout page)

    # created a field for payment link
    # used uuid.hex for generating token (also we can use random and secrets lib)
    # unique_token = uuid.uuid4().hex
    # lead.unique_token = unique_token
    # lead.payment_link = f"{web_base_url}/lead/checkout?lead_id={lead.id}&token={unique_token}"

    @http.route('/lead/checkout', type='http', auth='public', website=True)
    def lead_validate(self, **kw):
        # kw = kwargs, type arhguments
        lead_id =kw.get('lead_id')
        token = kw.get('token')

        lead = request.env['crm.lead'].sudo().search([('id', '=', lead_id)], limit=1)

        if lead.unique_token != token:
            # Valid token, proceed to checkout
            # Here you can render a checkout page or process the payment
            return request.redirect('/shop')
        else:
            product = lead.course_id.product_id
        # Create new order (incognito-safe)
            website = request.env['website'].get_current_website()
            order = website.sale_get_order(force_create=True)
            order.sudo().write({'lead_id': lead.id, 'opportunity_id': lead.id})
            order.order_line.unlink()
            order._cart_update(product_id=product.id, add_qty=1)
            checkout_url = f"/shop/cart?product_id={product.id}&token={token}&lead_id={lead.id}"
            return request.redirect(checkout_url)

    # SESSION HANDLING EXAMPLES

    @route('/session/step1', type='http', auth='public', methods=['POST'], csrf=False)
    def session_step1(self, **post):
        request.session['step1_data'] = post.get('name')
        return request.redirect('/session/step2')

    @route('/session/step2', type='http', auth='public', methods=['GET'], csrf=False)
    def session_step2(self, **post):
        step1_data = request.session.get('step1_data')
        return request.render('contact_us.thank-you-page')