from datetime import datetime, timedelta
from freezegun import freeze_time
from unittest.mock import patch

from odoo.addons.appointment.tests.common import AppointmentCommon
from odoo.addons.google_calendar.models.res_users import User as GoogleUser
from odoo.addons.google_calendar.tests.test_sync_common import TestSyncGoogle
from odoo.addons.mail.tests.common import mail_new_test_user
from odoo.addons.microsoft_calendar.models.res_users import User as MsftUser
from odoo.addons.microsoft_calendar.tests.common import TestCommon as MsftTestCommon
from odoo.addons.microsoft_calendar.utils.microsoft_calendar import MicrosoftCalendarService

from odoo.tests import users


class TestAppointmentNotificationCommon(AppointmentCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        attendee_ids = cls.env['res.partner'].create([
            {'name': f'p{n}', 'email': f'p{n}@test.lan'} for n in range(2)
        ])

        cls.calendar_event = cls.env['calendar.event'].create({
            'name': 'Test Notification Appointment',
            'appointment_type_id': cls.apt_type_bxls_2days.id,
            'start': datetime(2020, 2, 1, 10),
            'stop': datetime(2020, 2, 1, 11),
            'user_id': cls.apt_manager.id,
            'partner_ids': [(4, cls.apt_manager.partner_id.id)] + [(4, attendee.id) for attendee in attendee_ids],
        })

        cls.apt_type_resource.booked_mail_template_id = cls._create_template('calendar.attendee', {
            'body_html': 'Thanks for booking!',
            'subject': 'Thanks for booking, {{object.common_name}}',
        })


class TestAppointmentNotificationsMail(TestAppointmentNotificationCommon):
    @freeze_time('2020-02-01 09:00:00')
    def test_appointment_cancel_notification_mail(self):
        appointment = self.calendar_event
        self.env.flush_all()
        self.cr.precommit.run()
        with self.mock_mail_gateway():
            appointment.with_context(mail_notify_author=True).action_archive()
            self.env.flush_all()
            self.cr.precommit.run()
        self.assertMailMail(appointment.partner_id, 'sent', author=appointment.partner_id)
        self.assertMailMail(appointment.partner_ids - appointment.partner_id, 'sent', author=appointment.partner_id)


class TestSyncOdoo2GoogleMail(TestSyncGoogle, TestAppointmentNotificationCommon):
    @freeze_time('2020-02-01 09:00:00')
    @patch.object(GoogleUser, '_get_google_calendar_token', lambda user: 'some-token')
    def test_appointment_cancel_notification_gcalendar(self):
        self.env['res.users.settings'].create({'user_id': self.env.user.id})
        self.env.user.res_users_settings_id._set_google_auth_tokens('some-token', '123', 10000)
        appointment = self.calendar_event
        appointment.google_id = 'test_google_id'
        self.env.flush_all()
        self.cr.precommit.run()
        with self.mock_mail_gateway(mail_unlink_sent=False), self.mock_google_sync():
            appointment.action_archive()
            self.env.flush_all()
            self.cr.precommit.run()
        self.assertGoogleEventPatched('test_google_id', {'status': 'cancelled'}, timeout=3)
        self.assertNotSentEmail()


class TestAppointmentNotificationsMicrosoftCalendar(MsftTestCommon, TestAppointmentNotificationCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_public = mail_new_test_user(
            cls.env, login='user_public', groups='base.group_public', name='Public User'
        )
        cls.public_user_booking_partner = cls.env['res.partner'].create({
            'name': 'Booking attendee',
            'email': 'booking.attendee@test.lan',
        })

    def setUp(self):
        super().setUp()
        # attendee user in parent class is created in setUp
        sync_paused_attendee = self.attendee_user.copy(default={
            'email': 'ms.sync.paused@test.lan',
            'login': 'ms_sync_paused_user',
        })
        sync_paused_attendee.microsoft_synchronization_stopped = True

    @freeze_time('2020-02-01 09:00:00')
    @patch.object(MsftUser, '_get_microsoft_calendar_token', lambda user: 'some-token')
    def test_appointment_cancel_notification_msftcalendar(self):
        appointment = self.calendar_event
        appointment.microsoft_id = 'test_msft_id'
        with self.mock_mail_gateway(), patch.object(MicrosoftCalendarService, 'delete') as mock_delete:
            appointment.action_archive()
            self.env.flush_all()
            self.cr.precommit.run()
            self.env.cr.postcommit.run()
        mock_delete.assert_called_once_with('test_msft_id', token='some-token', timeout=3)
        self.assertNotSentEmail()
    
    @freeze_time('2020-02-01 09:00:00')
    @users('mike@organizer.com', 'john@attendee.com', 'ms_sync_paused_user', 'user_public')
    @patch.object(
        MsftUser, '_get_microsoft_calendar_token',
        lambda user: user.login not in ['user_public', 'john@attendee.com'] and 'some-token'
    )
    def test_sync_or_email_resource_appointment(self):
        """Check that resource appointments are synced even if there is no organizer, unless the attendee is not syncing."""
        for with_organizer in [True, False]:
            with self.subTest(with_organizer=with_organizer):
                is_public = self.env.user == self.user_public
                booking_partner = self.env.user.partner_id if not is_public else self.public_user_booking_partner
                expected_author = booking_partner if not is_public else self.user_public.partner_id
                if with_organizer:
                    expected_author = self.organizer_user.partner_id
                with self.mock_mail_gateway(mail_unlink_sent=False), patch.object(MicrosoftCalendarService, 'insert') as mock_insert:
                    mock_insert.return_value = ('1', '1')
                    meeting = self.env['calendar.event'].with_context(mail_notify_author=True).sudo(is_public).create({
                        'appointment_type_id': self.apt_type_resource.id,
                        'name': f'Resource Appointment {booking_partner.name}',
                        'partner_ids': booking_partner.ids,
                        'start': datetime.now() + timedelta(days=1),
                        'stop': datetime.now() + timedelta(days=1, hours=1),
                        'user_id': with_organizer and self.organizer_user.id,
                    })
                    self.env.flush_all()
                    self.cr.precommit.run()
                    self.cr.postcommit.run()
                # synced with the organizer (who can always sync in this test), but checked against the create user
                if meeting._check_microsoft_sync_status() and self.env.user._get_microsoft_sync_status() == "sync_active":
                    mock_insert.assert_called_once()
                    self.assertNotSentEmail()
                else:
                    mock_insert.assert_not_called()
                    self.assertMailMail(
                        booking_partner, 'sent',
                        author=expected_author,
                        fields_values={'subject': f'Thanks for booking, {booking_partner.name}'}
                    )
