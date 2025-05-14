import { patch } from "@web/core/utils/patch";
import { PosStore, posService } from "@point_of_sale/app/store/pos_store";
import { isFiscalPrinterActive, isFiscalPrinterConfigured } from "./helpers/utils";

patch(posService, {
    dependencies: [...posService.dependencies, "epson_fiscal_printer"],
});

patch(PosStore.prototype, {
    async setup(env, { epson_fiscal_printer }) {
        await super.setup(...arguments);
        if (isFiscalPrinterActive(this.config)) {
            const { it_fiscal_printer_https, it_fiscal_printer_ip } = this.config;
            this.fiscalPrinter = epson_fiscal_printer(
                it_fiscal_printer_https,
                it_fiscal_printer_ip
            );
            this.fiscalPrinter.getPrinterSerialNumber().then((sn) => {
                this.config.it_fiscal_printer_serial_number = sn;
            });
        }
    },
    getSyncAllOrdersContext(orders, options = {}) {
        const context = super.getSyncAllOrdersContext(orders, options);
        if (isFiscalPrinterActive(this.config)) {
            // No need to slow down the order syncing by generating the PDF in the server.
            // The invoice will be printed by the fiscal printer.
            context["generate_pdf"] = false;
        }
        return context;
    },
    // override
    async printReceipt() {
        if (!isFiscalPrinterActive(this.config)) {
            return super.printReceipt(...arguments);
        }

        this.fiscalPrinter.printDuplicateReceipt();
    },

    // EXTENDS 'point_of_sale'
    prepareProductBaseLineForTaxesComputationExtraValues(product, p = false) {
        const extraValues = super.prepareProductBaseLineForTaxesComputationExtraValues(product, p);
        extraValues.l10n_it_epson_printer = isFiscalPrinterConfigured(this.config);
        return extraValues;
    },
});
