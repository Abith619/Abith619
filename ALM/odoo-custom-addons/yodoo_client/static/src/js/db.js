odoo.define('yodoo_client.db_expiry', function (require) {
    "use strict";

    var WebClient = require('web.WebClient');
    var ajax = require('web.ajax');
    var core = require('web.core');
    var qweb = core.qweb;
    var session = require('web.session');

    ajax.loadXML('/yodoo_client/static/src/xml/db.xml', qweb);

    WebClient.include({
        events: {
            'click #accept_message_expiry': '_yodoo_click_db_expiry_ok',
        },
        start: function () {
            this.yodoo_check_db_expiry();
            this._super.apply(this, arguments);
        },

        yodoo_show_db_expiry: function (data) {
            var serie = session.server_version_info[0];
            var t = $(qweb.render('yodoo_client.db.expiry', data));
            $('.o_web_client').prepend(t);
            if (data.days2expiry < 1) {
                this.yodoo_hide_main(serie);
            }
        },

        yodoo_hide_main: function (serie) {
            if (serie === 11) {
                $('.o_main').hide("fast");
                $('#oe_main_menu_navbar').hide("fast");
            } else if (serie === 12) {
                $('.o_main').hide("fast");
                $('.o_main_navbar').hide("fast");
            } else {
                $('.o_action_manager').hide("fast");
                $('.o_main_navbar').hide("fast");
            }
        },

        yodoo_check_db_expiry: function () {
            var self = this;
            var url = '/saas/client/db/state/get';
            ajax.jsonRpc(url).then(
                function (result) {
                    if (result) {
                        var ame = result.accepted_message_expiry;
                        if (ame) {
                            setTimeout(
                                self.yodoo_check_db_expiry.bind(self),
                                60 * 1000);
                        } else if (result.expiry_type) {
                            self.yodoo_show_db_expiry(result);
                        } else {
                            setTimeout(
                                self.yodoo_check_db_expiry.bind(self),
                                60 * 1000);
                        }
                    }
                });
        },

        _yodoo_click_db_expiry_ok: function (e) {
            var self = this;
            e.preventDefault();
            ajax.jsonRpc(
                "/saas/client/db/expiry/accept",
                "call").then(function (data) {
                if (data.result === "ok") {
                    $(e.target)
                        .closest("#yodoo-client-db-expiry")
                        .hide("fast");
                    $('#yodoo-client-db-expiry').remove();
                    setTimeout(
                        self.yodoo_check_db_expiry.bind(self), 10000);
                }
            });
        },
    });
});
