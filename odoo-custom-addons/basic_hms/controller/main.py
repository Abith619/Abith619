from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.web import Home
from odoo.addons.portal.controllers.portal import CustomerPortal
import odoo.addons.web.controllers.main as main
from odoo.exceptions import ValidationError

class employee(Home):
    
    @http.route('/appointment',type="http",auth="public",website=True)
    def apply_job(self,**kw):
        many2one_connect = request.env['res.partner'].sudo().search([('is_doctor','=',True)])
        many2one_patient = request.env['res.partner'].sudo().search([('is_patient','=',True)])
        many_treat = request.env['medical.pathology'].sudo().search([])
        many2one_country = request.env['res.country'].sudo().search([])
        many2one_state = request.env['res.country.state'].sudo().search([('country_id','=',104)])
        many2one_area = request.env['res.city'].sudo().search([])
        many2many_feedback = request.env['medical.feedback'].sudo().search([])
        return http.request.render('basic_hms.appointment_page',{'many2one_connect':many2one_connect,
                                                                 'many2one_area':many2one_area,
                                                                 'many2one_patient':many2one_patient,
                                                                 'many_treat' : many_treat,
                                                                 'many2one_state':many2one_state,
                                                                 'many2one_country' : many2one_country,
                                                                 'many2many_feedback':many2many_feedback
                                                                 })
        
    @http.route('/website/page1',type="http",auth="public",website=True)
    def create(self,**kw):
        patient_name = kw.get('patient_id')
        phone_number = kw.get('contact_no')
        contact_number = kw.get('contact_number')
        gender = kw.get('sex')
        address = kw.get('address')
        city = kw.get('city')
        state = kw.get('state_id')
        zip_id = kw.get('zip')
        country_id = kw.get('country')
        dob_contact = kw.get('date_of_birth')
        marital_status = kw.get('marital_status')
        
        var = {
            'name' : patient_name,
            'whatsapp':contact_number,
            'mobile':phone_number,
            'patient_gender':gender,
            'marital_status':marital_status,
            'street':address,
            'city':city,
            'state_id':state,
            'zip':zip_id,
            'country_id':int(country_id),
            
            'dob_contact':dob_contact,
        }
        
        own = request.env['res.partner'].sudo().create(var)
        
        gender = kw.get('sex')
        review = kw.get('reg_types')
        age = kw.get('age')
        contact = kw.get('contact_no')
        whatsapp = kw.get('contact_number')
        app_date = kw.get('dates')
        dob_date = kw.get('date_of_birth')
        area = kw.get('city')
        address = kw.get('address')
        pin_code = kw.get('pin_code')
        state_id = kw.get('state')
        country = kw.get('country')
        treat = kw.get('treatment_for')
        marital_status = kw.get('marital_status')
        sub_own = own.id
        reg_type = kw.get('reg_type')
        height = kw.get('height')
        weight = kw.get('weight')
        data_value = request.httprequest.form.getlist('data_value')
        
        vals = {
            'patient_id' : sub_own,
            'sex':gender,
            'age':age,
            'dates':app_date,
            'date_of_birth':dob_date,
            'address':address,
            'pin_code':pin_code,
            'city':int(area),
            'state':state_id,
            'country':int(country),
            'treatment_for': treat,
            'contact_no':contact,
            'contact_number':whatsapp,
            'marital_status':marital_status,
            'reg_type':reg_type,
            'online_type':review,
            'direct_type':review,
            'qr_type':'qr',
            'weight':weight,
            'height':height,
            'data_value':data_value
        }
        
        create = request.env['medical.patient'].sudo().create(vals)
        token = create.name
        return request.render('basic_hms.applied_thanks',{'token':token})
