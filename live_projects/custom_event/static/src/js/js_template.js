import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { OriginalComponent } from "@original/module/path";

// Extend the OriginalComponent to add a custom implementation

class CustomComponent extends OriginalComponent {
    setup() {
        super.setup();
        this.orm = useService("orm"); // Initialize the ORM service for data access
    }

    async someMethod(...args) {
        // Fetch a configuration value from the model to decide which implementation to use
        const [configValue] = await this.orm.read(
            'your.model',     // Model name
            [1],              // Record ID
            ['field_name']    // Field to check for custom usage

        );

        if (configValue.use_custom_js) {

            // Custom code block if custom_js is enabled

            console.log("Field is enabled..");

            // Add custom logic here as needed

        } else {

            // Fallback to the original method implementation

            return super.someMethod(...args);

        }

    }

}



// Register your component in the registry to make it available in Odoo

registry.category("views").add("custom_component", CustomComponent);

