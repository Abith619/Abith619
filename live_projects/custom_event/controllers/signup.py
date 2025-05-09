import logging

from odoo import _
from odoo.http import request, route

from odoo.addons.auth_signup.controllers.main import AuthSignupHome

_logger = logging.getLogger(__name__)

class SignupVerifyEmail(AuthSignupHome):
    @route()
    def web_auth_signup(self, *args, **kw):
        if request.params.get("login") and not request.params.get("password"):
            return self.passwordless_signup()
        return super().web_auth_signup(*args, **kw)

    def passwordless_signup(self, *args, **kw):
        values = request.params
        qcontext = self.get_auth_signup_qcontext()

        if not values.get("email"):
            values["email"] = values.get("login")

        values.pop("redirect", "")
        values.pop("token", "")
        values["password"] = ""

        # Prepare user creation values
        user_values = {
            'name': values.get('name') or values.get('login'),
            'login': values.get('login'),
            'email': values.get('email'),
            'password': values.get('password'),  # Empty string or handle as needed
        }

        try:
            sudo_users = request.env['res.users'].with_context(create_user=True).sudo()
            user = sudo_users.create(user_values)

            # Optionally track signup IP
            ip = request.httprequest.headers.get('X-Forwarded-For', request.httprequest.remote_addr)
            user.x_signup_ip = ip

            request.env.cr.commit()  # Ensure it's saved before redirect
            return request.redirect('/web/login')  # Or another post-signup page
        except Exception as e:
            _logger.exception("User creation failed: %s", str(e))
            qcontext['error'] = _("Could not create user.")
            return request.render('auth_signup.signup', qcontext)
