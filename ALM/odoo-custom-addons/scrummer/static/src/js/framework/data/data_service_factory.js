"use strict";
// Copyright 2017 - 2018 Modoolar <info@modoolar.com>
// License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

odoo.define('scrummer.data_service_factory', function (require) {
    const DataService = require('scrummer.DataService');

    // Registry of custom implementations of DataService. If not defined, standard DataService will be generated.
    const custom_registry = new Map();
    const cached_data_services = new Map();

    const DataServiceFactory = {
        custom_registry,
        get(modelName, readonly) {
            if (!cached_data_services.has(modelName)) {
                const DataServiceClass = custom_registry.has(modelName) ? custom_registry.get(modelName) : DataService;
                const newDataServiceInstance = new DataServiceClass({model: modelName});
                newDataServiceInstance.setReadonly(readonly);
                cached_data_services.set(modelName, newDataServiceInstance);
            }
            return cached_data_services.get(modelName);
        }
    };
    window.DataServiceFactory = DataServiceFactory;
    return DataServiceFactory;
});
