import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("test_partial_quantity_check_fail", { steps: () => [
    {
        trigger: 'footer.o_barcode_control button.o_check_quality',
        run: 'click',
    },
    {
        trigger: '.modal-footer button.btn-danger:contains("fail")',
        run: 'click',
    },
    {
        trigger: '.modal-body input.o_input[id="qty_failed_0"]',
        run: 'edit 3'
    },
    {
        trigger: '.modal-body span.o_selection_badge:contains("WH/Stock/Section 1")',
        run: 'click'
    },
    {
        trigger: 'footer.modal-footer button.btn-primary:contains("Confirm")',
        run: 'click'
    },
    {
        trigger: 'body:not(:has(.modal))',
    },
    {
        trigger: 'header.o_barcode_header button.o_exit',
        run: 'click',
    }
]});

registry.category("web_tour.tours").add("test_operation_quality_check_barcode", {
    steps: () => [
        {
            trigger: ".o_button_operations",
            run: "click",
        },
        {
            trigger: ".o_barcode_picking_type:has(.o_kanban_record_title:contains('Receipts'))",
            run: "click",
        },
        {
            trigger: "button.o-kanban-button-new",
            run: "click",
        },
        {
            trigger: ".o_barcode_lines",
            run: "scan product1",
        },
        {
            trigger: ".fa-pencil",
            run: "click",
        },
        {
            trigger: ".o_digipad_increment",
            run: "click",
        },
        {
            trigger: ".o_save",
            run: "click",
        },
        {
            trigger: ".o_barcode_lines",
            run() {},
        },
        {
            trigger: ".o_barcode_lines",
            run: "scan product2",
        },
        {
            trigger:
                ".o_barcode_line:has(.o_barcode_line_title:contains(product2)) button.o_add_quantity",
            run: "click",
        },
        {
            trigger: ".o_validate_page",
            run: "click",
        },
        {
            trigger: ".modal-content:has(.modal-header:contains(product 1)) button[name=do_pass]",
            run: "click",
        },
        {
            trigger: ".modal-content:has(.modal-header:contains(product 2)) button[name=do_fail]",
            run: "click",
        },
        {
            trigger: ".o_notification_bar.bg-success",
            run() {},
        },
    ],
});

registry.category("web_tour.tours").add("test_operation_quality_check_delivery_barcode", {
    steps: () => [
        {
            trigger: ".o_button_operations",
            run: "click",
        },
        {
            trigger: ".o_barcode_picking_type:has(.o_kanban_record_title:contains('Delivery'))",
            run: "click",
        },
        {
            trigger: "button.o-kanban-button-new",
            run: "click",
        },
        {
            trigger: ".o_barcode_lines",
            run: "scan product1",
        },
        {
            trigger: ".fa-pencil",
            run: "click",
        },
        {
            trigger: ".o_digipad_increment",
            run: "click",
        },
        {
            trigger: ".o_save",
            run: "click",
        },
        {
            trigger: ".o_barcode_lines",
            run() {},
        },
        {
            trigger: ".o_barcode_lines",
            run: "scan product2",
        },
        {
            trigger:
                ".o_barcode_line:has(.o_barcode_line_title:contains(product2)) button.o_add_quantity",
            run: "click",
        },
        {
            trigger: ".o_validate_page",
            run: "click",
        },
        {
            trigger: ".modal-content:has(.modal-header:contains(product 1)) button[name=do_pass]",
            run: "click",
        },
        {
            trigger: ".modal-content:has(.modal-header:contains(product 2)) button[name=do_fail]",
            run: "click",
        },
        {
            trigger: ".o_notification_bar.bg-success",
            run() {},
        },
    ],
});
