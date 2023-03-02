/**
 * Orthanc - A Lightweight, RESTful DICOM Store
 * Copyright (C) 2012-2016 Sebastien Jodogne, Medical Physics
 * Department, University Hospital of Liege, Belgium
 * Copyright (C) 2017-2020 Osimis S.A., Belgium
 *
 * This program is free software: you can redistribute it and/or
 * modify it under the terms of the GNU Affero General Public License
 * as published by the Free Software Foundation, either version 3 of
 * the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Affero General Public License for more details.
 * 
 * You should have received a copy of the GNU Affero General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 **/


// Set the default compression
var compression = 'jpeg95';
var isFirst = true;
//var compression = 'deflate';
var unsupportedMessage = 'Error: The Orthanc core does not support the decoding of this image. Make sure that you have properly installed a suitable decoder plugin (e.g. the official GDCM decoder plugin).';


// Prevent the access to IE
if(navigator.appVersion.indexOf("MSIE ") != -1)
{
  alert("Please use Mozilla Firefox or Google Chrome. Microsoft Internet Explorer is not supported.");
}


function GetAuthorizationTokensFromUrl() {
  var urlVariables = window.location.search.substring(1).split('&');
  var dict = {};

  for (var i = 0; i < urlVariables.length; i++) {
      var split = urlVariables[i].split('=');

      if (split.length == 2 && (split[0] == "token" || split[0] == "auth-token" || split[0] == "authorization")) {
        dict[split[0]] = split[1];
      }
  }
  return dict;
};

var authorizationTokens = GetAuthorizationTokensFromUrl();

/* Copy the authoziation toekn from the url search parameters into HTTP headers in every request to the Rest API.  
Thanks to this behaviour, you may specify a ?token=xxx in your url and this will be passed 
as the "token" header in every request to the API allowing you to use the authorization plugin */
$.ajaxSetup(
  {
    headers : authorizationTokens
  }
);

function ResizeCornerstone()
{
  $('#dicomImage').height($(window).height() - $('#slider').parent().height());
  var element = $('#dicomImage').get(0);
  cornerstone.resize(element, true);
}


function SetWindowing(center, width)
{
  var element = $('#dicomImage').get(0);
  var viewport = cornerstone.getViewport(element);
  viewport.voi.windowCenter = center;
  viewport.voi.windowWidth = width;
  cornerstone.setViewport(element, viewport);
  UpdateViewportInformation();
}


function SetFullWindowing()
{
  var element = $('#dicomImage').get(0);
  var viewport = cornerstone.getViewport(element);
  var image = cornerstone.getEnabledElement(element).image;

  if (image.color) {
    // Ignore color images
    return;
  }

  var minValue = image.minPixelValue;
  var maxValue = image.maxPixelValue;
  if (minValue == undefined ||
      maxValue == undefined ||
      minValue == maxValue) {
    return; 
  }

  if (image.slope != undefined && 
      image.intercept != undefined) {
    minValue = minValue * image.slope + image.intercept;
    maxValue = maxValue * image.slope + image.intercept;
  }

  viewport.voi.windowCenter = (minValue + maxValue) / 2.0;
  viewport.voi.windowWidth = (maxValue - minValue) / 2.0;
  cornerstone.setViewport(element, viewport);
  UpdateViewportInformation();
}


function SetDefaultWindowing()
{
  var element = $('#dicomImage').get(0);
  var viewport = cornerstone.getViewport(element);
  var image = cornerstone.getEnabledElement(element).image;

  viewport.voi.windowCenter = image.windowCenter;
  viewport.voi.windowWidth = image.windowWidth;
  cornerstone.setViewport(element, viewport);
  UpdateViewportInformation();
}


function SetBoneWindowing()
{
  SetWindowing(300, 2000);
}


function SetLungWindowing()
{
  SetWindowing(-600, 1600);
}


function UpdateViewportInformation()
{
  var element = $('#dicomImage').get(0);
  var viewport = cornerstone.getViewport(element);

  $('#bottomleft').text('WW/WL:' + Math.round(viewport.voi.windowWidth) + '/' + Math.round(viewport.voi.windowCenter));
  $('#bottomright').text('Zoom: ' + viewport.scale.toFixed(2) + 'x');
}


function ToggleSeriesInformation()
{
  $('#topright').toggle();
}


function ToggleInterpolation()
{
  var element = $('#dicomImage').get(0);
  var viewport = cornerstone.getViewport(element);
  if (viewport.pixelReplication === true) {
    viewport.pixelReplication = false;
  } else {
    viewport.pixelReplication = true;
  }
  cornerstone.setViewport(element, viewport);
}


