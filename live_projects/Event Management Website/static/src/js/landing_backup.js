import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.VideoFormDisplay = publicWidget.Widget.extend({
    selector: "#wrapwrap",
    events: {
        "click #mute_button": "_toggleMute",
    },

    start: function () {
        this._super.apply(this, arguments);
        this._setupVideoListener();
    },

  _setupVideoListener: function () {
        var video = document.querySelector("#my_video");
        var formButton = document.querySelector("#form_button");
        let titleForm = document.querySelector(".s_title_form");

        if (video) {
          if (formButton) {
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

      },

    _toggleMute: function () {
        let video = document.querySelector("#my_video");
        let muteButton = document.querySelector("#mute_button");

        if (video && muteButton) {
            video.muted = !video.muted;
            muteButton.innerHTML = video.muted ? "🔇" : "🔊";
        }
    },
});