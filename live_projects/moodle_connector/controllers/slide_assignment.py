from odoo import http
from odoo.http import request
import base64


class AssignmentSubmitController(http.Controller):

    @http.route('/assignment/submit',type='http',auth='user',website=True,methods=['POST'],csrf=True)
    def submit_assignment(self, slide_id=None, channel_id=None, **kw):

    
        assignment_file = request.httprequest.files.get('assignment_file')

        if not assignment_file or not slide_id or not channel_id:
            return request.redirect('/slides/%s' % channel_id)

        partner = request.env.user.partner_id

    
        slide_partner = request.env['slide.slide.partner'].sudo().search([
            ('slide_id', '=', int(slide_id)),
            ('partner_id', '=', partner.id),
            ('channel_id', '=', int(channel_id)),
            ('is_assignment', '=', True),
        ], limit=1)

        if not slide_partner:
            return request.redirect('/slides/%s' % channel_id)

    
        if slide_partner.assignment_attachment_ids:
            return request.redirect('/slides/%s' % channel_id)

    
        attachment = request.env['ir.attachment'].sudo().create({
            'name': assignment_file.filename,
            'datas': base64.b64encode(assignment_file.read()),
            'res_model': 'slide.slide.partner',
            'res_id': slide_partner.id,
            'mimetype': assignment_file.content_type,
        })

        slide_partner.write({
            'assignment_attachment_ids': [(4, attachment.id)]
        })

    
        return request.redirect('/slides/%s' % channel_id)
