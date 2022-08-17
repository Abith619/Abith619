import logging
from functools import wraps

import werkzeug

from odoo import http
from odoo.service.db import exp_db_exist

from .utils import (
    check_saas_client_token,
    str_filter_falsy,
)
from .exceptions import DatabaseNotExists

_logger = logging.getLogger(__name__)


def require_saas_token(func):
    """
    Decorate the controller method that requires check_saas_client_token.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        token_hash = http.request.httprequest.environ.get(
            'HTTP_X_YODOO_TOKEN',
            kwargs.get('token_hash', None))
        check_saas_client_token(token_hash)
        return func(*args, **kwargs)

    return wrapper


def require_db_param(func):
    """
    Decorate the controller method that requires exp_db_exist.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        db = kwargs.get('db', None)
        if not db:
            raise werkzeug.exceptions.BadRequest("Database not specified")
        if not exp_db_exist(db):
            _logger.info(
                'Database %s is not found.', db)
            raise DatabaseNotExists()
        return func(*args, **kwargs)

    return wrapper


def wrap_str_falsy_values(*field_names):
    """ check the data passed to method and converf string falsy values
        to correct python valus:
            'none' -> None
            'false', '0' -> None

    """
    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            for fname in field_names:
                if fname in kwargs and isinstance(kwargs[fname], str):
                    kwargs[fname] = str_filter_falsy(kwargs[fname])
            return func(*args, **kwargs)
        return decorated
    return decorator
