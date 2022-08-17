odoo.define('netfarm_sal_12.cKanbanModel', function (require) {
"use strict";
var KanbanModel = require('web.KanbanModel');

var formatDate = 'DD MMM YYYY';

var sortByDate = function SortByDate(a, b){
      var ad = moment(a['date:day'], formatDate);
      var bd = moment(b['date:day'], formatDate);
      return ((ad < bd) ? -1 : ((ad > bd) ? 1 : 0));
}

var cKanbanModel = KanbanModel.extend({
    init: function () {
        this.curr = moment().startOf('week');
        this.week = this.get_week();
        this._super.apply(this, arguments);
    },
    get_week: function(){
        var i;
        var week = {};
        var today = this.curr;
        var mon = today.startOf('week');
        var week = [];
        for (i = 0; i <= 6; i++) {
            var new_date = moment(mon).add(i, 'days').format(formatDate);
            week.push(new_date);
        };
        return week;
    },
    _readGroup: function (list, options) {
        /*
        override: aggiunge le colonne per la settimana
        */
        var self = this;
        /* controllo che non ci siano date*/
        var count = 0;
        _.each(list.domain, function(tuple){
            if('date' == tuple[0]){
                count = count +1;
            }
        });
        if (count % 2 != 0 || count == 0){
            /*azzzero la data curr*/
            this.curr = moment().startOf('week');
            this.week = this.get_week();
        }
        var groupByField = list.groupedBy[0];
        var rawGroupBy = groupByField.split(':')[0];
        var fields = _.uniq(list.getFieldNames().concat(rawGroupBy));
        var orderedBy = _.filter(list.orderedBy, function(order){
            return order.name === rawGroupBy || list.fields[order.name].group_operator !== undefined;
        });
        return this._rpc({
                model: list.model,
                method: 'read_group',
                fields: fields,
                domain: list.domain,
                context: list.context,
                groupBy: list.groupedBy,
                orderBy: orderedBy,
                lazy: true,
            })
            .then(function (groups) {
                /* introduco le date mancanti */
                var used = []
                _.each(groups, function(g){
                    used.push(g['date:day']);
                });
                _.each(self.week, function(day){
                    var data = {
                        'date:day': day,
                        'date_count': 0,
                        'duration': 0
                    }
                    if($.inArray(day, used) < 0){
                        groups.push(data);
                    }
                });
                groups.sort(sortByDate)
                /* fine */
                var previousGroups = _.map(list.data, function (groupID) {
                    return self.localData[groupID];
                });
                list.data = [];
                list.count = 0;
                var defs = [];
                var openGroupCount = 0;

                _.each(groups, function (group) {
                    var aggregateValues = {};
                    _.each(group, function (value, key) {
                        if (_.contains(fields, key) && key !== groupByField) {
                            aggregateValues[key] = value;
                        }
                    });
                    // When a view is grouped, we need to display the name of each group in
                    // the 'title'.
                    var value = group[groupByField];
                    if (list.fields[rawGroupBy].type === "selection") {
                        var choice = _.find(list.fields[rawGroupBy].selection, function (c) {
                            return c[0] === value;
                        });
                        value = choice ? choice[1] : false;
                    }
                    var newGroup = self._makeDataPoint({
                        modelName: list.model,
                        count: group[rawGroupBy + '_count'],
                        domain: group.__domain,
                        context: list.context,
                        fields: list.fields,
                        fieldsInfo: list.fieldsInfo,
                        value: value,
                        aggregateValues: aggregateValues,
                        groupedBy: list.groupedBy.slice(1),
                        orderedBy: list.orderedBy,
                        orderedResIDs: list.orderedResIDs,
                        limit: list.limit,
                        openGroupByDefault: list.openGroupByDefault,
                        parentID: list.id,
                        type: 'list',
                        viewType: list.viewType,
                    });
                    var oldGroup = _.find(previousGroups, function (g) {
                        return g.res_id === newGroup.res_id && g.value === newGroup.value;
                    });
                    if (oldGroup) {
                        // restore the internal state of the group
                        delete self.localData[newGroup.id];
                        var updatedProps = _.omit(newGroup, 'limit', 'isOpen', 'offset', 'id');
                        if (options && options.onlyGroups || oldGroup.isOpen && newGroup.groupedBy.length) {
                            // If the group is opened and contains subgroups,
                            // also keep its data to keep internal state of
                            // sub-groups
                            // Also keep data if we only reload groups' own data
                            delete updatedProps.data;
                        }
                        // set the limit such that all previously loaded records
                        // (e.g. if we are coming back to the kanban view from a
                        // form view) are reloaded
                        oldGroup.limit = oldGroup.limit + oldGroup.loadMoreOffset;
                        _.extend(oldGroup, updatedProps);
                        newGroup = oldGroup;
                    } else if (!newGroup.openGroupByDefault || openGroupCount >= self.OPEN_GROUP_LIMIT) {
                        newGroup.isOpen = false;
                    } else {
                        newGroup.isOpen = '__fold' in group ? !group.__fold : true;
                    }
                    list.data.push(newGroup.id);
                    list.count += newGroup.count;
                    if (newGroup.isOpen && newGroup.count > 0) {
                        openGroupCount++;
                        defs.push(self._load(newGroup, options));
                    }
                });
                if (options && options.keepEmptyGroups) {
                    // Find the groups that were available in a previous
                    // readGroup but are not there anymore.
                    // Note that these groups are put after existing groups so
                    // the order is not conserved. A sort *might* be useful.
                    var emptyGroupsIDs = _.difference(_.pluck(previousGroups, 'id'), list.data);
                    _.each(emptyGroupsIDs, function (groupID) {
                        list.data.push(groupID);
                        var emptyGroup = self.localData[groupID];
                        // this attribute hasn't been updated in the previous
                        // loop for empty groups
                        emptyGroup.aggregateValues = {};
                    });
                }
                return $.when.apply($, defs).then(function () {
                    if (!options || !options.onlyGroups) {
                        // generate the res_ids of the main list, being the concatenation
                        // of the fetched res_ids in each group
                        list.res_ids = _.flatten(_.map(arguments, function (group) {
                            return group ? group.res_ids : [];
                        }));
                    }
                    return list;
                });
            });
    },
});
return cKanbanModel;
});