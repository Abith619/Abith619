import json
import uuid
import base64
import logging
import hashlib
from datetime import datetime, timedelta

import werkzeug.exceptions

import odoo
from odoo import http, registry, fields, SUPERUSER_ID
from odoo.tools import config
from odoo.http import request, Response
from ..utils import (
    DEFAULT_TIME_TO_LOGIN,
    DEFAULT_LEN_TOKEN,
    DEFAULT_ADMIN_SESSION_TTL,
    SAAS_CLIENT_API_VERSION,
    SAAS_TOKEN_FIELD,
    check_saas_client_token,
    get_yodoo_client_version,
    generate_random_password,
)
from ..http_decorators import (
    require_saas_token,
    require_db_param,
)

_logger = logging.getLogger(__name__)


class SAASClient(http.Controller):

    @http.route(
        '/saas/client/version_info',
        type='http',
        auth='none',
        metods=['POST'],
        csrf=False
    )
    @require_saas_token
    def get_saas_client_version_info(self, **params):
        module_version_info = get_yodoo_client_version().split('.')
        module_version_serie = '.'.join(module_version_info[0:2])
        module_version = '.'.join(module_version_info[-3:])

        data = {
            'odoo_version': odoo.release.version,
            'odoo_version_info': odoo.release.version_info,
            'odoo_serie': odoo.release.serie,
            'saas_client_version': module_version,
            'saas_client_serie': module_version_serie,
            'saas_client_api_version': SAAS_CLIENT_API_VERSION,
        }
        return http.Response(json.dumps(data), status=200)

    @http.route(
        ['/odoo/infrastructure/auth', '/saas/client/auth'],
        type='http',
        auth='none',
        metods=['POST'],
        csrf=False
    )
    @require_saas_token
    @require_db_param
    def create_temporary_login_data(self, db=None, ttl=DEFAULT_TIME_TO_LOGIN,
                                    user_uuid=None, user_id=None, **params):
        admin_access_credentials = config.get('admin_access_credentials', True)
        if not admin_access_credentials:
            _logger.warning(
                "Attempt to get temporary login/password, "
                "but this operation is disabled in Odoo config")
            raise werkzeug.exceptions.Forbidden(description='Feature disabled')

        token = config.get(SAAS_TOKEN_FIELD, False)
        token_hash = hashlib.sha256(token.encode('utf8')).hexdigest()

        random_token = generate_random_password(DEFAULT_LEN_TOKEN)
        uri_token = '%s:%s:%s' % (db, random_token, token_hash)
        uri_token = base64.b64encode(uri_token.encode("utf-8")).decode()
        data = {
            'token_user': str(uuid.uuid4()),
            'token_password': str(uuid.uuid4()),
            'temp_url': '/saas/client/auth/%s' % uri_token,
            'expire': fields.Datetime.to_string(
                datetime.now() + timedelta(seconds=int(ttl))),
            'token_temp': random_token,
            'user_uuid': user_uuid,
            'user_id': user_id if user_id else SUPERUSER_ID,
        }
        with registry(db).cursor() as cr:
            cr.execute("""
                INSERT INTO odoo_infrastructure_client_auth
                    (token_user, token_password, expire, token_temp,
                     user_uuid, user_id)
                VALUES (
                    %(token_user)s,
                    %(token_password)s,
                    %(expire)s,
                    %(token_temp)s,
                    %(user_uuid)s,
                    %(user_id)s
                );
            """, data)
        return Response(json.dumps(data), status=200)

    @http.route(
        ['/saas_auth/<token>', '/saas/client/auth/<token>'],
        type='http',
        auth='none',
        metods=['GET'],
        csrf=False
    )
    def yodoo_client_auth(self, token):
        try:
            token = base64.b64decode(token.encode('utf-8')).decode('utf-8')
            db, token_temp, token_hash = token.split(':')
        except (base64.binascii.Error, TypeError):
            _logger.warning(
                'Bad Data: url: %s not in BASE64', token)
            raise werkzeug.exceptions.BadRequest()

        check_saas_client_token(token_hash)

        # Check if user allows to logins
        with registry(db).cursor() as cr:
            cr.execute("""
                SELECT value
                FROM ir_config_parameter
                WHERE key = %(key)s
                LIMIT 1;
            """, {
                'key': 'yodoo_client.yodoo_allow_admin_logins',
            })
            data = cr.fetchall()
            # Note, if we try to set falsy value as param, then record will be
            # removed. Instead, if we try to set non-falsy value, then odoo
            # will save it as row in table ir_config_parameter
            # For detais see ir_config_parameter.set_param
            yodoo_allow_admin_logins = bool(data)

        if not yodoo_allow_admin_logins:
            _logger.warning(
                'Attempt to login as admin. Feature disabled on db level')
            raise werkzeug.exceptions.Forbidden(
                description='Client denies admin logins to this DB.')

        with registry(db).cursor() as cr:
            cr.execute("""
                SELECT id, token_user, token_password, user_uuid, user_id
                FROM odoo_infrastructure_client_auth
                WHERE token_temp=%(toke_temp)s AND
                expire > CURRENT_TIMESTAMP AT TIME ZONE 'UTC';
            """, {
                'toke_temp': token_temp
            })
            res = cr.fetchone()
        if not res:
            _logger.warning(
                'Temp url %s does not exist', token)
            raise werkzeug.exceptions.Forbidden()

        auth_id, user, password, user_uuid, user_id = res
        request.session.authenticate(db, user, password)

        # Do not rotate session. So user will keep same session as before.
        # TODO: handle admin sessions in better way
        request.session.rotate = False

        with registry(db).cursor() as cr:
            cr.execute("""
                UPDATE yodoo_client_auth_log
                SET login_state = 'expired',
                    logout_date = now()
                WHERE login_session = %(login_session)s
                  AND login_state = 'active';

                INSERT INTO yodoo_client_auth_log
                       (login_date, login_expire,
                        login_state, login_session,
                        login_remote_uuid, login_user_id)
                VALUES (%(login_date)s, %(login_expire)s,
                        'active', %(login_session)s,
                        %(user_uuid)s, %(user_id)s);

                DELETE FROM odoo_infrastructure_client_auth
                WHERE id = %(auth_id)s;
            """, {
                'login_date': fields.Datetime.now(),
                'login_session': request.session.sid,
                'login_expire': fields.Datetime.to_string(
                    datetime.now() + timedelta(
                        seconds=int(DEFAULT_ADMIN_SESSION_TTL))),
                'user_uuid': user_uuid,
                'user_id': user_id,
                'auth_id': auth_id,
            })
        return http.redirect_with_hash('/web')
