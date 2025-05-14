import { patch } from "@web/core/utils/patch";
import { PosOrder } from "@point_of_sale/app/models/pos_order";

patch(PosOrder.prototype, {
    // @Override
    set_to_invoice(to_invoice) {
        if (this.is_settling_account && this.lines.length === 0) {
            super.set_to_invoice(false);
        } else {
            super.set_to_invoice(to_invoice);
        }
    },
});
