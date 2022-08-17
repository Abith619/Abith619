odoo.define('netfarm_sal_12.cKanbanRecord', function (require) {
"use strict";

var config = require('web.config');
var core = require('web.core');
var Domain = require('web.Domain');
var field_utils = require('web.field_utils');
var utils = require('web.utils');
var Widget = require('web.Widget');
var widgetRegistry = require('web.widget_registry');

var _t = core._t;
var QWeb = core.qweb;
var rpc = require('web.rpc');

var KanbanRecord = require('web.KanbanRecord');

var cKanbanRecord = KanbanRecord.include({
    events: _.extend({}, KanbanRecord.prototype.events, {
        'click .ckrecord-check': 'ckard_check',
        'click .ckrecord-cancel': 'unlink_ckard',
        'click .ckanban-open': 'open_activity'
    }),
    unlink_ckard: function(e){
        var self = this;
        /* destroy the record widget */
        self.trigger_up('kanban_record_delete', {id: this.db_id, record: this});
    },
    ckard_check: function(ev){
        /* set the record netfarm.sal to done */
        var self = this;
        rpc.query({
            model: 'netfarm.sal',
            method: 'write',
            args: [self.recordData.id, {'done': 1}]
        }).then(function(){
            self.$el.find('.ckanban-right').addClass('ckanban-done');
            self.$el.find('.ckrecord-check').hide();
        });
    },
    open_activity: function(ev){
        var self = this;
        var value = self.recordData.ref_doc_id;


        var action = {
            views: [[false, 'form']],
            view_type: 'form',
            view_mode: 'form',
            res_model: value.model,
            type: 'ir.actions.act_window',
            target: 'new',
            res_id: value.res_id,
            flags:{'initial_mode': 'view'}
        };
        self.do_action(action);
    },
    _onGlobalClick: function (event) {
        /* se è una ckanban disabilito il click */
        var alive = this.trigger_up('ckanban_alive');
        if(alive.data.alive != 1){
            this._super(event);
        }
    },
    _render: function () {
        var alive = this.trigger_up('ckanban_alive');
        this._super();
        if(alive.data.alive == 1){
            var self = this;
            var height = this.recordData.height;
            this.$el.height(height);
            this.$el.resizable({
                handles: 's',
                grid: 40,
                start: function( event, ui ) {
                    /* save the old duration */
                    self.last_duration = self.recordData.duration;
                    var column_height = $(ui.element[0]).closest('.netfarm_calendar_kanban').height();
                    var this_height = ui.element[0].offsetTop + ui.size.height;
                    if(this_height > (column_height - 40)){
                        $(ui.element[0]).closest('.netfarm_calendar_kanban').css('height', (column_height + 80));
                        $('.o_content').stop().animate({scrollTop: $('.o_content').scrollTop()+80}, 200);
                    }else{
                        $('.o_content').stop().animate({scrollTop: $('.o_content').scrollTop()-80}, 200);
                    }
                },
                stop: function( event, ui ) {
                    var h = ui.size.height;
                    var new_value = h/80;
                    if(self.last_duration > new_value){
                        /* open reallocation */
                        console.log(self)
                        var action = {
                            name: _t('Reallocate Sal'),
                            views: [[false, 'form']],
                            view_type: 'form',
                            view_mode: 'form',
                            res_model: 'reallocate.sal',
                            type: 'ir.actions.act_window',
                            target: 'new',
                            context : {
                                'default_employee_id': self.recordData.employee_id.res_id,
                                'default_duration':self.last_duration - new_value,
                                'default_ref_doc_id': self.recordData.ref_doc_id.model+','+self.recordData.ref_doc_id.res_id,
                            }
                        };
                        self.do_action(action, {
                            on_close: function(){
                                self.trigger_up('ultra_reload');
                            }
                        });
                    }
                    rpc.query({
                        model: 'netfarm.sal',
                        method: 'write',
                        args: [self.recordData.id, {'duration': new_value}]
                    });
                },
                resize: function( event, ui ) {
                    var h = ui.size.height;
                    var new_value = h/80;
                    ui.element.find('.duration').text(new_value.toFixed(2).replace('.',','));
                    var column_height = $(ui.element[0]).closest('.netfarm_calendar_kanban').height();
                    var this_height = ui.element[0].offsetTop + ui.size.height;
                    if(this_height > (column_height - 40)){
                        $(ui.element[0]).closest('.netfarm_calendar_kanban').css('height', (column_height + 40));
                        $('.o_content').stop().animate({scrollTop: $('.o_content').scrollTop()+40}, 200);
                    }else{
                        $('.o_content').stop().animate({scrollTop: $('.o_content').scrollTop()-40}, 200);
                    }
                    self.recordData.duration = new_value;
                    self.trigger_up('reload_hour_block');
                }
            });
        }
    }
});

return cKanbanRecord;
});