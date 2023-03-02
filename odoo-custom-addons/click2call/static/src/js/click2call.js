odoo.define('click2call.fields', function (require) {
    "use strict";

    var basicFields = require('web.basic_fields');
    var core = require('web.core');
    var session = require('web.session');

    var _t = core._t;

    /**
     * Override of FieldPhone to add a button calling SMS composer if option activated (default)
     */

    var Phone = basicFields.FieldPhone;
    Phone.include({
        //--------------------------------------------------------------------------
        // Private
        //--------------------------------------------------------------------------

        /**
         * Api call 
         *
         * @private
         */
         _onClick2Call: function (ev) {
            ev.preventDefault();
            ev.stopPropagation();
            if (!session.click2call_url) {
                this.do_warn(_t('Configuration Error'), _t('Click2call API URL not found. please configure it from general setting menu'));
                return;
            }
            if (!session.premium_extension) {
                // this.do_warn(_t('User Error'), _t('Premium Extension not set on current login user. please set it from user form view'));
                return;
            }
            let url = new URL(session.click2call_url);
            url.searchParams.set('user_id', session.premium_extension);
            url.searchParams.set('remoto', this.value);
            fetch(url.href).then(function (response) {
                return response.json();
            })
            .then(function (myJson) {
                console.log(myJson);
            })
            .catch(function (error) {
                console.log("Error: " + error);
            });
        },

        /**
         * Add a button to call the composer wizard
         *
         * @override
         * @private
         */
        _renderReadonly: function () {
            var def = this._super.apply(this, arguments);
            var $composerButton = $('<a>', {
                title: _t('Click 2 Call'),
                href: '',
                class: 'ml-3 d-inline-flex align-items-center o_field_phone_sms',
                html: $('<small>', { class: 'font-weight-bold ml-1', html: 'Call' }),
            });
            $composerButton.prepend($('<i>', { class: 'fa fa-mobile' }));
            $composerButton.on('click', this._onClick2Call.bind(this));
            this.$el = this.$el.add($composerButton);
            return def;
        },
    });

    return Phone;

});

