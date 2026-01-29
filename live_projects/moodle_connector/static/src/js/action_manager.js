/** @odoo-module **/

import { registry } from "@web/core/registry";
import { download } from "@web/core/network/download";

registry.category("ir.actions.report handlers").add("csv", async (action) => {
    if (action.report_type === "csv") {
        await download({
            url: "/csv_reports",
            data: action.data,
        });
        return true;
    }
});
