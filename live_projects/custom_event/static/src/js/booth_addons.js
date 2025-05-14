/** @odoo-module **/
import BoothRegistration from "@website_event_booth/js/booth_register";
import { post } from "@web/core/network/http_service";
import { redirect } from "@web/core/utils/urls";
import { renderToElement } from "@web/core/utils/render";

BoothRegistration.include({
     async _onConfirmRegistrationClick(ev) {
        ev.preventDefault();
        ev.stopPropagation();

        ev.currentTarget.classList.add("disabled");
        ev.currentTarget.disabled = true;

        const formEl = this.el.querySelector("#o_wbooth_contact_details_form");
        if (this._isConfirmationFormValid(formEl)) {
            const formData = new FormData(formEl);
            const jsonResponse = await post(`/event/${encodeURIComponent(this.el.dataset.eventId)}/booth/confirm`, formData);
            if (jsonResponse.success) {
                this.el.querySelector('.o_wevent_booth_order_progress').remove();
                const boothCategoryId = this.el.querySelector('input[name=booth_category_id]').value;
                const boothRegistrationCompleteFormEl = renderToElement("event_booth_registration_complete", {
                    booth_category_id: boothCategoryId,
                    event_id: this.eventId,
                    event_name: jsonResponse.event_name,
                    contact: jsonResponse.contact,
                });
                formEl.insertAdjacentElement("afterend", boothRegistrationCompleteFormEl);
                formEl.remove();
            } else if (jsonResponse.redirect) {
                redirect(`/event/${this.el.dataset.eventId}/booth/addons-package`);
            }
            else if (jsonResponse.error) {
                this._updateErrorDisplay(jsonResponse.error);
            }
        }
        ev.currentTarget.classList.remove("disabled");
        ev.currentTarget.removeAttribute("disabled");
    },
});