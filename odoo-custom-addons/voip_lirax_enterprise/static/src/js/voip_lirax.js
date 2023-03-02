odoo.define('voip.lirax', function (require) {
    "use strict";

    var core = require('web.core');
    var VoipUserAgent = require('voip.user_agent');
    var basic_fields = require('web.basic_fields');
    var _t = core._t;
    var clean_number = function (number) {
        return number.replace(/[\s-/.\u00AD]/g, '');
    };
    var CALL_STATE = {
        NO_CALL: 0,
        RINGING_CALL: 1,
        ONGOING_CALL: 2,
    };

    VoipUserAgent.include({

        //--------------------------------------------------------------------------
        // Private
        //--------------------------------------------------------------------------

        /**
         * @override
         */
        hangup: function () {
            if (this.mode === "demo") {
                if (this.callState === CALL_STATE.ONGOING_CALL) {
                    this._onBye();
                } else {
                    this._onCancel();
                }
            } else {
                try {
                    this._finish();
                } catch (err) {
                    console.error('Cancel failed:', err);
                }
            }

        },
        /**
         * @override
         */
        makeCall: function (number) {
            if (this.mode === "demo") {
                var self = this;
                this.timerAccepted = setTimeout(function () {
                    self._onAccepted();
                }, 3000);
                return;
            }
            this._makeCall(number);
        },
        /**
         * @override
         */
        sendDtmf: function (number) {
            if (this.callState === CALL_STATE.ONGOING_CALL && this.mode !== "demo") {
                this.userAgent.sendDTMF(this.sipSession.line, number);
            }
        },
        /**
         * @override
         */
        transfer: function (number) {
            if (this.callState === CALL_STATE.ONGOING_CALL && this.mode !== "demo") {
                this.sipSession.toggleForward();
                this.userAgent.makeCall(number);
            }
        },
        /**
         * @override
         */
        _configureDomElements: function () {
            this.incomingtone = document.createElement("audio");
            this.incomingtone.loop = "true";
            this.incomingtone.src = "/voip/static/src/sounds/incomingcall.mp3";
            $("html").append(this.incomingtone);
        },
        /**
         * @override
         */
        _createUa: function (params) {
            if (!(params.login && params.password)) {
                this._triggerError(_t('Your credentials are not correctly set. Please check your configuration.'));
                return false;
            }
            try {
                var phone = new XPhone();
                // phone.wsURL = params.wsServer;
                phone.init(params);
                return phone;
            } catch (err) {
                this._triggerError(_t('The server configuration could be wrong. Please check your configuration.'));
                return false;
            }
        },
        /**
         * Listener for onCreate.
         *
         * @private
         * @param {Object} call
         */
        _createCall: function (call) {
            if (!this.sipSession) {
                this.sipSession = call;
            }
            if (call.type === this.userAgent.INCOMING) {
                return this._onInvite(call);
            }
        },
        /**
         * Listener for onConnect.
         *
         * @private
         * @param {Object} call
         */
        _onConnect: function (call) {
            if (call.type === this.userAgent.OUTGOING) {
                return this._onAccepted();
            }
        },

        /**
         * Listener for _onDestroy.
         *
         * @private
         */
        _onDestroy: function () {
            if (this.callState === CALL_STATE.ONGOING_CALL) {
                this._onBye();
            } else {
                this._onCancel();
            }

        },
        /**
         * Handles the sip session ending.
         *
         * @private
         * * @param {Object} call
         */
        _finish: function (call) {
            if (!call) {
                call = this.sipSession
            }
            this.userAgent.finishCall(call.line);
        },
        /**
         * Initialises the ua, binds events and appends audio in the dom.
         *
         * @private
         * @param {Object} result user and pbx configuration return by the rpc
         */
        _initUa: function (result) {
            this.infoPbxConfiguration = result;
            this.mode = result.mode;
            if (this.mode === "prod") {
                this.trigger_up('sip_error', {msg: _t("Connecting..."), connecting: true});
                if (!window.RTCPeerConnection) {
                    this._triggerError(_t('Your browser could not support WebRTC. Please check your configuration.'));
                    return;
                }
                this.userAgent = this._createUa(result);
                if (!this.userAgent) {
                    return;
                }
                this.alwaysTransfer = result.always_transfer;
                this.ignoreIncoming = result.ignore_incoming;
                if (result.external_phone) {
                    this.externalPhone = clean_number(result.external_phone);
                }
                var self = this;
                if (this.alwaysTransfer) {
                    self.userAgent.callOut = self.externalPhone;
                }
                // catch the error if the ws uri is wrong
                this.userAgent.onError = function (error) {
                    console.error('Error ', error);
                    return self._triggerError(_t('The websocket uri could be wrong.') +
                        _t(' Please check your configuration.'));
                };
                this.userAgent.onOpen = function () {
                    return self._onRegistered()
                };
                this.userAgent.onDestroy = function () {
                    return self._onDestroy()
                };
                this.userAgent.onCreate = function (call) {
                    return self._createCall(call)
                };
                this.userAgent.onConnect = function (call) {
                    return self._onConnect(call)
                };
            }
            this._configureDomElements()
        },
        /**
         * @override
         */
        _makeCall: function (number) {
            if (this.callState !== CALL_STATE.NO_CALL) {
                return;
            }
            try {
                number = clean_number(number);
                this.userAgent.makeCall(number);
            } catch (err) {
                this._triggerError(_t('the connection cannot be made. ') +
                    _t('Please check your configuration.</br> (Reason receives :') +
                    err.reason_phrase + ')');
                return;
            }
            this._setupOutCall();
        },
        /**
         * @override
         */
        _setupOutCall: function () {
            this.callState = CALL_STATE.RINGING_CALL;
        },
        /**
         * @override
         */
        _toggleMute: function (mute) {
            var call = this.sipSession;
            this.userAgent.holdCall(call.line);
        },
        /**
         * @override
         */
        _onAccepted: function () {
            this.callState = CALL_STATE.ONGOING_CALL;
            this.trigger_up('sip_accepted');
        },
        /**
         * @override
         */
        _onBye: function () {
            this.sipSession = false;
            this.callState = CALL_STATE.NO_CALL;
            this.trigger_up('sip_bye');
            if (this.mode === "demo") {
                clearTimeout(this.timerAccepted);
            }
        },
        /**
         * @override
         */
        _onCancel: function () {
            var self = this;

            function _rejectInvite() {
                if (!this.incomingCall) {
                    self.incomingtone.pause();
                    self._finish();
                }
            }

            if (this.notification) {
                self.notification.removeEventListener('close', _rejectInvite);
                self.notification.close('rejected');
                self.notification = undefined;
                self.incomingtone.pause();
            } else if (self.dialog && self.dialog.$el.is(":visible")) {
                self.dialog.close();
            }
            this.sipSession = false;
            this.callState = CALL_STATE.NO_CALL;
            this.trigger_up('sip_cancel');
            if (this.mode === "demo") {
                clearTimeout(this.timerAccepted);
            }
        },
        /**
         * @override
         */
        _onInvite: function (inviteSession) {
            if (this.ignoreIncoming || this.callState === CALL_STATE.ONGOING_CALL) {
                this._finish(inviteSession);
                return;
            }
            var self = this;
            var name = '';
            var number = inviteSession.phoneNumber;
            this._rpc({
                model: 'res.partner',
                method: 'search_read',
                domain: [
                    '|',
                    ['sanitized_phone', 'ilike', number],
                    ['sanitized_mobile', 'ilike', number],
                ],
                fields: ['id', 'display_name'],
                limit: 1,
            }).then(function (contacts) {
                    var incomingCallParams = {
                        number: number
                    };
                    var contact = false;
                    if (contacts.length) {
                        contact = contacts[0];
                        name = contact.display_name;
                        incomingCallParams.partnerId = contact.id;
                    }
                    var content = _t("Incoming call from ");
                    if (name) {
                        content += name + ' (' + number + ')';
                    } else {
                        content += number;
                    }
                    self.incomingtone.currentTime = 0;
                    self.incomingtone.play();

                    self.notification = self._sendNotification('Odoo', content);

                    function _rejectInvite() {
                        if (!self.incomingCall) {
                            self.incomingtone.pause();
                            try {
                                self._finish(inviteSession);
                            } catch (e) {
                            }
                        }

                    }

                    if (self.notification) {
                        self.notification.onclick = function () {
                            window.focus();
                            self._answerCall(inviteSession, incomingCallParams);
                            this.close();
                        };
                        self.notification.addEventListener('close', _rejectInvite);
                    } else {
                        var options = {
                            confirm_callback: function () {
                                self._answerCall(inviteSession, incomingCallParams);
                            },
                            cancel_callback: function () {
                                try {
                                    self._finish(inviteSession);
                                } catch (err) {
                                    console.error('Reject failed:', err);
                                }
                                self.incomingtone.pause();
                            },
                        };
                        self.dialog = Dialog.confirm(self, content, options);
                        self.dialog.on('closed', self, function () {
                            if (inviteSession && self.callState !== CALL_STATE.ONGOING_CALL) {
                                try {
                                    self._finish(inviteSession);
                                } catch (err) {
                                    console.error('Reject failed:', err);
                                }
                            }
                            self.incomingtone.pause();
                        });
                    }
                }
            );
        },
    });
    /**
     * Override of FieldPhone to use the DialingPanel to perform calls on clicks.
     */
    var Phone = basic_fields.FieldPhone;
    Phone.include({
        events: _.extend({}, Phone.prototype.events, {
            'click': '_onClick',
        }),

        //--------------------------------------------------------------------------
        // Handlers
        //--------------------------------------------------------------------------

        /**
         * Called when the phone number is clicked.
         *
         * @private
         * @param {MouseEvent} e
         */
        _onClick: function (e) {
            if (this.mode === 'readonly') {
                var pbxConfiguration;
                this.trigger_up('get_pbx_configuration', {
                    callback: function (output) {
                        pbxConfiguration = output.pbxConfiguration;
                    },
                });
                if (
                    pbxConfiguration.mode !== "demo" ||
                    (
                        pbxConfiguration.pbx_ip &&
                        pbxConfiguration.wsServer &&
                        pbxConfiguration.login &&
                        pbxConfiguration.password
                    )
                ) {
                    e.preventDefault();
                    var phoneNumber = this.value;
                    this._call(phoneNumber);
                }
            }
        },
    });
});
