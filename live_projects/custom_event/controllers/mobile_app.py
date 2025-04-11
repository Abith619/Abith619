from odoo import http
import base64
from io import BytesIO
from odoo.http import request, Controller, route
from odoo.exceptions import ValidationError

class ImageController(Controller):
    @route('/get_image/<int:image_id>', auth='public', type='http')
    def get_image(self, image_id):
        image_record = request.env['your.model'].sudo().browse(image_id)
        if image_record and image_record.image_field:
            return http.send_file(
                BytesIO(base64.b64decode(image_record.image_field)),
                filename='home.png',
                mimetype='image/png'
            )
        return http.Response(status=404)