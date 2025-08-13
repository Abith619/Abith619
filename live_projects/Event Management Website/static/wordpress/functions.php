function handle_my_form_submission() {
    check_ajax_referer('my_form_nonce', 'security');

    parse_str($_POST['form_data'], $form);

    // Do something with the form data
    // Example: $name = sanitize_text_field($form['name']);

    wp_send_json_success(['message' => 'Form submitted successfully!']);
}
add_action('wp_ajax_submit_my_form', 'handle_my_form_submission');
add_action('wp_ajax_nopriv_submit_my_form', 'handle_my_form_submission');
