jQuery(document).ready(function($) {
    $('#my-form').on('submit', function(e) {
        e.preventDefault();

        const formData = $(this).serialize();

        $.ajax({
            url: my_ajax_object.ajax_url,
            method: 'POST',
            data: {
                action: 'submit_my_form',
                security: my_ajax_object.nonce,
                form_data: formData
            },
            success: function(response) {
                alert('Success: ' + response.data.message);
            },
            error: function(xhr) {
                alert('Error: ' + xhr.responseText);
            }
        });
    });
});
