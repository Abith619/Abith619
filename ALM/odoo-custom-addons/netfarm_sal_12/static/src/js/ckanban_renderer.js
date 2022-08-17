odoo.define('netfarm_sal_12.cKanbanRenderer', function (require) {
"use strict";

var KanbanRenderer = require('web.KanbanRenderer');
var KanbanColumn = require('web.KanbanColumn');
var EmployeeBlock = require('netfarm_sal_12.EmployeeBlock');

var time = require('web.time');
var core = require('web.core');
var _t = core._t;
var data = require('web.data');
var rpc = require('web.rpc');

var cKanbanRenderer= KanbanRenderer.extend({
    _renderGrouped: function (fragment) {
        var self = this;
        this._super(fragment);
        /* assegno le classi alle colonne */
        _.each(this.widgets, function(widget){
            widget.$el.addClass('netfarm_calendar_kanban');
            var curr = moment().format('DD MMM YYYY');
            if (curr == widget.title){
                widget.$el.addClass('netfarm_calendar_kanban_today');
            }
            var dd = moment(widget.title, 'DD MMM YYYY').format('ddd');
            var tt = widget.$el.find('.o_column_title').text();
            widget.$el.find('.o_column_title').text(dd + ' ' + tt);
            /*
            abilito il drag&drop sul record
            metto il containment sel sortable a false e libero lo spazio di azione
            */
            widget.$el.sortable({
                cursor: 'grabbing',
                containment: false,
                update: function (event, ui) {
                    var record = ui.item.data('record');
                    if (typeof record === "undefined") {
                    }else{
                        var index = widget.records.indexOf(record);
                        if (index >= 0) {
                            if ($.contains(self.$el[0], record.$el[0])) {
                                // resequencing records
                                widget.trigger_up('kanban_column_resequence', {ids: widget._getIDs()});
                            }
                        } else {
                            // adding record to this column
                            var border = ui.offset.left;
                            var last_column = false;
                            _.each(self.widgets, function(col){
                                var col_offset = col.$el.offset();
                                if(border > col_offset.left){
                                    last_column = col;
                                }
                            });
                            if(last_column != false){
                                var new_date = moment(last_column.data.value, 'DD MMM YYYY').format('YYYY-MM-DD');
                                record.recordData.date = new_date;
                                rpc.query({
                                    model: 'netfarm.sal',
                                    method: 'write',
                                    args: [record.recordData.id, {'date': new_date}]
                                }).then(function(res){
                                   widget.trigger_up('kanban_column_resequence', {ids: widget._getIDs()});
                                });
                            }
                        }
                    }
                }
            });
        });
    },
    _renderView: function () {
        var render = this._super();
        this.$el.addClass('ckanban');
        return render;
    }
});
return cKanbanRenderer;
});