import re
import odoo
from odoo.service import db
from odoo import http
from odoo.tools import config

from .utils import (
    make_addons_to_be_installed,
    ensure_installing_addons_dependencies,
)

original_list_dbs = db.list_dbs
original_db_filter = http.db_filter
original_module_db_initialize = odoo.modules.db.initialize


def list_dbs(force=False):
    res = original_list_dbs(force)
    db_name_pattern = r"^tmp-.*-tmp$"
    return list(filter(lambda i: not(re.match(db_name_pattern, i)), res))


def db_filter(dbs, httprequest=None):
    httprequest = httprequest or http.request.httprequest
    dbs = original_db_filter(dbs, httprequest=httprequest)
    db_header = httprequest.environ.get('HTTP_X_ODOO_DBFILTER')
    if not db_header:
        return dbs
    return [db for db in dbs if re.match(db_header, db)]


def module_db_initialize(cr):
    original_module_db_initialize(cr)

    make_addons_to_be_installed(cr, ['yodoo_client'])

    auto_install_addons = config.get('yodoo_auto_install_addons', '')
    auto_install_addons = [a.strip() for a in auto_install_addons.split(',')]
    if auto_install_addons:
        make_addons_to_be_installed(cr, auto_install_addons)

    ensure_installing_addons_dependencies(cr)


def _post_load_hook():
    if config.get('yodoo_db_filter', False):
        http.db_filter = db_filter

    # Make autoinstall of yodoo_client
    odoo.modules.db.initialize = module_db_initialize
    odoo.service.db.list_dbs = list_dbs
