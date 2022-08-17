odoo.define('netfarm_sal_12.ActivityBlock', function (require) {
"use strict";
var core = require('web.core');
var qweb = core.qweb;
var _lt = core._lt;
var _t = core._t;
var Widget = require('web.Widget');
var rpc = require('web.rpc');

var RecordActivity = require('netfarm_sal_12.RecordActivity');

var ActivityBlock = Widget.extend({
    template: "netfarm_sal_12.activityblock",
    init: function (parent) {
        this._super(parent);
        var self = this;
        self.models_allowed = [];
        self.model_selected = false;
        self.title = _t('Activity');
        self.choose_first = _t('Choose Model');
        self.datas = [];
        self.offset = 0;
        self.filter = false;
        self.limit = 10;
        self.domain = [];
        self.filter = false;
        self.total = 0;
    },
    events: {
        'change .models_select': 'choose_model',
        'click .page-next': 'page_next',
        'click .page-prev': 'page_prev',
        'keyup .search-object': 'input_change',
    },
    willStart: function(){
        var self = this;
        return $.when(this.get_options()).then(function(options){
            self.models_allowed = options.models_allowed;
            self.model_selected = options.model_selected;
            rpc.query({
                model: self.model_selected,
                method: 'search_count',
                args: [[]]
            }).then(function(count){
                self.total = count;
            });
            self.do_search();
        });
    },
    get_options: function(){
        return rpc.query({model: 'res.config.settings', method: 'get_sal_config'});
    },
    choose_model: function(e){
        /* when a model is selected configure some params */
        var self = this;
        self.offset = 0;
        self.filter = false;
        var value = e.currentTarget.value;
        var check_model = self.check_model_permission(value);
        if(check_model){
            return self.do_warn(_t('Model"') + value + _t('" not allowed!'));
        }else{
            self.model_selected = value;
            self.do_search();
            rpc.query({
                model: self.model_selected,
                method: 'search_count',
                args: [[]]
            }).then(function(count){
                self.total = count;
            });
        }
    },
    check_model_permission: function(model_name){
        /* check if selected model is allowed */
        var self = this;
        var check_model = true;
        _.each(self.models_allowed, function(m){
            if(m[0] == model_name){
                check_model = false;
            }
        });
        return check_model;
    },
    destroy_all_record: function(){
        var self = this;
        _.each(self.datas, function(data){
            data.destroy();
        });
        self.datas = [];
    },
    page_next: function(){
        var self = this;
        var new_offset = self.offset + self.limit;
        if (new_offset <= self.total && self.filter == false){
            self.offset = self.offset + self.limit;
            self.do_search();
        }
    },
    page_prev: function(){
        var self = this;
        var new_offset = self.offset - self.limit;
        if (new_offset >= 0 && self.filter == false){
            self.offset = new_offset;
            self.do_search();
        }
    },
    input_change: function(e){
        var self = this;
        var value = e.currentTarget.value;
        if (value.length > 2){
            var filter = value;
            self.filter = filter;
            self.offset = 0;
        }else{
            self.filter = false;
            self.offset = 0;
        }
        if (self.filter === false){
            self.domain = [];
            self.do_search();
        }else{
            rpc.query({
                model: self.model_selected,
                method: 'name_search',
                kwargs: {'name': value, limit: self.limit}
            }).then(function(results){
                self.destroy_all_record();
                _.each(results, function(res){
                    var ids = [];
                    ids.push(parseInt(res[0]));
                    self.domain = [['id','in',ids]];
                    self.do_search();
                });
                self.render_records();
            });
        }
    },
    do_search: function(){
        var self = this;
        self.destroy_all_record();
        return rpc.query({
            model: self.model_selected,
            method: 'search_read',
            domain: self.domain,
            limit: self.limit,
            order: 'id desc',
            offset: self.offset
        }).then(function(results){
            _.each(results, function(res){
                var record = new RecordActivity(self, res, self.model_selected);
                self.datas.push(record);
            });
            self.render_records();
        });
    },
    render_records: function () {
        var self = this;
        _.each(self.datas, function(record){
            record.appendTo(self.$el.find('.content-activity'));
        });
    }
});

return ActivityBlock;
});