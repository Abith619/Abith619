/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { post } from "@web/core/network/http_service";
import { redirect } from "@web/core/utils/urls";
import { renderToElement } from "@web/core/utils/render";
import '@website_event_booth/js/booth_register';

publicWidget.registry.boothRegistration.include({
    async _onConfirmRegistrationClick(ev) {
        ev.preventDefault();
        ev.stopPropagation();

        ev.currentTarget.classList.add("disabled");
        ev.currentTarget.disabled = true;

        const formEl = this.el.querySelector("#o_wbooth_contact_details_form");
        console.log("formEl")
        if (this._isConfirmationFormValid(formEl)) {
            const formData = new FormData(formEl);
            const jsonResponse = await post(`/event/${encodeURIComponent(this.el.dataset.eventId)}/booth/confirm`, formData);
            console.log("_isConfirmationFormValid")
            if (jsonResponse.success) {
                console.log("success")
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
            } else if (jsonResponse.error) {
                console.log("error")
                this._updateErrorDisplay(jsonResponse.error);
            } else if (jsonResponse.redirect) {
              console.log("redirect")
                redirect(`/event/${this.el.dataset.eventId}/booth/addons-package`);
            }
        }
        console.log("no if")
        ev.currentTarget.classList.remove("disabled");
        ev.currentTarget.removeAttribute("disabled");
    },
});
