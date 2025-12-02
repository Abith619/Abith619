/** @odoo-module */

import { FormRenderer } from "@web/views/form/form_renderer";
import { patch } from "@web/core/utils/patch";

patch(FormRenderer.prototype, {
    async renderView() {
        await this._super(...arguments);

        console.log("Form View Rendered!");

        // Only run on PowerBI models
        const model = this.props.record.resModel;
        if (!["pbi.report", "pbi.dashboard"].includes(model)) {
            return;
        }

        const data = this.props.record.data;
        const models = window["powerbi-client"].models;

        const embedConfig = {
            type: "report",
            id: data.report_id,
            accessToken: data.access_token,
            embedUrl: data.embedurl,
            permissions: models.Permissions.All,
            tokenType: models.TokenType.Aad,
            settings: {
                panes: {
                    filters: {
                        visible: data.filters_visible || false,
                    },
                },
            },
        };

        const reportContainer = this.el.querySelector("#reportContainer");

        if (reportContainer) {
            const report = powerbi.embed(reportContainer, embedConfig);

            report.on("loaded", () => {
                console.log("Power BI report loaded!");
            });

            report.on("error", (event) => {
                console.error("Power BI report error:", event.detail);
            });
        }
    },
});
