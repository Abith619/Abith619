# -*- coding: utf-8 -*-
from sqlite3 import DatabaseError
import werkzeug
from odoo import http
from odoo.http import request
from odoo.addons.auth_signup.models.res_users import SignupError
from ..JwtRequest import jwt_request
from ..util import is_valid_email
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
import datetime
from datetime import timedelta,date
import jwt
import logging
_logger = logging.getLogger(__name__)

SENSITIVE_FIELDS = ['password', 'password_crypt', 'new_password', 'create_uid', 'write_uid']
SECRET_KEY = "6+8RpZ7ccvF1mPnCV4MDL7/ROLEIBp4f3hqRhvOeTx4="


class JwtController(http.Controller):

    @http.route('/api/http/hello', type='http', auth='public', csrf=False, cors='*')

    @jwt_request.middlewares('api_key')
    def hello(self, **kw):
        return jwt_request.response({ 'message': 'hello!', 'key_info': jwt_request.data.get('key_info') })

    @http.route('/api/http/login', type='json', auth='public', csrf=False, cors='*', methods=['POST'])
    def login(self, email=None, password=None, **kw):
        email = request.params.get('email')
        password =request.params.get('password')
        token = jwt_request.login(email, password)

        login_email = request.env['res.users'].sudo().search([('login', '=', email)])
        if login_email:
            if token:
                login_orm = request.env['res.users'].sudo().search([('login', '=', email)])
                # type_users = login_orm.type_users
                # new_create_doc = request.env['doctor.registration'].sudo().search_read([('res_users','=',login_orm.id),('status','=','active')],fields=['status','res_users'])
                # if new_create_doc:
                res = {
                "accessToken": token,
                "status": "success",
                "message": "Login Successfully",
                'status_message':"success",
                # 'type_users': login_orm['type_users'],
                'data': {
                    'email':login_orm['email'],
                    # 'phone_number':login_orm['phone_number'],
                    'name':login_orm['name'],
                    'partner_id':login_orm['partner_id'].id,
                }
                }
                return res
                
            else:
                res={
                    'status':"failure",
                    'message':"Invalid Email Or Password",
                    'status_message':"invalid"
                }
                return res
        else:
            res={
                'status':"failure",
                'message':"You have not Registered, Please Register.",
                'status_message':"notfound"

            }
            return res


    @http.route('/api/http/me', type='http', auth='public', csrf=False, cors='*')
    @jwt_request.middlewares('jwt')
    def me(self, **kw):
        return jwt_request.response(request.env.user.to_dict())


    @http.route('/api/http/logout', type='http', auth='public', csrf=False, cors='*')
    @jwt_request.middlewares('jwt')
    def logout(self, **kw):
        jwt_request.logout()
        return jwt_request.response()


    @http.route('/api/regis', type='http', auth='public', csrf=False, cors='*', methods=['POST'])
    def regis(self, email=None, name=None, password=None,user='user' ,**kw):

        
        name =request.params.get('name')
        email = request.params.get('email')
        password =request.params.get('password')
        user=request.params.get('user')
        # phone_number=request.params.get('mobileno')
        # gender=request.params.get('gender')
        # location=request.params.get('location')
        # dob=request.params.get('dob')
        '''
        In previous version, we use auth_signup to register an external (portal) user.
        For this demo, we use res.users.create instead, this will create an internal user
        '''
        if not is_valid_email(email):
            return jwt_request.response(status=400, data={'message': 'Invalid email address','status': 'failure'})
        if not name:
            return jwt_request.response(status=400, data={'message': 'Name cannot be empty','status': 'failure'})
        if not password:
            return jwt_request.response(status=400, data={'message': 'Password cannot be empty','status': 'failure'})
        # if not dob:
        #     return jwt_request.response(status=400, data={'message': 'dob cannot be empty','status': 'failure'})

        # sign up
        try:
            if request.env['res.users'].sudo().search([('login', '=', email)]):
                return jwt_request.response(status=400, data={'message': 'Email address is already exist','status': 'failure'})
            # if request.env['res.users'].sudo().search([('phone_number', '=', phone_number)]):
            #     return jwt_request.response(status=400, data={'message': 'phone_number is already exist','status': 'failure'})
            user = request.env['res.users'].sudo().create({
                'login': email,
                'password': password,
                'name': name,
                'email': email,
                # 'type_users': user,

            })
            # return user

            if user:
                
                # no need to authenticate user here
                # cuz we just respond data right away
                # if you really need to authenticate user, use jwt_request.login(email, password)
                # token can be used instead of password
                # create token


                token = jwt_request.create_token(user)
                return {
                    'message':'Successfully Login',
                     'status':'success',
                    'user': user.to_dict(),
                    'accessToken': token,
                    'data': {
                    'email':user['email'],
                    'name':user['name'],
                    'partner_id':user['partner_id'].id,
                    }
                    
                }
        except Exception as e:
            _logger.error(str(e))
            return jwt_request.response_500({
                'message': 'Server error'
            })


    @http.route('/api/http/signup', type='http', auth='public', csrf=False, cors='*', methods=['POST'])
    def register(self, email=None, name=None, password=None, **kw):
        '''
        Sign up using auth_signup modules
        '''
        if not is_valid_email(email):
            return jwt_request.response(status=400, data={'message': 'Invalid email address'})
        if not name:
            return jwt_request.response(status=400, data={'message': 'Name cannot be empty'})
        if not password:
            return jwt_request.response(status=400, data={'message': 'Password cannot be empty'})

        # sign up
        try:
            model = request.env['res.users'].sudo()
            signup = getattr(model, 'signup')
            if signup:
                if request.env['res.users'].sudo().search([('login', '=', email)]):
                    return jwt_request.response(status=400, data={'message': 'Email address is not available'})
                data = {
                    'login': email,
                    'password': password,
                    'name': name,
                    'email': email,
                }
                # signup return a tuple (db, login, password)
                # you can use that to call jwt_request.login(login, password)
                signup(data)
                # but, we just need to retrieve the newly created user
                user = model.search([
                    ('login', '=', email)
                ])
                if user:
                    token = jwt_request.create_token(user)
                    return jwt_request.response({
                        'user': user.to_dict(),
                        'token': token
                    })
                raise Exception()
        except SignupError:
            return jwt_request.response({
                'message': 'Signup is currently disabled',
            }, 400)
        except Exception as e:
            _logger.error(str(e))
            return jwt_request.response_500({
                'message': 'Cannot create user'
            })

    def _response_auth(self, token: str):
        return jwt_request.response({
            'user': request.env.user.to_dict(),
            'token': token,
        })


        

    