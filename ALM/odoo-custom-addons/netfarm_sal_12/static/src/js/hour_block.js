odoo.define('netfarm_sal_12.HourBlock', function (require) {
"use strict";
var core = require('web.core');
var qweb = core.qweb;
var _lt = core._lt;
var _t = core._t;
var Widget = require('web.Widget');
var rpc = require('web.rpc');

var HourBlock = Widget.extend({
    template: 'netfarm_sal_12.hour_block',
    init: function(parent, day, total, assigned){
        this._super(parent);
        this.day = day;
        this.employee = false;
        this.total_assigned = assigned;
        this.total_daily = total;
    },
    start: function(){
        this.style();
        var top = (this.total_daily * 80);
        var h1 = this.$el.outerHeight();
        var h2 = this.$el.closest('.netfarm_calendar_kanban').find('.o_kanban_header').outerHeight();

        if (top > 0){
            top = top + h1 + h2;
            this.$el.closest('.netfarm_calendar_kanban').append('<div class="linea" style="top:'+ top +'px"></div>');
        }
        return this._super();
    },
    style: function(){
        /*if(this.total_daily == 0){
            this.$el.closest('.netfarm_calendar_kanban').css('color', '#f0eeee');
        }*/
        if(this.total_daily < this.total_assigned){
            this.$el.addClass('red_hour');
        }else{
            this.$el.removeClass('red_hour');
        }
    },
    reload: function(){
        this.$el.find('.assigned').text(this.total_assigned)
    }
})

return HourBlock;
});