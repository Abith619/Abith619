from odoo import _
import uuid
from odoo.http import request, route, Controller
from odoo.addons.auth_signup.controllers.main import AuthSignupHome

class AuthSignupConfirmation(AuthSignupHome):
    @route('/web/signup', type='http', auth='public', website=True, sitemap=False)
    def web_auth_signup(self, *args, **kw):

        email = kw.get('login')
        name = kw.get('name')

        if not email or not name:
            return request.render("auth_signup.signup", {
                'error_message': _("Email and Name are required."),
                'providers': [],
            })

        existing_user = request.env['res.users'].sudo().search([('login', '=', email)], limit=1)
        if existing_user:
            return request.render("auth_signup.signup", {
                'error_message': _("This email is already registered. Please log in."),
                'providers': [],
            })

        else:
            token = str(uuid.uuid4())
            request.session['auth_signup_token'] = token
            portal_group = request.env.ref('base.group_portal')
            object = request.env['res.users'].sudo().create({
                'name': name,
                'login': email,
                'email': email,
                'active': True,
                'signup_type': token,
                'groups_id': [(4, portal_group.id)]
            })

            template = request.env['mail.template'].browse(request.env.ref('custom_event.signup_confirmation_email_template').id)
            if object.partner_id:
                template.sudo().send_mail(object.id, force_send=True)

            return request.render("auth_signup.signup", {
                'success_message': _("A confirmation email has been sent to %s.") % email,
                'providers': [],
            })

class PasswordSetupController(Controller):

    @route('/web/set_password', type='http', auth='public', website=True)
    def set_password_form(self, token=None, **kwargs):
        user = request.env['res.users'].sudo().search([('signup_type', '=', token)], limit=1)
        if not user:
            return request.render("custom_event.token_invalid", {})

        return request.render("custom_event.set_password_form", {
            'token': token,
            'user': user
        })

    @route('/web/set_password/submit', type='http', auth='public', methods=['POST'], website=True, csrf=True)
    def set_password_submit(self, token=None, password=None, **kwargs):
        user = request.env['res.users'].sudo().search([('signup_type', '=', token)], limit=1)
        if not user or not password:
            return request.redirect('/web/set_password?token=%s&error=1' % token)
        if user:
            user.sudo().write({
            'password': password,
        })
            return request.render("custom_event.password_set_success", {})
        else:
            return request.render("custom_event.token_invalid", {})
