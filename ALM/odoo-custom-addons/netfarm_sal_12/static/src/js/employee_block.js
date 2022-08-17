odoo.define('netfarm_sal_12.EmployeeBlock', function (require) {
"use strict";
var core = require('web.core');
var qweb = core.qweb;
var _lt = core._lt;
var _t = core._t;
var Widget = require('web.Widget');
var rpc = require('web.rpc');

var EmployeeBlock = Widget.extend({
    template: "netfarm_sal_12.employee_block",
    init: function(parent){
        this._super(parent);
        this.datas = [];
        this.title = _t('Employees');
        this.employees = [];
        this.departments = [];
        this.choose_first = _t('Choose Department');
        this.selected_employee = false;
        this.selected_department = false;
        this.hours = false;
    },
    events: {
        'change .dep_select': '_select_dep',
        'click .select_employee': '_select_employee'
    },
    willStart: function(){
        var self = this;
        return $.when(this.get_employees(), this.get_selected_employee_data()).then(function(employees, datas){
            self.employees = employees[0];
            self.departments = employees[1];
            self.selected_employee = datas.employee;
            self.selected_department = datas.department_id;
            self._get_hours(self.selected_employee);
            self.trigger_up('load_hour_blocks');
        });
    },
    get_employees: function(){
        /* get all employees */
        return rpc.query({model: 'hr.employee', method: 'get_employees', args: []});
    },
    get_selected_employee_data: function(){
        return rpc.query({model: 'hr.employee', method: 'get_selected_employee_data', args: [this.domain_selected_employee]});
    },
    _select_dep: function(e){
        var self = this;
        self.$el.find('.d-block').removeClass('d-block').addClass('d-none');
        var value = e.currentTarget.value;
        self.$el.find('#dep'+value).removeClass('d-none').addClass('d-block');
        self.selected_department = value;
    },
    _select_employee: function(e){
        var self = this;
        self.selected_employee = $(e.currentTarget).attr('data-id');
        var name = e.currentTarget.innerText;
        self.$el.find('.selected_employee').removeClass('selected_employee');
        $(e.currentTarget).addClass('selected_employee');
        self._get_hours(self.selected_employee);
        self.trigger_up('change_employee', {'employee': self.selected_employee, 'name': name});
    },
    _get_hours: function(employee_id){
        var self = this;
        _.each(self.employees, function(employee){
            _.each(employee, function(em){
                if(em.id == employee_id){
                    self.hours = em.hours;
                }
            })
        });
    }
});

return EmployeeBlock;
});