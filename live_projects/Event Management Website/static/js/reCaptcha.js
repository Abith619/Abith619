document.addEventListener("DOMContentLoaded", function () {
    grecaptcha.ready(function () {
        grecaptcha.execute('6Lca6worAAAAAFnqFDFMy_2UdN1WqzEkidKgyKkj', { action: 'submit' })
            .then(function (token) {
                console.log('Google reCAPTCHA Loaded');
                console.log('reCAPTCHA token:', token);
                document.getElementById('g-recaptcha-response').value = token;

                let recaptchaContainer = document.getElementById("recaptcha-container");
                if (recaptchaContainer) {
                    recaptchaContainer.innerHTML = "";
                    grecaptcha.render(recaptchaContainer, {
                        sitekey: "6Lca6worAAAAAFnqFDFMy_2UdN1WqzEkidKgyKkj"
                    });
                } else {
                    console.error("❌ reCAPTCHA container not found!");
                }
            })
            .catch(function (error) {
                console.error("❌ reCAPTCHA error: ", error);
            });
    });
});