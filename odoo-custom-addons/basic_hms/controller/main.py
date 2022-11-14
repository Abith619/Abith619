from odoo import http
import odoo
from odoo.http import request
from odoo.addons.portal.controllers.web import Home
from odoo.addons.portal.controllers.portal import CustomerPortal
import odoo.addons.web.controllers.main as main
from odoo.exceptions import ValidationError
import base64
from datetime import datetime
import werkzeug
import base64
from io import BytesIO


class employee(Home):
    
    # @http.route('/',type="http",auth="public",website=True)
    # def index(self, **kw):
    #    super(employee, self).index()
    #    return request.render('website.homepage', {})
    
    @http.route('/appointment',type="http",auth="public",website=True)
    def apply_job(self,**kw):
        many2one_connect = request.env['res.partner'].sudo().search([('is_doctor','=',True)])
        many2one_area = request.env['res.city'].sudo().search([])
        many2one_patient = request.env['res.partner'].sudo().search([('is_patient','=',True)])
       
        return http.request.render('basic_hms.appointment_page',{'many2one_connect':many2one_connect,
                                                                 'many2one_area':many2one_area,
                                                                 'many2one_patient':many2one_patient})
        
    @http.route('/website/page1',type="http",auth="public",website=True)
    def create(self,**kw):
        
        patient_name = kw.get('name')
        phone_number = kw.get('phone_number')
        contact_number = kw.get('contact_number')
        gender = kw.get('gender')
        
        request.session['var'] = patient_name
        
        var = {
            'name' : patient_name,
            'whatsapp':contact_number,
            'mobile':phone_number,
            'patient_gender':gender,
        }
        
        own = request.env['res.partner'].sudo().create(var)
        
        gender = kw.get('gender')
        age = kw.get('age')
        treat = kw.get('treatment_for')
        contact = kw.get('phone_number')
        whatsapp = kw.get('contact_number')
        date = kw.get('dates')
        area = kw.get('region')
        
        sub_own = own.id
        
        wec = request.env['medical.pathology'].sudo().create({
            'name' : treat
        })
        
        menu = wec.id
        vals = {
            'patient_id' : sub_own,
            'gender':gender,
            'age':age,
            'dates':date,
            'region':area,
            'treatment_for': menu,
            'phone_number':contact,
            'contact_number':whatsapp,
            'types_app':'web',
        }
        request.env['medical.appointment'].sudo().create(vals)
        
        return request.render('basic_hms.applied_thanks',{})
        
        
    # @http.route('/web/login', type='http', auth="none", sitemap=False)
    # def web_login(self, redirect=None, **kw):
    #     main.ensure_db()
    #     request.params['login_success'] = False
    #     if request.httprequest.method == 'GET' and redirect and request.session.uid:
    #         return http.redirect_with_hash(redirect)

    #     if not request.uid:
    #         request.uid = odoo.SUPERUSER_ID

    #     values = request.params.copy()
    #     try:
    #         values['databases'] = http.db_list()
    #     except odoo.exceptions.AccessDenied:
    #         values['databases'] = None

    #     if request.httprequest.method == 'POST':
    #         old_uid = request.uid
    #         try:
    #             uid = request.session.authenticate(request.session.db, request.params['login'], request.params['password'])
    #             request.params['login_success'] = True

    #             # You can redirect to any view from here
    #             url = '/web#id={0}&view_type={1}&model={2}'.format(1, 'form', 'res.partner')
    #             return werkzeug.utils.redirect(url)

    #             # return http.redirect_with_hash(self._login_redirect(uid, redirect=redirect))
    #         except odoo.exceptions.AccessDenied as e:
    #             request.uid = old_uid
    #             if e.args == odoo.exceptions.AccessDenied().args:
    #                 values['error'] = _("Wrong login/password")
    #             else:
    #                 values['error'] = e.args[0]
    #     else:
    #         if 'error' in request.params and request.params.get('error') == 'access':
    #             values['error'] = _('Only employee can access this database. Please contact the administrator.')

    #     if 'login' not in values and request.session.get('auth_login'):
    #         values['login'] = request.session.get('auth_login')

    #     if not odoo.tools.config['list_db']:
    #         values['disable_database_manager'] = True

    #     # otherwise no real way to test debug mode in template as ?debug =>
    #     # values['debug'] = '' but that's also the fallback value when
    #     # missing variables in qweb
    #     if 'debug' in values:
    #         values['debug'] = True

    #     response = request.render('web.login', values)
    #     response.headers['X-Frame-Options'] = 'DENY'
    #     return response