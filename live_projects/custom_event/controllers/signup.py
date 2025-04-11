from odoo import _, http
from odoo.http import request, route
from odoo.addons.auth_signup.controllers.main import AuthSignupHome

class AuthSignupConfirmation(AuthSignupHome):
    @route('/web/signup', type='http', auth="public", website=True, csrf=True, methods=['GET', 'POST'])
    def web_auth_signup(self, **post):

        email = post.get('login')
        name = post.get('name')

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
            portal_group = request.env.ref('base.group_portal')
            object = request.env['res.users'].sudo().create({
                'name': name,
                'login': email,
                'email': email,
                'active': True,
                'groups_id': [(4, portal_group.id)]
            })

            template = request.env['mail.template'].browse(request.env.ref('custom_event.signup_confirmation_email_template').id)
            if object.partner_id:
                template.sudo().send_mail(object.id, force_send=True)

            return request.render("auth_signup.signup", {
                'success_message': _("A confirmation email has been sent to %s.") % email,
                'providers': [],
            })