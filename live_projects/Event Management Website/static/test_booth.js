function _boothChange() {
    let checkedRadio = document.querySelector('input[name="booth_category_id"]:checked');
    let checkboxes = document.querySelectorAll('input[name="event_booth_ids"]');

    if (!checkedRadio || checkboxes.length === 0) return;

    setTimeout(() => {
        function processCheckboxes() {
            setTimeout(() => {
                let checkboxes = document.querySelectorAll('input[name="event_booth_ids"]');

                if (checkboxes.length > 0) {
                    checkboxes.forEach(checkbox => (checkbox.checked = false));

                    checkboxes[0]?.click();
                }
            }, 500);
        }
        if (checkboxes.length > 0) {
            processCheckboxes();
            return;
        }
    });

    setTimeout(() => {
        checkboxes[0].click();
    }, 500);
}


function _setupVideoListener() {
    let video = document.querySelector("#my_video");
    let formButton = document.querySelector("#form_button");
    let titleForm = document.querySelector(".s_title_form");

    console.log("JS Loaded");

    if (video && formButton && titleForm) {
        setTimeout(() => {
            titleForm.style.display = "block";
            formButton.style.display = "block";
            formButton.style.visibility = "visible";
            formButton.style.opacity = "1";
            formButton.style.transform = "translateX(0)";
            formButton.style.animation = "slideInFromRight 0.5s ease-out forwards";
        }, 3000);

        setTimeout(() => {
            window.location.href = "/coming-soon";
        }, 7000);
    }
}

function _toggleMute() {
    let video = document.querySelector("#my_video");
    let muteButton = document.querySelector("#mute_button");

    console.log("Mute button clicked");

    if (video && muteButton) {
        video.muted = !video.muted;
        muteButton.innerHTML = video.muted ? "🔇" : "🔊";
    }
}
