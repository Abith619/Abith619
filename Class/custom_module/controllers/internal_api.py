from odoo import http
from odoo.http import request, Controller, route, Response
import json

class APIController(Controller):

    #                                       type='http' for REST API

    @route('/api/patients/create', type='http', auth='public', methods=['POST'], csrf=False)
    def create_patient(self, **kwargs):
        name = kwargs.get('name')
        # age = kwargs.get('age')
        phone = kwargs.get('phone')
        patient = request.env['res.partner'].sudo().create({
            'name': name,
            # 'age': age,
            'phone': phone,
            'is_patient': True,
        })
        if patient:
            return Response(
                json.dumps({"status": "success", "message": "Patient created successfully"}),
                content_type='application/json'
            )
        else:
            return Response(
                json.dumps({"status": "failed", "message": "Failed to create patient"}),
                content_type='application/json'
            )
    # <int:patient_id> to get the patient id from the URL

    @route('/api/patients/<int:patient_id>', type='http', auth='public', methods=['PUT'], csrf=False)
    def update_patient(self, patient_id, **kwargs):

        name = kwargs.get('name')
        phone = kwargs.get('phone')

        patient = request.env['res.partner'].sudo().browse(patient_id)

        if not patient.exists():
            return Response(
                json.dumps({'error': 'Patient not found'}),
                status=404,
                headers=[('Content-Type', 'application/json')]
            )

        patient.write({
            'name': name,
            'phone': phone,
        })

        return Response(
            json.dumps({'success': True}),
            status=200,
            headers=[('Content-Type', 'application/json')]
        )

    # csrf only used in Forms, not in API calls

    @route('/api/patients', type='http', auth='public', methods=['GET'], csrf=False)
    def get_patients_rest(self, **kwargs):
        patients = request.env['res.partner'].sudo().search([
            ('is_patient', '=', True)
        ])

        data = []
        for patient in patients:
            data.append({
                'id': patient.id,
                'name': patient.name,
                'phone': patient.phone,
                'email': patient.email,
            })

        return request.make_response(
            json.dumps({
                "status": "success",
                "count": len(data),
                "patients": data
            }),
            headers=[('Content-Type', 'application/json')],
            status=200
        )

    @route('/api/patients/<int:patient_id>', type='http', auth='public', methods=['GET','PUT'], csrf=False)
    def patient_api(self, patient_id, **kwargs):
        token = request.httprequest.headers.get('Authorization')
        user = request.env.user
        if token and user and user.token == token:
            if request.httprequest.method == 'GET':
                patient = request.env['res.partner'].sudo().browse(patient_id)
                if patient:
                    return Response(
                        json.dumps({
                            'id': patient.id,
                            'name': patient.name,
                            'phone': patient.phone,
                            'email': patient.email,
                        }),
                        headers=[('Content-Type', 'application/json')],
                        status=200
                    )
            elif request.httprequest.method == 'PUT':
                name = kwargs.get('name')
                phone = kwargs.get('phone')
                email = kwargs.get('email')

                patient_orm = request.env['res.partner'].sudo().search([('email', '=', email)])

                if patient_orm:
                    patient_orm.write({
                            'name': name,
                            'phone': phone,
                        })
                    return Response(
                        json.dumps({'status': 'updated', 'message': 'Patient updated successfully'}),
                        content_type='application/json'
                    )
#                                                                   https://www.cybrosys.com/blog/how-to-call-json-rpc-to-webcontroller-in-odoo18
    # Add the below headers and body in postman while making JSON-RPC call
    # JSON-RPC is used to call a method on the server and pass parameters
# Headers for JSON-RPC call
    #    Content-Type: application/json
# Body for JSON-RPC call
    # {
    #     "jsonrpc": "2.0",
    #     "method": "call",
    #     "params": {},
    #     "id": 1
    # }
    # @route('/api/patients', type='json', auth='public', methods=['GET'], csrf=False)
    # def get_patients_rpc(self, **kwargs):
    #     partners = request.env['res.partner'].sudo().search([
    #         ('is_patient', '=', True)
    #     ])

    #     data = []
    #     for partner in partners:
    #         data.append({
    #             'id': partner.id,
    #             'name': partner.name,
    #             'phone': partner.phone,
    #             'email': partner.email,
    #         })

    #     return {
    #         "status": "success",
    #         "count": len(data),
    #         "patients": data
    #     }
        # Call json-rpc function from UI by using the below js code
    # /** @odoo-module **/
    # import publicWidget from "@web/legacy/js/public/public_widget";
    # import { rpc } from "@web/core/network/rpc";
    # import { onWillStart } from "@odoo/owl";
    # publicWidget.registry.TestRpcController = publicWidget.Widget.extend({
    #     selector: ".o_test_widget",
    #     start: function () {
    #         return this._super(...arguments).then(async () => {
    #         const data = await rpc("/my/route", {});
    #     });},
    # });
