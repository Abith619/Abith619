import { Component } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";
import { unique } from "@web/core/utils/arrays";
import { useService } from "@web/core/utils/hooks";
import { gt } from "@point_of_sale/utils";
import { ScaleCertificationDialog } from "@pos_iot/app/scale_certification_status/scale_certification_dialog";

export class ScaleCertificationStatus extends Component {
    static props = {};
    static template = "pos_iot.ScaleCertificationStatus";

    setup() {
        this.pos = useService("pos");
        this.orm = useService("orm");
        this.dialog = useService("dialog");
    }

    get certificationErrors() {
        const errors = [];
        if (this.decimalAccuracy.digits < 3) {
            errors.push(_t("Decimal accuracy is less than 3 decimal places"));
        }
        if (this.unitsOfMeasureWithLowAccuracy.length > 0) {
            errors.push(
                _t(
                    "The following units of measure have insufficient rounding accuracy: %s",
                    this.unitsOfMeasureWithLowAccuracy.map((uom) => uom.name).join(", ")
                )
            );
        }
        return errors;
    }

    get isCertified() {
        return this.certificationErrors.length === 0;
    }

    openDialog() {
        this.dialog.add(ScaleCertificationDialog, {
            errors: this.certificationErrors,
            autoFix: this.fixCertificationErrors.bind(this),
        });
    }

    async fixCertificationErrors() {
        await this.orm.call("pos.config", "fix_rounding_for_scale_certification", [
            this.unitsOfMeasureWithLowAccuracy.map((uom) => uom.id),
        ]);

        window.location.reload();
    }

    get decimalAccuracy() {
        return this.pos.models["decimal.precision"].find(
            (dp) => dp.name === "Product Unit of Measure"
        );
    }

    get unitsOfMeasureWithLowAccuracy() {
        const unitsOfMeasure = unique(
            this.pos.models["product.product"]
                .filter((product) => product.to_weight)
                .map((product) => product.uom_id)
        );
        return unitsOfMeasure.filter((uom) => gt(uom.rounding, 0.001, { decimals: 3 }));
    }
}
