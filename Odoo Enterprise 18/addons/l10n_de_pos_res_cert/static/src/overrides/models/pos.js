/** @odoo-module */

import { PosStore } from "@point_of_sale/app/store/pos_store";
import { patch } from "@web/core/utils/patch";
import { uuidv4 } from "@point_of_sale/utils";

patch(PosStore.prototype, {
    isRestaurantCountryGermanyAndFiskaly() {
        return this.isCountryGermanyAndFiskaly() && this.config.module_pos_restaurant;
    },
    //@Override
    disallowLineQuantityChange() {
        const result = super.disallowLineQuantityChange(...arguments);
        return this.isRestaurantCountryGermanyAndFiskaly() || result;
    },
    //@Override
    _updateOrder(orderResponseData, tableOrders) {
        const order = super._updateOrder(...arguments);
        if (this.isRestaurantCountryGermanyAndFiskaly() && orderResponseData.differences && order) {
            order.createAndFinishOrderTransaction(orderResponseData.differences);
        }
        return order;
    },
    //@Override
    _postRemoveFromServer(serverIds, data) {
        if (this.isRestaurantCountryGermanyAndFiskaly() && data.length > 0) {
            // at this point of the flow, it's impossible to retrieve the local order, only the ids were stored
            // therefore we create an "empty" order object in order to call the needed methods
            data.forEach(async (elem) => {
                const order = this.createNewOrder();
                await this.cancelOrderTransaction(order, elem.differences);
            });
        }
        return super._postRemoveFromServer(...arguments);
    },
    async retrieveAndSendLineDifference(order) {
        const data = await this.data.call("pos.order", "retrieve_line_difference", [
            [order.serialize({ orm: true })],
        ]);
        if (data[order.uuid].length > 0) {
            await this.sendLineDifference(order, data[order.uuid]);
        }
    },
    async cancelOrderTransaction(order, lineDifference) {
        if (lineDifference.length > 0) {
            await this.createAndFinishOrderTransaction(lineDifference);
        }
        await this.createTransaction(order);
        await this.cancelTransaction(order);
    },
    async sendLineDifference(order, difference) {
        await this.createAndFinishOrderTransaction(difference);
        order.uiState.fiskalyLinesSent = true;
    },
    async createAndFinishOrderTransaction(lineDifference) {
        const transactionUuid = uuidv4();
        if (!this.getApiToken()) {
            await this._authenticate();
        }

        lineDifference.forEach((line) => {
            line.quantity = line.qty.toString(); // Fiskaly ask this to be a string and called quantity
            line.price_per_unit = this.env.utils.roundCurrency(line.price_per_unit).toFixed(2);
        });

        const baseUrl = this.getApiUrl();
        const tssId = this.getTssId();
        const apiToken = this.getApiToken();
        const isApiV2 = this.isUsingApiV2();
        const clientId = this.getClientId();
        try {
            const activeData = { state: "ACTIVE", client_id: clientId };
            const activeResponse = await fetch(
                `${baseUrl}/tss/${tssId}/tx/${transactionUuid}${isApiV2 ? "?tx_revision=1" : ""}`,
                {
                    method: "PUT",
                    headers: {
                        Authorization: `Bearer ${apiToken}`,
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(activeData),
                }
            );

            if (!activeResponse.ok) {
                throw new Error(`Failed to activate transaction: ${activeResponse.status}`);
            }

            const finishedData = {
                state: "FINISHED",
                client_id: clientId,
                schema: {
                    standard_v1: {
                        order: { line_items: lineDifference },
                    },
                },
            };

            const finishedResponse = await fetch(
                `${baseUrl}/tss/${tssId}/tx/${transactionUuid}?${
                    isApiV2 ? "tx_revision=2" : "last_revision=1"
                }`,
                {
                    method: "PUT",
                    headers: {
                        Authorization: `Bearer ${apiToken}`,
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(finishedData),
                }
            );

            if (!finishedResponse.ok) {
                throw new Error(`Failed to finish transaction: ${finishedResponse.status}`);
            }
        } catch (error) {
            if (error.status === 401) {
                // Handle token expiration, re-authenticate, and retry
                await this._authenticate();
                return this.createAndFinishOrderTransaction(transactionUuid, lineDifference);
            }
            console.error("Error in createAndFinishOrderTransaction:", error);
            throw error; // Re-throw for higher-level error handling
        }
    },
    async syncAllOrders(options = {}) {
        if (!this.isRestaurantCountryGermanyAndFiskaly()) {
            return super.syncAllOrders(options);
        }

        const { orderToCreate, orderToUpdate } = this.getPendingOrder();
        const orders = [...orderToCreate, ...orderToUpdate];

        if (orders.length === 0) {
            return super.syncAllOrders(options);
        }

        const ordersCheckDifference = orders
            .filter((o) => !o.uiState.fiskalyLinesSent)
            .map((elem) => elem.serialize({ orm: true }));

        let differences = {};
        if (ordersCheckDifference.length > 0) {
            differences = await this.data.call("pos.order", "retrieve_line_difference", [
                ordersCheckDifference,
            ]);
        }

        let fiskalyError;
        if (Object.keys(differences).length > 0) {
            for (const orderJsonData of ordersCheckDifference) {
                if (!fiskalyError && differences[orderJsonData.uuid].length > 0) {
                    const order = this.models["pos.order"].getBy("uuid", orderJsonData.uuid);
                    try {
                        await this.sendLineDifference(order, differences[orderJsonData.uuid]);
                    } catch (error) {
                        fiskalyError = error;
                    }
                }
            }
            if (fiskalyError) {
                fiskalyError.code = "fiskaly";
                throw fiskalyError;
            }
        }

        return super.syncAllOrders(options);
    },
});
