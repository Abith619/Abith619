// Copyright 2017 - 2018 Modoolar <info@modoolar.com>
// License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

odoo.define('scrummer.attachments', (require) => {
    "use strict";
    const scrummer_data = require('scrummer.data');
    const BaseWidgets = require('scrummer.BaseWidgets');
    const AbstractModelList = require('scrummer.abstract_model_list');
    const dialog = require('scrummer.dialog');
    const _t = require('web.core')._t;
    const Waves = window.Waves;

    /**
     * This widgets looks and reacts differently according to its state.
     * It can be downloadable, which means that attachment is already stored, and download can be initiated.
     * When widget has downloadable set to true, it enables user to delete the attachment.
     * When user selects a file, or drag&drop file to AttachmentsWidget, an non downloadable AttachmentsItem widget
     * gets created and rendered. Until file gets uploaded and prepared for download, this widget provides user
     * with visual feedback that file upload is in progress, and gives user an ability to abort file upload.
     */
    const AttachmentsItem = AbstractModelList.AbstractModelListItem.extend({
        template: "scrummer.attachments.item",
        max_upload_size: 25 * 1024 * 1024,
        init(parent, options) {
            this._super(parent, options);
            this.record = this.record || {};
            if (!this.record.downloadable) {
                this._require_obj("record", ['file', 'res_model', 'res_id', 'convertTimeout']);
                this.record.name = this.record.file.name;
                this._fileUploadedDef = $.Deferred();
                this.fileUploaded = this._fileUploadedDef.promise();
            }
        },
        willStart() {
            const superPromise = this._super();
            if (this.record.downloadable) {
                return $.when(superPromise, this.prepareUserImage());
            }
            return superPromise;
        },
        prepareUserImage() {
            return scrummer_data.cache.get("get_user", {id: this.record.create_uid[0]}).then((user) => {
                this.user_image_url = scrummer_data.getImage("res.users", user.id, user.write_date);
            });
        },
        renderElement() {
            this._super();
            if (this.record.downloadable) {
                this.$el.addClass("downloadable");
                this.$el.addClass("complete");
            }
        },
        start() {
            if (this.record.downloadable) {
                this.$(".delete").click(this.remove.bind(this));
            } else {
                // This is a case of uploading/creating new attachment
                this.loadFile(this.record.file);
                this.$(".abort").click(this.destroy.bind(this));
                this.$(".retry").click(() => {
                    this.$el.removeClass("with-error");
                    this.loadFile(this.record.file);
                });

            }
            this.$(".tooltipped").tooltip();
            return this._super();
        },
        loadFile(file) {
            if (file.size > this.max_upload_size) {
                this.$el.addClass("with-error");
                const maxUploadMB = (this.max_upload_size / 1024) / 1024;
                this.setError(_t("File exceed the maximum file size of ") + maxUploadMB + "MB");
                this.setProgress(0);
                this.$(".retry").hide();
                return false;
            }
            this.setStatus(_t("Preparing file..."));
            this.setProgress(false);
            const fileReader = new FileReader();
            const self = this;
            fileReader.onloadend = (upload) => {
                let data = upload.target.result;
                data = data.split(',')[1];
                self.uploadFile(data);
            };
            fileReader.readAsDataURL(file);
        },
        setError(error) {
            this.$(".error").text(error);
        },
        setStatus(status) {
            this.$(".status").text(status);
        },
        setProgress(progress) {
            if (progress === false) {
                //show indeterminate progress bar
                this.$(".progress").empty().append($('<div class="indeterminate"/>'));
            } else if (Number(progress) === progress && progress >= 0 && progress <= 1) {
                this.$(".progress").empty().append($('<div class="determinate" style="width: ' + (progress * 100) + '%"/>'));
            } else {
                throw new Error("Illegal argument");
            }
        },
        uploadFile(file_base64) {
            if (this.record.file.size === false) {
                this.setError(_t("Browser couldn't load file"));
            } else {
                this.setStatus(_t("Uploading file..."));
                scrummer_data.getDataSet("ir.attachment").create({
                    res_id: this.record.res_id,
                    res_model: this.record.res_model,
                    name: this.record.file.name,
                    datas: file_base64,
                    datas_fname: this.record.file.name
                }).then(this.onFileUploaded.bind(this), this.onFileUploadError.bind(this));
            }
        },
        onFileUploaded(id) {
            this._fileUploadedDef.resolve(arguments);
            this.setId(id);
            this.setProgress(1);
            this.$(".delete").click(this.remove.bind(this));
            this.$el.addClass("complete");
            this.attachmentLoaded = scrummer_data.getDataSet("ir.attachment").read_ids([id], ["name", "datas_fname", "local_url", "create_uid", "create_date",]);
            setTimeout(this.convertToLink.bind(this), this.record.convertTimeout);
        },
        onFileUploadError() {
            this._fileUploadedDef.reject(arguments);
            this.setProgress(0);
            this.$el.addClass("with-error");
            this.setError(_t("Error while uploading file"));
        },
        convertToLink() {
            this.attachmentLoaded.then((result) => {
                const attachment = result[0];
                Object.assign(this.record, attachment);
                this.record.downloadable = true;
                this.$el.addClass("downloadable");
                this.$(".name").html(`<a href="${this.record.local_url}" download="${this.record.datas_fname}" target="_blank">${this.record.name}</a>`);
                this.prepareUserImage().then(() => {
                    const image = $(`<img src="${this.user_image_url}" class="circle valign image tooltipped"
                    data-position="bottom" data-delay="50" data-tooltip="${this.record.create_uid[1]} @ ${this.record.create_date}"/>`);
                    image.insertBefore(this.$(".meta"));
                    image.tooltip();
                });

            });
        },
        remove() {
            dialog.confirm(_t("Delete attachment"), _t("Are you sure you want to delete this attachment?"), _t("yes")).done(() => {
                this.dataset.unlink([this.record.id]).then(() => {
                    this.trigger_up("remove_attachment", {id: this.record.id});
                });
            });
        },
        destroy() {
            if (this.__destroying) {
                this._super();
            } else {
                this.__destroying = true;
                this.$el.addClass("fade-out");
                const self = this;
                this.$el.one('webkitAnimationEnd oanimationend msAnimationEnd animationend', () => self.destroy());
            }
        }
    });
    AttachmentsItem.sort_by = "create_date";

    const AttachmentsWidget = BaseWidgets.AgileBaseWidget.extend({
        template: "scrummer.attachments",
        multiple: true,
        convertTimeout: 3000,
        custom_events: {
            'remove_attachment': function (evt) {
                this.attachmentsList.removeItem(evt.data.id);
            }
        },
        init(parent, options) {
            Object.assign(this, options);
            this._super(parent, options);
            this._require_prop("res_id");
            this._require_prop("res_model");
            this._require_prop("attachments");
            // All those attachments are already stored, so set downloadable to true
            this.attachments.forEach((e) => {
                e.downloadable = true;
            });
        },
        renderElement() {
            this._super();
            this.$(".attachments-input").attr("multiple", this.multiple);
            this.attachmentsList = new AbstractModelList.ModelList(this, {
                model: "ir.attachment",
                data: this.attachments,
                ModelItem: AttachmentsItem,
            });
            this.attachmentsList.appendTo(this.$el);
        },
        start() {
            this.initDragAndDrop();
            this.$(".upload-files").click(() => this.$(".attachments-input").trigger("click"));
            this.$(".attachments-input").change((e) => this.uploadFiles(e.target.files));
            return this._super();
        },
        initDragAndDrop() {
            let dragCounter = 0;
            const removeTimeout = setTimeout(() => this.$el.removeClass('waves-effect'), 700);
            let captureDragover = false;
            const finalizeWave = () => {
                Waves.calm(this.$el[0]);
                this.$el.removeClass('is-dragover');
            };
            this.$el.on('drag dragstart dragend dragover dragenter dragleave drop', (e) => {
                e.preventDefault();
                e.stopPropagation();
            })
                .on('dragover dragenter dragstart', (e) => {
                    this.$el.addClass('is-dragover');
                    if ((e.type === "dragenter" || e.type === "dragstart") && dragCounter++ === 0) {
                        captureDragover = true;
                    }
                    if (e.type === "dragover" && captureDragover) {
                        captureDragover = false;
                        clearTimeout(removeTimeout);
                        this.$el.addClass('waves-effect');
                        window.Waves.ripple(this.$el[0], {
                            wait: 999999,
                            position: {
                                // This position relative to HTML element. Unit: px
                                x: e.originalEvent.layerX,
                                y: e.originalEvent.layerY
                            }
                        });
                    }
                })
                .on('dragleave dragend drop', (e) => {
                    if (e.type === "dragleave" && --dragCounter === 0) {
                        finalizeWave();
                    }
                })
                .on('drop', (e) => {
                    finalizeWave();
                    const droppedFiles = e.originalEvent.dataTransfer.files;
                    this.uploadFiles(droppedFiles);
                    dragCounter = 0;
                });
        },
        uploadFiles(fileList) {
            if (fileList.length > 0) {
                const attachmentPromises = [];
                this.trigger_up("attachment_upload_started");
                for (const file of fileList) {
                    const item = this.attachmentsList.addItem({
                        // attributes: {"data-id": item.id},
                        file: file,
                        res_id: this.res_id,
                        res_model: this.res_model,
                        convertTimeout: this.convertTimeout,
                        dataset: scrummer_data.getDataSet("ir.attachment"),
                        order_field: AttachmentsItem.sort_by
                    });
                    attachmentPromises.push(item.fileUploaded);
                }
                $.when(...attachmentPromises).always(() => this.trigger_up("attachment_upload_finished"));
            }
        },
        getIds() {
            return [...this.attachmentsList.list.keys()].filter((x) => x);
        }
    });
    return {
        AttachmentsWidget,
        AttachmentsItem
    };
});
