$('#series').live('pagebeforecreate', function() {
  //$('#series-preview').parent().remove();

  var b = $('<a>')
    .attr('data-role', 'button')
    .attr('href', '#')
    .attr('data-icon', 'search')
    .attr('data-theme', 'e')
    .text('Orthanc Web Viewer');

  b.insertBefore($('#series-delete').parent().parent());
  b.click(function() {
    if ($.mobile.pageData) {
      var urlSearchParams = {
        "series" : $.mobile.pageData.uuid
      };
      if ("authorizationTokens" in window) {
        for (var token in authorizationTokens) {
          urlSearchParams[token] = authorizationTokens[token];
        }
      }

      window.open('../web-viewer/app/viewer.html?' + $.param(urlSearchParams));
    }
  });
});
