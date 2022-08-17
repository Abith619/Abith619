odoo.define('netfarm_sal_12.cKanbanController', function (require) {
"use strict";
var KanbanController = require('web.KanbanController');
var core = require('web.core');
var qweb = core.qweb;
var _lt = core._lt;
var _t = core._t;
var session = require('web.session');
var EmployeeBlock = require('netfarm_sal_12.EmployeeBlock');
var ActivityBlock = require('netfarm_sal_12.ActivityBlock');
var HourBlock = require('netfarm_sal_12.HourBlock');
var rpc = require('web.rpc');
var Dialog = require('web.Dialog');

var cKanbanController = KanbanController.extend({
    start: function () {
        this.model.employee_block = new EmployeeBlock(this);
        this.model.activity_block = new ActivityBlock(this);
        this.get_selected_employee();
        this.model.employee_block.prependTo(this.$el);
        this.model.activity_block.prependTo(this.$el);
        var res = this._super();
        return res;
    },
    custom_events: _.extend({}, KanbanController.prototype.custom_events, {
        change_employee : '_change_employee',
        choose_column_drag: '_choose_column_drag',
        ckanban_alive: '_ckanban_alive',
        get_employee: '_get_employee',
        load_hour_blocks: '_load_hour_blocks',
        reload_hour_block:'_reload_hour_block',
        ultra_reload: '_ultra_reload'
    }),
    _ultra_reload: function(e){
        var self = this;
        self.reload().then(function(){self._load_hour_blocks()});
    },
    _ckanban_alive: function(e){
        e.data = {'alive': 1};
        return e;
    },
    _get_employee: function(e){
        e.data = {'employee': this.model.employee_block.selected_employee};
        return e;
    },
    _onReload: function (event) {
        event.stopPropagation(); // prevent other controllers from handling this request
        var data = event && event.data || {};
        var handle = data.db_id;
        if (handle) {
            // reload the relational field given its db_id
            this.model.reload(handle).then(this._confirmSave.bind(this, handle));
        } else {
            // no db_id given, so reload the main record
            this.reload({
                fieldNames: data.fieldNames,
                keepChanges: data.keepChanges || false,
            });
        }
        this._load_hour_blocks();
    },
    _load_hour_blocks: function(e){
        var self = this;
        _.each(this.model.employee_block.hours, function(h, key){
            var widget = self.renderer.widgets[key];
            var duration = 0;
            _.each(widget.records, function(record){
                duration = duration + record.recordData.duration;
            });
            widget.hour_block = new HourBlock(widget, moment(widget.title, 'DD MMM YYYY').weekday(), h, duration);
            widget.hour_block.prependTo(widget.$el);
        });
    },
    _reload_hour_block: function(){
        _.each(this.renderer.widgets, function(widget){
            var duration = 0;
            _.each(widget.records, function(record){
                duration = duration + record.recordData.duration;
            });
            widget.hour_block.total_assigned = duration;
            widget.hour_block.reload();
            widget.hour_block.style();
        });

    },
    renderButtons: function($node) {
        var self = this;
        this.$buttons = $(qweb.render("netfarm_sal_12.buttons", {'widget': this}));
        this.$buttons.on('click', 'button.o-kanban-button-new', function () {
                /* open transient model create.sal */
                var action = {
                    name: _t('Create Sal'),
                    views: [[false, 'form']],
                    view_type: 'form',
                    view_mode: 'form',
                    res_model: 'create.sal',
                    type: 'ir.actions.act_window',
                    target: 'new',
                    context : {
                        'default_employee_id': self.model.employee_block.selected_employee
                    }
                };
                self.do_action(action, {
                    on_close: function(){
                        self.reload().then(function(){self._load_hour_blocks()});
                    }
                });
            });
        this.$buttons.on('click', 'button.o_ckanban_button_next', function(){
            var next_week = self.model.curr.add(1, 'weeks');
            self.model.curr = next_week;
            self.model.week = self.model.get_week();
            var remove = self.remove_domain('date');
            var domain = self.get_date_domain();
            self.searchView.updateFilters(domain, remove);
            self.reload().then(function(){self._load_hour_blocks()});
        });
        this.$buttons.on('click', 'button.o_ckanban_button_prev', function(){
            var prev_week = self.model.curr.subtract(1, 'weeks');
            self.model.curr = prev_week;
            self.model.week = self.model.get_week();
            var remove = self.remove_domain('date');
            var domain = self.get_date_domain();
            self.searchView.updateFilters(domain, remove);
            self.reload().then(function(){self._load_hour_blocks()});
        });
        this.$buttons.on('click', 'button.o_ckanban_button_today', function(){
            var prev_week = moment().startOf('week');
            self.model.curr = prev_week;
            self.model.week = self.model.get_week();
            var remove = self.remove_domain('date');
            var domain = self.get_date_domain();
            self.searchView.updateFilters(domain, remove);
            self.reload().then(function(){self._load_hour_blocks()});
        });
        this._updateButtons();
        this.$buttons.appendTo($node);
    },
    get_date_domain: function(){
        var curr = this.model.curr;
        var new_date = moment(curr).add(6, 'days');
        var domain = [];
        domain.push({
            'domain': [['date', '>=', curr.format('YYYY-MM-DD')], ['date', '<=', new_date.format('YYYY-MM-DD')]],
            'help': _t('Date between ') + curr.format('DD MMM YYYY') + ' and ' + new_date.format('DD MMM YYYY')}
        );
        return domain;
    },
    remove_domain: function(field){
        /* ritorna i domini da togliere dalla search_view
        se field è presente nel dominio */
        var self = this;
        var remove = [];
        _.each(this.searchView.query.models, function(q){
            var tuple = q.attributes.values[0].value.attrs.domain;
            if (tuple.indexOf(field) >= 0){
                remove.push(q);
            }
        });
        return remove;
    },
    get_selected_employee: function(){
        // return selected employee from domain
        var self = this;
        var user = session.uid
        var new_domain = ['user_id', '=', user];
        var datas = self.searchView.build_search_data();
        var domain = datas.domains;
        _.each(domain, function(tuple){
            if (tuple[0].indexOf("employee_id") >= 0){
                var spl = tuple[0].split('.');
                new_domain = ['id', '=', tuple[2]]
                if (spl.length > 1){
                    spl.shift();
                    new_domain = [spl.join('.'), tuple[1], tuple[2]];
                }
            }
        });
        this.model.employee_block.domain_selected_employee = new_domain;
    },
    _change_employee: function(employee){
        var self = this;
        var domain = [];
        var remove = this.remove_domain('employee_id');
        domain.push({
            'domain': [['employee_id', '=', parseInt(employee.data.employee)]],
            'help': _('Employee is ') + employee.data.name}
        );
        this.searchView.updateFilters(domain, remove);
        self.reload().then(function(){self._load_hour_blocks()});
    },
    _choose_column_drag: function(e){
        /*
        sceglie la colonna in base al bordo sinistro del drag.
        */
        var self = this;
        var border = e.data.border;
        var last_column = false;
        _.each(this.renderer.widgets, function(col){
            var col_offset = col.$el.offset();
            if(border > col_offset.left){
                last_column = col;
            }
        });
        if(last_column != false){
            var attrs = {
                'employee_id': parseInt(this.model.employee_block.selected_employee),
                'duration': 1,
                'ref_doc_id': this.model.activity_block.model_selected + ',' + e.data.record.data.id,
                'date': moment(last_column.data.value, 'DD MMM YYYY').format('YYYY-MM-DD'),
                'sequence': 99
            }
            rpc.query({
                model: 'netfarm.sal',
                method: 'create',
                args: [attrs]
            }).then(function(res){
                self.reload().then(function(){self._load_hour_blocks()});
            });
        }
    },
    _resequenceRecords: function (column_id, ids) {
        var self = this;
        return this.model.resequence(this.modelName, ids, column_id).then(function () {
            self.reload().then(function(){self._load_hour_blocks()});
            self._updateEnv();
        });
    },
    _deleteRecords: function (ids) {
        var self = this;
        function doIt() {
            return self.model
                .deleteRecords(ids, self.modelName)
                .then(function(){
                    self.reload().then(function(){self._load_hour_blocks()});
                } );
        }
        if (this.confirmOnDelete) {
            Dialog.confirm(this, _t("Are you sure you want to delete this record?"), {
                confirm_callback: doIt,
            });
        } else {
            doIt();
        }
    },
});
return cKanbanController;
});