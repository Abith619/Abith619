/** @odoo-module **/
import { registry } from "@web/core/registry";

try {
    registry.category("components").remove("html_editor.UploadProgressToast");
    console.log("🚫 UploadProgressToast disabled successfully");
} catch (err) {
    console.warn("UploadProgressToast disable skipped:", err);
}
