import { browser } from "@web/core/browser/browser";
import {
    contains,
    defineModels,
    mountView,
    onRpc,
    patchWithCleanup,
    webModels,
} from "@web/../tests/web_test_helpers";
import { mailModels } from "@mail/../tests/mail_test_helpers";
import { describe, expect, test } from "@odoo/hoot";

import {
    DocumentsModels,
    getBasicPermissionPanelData,
    getDocumentsTestServerData,
} from "./helpers/data";
import { makeDocumentsMockEnv } from "./helpers/model";
import { basicDocumentsListArch } from "./helpers/views/list";
import { getEnrichedSearchArch } from "./helpers/views/search";

describe.current.tags("desktop");

defineModels({
    ...webModels,
    ...mailModels,
    ...DocumentsModels,
});

test("Open share with view user_permission", async function () {
    onRpc("/documents/touch/accessTokenFolder1", () => true);
    const serverData = getDocumentsTestServerData();
    const { id: folder1Id, name: folder1Name } = serverData.models["documents.document"].records[0];
    patchWithCleanup(browser.navigator.clipboard, {
        writeText: async (url) => {
            expect.step("Document url copied");
            expect(url).toBe("https://localhost:8069/odoo/documents/accessTokenFolder1");
        },
    });
    await makeDocumentsMockEnv({
        serverData,
        mockRPC: async function (route, args) {
            if (args.method === "permission_panel_data") {
                expect(args.args[0]).toEqual(folder1Id);
                expect.step("permission_panel_data");
                return getBasicPermissionPanelData({
                    access_url: "https://localhost:8069/odoo/documents/accessTokenFolder1",
                });
            }
            if (args.method === "can_upload_traceback") {
                return false;
            }
        },
    });
    await mountView({
        type: "list",
        resModel: "documents.document",
        arch: basicDocumentsListArch,
        searchViewArch: getEnrichedSearchArch(),
    });
    await contains(`.o_data_row:contains(${folder1Name}) .o_list_record_selector`).click();
    await contains("button:contains(Share)").click();

    await contains(".o_clipboard_button", { timeout: 1500 }).click();
    expect.verifySteps(["permission_panel_data", "Document url copied"]);
});
