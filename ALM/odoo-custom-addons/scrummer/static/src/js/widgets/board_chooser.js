// Copyright 2017 - 2018 Modoolar <info@modoolar.com>
// License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

odoo.define('scrummer.board_chooser', function (require) {
    "use strict";

    const ScrummerData = require('scrummer.data');
    const AbstractModelList = require('scrummer.abstract_model_list');
    const AgileBaseWidget = require('scrummer.BaseWidgets').AgileBaseWidget;
    const storage_service = require('scrummer.storage_service');
    const DataServiceFactory = require('scrummer.data_service_factory');
    const hash_service = require('scrummer.hash_service');
    const _t = require('web.core')._t;
    const crash_manager = require('web.crash_manager');

    const BoardListItem = AgileBaseWidget.extend({
        _name: "BoardListItem",
        template: "scrummer.list.board_chooser_item",
        init(parent, options) {
            this._super(parent, options);
            Object.assign(this, options);
        },
        start() {
            if (this.id === hash_service.get("board")) {
                this.destroy();
            } else {
                // When clicked on project in dashboard, fetch all boards and open last board.
                this.$("a").click(() => {
                    this.selectBoard();
                });
            }
            return this._super();
        },
        selectBoard() {
            this.trigger_up("set_board", {id: this.record.id});
            this.destroy();
        }
    });
    BoardListItem.sort_by = "id";
    const BoardChooser = AgileBaseWidget.extend({
        _name: "BoardChooser",
        template: "scrummer.board_chooser",
        custom_events: {
            'set_board': '_onSetBoard',
        },
        _onSetBoard(evt) {
            this.setBoard(evt.data.id);
        },
        init(parent, options) {
            Object.assign(this, options);
            this._super(parent, options);
            this.current_board = parseInt(hash_service.get("board"), 10);
            this.current_project = parseInt(hash_service.get("project"), 10);
        },
        willStart() {
            return $.when(
                this._super(),
                // Store reference to current_user, so that we can use it in synchronous methods
                ScrummerData.cache.get("current_user").then((user) => {
                    this.user = user;
                }),
                // If current_project is set, fetch it and store so that it can be used in synchronous project_image_url method
                this.current_project && DataServiceFactory.get("project.project").getRecord(this.current_project).then((project) => {
                    this.project = project;
                })
            ).then(() => {
                const board_service = DataServiceFactory.get("project.agile.board");
                const project_ids = this.current_project ? [this.current_project] : this.user.team_ids[this.user.team_id[0]].project_ids;
                const board_filter = [
                    "|",
                    "&",
                    ["visibility", "=", "global"],
                    ["project_ids", "in", project_ids],

                    "|",
                    "&",
                    "&",
                    ["visibility", "=", "team"],
                    ["team_id", "=", this.user.team_id[0]],
                    ["project_ids", "in", project_ids],

                    "&",
                    "&",
                    ["visibility", "=", "user"],
                    ["user_id", "=", this.user.id],
                    ["project_ids", "in", project_ids],

                ];
                return board_service.dataset.id_search("", board_filter).then((board_ids) => board_service.getRecords(board_ids, true).then((records) => {
                    this.boards = records;
                    if (this.boards.size === 0) {
                        const msgPart = this.project ? _t("Project ") + this.project.name + " does not have"
                            : _t("None of the projects have");
                        crash_manager.show_error({
                            type: _t("Configuration error"),
                            message: msgPart + _t(" board associated with it."),
                            data: {debug: ""}
                        });
                        hash_service.setHash("page", "dashboard");
                        return $.Deferred().reject();
                    }
                    if (!this.boards.has(this.current_board) && this.boards.size > 0) {
                        this.setBoard([...this.boards.keys()][0]);
                    } else {
                        // save current board;
                        this.board = this.boards.get(this.current_board);
                    }
                }));
            });
        },
        setBoard(id) {
            storage_service.set("board", id);

            const boardTypeChanged = typeof this.board === "undefined" ||
                this.board.type !== this.boards.get(id).type;
            hash_service.setHash("board", id, true, boardTypeChanged);

            if (this.board) {
                this.boardList.addItem(this.board);
            }
            this.board = this.boards.get(id);
            if (boardTypeChanged) {
                hash_service.delete("view");
                this.trigger_up("board_type_changed");
            }
            this.$("a.available-boards").html(this.board.name + ' <i class="mdi mdi-menu-down right"></i>');
        },
        start() {
            // Materialize Dropdown
            this.boardList._is_added_to_DOM.then(() => {
                $('.dropdown-button').dropdown({
                    /* eslint-disable no-inline-comments*/
                    inDuration: 300,
                    outDuration: 125,
                    constrain_width: true, // Does not change width of dropdown to that of the activator
                    hover: false, // Activate on click
                    alignment: 'left', // Aligns dropdown to left or right edge (works with constrain_width)
                    gutter: 0, // Spacing from edge
                    belowOrigin: true // Displays dropdown below the button
                });
            });
        },

        renderElement() {
            this._super();
            const data = [...this.boards.values()];
            this.boardList = new AbstractModelList.ModelList(this, {
                model: "project.agile.board",
                // useDataService: true,
                // domain: [["project_ids", "in", this.current_project ? [this.current_project] : user.team_ids[user.team_id[0]].project_ids]],
                data,
                tagName: "ul",
                id: "board-chooser-dropdown",
                className: "dropdown-content",
                ModelItem: BoardListItem
            });
            // Adding backlog task list
            this.boardList.insertAfter(this.$(".available-boards"));
        },

        project_image_url() {
            return this.current_project
                ? ScrummerData.getImage("project.project", this.current_project, this.project.write_date)
                : ScrummerData.getImage("project.agile.team", this.user.team_id[0]);
        }
    });
    return {
        BoardChooser,
        BoardListItem
    };
});