function ToggleInversion()
{
  var element = $('#dicomImage').get(0);
  var viewport = cornerstone.getViewport(element);
  if (viewport.invert === true) {
    viewport.invert = false;
  } else {
    viewport.invert = true;
  }
  cornerstone.setViewport(element, viewport);
}


function DownloadInstance(instance)
{
  // http://stackoverflow.com/a/3749395/881731
  var hiddenIFrameID = 'hiddenDownloader',
  iframe = document.getElementById(hiddenIFrameID);
  if (iframe === null) {
    iframe = document.createElement('iframe');
    iframe.id = hiddenIFrameID;
    iframe.style.display = 'none';
    document.body.appendChild(iframe);
  }

  var id = instance;
  var pos = instance.indexOf('_');
  if (pos != -1) {
    // Remove the frame index (after the underscore)
    id = id.substring(0, pos);
  }

  iframe.src = '../../instances/' + id + '/file';
}


function AdjustZoom()
{
  var element = $('#dicomImage').get(0);
  cornerstone.fitToWindow(element);
}


function ZoomIn()
{
  var element = $('#dicomImage').get(0);
  var viewport = cornerstone.getViewport(element);
  viewport.scale /= 0.5;
  cornerstone.setViewport(element, viewport);
  UpdateViewportInformation();
}


function ZoomOut()
{
  var element = $('#dicomImage').get(0);
  var viewport = cornerstone.getViewport(element);
  viewport.scale *= 0.5;
  cornerstone.setViewport(element, viewport);
  UpdateViewportInformation();
}



(function (cornerstone) {
  'use strict';

  function PrintRange(pixels)
  {
    var a = Infinity;
    var b = -Infinity;

    for (var i = 0, length = pixels.length; i < length; i++) {
      if (pixels[i] < a)
        a = pixels[i];
      if (pixels[i] > b)
        b = pixels[i];
    }    

    console.log(a + ' ' + b);
  }

  function ChangeDynamics(pixels, source1, target1, source2, target2)
  {
    var scale = (target2 - target1) / (source2 - source1);
    var offset = (target1) - scale * source1;

    for (var i = 0, length = pixels.length; i < length; i++) {
      pixels[i] = scale * pixels[i] + offset;
    }    
  }


  function getPixelDataDeflate(image) {
    // Decompresses the base64 buffer that was compressed with Deflate
    var s = pako.inflate(window.atob(image.Orthanc.PixelData));
    var pixels = null;

    if (image.color) {
      var buf = new ArrayBuffer(s.length / 3 * 4); // RGB32
      pixels = new Uint8Array(buf);
      var index = 0;
      for (var i = 0, length = s.length; i < length; i += 3) {
        pixels[index++] = s[i];
        pixels[index++] = s[i + 1];
        pixels[index++] = s[i + 2];
        pixels[index++] = 255;  // Alpha channel
      }
    } else{
      var buf = new ArrayBuffer(s.length * 2); // uint16_t or int16_t

      if (image.Orthanc.IsSigned) {
        pixels = new Int16Array(buf);
      } else {
        pixels = new Uint16Array(buf);
      }

      var index = 0;
      for (var i = 0, length = s.length; i < length; i += 2) {
        var lower = s[i];
        var upper = s[i + 1];
        pixels[index] = lower + upper * 256;
        index++;
      }
    }

    return pixels;
  }


  // http://stackoverflow.com/a/11058858/881731
  function str2ab(str) {
    var buf = new ArrayBuffer(str.length);
    var pixels = new Uint8Array(buf);
    for (var i = 0, strLen=str.length; i<strLen; i++) {
      pixels[i] = str.charCodeAt(i);
    }
    return pixels;
  }

  function getPixelDataJpeg(image) {
    var jpegReader = new JpegImage();
    var jpeg = str2ab(window.atob(image.Orthanc.PixelData));
    jpegReader.parse(jpeg);
    var s = jpegReader.getData(image.width, image.height);
    var pixels = null;

    if (image.color) {
      var buf = new ArrayBuffer(s.length / 3 * 4); // RGB32
      pixels = new Uint8Array(buf);
      var index = 0;
      for (var i = 0, length = s.length; i < length; i += 3) {
        pixels[index++] = s[i];
        pixels[index++] = s[i + 1];
        pixels[index++] = s[i + 2];
        pixels[index++] = 255;  // Alpha channel
      }
    } else {
      var buf = new ArrayBuffer(s.length * 2); // uint16_t or int16_t

      if (image.Orthanc.IsSigned) {
        pixels = new Int16Array(buf);
      } else {
        pixels = new Uint16Array(buf);
      }

      var index = 0;
      for (var i = 0, length = s.length; i < length; i++) {
        pixels[index] = s[i];
        index++;
      }

      if (image.Orthanc.Stretched) {
        ChangeDynamics(pixels, 0, image.Orthanc.StretchLow, 255, image.Orthanc.StretchHigh);
      }
    }

    return pixels;
  }
  

  function getOrthancImage(imageId) {
    var result = null;

    $.ajax({
      type: 'GET',
      url: '../instances/' + compression + '-' + imageId,
      dataType: 'json',
      cache: true,
      async: false,
      success: function(image) {
        image.imageId = imageId;
        if (image.color)
          image.render = cornerstone.renderColorImage;
        else
          image.render = cornerstone.renderGrayscaleImage;

        if (isFirst) {
          if (image.Orthanc.PhotometricInterpretation == "MONOCHROME1") {
            image.invert = true;
          } else {
            image.invert = false;
          }

          isFirst = false;
        }
        
        image.getPixelData = function() {
          if (image.Orthanc.Compression == 'Deflate')
            return getPixelDataDeflate(this);

          if (image.Orthanc.Compression == 'Jpeg')
            return getPixelDataJpeg(this);

          // Unknown compression
          return null;
        }

        result = image;
      },
      error: function() {
        alert(unsupportedMessage);
        return null;
      }
    });
    
    var deferred = $.Deferred();
    deferred.resolve(result);
    return deferred;
  }

  // register our imageLoader plugin with cornerstone
  cornerstone.registerImageLoader('', getOrthancImage);

}(cornerstone));


