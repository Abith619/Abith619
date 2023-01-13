import cornerstone from 'cornerstone-core';
import dicomweb from 'dicomweb-client';

odoo.define('basic_dicom', function (require) {
    'use strict';
    var core = require('web.core');
    var Widget = require('web.Widget');
    var myModule = require('./opt/odoo14/node_modules/cornerstone-core');
    var cornerstone = require('cornerstone-core');
    var dicomweb = require('dicomweb-client');
    const imageId = cornerstoneFileImageLoader.fileManager.add(file);
    var cornerstoneWADOImageLoader = require('cornerstone-wado-image-loader');

    var DicomViewer = Widget.extend({
        template: 'my_template_dicom',
        start: function open_viewer() {
            var element = $('#viewer')[0];
            cornerstone.enable(element);
            var config = {
                server: 'https://pydicom.mo.vc/dicom/image',
                imageId: 'wado?requestType=WADO&studyUID=1.2.3.4&seriesUID=5.6.7.8&objectUID=9.10.11.12',
                studyInstanceUid: '1.2.3.4',
                // seriesInstanceUid: '5.6.7.8'
            };
            var imageId = dicomweb.getImageId(config);
            this._super.apply(this, arguments);
            var element = document.getElementById("dicom-viewer");
            cornerstone.enable(element);
            cornerstone.loadImage("data:image/jpeg;base64,{{ image_data }}").then(function(image) {
                cornerstone.displayImage(element, image);
            });
        },
    });
    core.action_registry.add('basic_dicom.my_template_dicom', DicomViewer);
});
