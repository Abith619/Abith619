// Copyright 2017 - 2018 Modoolar <info@modoolar.com>
// License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).
odoo.define('scrummer.page.dashboard', function (require) {
    "use strict";

    const ModelList = require('scrummer.model_list');
    const AbstractModelList = require('scrummer.abstract_model_list');
    const qweb = require('web.core').qweb;
    const _t = require('web.core')._t;
    const AgileBaseWidgets = require('scrummer.BaseWidgets');
    const hash_service = require('scrummer.hash_service');
    const SubheaderWidget = require('scrummer.subheader').SubheaderWidget;
    const data = require('scrummer.data');
    const pluralize = require('pluralize');
    const ActivityStream = require('scrummer.activity_stream').ActivityStream;

    const AssignedToMeMenuItem = ModelList.SimpleTaskItem.extend({
        start() {
            this.$(".task-menu").hide();
            this.$(".task-key").click(() => {
                hash_service.setHash("project", this.record.project_id[0]);
            });
            return this._super();
        }
    });
    AssignedToMeMenuItem.sort_by = "agile_order";
    const AssignedToMe = AgileBaseWidgets.AgileBaseWidget.extend({
        _name: "AssignedToMe",
        template: 'scrummer.dashboard.assigned_to_me',
        init(parent, options) {
            this._super(parent, options);
            this.estimates = {
                todo: 0,
                in_progress: 0,
                done: 0,
            };
            this.assignedToMeList = new AbstractModelList.ModelList(this, {
                template: "scrummer.backlog.task_list",
                model: "project.task",
                ModelItem: AssignedToMeMenuItem,
                emptyPlaceholder: $("<div>" + _t("You havent commited to any task in this team.") + "</div>"),
                fields: ["name",
                    "agile_order",
                    "story_points",
                    "project_id",
                    "key",
                    "color",
                    "priority_id",
                    "parent_id",
                    "parent_key",
                    "type_id",
                    "user_id",
                    "priority_scrummer_icon_color",
                    "priority_scrummer_icon",
                    "type_scrummer_icon_color",
                    "type_scrummer_icon",
                    "wkf_state_type"],
                domain: $.when(data.xmlidToResId("scrummer.project_task_type_epic"), data.cache.get("current_user"))
                    .then((type_epic, user) => [["user_id", "=", data.session.uid],
                        ["type_id", "!=", type_epic],
                        ["project_id", "in", user.team_ids[user.team_id[0]].project_ids]]),
                _name: "Assigned to me",
                attributes: {"data-id": this.id}
            });
        },
        renderElement() {
            this._super();
            this.assignedToMeList.appendTo(this.$el);
            this.assignedToMeList._is_rendered.then(() => {
                const items = this.assignedToMeList.data;
                this.$(".list-preloader").remove();
                this.$(".list-count").text(items.length + " " + pluralize('issue', items.length));
                for (const task of items) {
                    this.estimates[task.wkf_state_type] += task.story_points;
                }
                this.$(".estimates .estimate.todo").html(this.estimates.todo);
                this.$(".estimates .estimate.in_progress").html(this.estimates.in_progress);
                this.$(".estimates .estimate.done").html(this.estimates.done);
                this.$(".estimates").show();
            });
            this.assignedToMeList._is_added_to_DOM.then(() => {
                this.assignedToMeList.$('.tooltipped').tooltip({delay: 50});
            });
        }
    });

    const ProjectItem = AbstractModelList.AbstractModelListItem.extend({
        _name: "ProjectItem",
        template: "scrummer.list.project_item",
        //order_field: "agile_order",
        init(parent, options) {
            this._super(parent, options);
        },
        start() {
            // When clicked on project in dashboard, fetch all boards and open last board.
            this.$("a.project-key").click(() => {
                hash_service.setHash("project", this.record.id, false);
                hash_service.setHash("page", "board", false);
            });
            return this._super();
        },
        image_url() {
            return data.getImage("project.project", this.record.id, this.record.__last_update);
        }
    });
    ProjectItem.sort_by = "agile_order";

    const DashboardPage = AgileBaseWidgets.AgileViewWidget.extend({
        title: _t("Dashboard"),
        _name: "Dashboard",
        template: "scrummer.page.dashboard",
        // Disable floating actions button
        menuItemsContainer: false,
        init(parent, options) {
            this._super(parent, options);
        },
        start() {
            const allTasks = $("<a class='list-header-right'>Team backlog</a>");
            this.$("#project-list").parent().find("div.list-title").append(allTasks);
            allTasks.click(() => {
                hash_service.delete("project");
                hash_service.setHash("page", "board");
            });
            this.projectList._is_added_to_DOM.then(() => {
                this.$('.list-preloader.projects').remove();
            });
            this.trigger_up('menu.removed');
        },
        renderElement() {
            this._super();
            this.projectList = new AbstractModelList.ModelList(this, {
                model: "project.project",
                emptyPlaceholder: $(qweb.render("scrummer.dashboard.project-list.empty", {})),
                fields: [
                    "name",
                    "image_key",
                    "user_id",
                    "key",
                    "state",
                    "partner_id",
                    "todo_estimation",
                    "in_progress_estimation",
                    "done_estimation",
                    "__last_update"
                ],
                domain: $.when(data.cache.get("current_user"))
                    .then((user) => [["id", "in", user.team_ids[user.team_id[0]].project_ids], ["workflow_id", "!=", false]]),
                ModelItem: ProjectItem
            });
            this.projectList.appendTo(this.$("#project-list"));

            this.assignedToMeList = new AssignedToMe(this);
            this.assignedToMeList.appendTo(this.$("#assigned-to-me"));

            this.activityStream = new ActivityStream(this, {
                showMessageName: true,
                withShadow: true,
                listTitle: _t("Activity Stream"),
            });
            this.activityStream.appendTo(this.$("#activity-stream"));

            this.subheader = new SubheaderWidget(this);
            this.subheader.appendTo(this.$("#subheader-wrapper"));
        },
    });

    return {
        DashboardPage,
        AssignedToMe,
        AssignedToMeMenuItem,
        ProjectItem
    };
});
