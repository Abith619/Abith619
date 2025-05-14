document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.product-demo');

    buttons.forEach(function (button) {
      button.addEventListener('click', function () {
        const productdemo = this.getAttribute('productdemo');

        setTimeout(() => {
          const inputField = document.getElementById('productdemo');
          if (inputField) {
            inputField.value = productdemo;
          }

          const submitButtons = document.querySelectorAll('.product-demo');
          submitButtons.forEach(function (submitBtn) {
            submitBtn.addEventListener('click', function (e) {
              const name = document.querySelector('input[name="text-555"]');
              const email = document.querySelector('input[name="email-555"]');
              const phone = document.querySelector('input[name="tel-555"]');

              if (!name.value.trim() || !email.value.trim()) {
                e.preventDefault(); // stop form submission
                alert("Please enter the required field");
                return;
              }

        // Api Start
        const data = {
          first_name: name.value.trim(),
          last_name: "",
          email: email.value.trim(),
          company: "",
          message: "",
          phone: phone.value.trim(),
          form_from:productdemo
        };

        // Send data via POST
        fetch('https://bws.binarywavesolutions.com/api/bws_lead', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        })
        .then(response => {
          if (response.ok) {
            alert("Demo booked successfully!");
          } else {
            alert("Failed to book demo. Please try again.");
          }
        })
        .catch(error => {
          console.error("Error:", error);
          alert("Error submitting form.");
        });
             });
          });
        }, 1000);
      });
    });
  });