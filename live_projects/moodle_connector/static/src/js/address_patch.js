/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.AddressMultiStep = publicWidget.Widget.extend({
    selector: '#wrap',

    start: function () {
        this._super.apply(this, arguments);

        // Only activate on the address form page
        if (window.location.pathname.includes("/shop/address")) {
            console.log("✅ Multi-step form active on /shop/address");

            const form = document.querySelector("form#address_form, form.oe_website_sale");
            if (!form) {
                console.warn("⚠️ No address form found, skipping multistep initialization");
                return;
            }

            // Identify major form sections
            const sections = form.querySelectorAll(
                ".Personal, .Academic, .Program, .Faith, .Online, .Additional, .Document, .Consents"
            );

            if (!sections.length) {
                console.warn("⚠️ No custom form sections found.");
                return;
            }

            console.log(`✅ Found ${sections.length} form sections for multi-step logic.`);
    
        }
    },
});
