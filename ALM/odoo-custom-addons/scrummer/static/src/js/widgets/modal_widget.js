// Copyright 2017 - 2018 Modoolar <info@modoolar.com>
// License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

odoo.define('scrummer.widget.modal', function (require) {
    "use strict";
    const BaseWidgets = require('scrummer.BaseWidgets');
    const DataServiceFactory = require('scrummer.data_service_factory');
    const scrummer_data = require('scrummer.data');
    const helpers = require('scrummer.helpers');
    const Many2One = require('scrummer.widget.many2one').Many2One;
    const Many2ManyTags = require('scrummer.widget.many2many_tags').Many2ManyTags;
    const _t = require("web.core")._t;
    const Attachments = require('scrummer.attachments');
    const hash_service = require('scrummer.hash_service');
    const Materialize = window.Materialize;

    const ModalWidget = BaseWidgets.AgileBaseWidget.extend({
        /* eslint-disable no-unused-vars, no-empty-function */
        validateOptions: {},
        init(parent, options) {
            this._super(parent, options);
            Object.assign(this, options);
            // Inheriting widgets can override getDefaults method for setting defaults,
            // but defaults passed in option will have higher priority
            this.defaults = typeof this.defaults === "object" ? Object.assign({}, this.getDefaults(), this.defaults) : this.getDefaults();
            this.setEditingState();
        },
        /**
         *
         * @param {{}} options
         *
         * @param {String} options.field
         * @param {Array} options.data
         * @param {String} options.key
         * @param {String} options.value
         * @param {String} options.mdi
         * @param {String} options.iconColor
         * @param {String} options.iconUrl
         * @param {Function} options.selectedValue
         * @param {Function} options.changeHandler
         */
        prepareSelection(options) {
            // Setting project selection
            const {field, data, key = "id", value = "name", mdi, iconColor, selectedValue, changeHandler} = options;
            const optionNodes = [];

            // If data is object, convert it to array for further manipulation
            const array = Array.isArray(data) ? data : Object.keys(data).map((k) => data[k]);

            for (const element of array) {
                const option = $('<option value="' + element[key] + '">' + element[value].trim() + '</option>');
                if (mdi) {
                    option.data("mdi", element[mdi]);
                }
                if (iconColor) {
                    option.data("iconColor", element[iconColor]);
                }
                optionNodes.push(option);
            }
            const selectionNode = this.$("form [name='" + field + "']");
            selectionNode.find("option:not(:first)").remove();
            selectionNode.removeClass().append(...optionNodes);

            // Select default value
            if (selectedValue) {
                selectionNode.val(selectedValue);
                if (changeHandler) {
                    changeHandler.bind(selectionNode[0])();
                }
            }

            selectionNode.material_select();
            selectionNode.off().change(function () {
                $(this).valid();
                if (changeHandler) {
                    changeHandler.bind(this)();
                }
            });
        },
        setEditingState() {
        },
        setDefaultState() {
        },
        start() {
            const form = this.$("form");
            if (form.data("validator")) {
                Object.assign(form.data("validator").settings, this.getValidateOptions());
            } else {
                form.validate(this.getValidateOptions());
            }
            form.submit((e) => {
                e.preventDefault();
                // This check is here to make sure that submit is triggered by
                // clicking on confirmation button and not by materialNote dropdown button
                if (!this.submitting) {
                    return;
                }
                this.submitting = false;

                if (!$(e.target).valid()) {
                    return;
                }
                const formData = $(e.target).serializeObject();
                this.$("[data-is-dirty='false']").each(function () {
                    delete formData[this.name];
                });
                this.loadData(formData);
                if (typeof this.beforeHook === "function") {
                    this.beforeHook(formData);
                }
                if (Object.keys(formData).length) {
                    const submitDef = this.submit(formData, $(e.target));
                    if (typeof this.afterHook === "function") {
                        $.when(submitDef).then((result) => {
                            this.afterHook(result, formData, $(e.target));
                        });
                    }
                }
                this.closeModal();
            });
            this.$(".modal-submit").click(this.confirmationHandler.bind(this));
            return this._super();
        },
        beforeCloseModal() {
            return true;
        },
        closeModal() {
            if (this.beforeCloseModal()) {
                this.$el.materialModal("close");
            }
        },
        destroy() {
            this.setDefaultState();
            return this._super.apply(this, arguments);
        },
        /**
         * This method should return dictionary with default values.
         * If options.defaults is passed to constructor, it will override value from this method.
         *
         * @returns {{}} Dictionary with
         */
        getDefaults() {
            return {};
        },
        /**
         * This method should prepare, transform and format data required by submit method
         * @param {Object} data
         */
        loadData(data) {
        },

        confirmationHandler() {
            // This boolean is necessary because materialNote triggers form submit when clicked on dropdown.
            this.submitting = true;
            this.$("form").submit();
        },
        /**
         * @returns {Object} jQuery.validate options object
         */
        getValidateOptions() {
            return {
                ignore: ".note-editable"
            };
        },
        submit() {
            console.warn("Modal form submit method not implemented!");
        },
        addedToDOM() {
            const modalWidgetThis = this;
            this.$el.materialModal({
                dismissible: false,
                ready: modalWidgetThis.modalReady.bind(this),
                complete: modalWidgetThis.destroy.bind(this),
            });
            this.$(".planned_hours_help").tooltip({
                tooltip: "Combine: w-weeks, d-days, h-hours, m-minutes. (1 day means 8 hours) Separate with space.",
                position: "left",
            });
            this.$el.materialModal("open");

            this.$(".materialnote").materialnote({
                toolbar: this.materialnoteToolbar,
                height: 100,
                defaultBackColor: '#fff',
                focus: true,
            });
            this.$('.datepicker').pickadate({
                // Creates a dropdown to control month
                selectMonths: true,
                // Creates a dropdown of 15 years to control year,
                selectYears: 15,
                today: 'Today',
                clear: 'Clear',
                close: 'Ok',
                format: 'yyyy-mm-dd',
                // Close upon selecting a date,
                closeOnSelect: false
            });
            if (this.edit) {
                // this.$("form select, form input").attr("data-is-dirty", false);
                // this.$("form select, form input").change(function () {
                //     $(this).attr("data-is-dirty", true);
                // });
                this.populateMaterialNote();
            }
            this.$el.on("keydown.modal", (e) => {
                // Close on escape;
                if (e.keyCode === 27) {
                    this.closeModal();
                }
            });
            return this._super();
        },
        modalReady() {
            Materialize.updateTextFields();
            if (this.focus) {
                this.$("form [name=" + this.focus + "]").focus();
            }
        },
        renderElement() {
            this._super();
            if (this.edit) {
                this.populateFieldValues();
            }
        },
        populateFieldValues() {
            throw new Error("In order to open modal in edit mode, populateFieldValues should be overriden.");
        },
        populateMaterialNote() {
            throw new Error("In order to open modal in edit mode with materialNote, populateMaterialNote should be overriden.");
        },
        materialnoteToolbar: [
            ['style', ['style', 'bold', 'italic', 'underline', 'strikethrough', 'clear']],
            ['fonts', ['fontsize', 'fontname']],
            ['color', ['color']],
            ['undo', ['undo', 'redo']],
            ['ckMedia', ['ckImageUploader', 'ckVideoEmbeeder']],
            ['misc', ['link', 'table', 'hr', 'codeview', 'fullscreen']],
            ['para', ['ul', 'ol', 'paragraph', 'leftButton', 'centerButton', 'rightButton', 'justifyButton', 'outdentButton', 'indentButton']],
            ['height', ['lineheight']]
        ],
    });

    const NewItemModal = ModalWidget.extend({
        template: "scrummer.widget.modal.new_item",
        focus: "name",
        init(parent, options) {
            this._super(parent, options);
            this.board_id = parseInt(hash_service.get("board"), 10);
            this._require_prop("board_id", "board_id is not set in url");

            if (this.edit) {
                if (!this.edit._is_dataservice) {
                    throw new Error("edit option must be instance of dataservice!");
                }
                this.currentProjectId = this.edit.project_id[0];
                // Just for for consistancy
                if (this.edit.parent_id) {
                    this.parent_id = this.edit.parent_id[0];
                }
            }
        },
        willStart() {
            const superPromise = this._super().then(DataServiceFactory.get("project.agile.board").getRecord(this.board_id).then((board) => {
                this.board = board;
            }));
            // Fetch parent item
            if (this.is_sub_item()) {
                return superPromise.then(() => DataServiceFactory.get("project.task").getRecord(this.parent_id).then((parent) => {
                    this.parent = parent;
                }));
            }
            return superPromise;
        },
        is_sub_item: function () {
            return this.parent_id;
        },
        renderElement() {
            this._super();
            if (this.edit && !this.edit.date_deadline) {
                this.$("input[name='date_deadline']").val("");
            }
            const thisModal = this;
            this.projectMany2one = new Many2One(this, {
                label: _t("Project"),
                model: "project.project",
                field_name: "project_id",
                className: "s12 m6 l6",
                domain: scrummer_data.cache.get("current_user").then((user) => [
                    ["board_ids", "=", this.board_id],
                    ["id", "in", user.team_ids[user.team_id[0]].project_ids],
                ]),
                changeHandler(evt) {
                    thisModal.currentProjectId = parseInt(evt.target.value, 10);
                    thisModal.projectChanged();
                },
                // Default project in following order of priority: 1. From edit object; 2. from parent; 3. from defaults object;
                default: this.edit && this.edit.project_id ? {
                        id: this.edit.project_id[0],
                        name: this.edit.project_id[1]
                    }
                    : this.parent && this.parent.project_id ? {
                            id: this.parent.project_id[0],
                            name: this.parent.project_id[1]
                        }
                        : this.defaults && this.defaults.project ? this.defaults.project : null
            });
            this.projectMany2one.appendTo(this.$("#project_id_placeholder"));

            if (this.edit) {
                this.resolutionMany2one = new Many2One(this, {
                    label: _t("Resolution"),
                    model: "project.task.resolution",
                    field_name: "resolution_id",
                    default: this.edit.resolution_id ? {
                        id: this.edit.resolution_id[0],
                        name: this.edit.resolution_id[1]
                    } : null,
                });
                this.resolutionMany2one.appendTo(this.$("#resolution_id_placeholder"));
            }
            const tagsOptions = {
                comodel: "project.tags",
            };
            this.edit && Object.assign(tagsOptions, {
                // model: "project.task",
                // res_id: "",
                res_ids: this.edit.tag_ids,
            });
            this.tagsMany2Many = new Many2ManyTags(this, tagsOptions);
            this.tagsMany2Many.appendTo(this.$("#tags_placeholder"));

            if (this.edit) {
                this.$("#project_id_placeholder, #resolution_id_placeholder, #tags_placeholder").addClass("col s12 m4 l4");
            } else {
                this.$("#project_id_placeholder, #tags_placeholder").addClass("col s12 m6 l6");
            }

        },
        loadData(task) {
            if (!(task.date_deadline && task.date_deadline.length)) {
                task.date_deadline = false;
            }
            task.tag_ids = [[6, false, this.tagsMany2Many.val().map((id) => parseInt(id, 10))]];
            task.description = this.$(".materialnote").code();
            task.story_points = task.story_points ? task.story_points : 0;
            if (this.is_sub_item() && !this.edit) {
                task.sprint_id = this.parent.sprint_id ? this.parent.sprint_id[0] : false;
                task.agile_order = this.parent.agile_order + 0.01;
            }
            const planned_hours_raw = this.$("input[name='planned_hours']").val();
            try {
                if (planned_hours_raw) {
                    task.planned_hours = helpers.time.parse(planned_hours_raw);
                }
            } catch (e) {
                console.error(e);
                return;
            }
        },
        getValidateOptions() {
            return {
                ...this._super(),
                ...{
                    rules: {
                        type_id: "required",
                        priority_id: "required",
                        project_id: "required",
                        name: "required",
                        story_points: "number",
                        planned_hours: "scrummer.time",
                        date_deadline: "date",
                    },
                    messages: {
                        story_points: _t("Estimate should be in story points (number)")
                    }
                }
            };
        },
        submit(task) {
            if (this.is_sub_item() && !this.edit) {
                task.parent_id = this.parent.id;
            }

            if (this.edit) {
                return this.edit.write(task);
            }
            return scrummer_data.getDataSet("project.task").create(task);

        },
        start() {
            if (this.currentProjectId) {
                this.projectChanged();
            } else {
                this.prepareSelection({
                    field: "type_id",
                    data: [],
                    mdi: "scrummer_icon",
                    iconColor: "scrummer_icon_color",
                });
                this.preparePriority();
            }

            if (this.is_sub_item() && !this.edit) {
                this.$("#add-task-modal-project").attr("readonly", 1);
                this.$("#new_item_modal_parent_name").val(this.parent.name);
                this.$(".modal-content h4").html("<i class='mdi mdi-subdirectory-arrow-right'/> Add subtask");

            } else {
                this.$(".parent").hide();
            }

            return this._super();
        },
        addedToDOM() {
            if (this.edit) {
                this.$(".materialnote").parent().hide();
            }
            return this._super();
        },
        getAllowedTypes() {
            const allowedTypes = {};

            const task_types = this.parent ? this.types[this.parent.type_id[0]].type_ids : this.project_types;
            const table_allowed_task_types = this.board.table_task_type_ids;

            if (table_allowed_task_types && table_allowed_task_types.length > 0) {
                for (const type_id of task_types) {
                    if (table_allowed_task_types.includes(type_id)) {
                        allowedTypes[type_id] = this.types[type_id];
                    }
                }
            } else {
                for (const type_id of task_types) {
                    allowedTypes[type_id] = this.types[type_id];
                }
            }
            return allowedTypes;
        },
        getSelectedType(allowedTypes) {
            return this.edit ? this.edit.type_id[0]
                : Object.keys(allowedTypes).length === 1 ? Object.keys(allowedTypes)[0]
                    : this.currentProjectId ? this.project.default_task_type_id[0] : null;
        },
        projectChanged() {
            const thisModal = this;
            $.when(
                DataServiceFactory.get("project.project", true).getRecord(this.currentProjectId),
                scrummer_data.cache.get("project.type.task_types_priorities", {id: this.currentProjectId})).then((project, result) => {
                Object.assign(this, result);
                this.project = project;
                const allowedTypes = this.getAllowedTypes();
                const selectedType = this.getSelectedType(allowedTypes);
                this.prepareSelection({
                    field: "type_id",
                    data: allowedTypes,
                    mdi: "scrummer_icon",
                    iconColor: "scrummer_icon_color",
                    selectedValue: selectedType,
                    changeHandler: function () {
                        thisModal.preparePriority(this.value);
                        this.value && thisModal.types[this.value].allow_story_points
                            ? thisModal.$(".estimate").show()
                            : thisModal.$(".estimate").hide();
                    }
                });
                const selectedPriority = this.edit ? this.edit.priority_id[0] : null;
                this.preparePriority(selectedType, selectedPriority);
            });

        },
        preparePriority(type_id, priority_id) {
            if (!type_id) {
                this.prepareSelection({
                    field: "priority_id",
                    data: []
                });
                return;
            }
            const prioritiesForType = this.types[type_id].priority_ids.map((key) => this.priorities[key]);
            const defaultPriority = priority_id || this.types[type_id].default_priority_id;
            this.prepareSelection({
                field: "priority_id",
                data: prioritiesForType,
                mdi: "scrummer_icon",
                iconColor: "scrummer_icon_color",
                selectedValue: defaultPriority
            });
            this.$("form [name=priority_id]").valid();
        },
        populateFieldValues() {
            this.$("input[name=name]").val(this.edit.name.trim());
            this.$("input[name=story_points]").val(this.edit.story_points);

            this.formated_time = helpers.time.format(this.edit.planned_hours);
            this.$("input[name=planned_hours]").val(this.formated_time);

            this.$("input[name=date_deadline]").val(this.edit.date_deadline);
            this.$(".modal-submit").text("Update");
        },
        populateMaterialNote() {
            this.$(".materialnote").code(this.edit.description);
        },
        setEditingState() {
            if (this.edit) {
                if (this.edit._is_dataservice) {
                    this.editingPromise = $.Deferred();
                    this.edit._edit(this.editingPromise);
                }
                if (this.edit.parent_id) {
                    DataServiceFactory.get("project.task").getRecord(this.edit.parent_id[0]).then((record) => {
                            this.parentRecord = record;
                            this.parentEditingPromise = $.Deferred();
                            this.parentRecord._edit(this.parentEditingPromise);
                        }
                    );
                }
            }
        },
        setDefaultState() {
            if (this.edit) {
                if (this.edit._is_dataservice) {
                    this.editingPromise.resolve();
                }
                if (this.edit.parent_id) {
                    this.parentEditingPromise.resolve();
                }
            }
        },
    });

    const TaskStageConfirmationModal = ModalWidget.extend({
        template: "scrummer.widget.modal.task_stage_confirmation",
        focus: "name",
        init(parent, options) {
            this._super(parent, options);
            this._require_prop("taskId");
            this._require_prop("stageId");
            this._require_prop("stageName");
            this._require_prop("userName");

            // It is possible that the task is unassigned.
            // Q: Should we automatically assign task to the current user when changing state if there is no user defined on task?
            //this._require_prop("userId");
        },
        willStart() {
            return $.when(this._super(), scrummer_data.cache.get("current_user").then((user) => scrummer_data.cache.get("team_members", {teamId: user.team_id[0]})).then((members) => {
                this.members = members;
            }));
        },

        renderElement() {
            this._super(arguments);
            this.resolutionMany2one = new Many2One(this, {
                label: _t("Resolution"),
                model: "project.task.resolution",
                field_name: "resolution_id",
            });
            this.resolutionMany2one.insertAfter(this.$("input[name='stage_id']").closest(".input-field"));
        },

        loadData(confirmation) {
            confirmation.log_message = Boolean(confirmation.log_message);
            confirmation.message = this.$(".materialnote").code();
        },

        submit(confirmation, form) {
            const taskId = form.find("#task_id").val();
            confirmation.stageName = this.stageName;
            const payload = {
                "values": {
                    stage_id: confirmation.stage_id,
                    resolution_id: confirmation.resolution_id
                },
                "message": confirmation.message,
                "log_message": confirmation.log_message,
            };
            return scrummer_data.session.rpc(`/scrummer/web/data/task/${taskId}/confirm_stage_change`, payload);
        },

        start() {
            // TODO: initialize those from qweb template
            this.$("#task_id").val(this.taskId);
            this.$("#stage_id").val(this.stageId);
            this.$("#stage_name").val(this.stageName);
            this.$("#user_name").val(this.userName);

            return this._super();
        }
    });

    const WorkLogModal = ModalWidget.extend({
        _name: "WorkLogModal",
        template: "scrummer.widget.modal.work_log",
        focus: "unit_amount",
        init(parent, options) {
            this._super(parent, options);
            this._require_obj("task");
            if (!this.task._is_dataservice) {
                throw new Error("task option must be instance of dataservice!");
            }
            this._require_prop("userId");
        },
        setEditingState() {
            if (this.task && this.task._is_dataservice) {
                this.editingPromise = $.Deferred();
                this.task._edit(this.editingPromise);
            }
        },
        setDefaultState() {
            if (this.task && this.task._is_dataservice) {
                this.editingPromise.resolve();
            }
        },
        loadData(worklog) {
            worklog.user_id = this.edit ? this.edit.user_id[0] : this.userId;
            worklog.task_id = this.task.id;

            const unit_amount_raw = this.$("#work_log_modal_unit_amount").val();
            try {
                if (unit_amount_raw) {
                    worklog.unit_amount = helpers.time.parse(unit_amount_raw);
                }
            } catch (e) {
                console.error(e);
                return;
            }


        },
        submit(worklog) {
            const aal_dataset = scrummer_data.getDataSet('account.analytic.line');
            worklog.is_timesheet = true;
            worklog.project_id = this.task.project_id[0];
            if (this.edit) {
                return aal_dataset.write(this.edit.id, worklog).then(() => {
                    const aal_service = DataServiceFactory.get("account.analytic.line");
                    return aal_service.updateRecord([this.edit.id]).then(() => aal_service.getRecord(this.edit.id));
                });
            }

            return aal_dataset.create(worklog);

        },
        renderElement() {
            this._super();
            this.$('#work_log_modal_task_name').val(this.task.name);
            if (!this.edit) {
                this.$('#work_log_modal_date').val(moment().format("YYYY-MM-DD"));
            }
        },
        start() {
            this.$('.datepicker').pickadate({
                format: 'yyyy-mm-dd',
                selectMonths: true,
                selectYears: 1
            });

            return this._super();
        },
        addedToDOM() {
            this._super();
            this.$(".unit_amount_help").tooltip({
                tooltip: "Combine: w-weeks, d-days, h-hours, m-minutes. (1 day means 8 hours) Separate with space.",
                position: "left",
            });
        },
        populateFieldValues() {
            this.$('#work_log_modal_date').val(this.edit.date);
            this.formated_time = helpers.time.format(this.edit.unit_amount);
            this.$('#work_log_modal_unit_amount').val(this.formated_time);
            this.$('#work_log_modal_name').val(this.edit.name);
            this.$('.modal-submit').text("Update");
        },
        populateMaterialNote() {
            return;
        },
        getValidateOptions() {
            return {
                ...this._super(),
                ...{
                    rules: {
                        name: {
                            required: true,
                            minlength: 15
                        },
                        unit_amount: {
                            required: true,
                            "scrummer.time": true
                        },
                    }
                }
            };
        },
    });

    const LinkItemModal = ModalWidget.extend({
        _name: "LinkItemModal",
        template: "scrummer.widget.modal.link_item",
        focus: "relation_id",
        init(parent, options) {
            this._super(parent, options);
            this._require_obj("task");
            if (!this.task._is_dataservice) {
                throw new Error("task option must be instance of dataservice!");
            }
        },
        setEditingState() {
            if (this.task && this.task._is_dataservice) {
                this.editingPromise = $.Deferred();
                this.task._edit(this.editingPromise);
            }
        },
        setDefaultState() {
            if (this.task && this.task._is_dataservice) {
                this.editingPromise.resolve();
            }
        },
        willStart() {
            return $.when(this._super(), DataServiceFactory.get("project.task.link.relation").getAllRecords().then((relations) => {
                Object.assign(this, {relations});
            }));
        },
        loadData(link) {
            link.comment = this.$(".materialnote").code();
            link.task_left_id = this.task.id;
        },
        submit(link) {
            return scrummer_data.session.rpc('/scrummer/web/data/task/create_link', {link});
        },
        start() {
            this.prepareSelection({
                field: "relation_id",
                data: this.relations
            });
            this.taskRight = new Many2One(this, {
                label: _t("With item"),
                model: "project.task",
                field_name: "task_right_id",
                domain: this.task_ids ? [["id", "in", this.task_ids]] : scrummer_data.cache.get("current_user")
                    .then((user) => [["id", "!=", this.task_id], ["project_id", "in", user.team_ids[user.team_id[0]].project_ids]])
            });
            this.taskRight.insertAfter(this.$("#task_right_anchor"));

            return this._super();
        },
        getValidateOptions() {
            return {
                ...this._super(),
                ...{
                    rules: {
                        relation_id: "required",
                        task_right_id: "required",
                    },
                }
            };
        },
    });

    const CommentItemModal = ModalWidget.extend({
        _name: "CommentItemModal",
        template: "scrummer.widget.modal.comment_item",
        init(parent, options) {
            this._super(parent, options);
            this._require_obj("task");
            if (!this.task._is_dataservice) {
                throw new Error("task option must be instance of dataservice!");
            }
        },
        setEditingState() {
            if (this.task && this.task._is_dataservice) {
                this.editingPromise = $.Deferred();
                this.task._edit(this.editingPromise);
            }
        },
        setDefaultState() {
            if (this.task && this.task._is_dataservice) {
                this.editingPromise.resolve();
            }
        },
        willStart() {
            return $.when(this._super(),
                scrummer_data.xmlidToResId("mail.mt_comment").then((id) => {
                    this.commentSubtypeId = id;
                })
            );
        },
        renderElement() {
            this._super();
            if (this.edit) {
                this.$(".modal-submit").text("Update");
                this.$(".modal-content h4").html("<i class='mdi mdi-comment-account'/> Update comment");
            }
            this.attachmentsWidget = new Attachments.AttachmentsWidget(this, {
                attachments: [],
                res_id: this.task.id,
                res_model: "project.task"
            });
            this.attachmentsWidget.appendTo(this.$(".attachment"));
        },
        loadData(comment) {
            comment.log_message = Boolean(comment.log_message);
            comment.body = this.$(".materialnote").code();
            comment.attachment_ids = this.attachmentsWidget.getIds();
        },
        submit(comment) {
            if (!this.edit) {
                return scrummer_data.session.rpc(`/scrummer/web/data/task/${this.task.id}/add_comment`, {comment});
            }

            return scrummer_data.session.rpc(`/scrummer/web/data/task/${this.task.id}/update_comment/${this.edit.id}`, {comment});

        },
        populateFieldValues() {
            if (this.edit.subtype_id[0] === this.commentSubtypeId) {
                this.$("input[name='log_message']").prop('checked', true);
            }
        },
        populateMaterialNote() {
            this.$(".materialnote").code(this.edit.body);
        }
    });

    return {
        ModalWidget,
        NewItemModal,
        TaskStageConfirmationModal,
        WorkLogModal,
        LinkItemModal,
        CommentItemModal,
    };
});
