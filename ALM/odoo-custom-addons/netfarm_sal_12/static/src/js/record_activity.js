odoo.define('netfarm_sal_12.RecordActivity', function (require) {
"use strict";
var core = require('web.core');
var qweb = core.qweb;
var _lt = core._lt;
var _t = core._t;
var Widget = require('web.Widget');
var rpc = require('web.rpc');

var RecordActivity = Widget.extend({
    template: "netfarm_sal_12.record_activity",
    events: {
        'click .card-open': 'open_form',
        'click .create_sal': 'create_sal'
    },
    init: function (parent, data, data_model) {
        this._super(parent);
        this.data = data;
        this.data_model = data_model;
    },
    start: function(){
        var self = this;
        /* initialize draggable */
        self.$el.draggable({
            opacity: 1,
            helper: "clone",
            scroll: false,
            zIndex: 999999999,
            containment:"window",
            appendTo: "body",
            start: function(e, ui){
                $(e.target).css('cursor', 'grabbing');
            },
            revert: 0,
            stop: function(e, ui){
                $(e.target).css('cursor', 'grab');
                self._dragStop(ui);
            }
        });
    },
    _dragStop: function(ui){
        var self = this;
        var border = ui.offset.left;
        var last_column = false;
        self.trigger_up('choose_column_drag', {'border': border, 'record': self});
    },
    open_form: function(e){
        var self = this;
        var res_id = self.data.id;
        var action = {
            name: self.data.display_name,
            views: [[false, 'form']],
            view_type: 'form',
            view_mode: 'form',
            res_model: self.data_model,
            type: 'ir.actions.act_window',
            target: 'new',
            res_id: res_id,
            flags:{'initial_mode': 'view'}
        };
        self.do_action(action);
    },
    create_sal: function(e){
        var self = this;
        var res_id = self.data.id;
        var ref = self.data_model +','+ res_id
        var em = self.trigger_up('get_employee');
        var action = {
            name: _t('Create Sal'),
            views: [[false, 'form']],
            view_type: 'form',
            view_mode: 'form',
            res_model: 'create.sal',
            type: 'ir.actions.act_window',
            target: 'new',
            context : {
                'default_employee_id': em.data.employee,
                'default_ref_doc_id': ref
            }
        };
        self.do_action(action, {
            on_close: function(){
                self.trigger_up('ultra_reload');
            }
        });
    },
});

return RecordActivity;
});