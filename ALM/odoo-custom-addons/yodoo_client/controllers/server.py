import json
import logging

from odoo import http
from odoo.http import Response
from ..utils import (
    prepare_saas_module_info_data,
    prepare_server_fast_statistic_data,
    prepare_server_slow_statistic_data,
)
from ..http_decorators import (
    require_saas_token,
)


_logger = logging.getLogger(__name__)


class SAASClientInstance(http.Controller):

    @http.route(
        ['/saas/client/module/info', '/saas/client/server/module/info'],
        type='http',
        auth='none',
        metods=['POST'],
        csrf=False
    )
    @require_saas_token
    def get_client_module_info(self, **params):
        data = prepare_saas_module_info_data()
        return Response(json.dumps(data), status=200)

    @http.route(
        ['/saas/client/server/fast/stat', '/saas/client/server/stat/fast'],
        type='http',
        auth='none',
        metods=['POST'],
        csrf=False
    )
    @require_saas_token
    def get_server_fast_statistic(self, **params):
        data = prepare_server_fast_statistic_data()
        return Response(json.dumps(data), status=200)

    @http.route(
        ['/saas/client/server/slow/stat', '/saas/client/server/stat/slow'],
        type='http',
        auth='none',
        metods=['POST'],
        csrf=False
    )
    @require_saas_token
    def get_server_slow_statistic(self, **params):
        data = prepare_server_slow_statistic_data()
        return Response(json.dumps(data), status=200)
