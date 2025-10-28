from odoo import http
from odoo.http import request, route, Controller

class AppointmentController(Controller):

    @route(['/'], type='http', auth="public", website=True, csrf=False)
    def appointment_form(self, **post):
        return request.render("appointment_booking.appointment_form_template")

    @route(['/appointment/submit'], type='http', auth="public", website=True, csrf=False)
    def appointment_submit(self, **post):
        vals = {
            "name": post.get("name"),
            "email": post.get("email"),
            "phone": post.get("phone"),
            "date": post.get("date"),
            "slot": post.get("slot"),
            "notes": post.get("notes"),
            "service": post.get("services"),
        }
        booking = request.env["appointment.booking"].sudo().create(vals)

        mail_values = {
            'subject': f"New Appointment: {booking.name}",
            'body_html': f"""
                <p>Hello,</p>
                <p>A new appointment has been booked:</p>
                <ul>
                    <li><b>Name:</b> {booking.name}</li>
                    <li><b>Email:</b> {booking.email}</li>
                    <li><b>Phone:</b> {booking.phone}</li>
                    <li><b>Date:</b> {booking.date}</li>
                    <li><b>Slot:</b> {booking.slot}</li>
                    <li><b>Service:</b> {booking.service}</li>
                </ul>
            """,
            'email_from': request.env.user.company_id.email or 'reports@kashtechllc.com',
            'email_to': 'bdsupport@kashtechllc.com',
        }
        request.env['mail.mail'].sudo().create(mail_values).send()

        return request.render("appointment_booking.appointment_thanks")
