from odoo import api, fields, models, _
import base64, io
from odoo.exceptions import  ValidationError
import pydicom
from pydicom.data import get_testdata_file
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image
import subprocess
import os
from dicomweb_client.api import DICOMwebClient, DICOMfileClient
from dicomweb_client.ext.gcp.session_utils import create_session_from_gcp_credentials
from dicomweb_client.ext.gcp.uri import GoogleCloudHealthcareURL

class dicom_view(models.Model):
    _name = 'dicom.view'
    _rec_name = 'report_name'

    report_name = fields.Char(string='Report Name')
    upload_dcm = fields.Many2many('ir.attachment', string='Upload Report')

    def button_field_onchange(self):
        instance = DICOMwebClient.retrieve_instance(
        study_instance_uid='1.2.826.0.1.3680043.8.1055.1.20111103111148288.98361414.79379639',
        series_instance_uid='1.2.826.0.1.3680043.8.1055.1.20111103111208937.49685336.24517034',
        sop_instance_uid='1.2.826.0.1.3680043.8.1055.1.20111103111208937.40440871.13152534'
    )

        # client = DICOMwebClient(url="https://mydicomwebserver.com")
        # client = DICOMfileClient("/path/to/directory")
        # session = create_session_from_gcp_credentials()

        # url = GoogleCloudHealthcareURL(
        #     project_id='my-project',
        #     location='us-east4',
        #     dataset_id='my-dataset',
        #     dicom_store_id='my-store'
        # )

        # client = DICOMwebClient(
        #     url=str(url),
        #     session=session
        # )
        # Slicer.main()
        # os.chdir(os.getcwd())
        # raise ValidationError(a)
        # file_path = os.path.join('/opt/odoo14/Slicer/', 'Slicer')
        # with open(file_path, 'r') as f:
        #     pass
            # subprocess.run(['Slicer'])
        # subprocess.run(['chmod','+x',"/opt/odoo14/Slicer/Slicer"])
        # return {'type': 'ir.actions.act_window',
        #         'view_mode':'form',
        #         # 'tag': 'reload',
        #         }

    # def open_slicer(self):
    #     return web.Browser(url='https://slicer.org').open_new()

    # def generate_plot(self):
        # raise ValidationError('Hi')
        # Generate some data
        # x = [1, 2, 3, 4]
        # y = [10, 20, 30, 40]

        # # Create a figure and axes
        # fig, ax = plt.subplots()

        # # Plot the data
        # ax.plot(x, y)

        # # Save the figure to a temporary buffer
        # buf = io.BytesIO()
        # plt.savefig(buf, format='png')
        # buf.seek(0)

        # # Create an Image object
        # image = Image.open(buf)

        # # Save the image to a buffer
        # image_buf = io.BytesIO()
        # image.save(image_buf, format='png')
        # image_buf.seek(0)

        # # Return the image buffer
        # return image_buf

    # def open_viewer(self):

    #     filename = get_testdata_file("CT_small.dcm")

    #     ds = pydicom.dcmread(filename, force=True)

    #     plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
        
    #     return plt.show()

    

    # def plot_button_clicked(self):
    #     def plot_data(data):
    #         x = [1, 2, 3]
    #         y = data
    #         plt.plot(x, y)

    #     data = [1, 2, 3]

    #     root = tk.Tk()
    #     figure = plt.figure()
    #     canvas = FigureCanvasTkAgg(figure, root)

    #     plot_data(data)

    #     canvas.get_tk_widget().pack()
    #     root.mainloop()

        # matplotlib.use('Agg')

        # # Create the Matplotlib plot
        # fig = plt.figure()
        # ax = fig.add_subplot(111)
        # ax.plot([1, 2, 3, 4])

        # # Show the plot in a separate window
        # return plt.show()
        
        # filename = get_testdata_file("CT_small.dcm")
        # ds = pydicom.dcmread(filename, force=True)
        # FieldBinary = self.env['dicom.view']._fields[self.upload_dcm]
        # raise ValidationError(FieldBinary)
        # FieldBinary.write({'upload_dcm': ds})
        # image_data = ds.pixel_array

        # plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
        # plt.show()
        # matplotlib.use('Agg')

        # fig = plt.figure()
        # ax = fig.add_subplot(111)
        # ax.plot([1, 2, 3, 4])
        # plt.show()

        # os.chmod('plot.png', 0o777)
        
        # # Draw the plot to a canvas
        # fig.savefig('plot.png')
        # canvas = FigureCanvas(fig)

        # # Get the raw image data from the canvas
        # image_data = canvas.buf

        # # Save the image data to a PNG file
        # with open('plot.png', 'wb') as f:
        #     f.write(image_data)

        # reader = vtk.vtkDICOMImageReader()
        # reader.SetFileName('image.dcm')
        # reader.Update()

        # # Set up the image viewer
        # viewer = vtk.vtkImageViewer()
        # viewer.SetInputConnection(reader.GetOutputPort())

        # # Set the size of the window
        # viewer.SetSize(800, 600)

        # # Set the window title
        # viewer.SetWindowName('DICOM Image')

        # # Show the image
        # viewer.Render()

        # # Start the event loop
        # viewer.Start()