$(document).ready(function() {
  $('#open-toolbar').button({
    icons: { primary: 'ui-icon-custom-orthanc' },
    text: false
  });

  $('#unstable').tooltip();

  var series = window.url('?series', window.location.search);
  if (series == null)
    return;

  console.log('Displaying series: ' + series);
  var instances = [ ];

  $.ajax({
    type: 'GET',
    url: '../series/' + series,
    dataType: 'json',
    cache: false,
    async: false,
    success: function(volume) {
      if (volume.Slices.length != 0) {
        instances = volume.Slices;
        $('#topright').html(volume.PatientID + '<br/>' +
                            volume.PatientName + '<br/>' +
                            volume.StudyDescription + '<br/>' +
                            volume.SeriesDescription + '<br/>');
      }
    },
    failure: function() {
      alert(unsupportedMessage);
    }
  });
  
  if (instances.length == 0)
  {
    console.log('No image in this series');
    return;
  }


  $.ajax({
    type: 'GET',
    url: '../is-stable-series/' + series,
    dataType: 'json',
    cache: false,
    async: true,
    success: function(stable) {
      if (!stable) {
        $('#unstable').show();
      }
    }
  });
  

  var currentImageIndex = 0;

  // updates the image display
  function updateTheImage(imageIndex) {
    return cornerstone.loadAndCacheImage(instances[imageIndex]).then(function(image) {
      currentImageIndex = imageIndex;
      var viewport = cornerstone.getViewport(element);
      cornerstone.displayImage(element, image, viewport);
    });
  }

  // image enable the element
  var element = $('#dicomImage').get(0);
  cornerstone.enable(element);

  // set event handlers
  /*function onImageRendered(e, eventData) {
    $('#topright').text('Render Time:' + eventData.renderTimeInMs + ' ms');
  }
  $(element).on('CornerstoneImageRendered', onImageRendered);*/

  // load and display the image
  var imagePromise = updateTheImage(0);

  // add handlers for mouse events once the image is loaded.
  imagePromise.then(function() {
    viewport = cornerstone.getViewport(element);
    UpdateViewportInformation();

    // add event handlers to pan image on mouse move
    $('#dicomImage').mousedown(function (e) {
      var lastX = e.pageX;
      var lastY = e.pageY;
      var mouseButton = e.which;

      $(toolbar).hide();

      $(document).mousemove(function (e) {
        var deltaX = e.pageX - lastX,
        deltaY = e.pageY - lastY;
        lastX = e.pageX;
        lastY = e.pageY;

        if (mouseButton == 1) {
          var viewport = cornerstone.getViewport(element);
          viewport.voi.windowWidth += (deltaX / viewport.scale);
          viewport.voi.windowCenter += (deltaY / viewport.scale);
          cornerstone.setViewport(element, viewport);
          UpdateViewportInformation();
        }
        else if (mouseButton == 2) {
          var viewport = cornerstone.getViewport(element);
          viewport.translation.x += (deltaX / viewport.scale);
          viewport.translation.y += (deltaY / viewport.scale);
          cornerstone.setViewport(element, viewport);
        }
        else if (mouseButton == 3) {
          var viewport = cornerstone.getViewport(element);
          viewport.scale += (deltaY / 100);
          cornerstone.setViewport(element, viewport);
          UpdateViewportInformation();
        }
      });

      $(document).mouseup(function (e) {
        $(document).unbind('mousemove');
        $(document).unbind('mouseup');
      });
    });

    $('#dicomImage').on('mousewheel DOMMouseScroll', function (e) {
      // Firefox e.originalEvent.detail > 0 scroll back, < 0 scroll forward
      // chrome/safari e.originalEvent.wheelDelta < 0 scroll back, > 0 scroll forward
      if (e.originalEvent.wheelDelta < 0 || e.originalEvent.detail > 0) {
        currentImageIndex ++;
        if (currentImageIndex >= instances.length) {
          currentImageIndex = instances.length - 1; 
        }         
      } else {
        currentImageIndex --;
        if (currentImageIndex < 0) {
          currentImageIndex = 0;
        }         
      }

      updateTheImage(currentImageIndex);
      $('#slider').slider("option", "value", currentImageIndex);

      //prevent page fom scrolling
      return false;
    });
  });


  $('#slider').slider({
    min: 0,
    max: instances.length - 1,
    slide: function(event, ui) {
      updateTheImage(ui.value);
    }
  });

  var toolbar = $.jsPanel({
    position: { top: 50, left: 10 },
    size: { width: 155, height: 200 },
    content: $('#toolbar-content').clone().show(),
    controls: { buttons: 'none' },
    title: '<a target="_blank" href="http://www.orthanc-server.com/"><img src="images/orthanc-logo.png" /></a>'
  });

  $('#open-toolbar').click(function() {
    toolbar.toggle();
  });

  $(toolbar).hide();

  $('.toolbar-view', toolbar).buttonset()
    .children().first().button({
      icons: { primary: 'ui-icon-info' },
      text: false
    }).click(ToggleSeriesInformation).next().button({
      icons: { primary: 'ui-icon-custom-inversion' },
      text: false
    }).click(ToggleInversion).next().button({
      icons: { primary: 'ui-icon-custom-interpolation' },
      text: false
    }).click(ToggleInterpolation).next().button({
      icons: { primary: 'ui-icon-circle-triangle-s' },
      text: false
    }).click(function() {
      DownloadInstance(instances[currentImageIndex]);
    });

  $('.toolbar-zoom', toolbar).buttonset()
    .children().first().button({
      icons: { primary: 'ui-icon-image' },
      text: false
    }).click(AdjustZoom).next().button({
      icons: { primary: 'ui-icon-zoomin' },
      text: false
    }).click(ZoomIn).next().button({
      icons: { primary: 'ui-icon-zoomout' },
      text: false
    }).click(ZoomOut);

  $('.toolbar-windowing', toolbar).buttonset()
    .children().first().button({
      icons: { primary: 'ui-icon-custom-default' },
      text: false
    }).click(SetDefaultWindowing).next().button({
      icons: { primary: 'ui-icon-custom-stretch' },
      text: false
    }).click(SetFullWindowing).next().button({
      icons: { primary: 'ui-icon-custom-lung' },
      text: false
    }).click(SetLungWindowing).next().button({
      icons: { primary: 'ui-icon-custom-bone' },
      text: false
    }).click(SetBoneWindowing);


  function SetCompression(c)
  {
    compression = c;
    cornerstone.imageCache.purgeCache();
    updateTheImage(currentImageIndex);
    cornerstone.invalidateImageId(instances[currentImageIndex]);
  }

  $('.toolbar-quality', toolbar).buttonset()
    .children().first().button({
      label: 'L'
    }).click(function() {
      SetCompression('jpeg80');
    }).next().button({
      label: 'M'
    }).click(function() {
      SetCompression('jpeg95');
    }).next().button({
      label: 'H'
    }).click(function() {
      SetCompression('deflate');
    });


  ResizeCornerstone();
  $(window).resize(function(e) {
    if (!$(e.target).hasClass('jsPanel'))  // Ignore toolbar resizing
    {
      ResizeCornerstone();
    }
  });

});
