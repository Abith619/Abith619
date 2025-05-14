import hashlib

from odoo import http
from odoo.http import request
from odoo.tools import file_open

SCALE_FILES = [
    'point_of_sale/static/src/app/screens/scale_screen/scale_service.js',
    'point_of_sale/static/src/app/screens/scale_screen/scale_screen.js',
    'point_of_sale/static/src/app/screens/scale_screen/scale_screen.xml',
    'hw_drivers/iot_handlers/drivers/SerialScaleDriver.py',
    'pos_iot/static/src/overrides/components/scale_screen/scale_service.js',
]

def calculate_scale_checksum():
    files_data = []
    main_hash = hashlib.sha256()
    for path in sorted(SCALE_FILES):
        with file_open(path, 'rb') as file:
            content = file.read()
        content_hash = hashlib.sha256(content).hexdigest()
        files_data.append({
            'name': path,
            'size_in_bytes': len(content),
            'contents': content.decode(),
            'hash': content_hash
        })
        main_hash.update(content_hash.encode())

    return main_hash.hexdigest(), files_data

class ChecksumController(http.Controller):
    @http.route('/scale_checksum', auth='user')
    def handler(self):
        main_hash, files_data = calculate_scale_checksum()

        # TODO master: change this to use a view like pos_blackbox_be
        file_hashes = '\n'.join([f"{file['name']}: {file['hash']} (size in bytes: {file['size_in_bytes']})" for file in files_data])
        file_contents = '\n'.join([
f"""--------------------------------------------------------------------
{file['name']}
--------------------------------------------------------------------
{file['contents']}"""
            for file in files_data
        ])

        response_text = f"""
SIGNATURES:
--------------------------------------------------------------------
GLOBAL HASH: {main_hash}
{file_hashes}
--------------------------------------------------------------------

CONTENT:
{file_contents}"""

        headers = [
            ('Content-Length', len(response_text)),
            ('Content-Type', 'text/plain'),
        ]
        return request.make_response(response_text, headers)
