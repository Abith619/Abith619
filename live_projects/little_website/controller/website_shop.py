from odoo import http
from odoo.http import request
from werkzeug.utils import redirect
from odoo.addons.portal.controllers.web import Home
from odoo.addons.portal.controllers.portal import CustomerPortal
import odoo.addons.web.controllers.main as main
from odoo.exceptions import ValidationError
import os

class websitecustom(Home):

    @http.route('/webshop',type="http",auth="public",website=True)
    def web_shop(self, **kw):
        
        return http.request.render('new_module.webshop_homes',{})
    

    def _login_redirect(self, uid, redirect=None):
        if not redirect and request.params.get('login_success'):
            if request.env['res.users'].browse(uid)._is_internal():
                redirect = '/web?' + request.httprequest.query_string.decode()
            else:
                redirect = '/shop'
        return super()._login_redirect(uid, redirect=redirect)
    
    