// Copyright 2017 - 2018 Modoolar <info@modoolar.com>
// License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

odoo.define('scrummer.app_cache', function (require) {
    "use strict";
    const data = require('scrummer.data');
    const DependencyCache = require('scrummer.dependency_cache');
    const DataServiceFactory = require('scrummer.data_service_factory');

    data.cache.add("xmlidToResId", DependencyCache.AbstractDependency.extend({
        resolve() {
            this._require_obj("params", ["xmlId"]);
            this.getDataSet("ir.model.data")
                .call("xmlid_to_res_id", [this.params.xmlId])
                .then(this.deferred.resolve, this.deferred.reject);
        },
    }));
    data.cache.add("model_info", DependencyCache.AbstractDependency.extend({
        resolve() {
            this._require_obj("params", ["model"]);
            data.session.rpc("/scrummer/model/info", {model_name: this.params.model})
                .then((model) => {
                    model.fields_list = Object.keys(model.fields);
                    this.deferred.resolve(model);
                }, this.deferred.reject);
        },
    }));

    data.cache.add("project.type.task_types_priorities", DependencyCache.AbstractDependency.extend({
        resolve() {
            this._require_obj("params", ["id"]);
            data.session.rpc(`/scrummer/web/data/project/${this.params.id}/task_types_and_priorities`)
                .then(this.deferred.resolve, this.deferred.reject);
        }
    }));
    data.cache.add("default_task_type_priorities", DependencyCache.AbstractDependency.extend({
        resolve() {
            $.when(this.cache.get("default_task_type_id"),
                DataServiceFactory.get("project.task.priority").getAllRecords(true),
                DataServiceFactory.get("project.task.type2").getAllRecords(true)).then((taskTypeId, priorities, types) => {
                const result = [];
                types.get(taskTypeId).priority_ids.forEach((p_id) => result.push(priorities.get(p_id)));
                this.deferred.resolve(result);
            });
        }
    }));
    data.cache.add("default_task_type_id", DependencyCache.AbstractDependency.extend({
        resolve() {
            $.when(this.cache.get("default_task_type_id"),
                DataServiceFactory.get("project.task.priority").getAllRecords(true),
                DataServiceFactory.get("project.task.type2").getAllRecords(true)).then((taskTypeId, priorities, types) => {
                const result = [];
                types.get(taskTypeId).priority_ids.forEach((p_id) => result.push(priorities.get(p_id)));
                this.deferred.resolve(result);
            });
        }
    }));
    data.cache.add("project.workflow", DependencyCache.AbstractDependency.extend({
        resolve() {
            this._require_obj("params", ["id"]);
            data.session.rpc(`/scrummer/web/data/workflow/${this.params.id}`).then((workflow) => {
                // Create map with stage_id -> workflow state_id
                workflow.stageToState = {};
                for (const state_id in workflow.states) {
                    const state = workflow.states[state_id];
                    workflow.stageToState[state.stage_id] = state_id;
                }
                this.deferred.resolve(workflow);
            });
        }
    }));
    data.cache.add("board_for_project", DependencyCache.AbstractDependency.extend({
        resolve() {
            this._require_obj("params", ["id"]);
            this.getDataSet("project.project").read_slice(["name", "board_ids"], {
                domain: [['id', '=', this.params.id]]
            }).then((response) => {
                const project = response[0];
                // Get id of first board available on project
                this.deferred.resolve(project.board_ids[0]);
            });
        }
    }));
    data.cache.add("projects_in_board", DependencyCache.AbstractDependency.extend({
        resolve() {
            this._require_obj("params", ["id"]);
            this._require_obj("params", ["team_id"]);

            this.getDataSet("project.project").read_slice(["name"], {
                domain: this.cache.get("current_user").then((user) => [
                    ["board_ids", "=", this.params.id],
                    ["id", "in", user.team_ids[this.params.team_id].project_ids],
                ])
            }).then((projects) => {
                const map = new Map();
                projects.forEach((project) => map.set(project.id, project));
                this.deferred.resolve(map);
            });

        }
    }));
    data.cache.add("team_members", DependencyCache.AbstractDependency.extend({
        resolve() {
            this._require_obj("params", ["teamId"]);
            DataServiceFactory.get("project.agile.team").getRecord(this.params.teamId).then((team) => {
                DataServiceFactory.get("res.users").getRecords(team.member_ids).then(this.deferred.resolve, this.deferred.reject);
            });
        }
    }));
    data.cache.add("current_user", DependencyCache.AbstractDependency.extend({
        resolve() {
            data.session.rpc("/scrummer/session_user").then((user) => {
                user.imageUrl = data.getImage("res.users", user.id, user.write_date);
                this.deferred.resolve(user);
            }, this.deferred.reject);
        }
    }));
    data.cache.add("get_user", DependencyCache.AbstractDependency.extend({
        resolve() {
            this._require_obj("params", ["id"]);

            const cacheMiss = () => {
                this.cache.get("model_info", {model: 'res.users'})
                    .then((model) => {
                        this.getDataSet(model.name)
                            .read_ids([this.params.id], model.fields_list)
                            .then((result) => {
                                const user = result[0];
                                this.deferred.resolve(user);
                            }, this.deferred.reject);
                    });
            };

            this.cache.get("current_user").then((session_user) => {
                // Current user doesn't have team
                if (!Array.isArray(session_user.team_id)) {
                    cacheMiss();
                }
                this.cache.get("team_members", {teamId: session_user.team_id[0]}).then((members) => {
                    // First check team_members, otherwise
                    const user = members.find((e) => e.id === this.params.id);
                    if (user) {
                        this.deferred.resolve(user);
                    } else {
                        cacheMiss();
                    }
                });
            });
        }
    }));
    data.cache.add("get_message_subtypes", DependencyCache.AbstractDependency.extend({
        resolve() {
            this._require_obj("params", ["res_model"]);
            const priorityIdsPromise = this.getDataSet("mail.message.subtype").id_search("", [["res_model", "=", this.params.res_model]]);
            priorityIdsPromise.then((ids) => {
                DataServiceFactory.get("mail.message.subtype").getRecords(ids).then((records) => {
                    this.deferred.resolve(records);
                }, this.deferred.reject);
            }, this.deferred.reject);
        }
    }));
    data.cache.add("project.task.link.relation.nameOrderMaps", DependencyCache.AbstractDependency.extend({
        resolve() {
            DataServiceFactory.get("project.task.link.relation").getAllRecords().then((relations) => {
                const nameToOrderMap = new Map();
                const orderToNameMap = new Map();
                relations.forEach((relation) => {
                    nameToOrderMap.set(relation.name, relation.sequence);
                    orderToNameMap.set(relation.sequence, relation.name);
                });
                this.deferred.resolve(nameToOrderMap, orderToNameMap);
            }, this.deferred.reject);
        }
    }));

    data.xmlidToResId = function (xmlId) {
        return data.cache.get("xmlidToResId", {xmlId});
    };
    data.getMessageSubtypes = function (res_model) {
        // return DataServiceFactory.get("project.task.priority").getAllRecords();
        return data.cache.get("get_message_subtypes", {res_model});
    };

});
