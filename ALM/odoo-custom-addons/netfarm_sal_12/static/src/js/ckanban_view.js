odoo.define('web.cKanbanView', function (require) {
"use strict";
var KanbanView = require('web.KanbanView');

/* MY CUSTOM CKANBAN */
var cKanbanModel = require('netfarm_sal_12.cKanbanModel');
var cKanbanRenderer = require('netfarm_sal_12.cKanbanRenderer');
var cKanbanController = require('netfarm_sal_12.cKanbanController');

var cKanbanView = KanbanView.extend({
    config: _.extend({}, KanbanView.prototype.config, {
        Model: cKanbanModel,
        Renderer: cKanbanRenderer,
        Controller: cKanbanController,
    }),
});
var viewRegistry = require('web.view_registry');
viewRegistry.add('ckanban_view', cKanbanView);
});