import base64
from odoo import http
from odoo.http import request
from dicomweb_client.api import DICOMwebClient, DICOMfileClient, DICOMClient
import pydicom
from pydicom.data import get_testdata_file
import matplotlib.pyplot as plt

class MyController(http.Controller):
    
    @http.route('/dicom/image', type='http', auth='public')
    def fetch_dicom_image(self, **kw):

        filename = get_testdata_file("CT_small.dcm")
        dataset = pydicom.dcmread(filename, force=True)
        plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
        plt.show()
        image_data = plt.show()

        # with open('/basic_dicom/static/cornerstone.js', 'rb') as f:
        #     cornerstone_js = f.read()
        
        # cornerstone_js_id = http.request.env['ir.attachment'].create({
        #     'datas': cornerstone_js,
        #     'datas_fname': 'cornerstone.js',
        #     'mimetype': 'application/javascript'
        # }).id
        # cornerstone_css_id = http.request.env['ir.attachment'].create({
        #     'datas': cornerstone_css,
        #     'datas_fname': 'cornerstone.css',
        #     'mimetype': 'text/css'
        # }).id

        # http.request.env['web.assets_backend']._load_asset('cornerstone.js')
        return http.request.render('basic_dicom.my_template_dicom', {'image_data': image_data })
