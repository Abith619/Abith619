import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";
import { _t } from "@web/core/l10n/translation";
import { SelectionPopup } from "@point_of_sale/app/utils/input_popups/selection_popup";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

patch(PosStore.prototype, {
    async setup() {
        await super.setup(...arguments);
        this.setAllTotalDueOfPartners(this.models["res.partner"].getAll());
    },
    getPartnerCredit(partner) {
        const order = this.get_order();
        const partnerInfos = {
            totalDue: 0,
            totalWithCart: order ? order.get_total_with_tax() : 0,
            creditLimit: 0,
            useLimit: false,
            overDue: false,
        };

        if (!partner) {
            return partnerInfos;
        }

        if (partner.parent_name) {
            const parent = this.models["res.partner"].find((p) => p.name === partner.parent_name);

            if (parent) {
                partner = parent;
            }
        }

        partnerInfos.totalDue = partner.total_due || 0;
        partnerInfos.totalWithCart += partner.total_due || 0;
        partnerInfos.creditLimit = partner.credit_limit || 0;
        partnerInfos.overDue = partnerInfos.totalWithCart > partnerInfos.creditLimit;
        partnerInfos.useLimit =
            this.company.account_use_credit_limit &&
            partner.credit_limit > 0 &&
            partnerInfos.overDue;

        return partnerInfos;
    },
    async refreshTotalDueOfPartner(partner) {
        const total_due = await this.data.call("res.partner", "get_total_due", [
            partner.id,
            this.config.currency_id.id,
        ]);
        partner.total_due = total_due;
        this.deviceSync.dispatch({ "res.partner": [partner] });
        return [partner];
    },
    async setAllTotalDueOfPartners(partners) {
        const partners_total_due = await this.data.call("res.partner", "get_all_total_due", [
            partners.map((p) => p.id),
            this.config.currency_id.id,
        ]);
        for (const partner of partners) {
            partner.total_due = partners_total_due[partner.id];
        }
        return [partners];
    },
    async settleCustomerDue(partner) {
        const payLaterPM = this.config.payment_method_ids.find((pm) => pm.type === "pay_later");
        if (!payLaterPM) {
            this.dialog.add(AlertDialog, {
                title: _t("Missing Payment Method"),
                body: _t(
                    "Please contact your administrator to configure a payment method for settling dues or making deposits."
                ),
            });
            return;
        }
        const updatedDue = await this.refreshTotalDueOfPartner(partner);
        const totalDue = updatedDue ? updatedDue[0].total_due : partner.total_due;
        const paymentMethods = this.config.payment_method_ids.filter(
            (method) => method.type != "pay_later"
        );
        const selectionList = paymentMethods.map((paymentMethod) => ({
            id: paymentMethod.id,
            label: paymentMethod.name,
            item: paymentMethod,
        }));
        this.dialog.add(SelectionPopup, {
            title: _t("Select the payment method to settle the due"),
            list: selectionList,
            getPayload: (selectedPaymentMethod) => {
                // Reuse an empty order that has no partner or has partner equal to the selected partner.
                let newOrder;
                const emptyOrder = this.get_open_orders().find(
                    (order) =>
                        order.lines.length === 0 &&
                        order.payment_ids.length === 0 &&
                        (!order.partner || order.partner.id === partner.id)
                );
                if (emptyOrder) {
                    newOrder = emptyOrder;
                    // Set the empty order as the current order.
                    this.set_order(newOrder);
                } else {
                    newOrder = this.add_new_order();
                }
                const payment = newOrder.add_paymentline(selectedPaymentMethod);
                newOrder.is_settling_account = true;
                payment.set_amount(totalDue);
                newOrder.set_partner(partner);
                this.showScreen("PaymentScreen", { orderUuid: this.selectedOrderUuid });
            },
        });
    },
});
