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

        sudo_users = request.env["res.users"].with_context(create_user=True).sudo()
        ip = request.httprequest.headers.get('X-Forwarded-For', request.httprequest.remote_addr)
        sudo_users.x_signup_ip = ip

        try:
            with request.cr.savepoint():
                sudo_users.signup(values, qcontext.get("token"))
                sudo_users.reset_password(values.get("login"))

            qcontext["message"] = _("Please check your email to activate your account!")
            return request.render("auth_signup.reset_password", qcontext)

        except Exception as error:
            _logger.exception("Signup error: %s", error)
            if request.env["res.users"].sudo().search([("login", "=", values.get("login"))]):
                qcontext["error"] = _(
                    "Another user is already registered using this email address."
                )
            else:
                qcontext["error"] = _(
                    "Something went wrong, please try again later or contact us."
                )
            return request.render("auth_signup.signup", qcontext)