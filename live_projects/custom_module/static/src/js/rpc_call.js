/** @odoo-module **/
    import publicWidget from "@web/legacy/js/public/public_widget";
    import { rpc } from "@web/core/network/rpc";
    import { onWillStart } from "@odoo/owl";

    publicWidget.registry.TestRpcController = publicWidget.Widget.extend({
        selector: ".o_test_widget",
        start: function () {
            return this._super(...arguments).then(async () => {
            const data = await rpc("/my/route", {});
        });},
    });
