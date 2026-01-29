from odoo import http
from odoo.http import request
import logging
import base64
import pytz
from datetime import date
from odoo.addons.website_sale.controllers.main import WebsiteSale

_logger = logging.getLogger(__name__)


class WebsiteSaleController(WebsiteSale):

    binary_fields = [
        'photo', 'certificates', 'government_id', 'electronic_signature'
    ]

    pdf_fields = [
        'academic_transcript', 'recommendation_letter', 'personal_statement',
        'proof_upload', 'transcript_upload'
    ]

    # -------------------------------------------------------------------------
    # BUILD LEAD DESCRIPTION
    # -------------------------------------------------------------------------
    def _section_html(self, title, fields, post):
        html = [f"<h3 style='color:#004080;'>{title}</h3>"]
        for key in fields:
            val = post.get(key)
            if val:
                html.append(f"<b>{key.replace('_', ' ').title()}:</b> {val}<br/>")
        return "".join(html)

    def _build_description(self, post):
        parts = [
            "<h2>🎓 Admission Form Submission</h2><hr/>",
            self._section_html("Contact Information", [
                'legal_first_name', 'middle_name', 'legal_last_name',
                'preferred_name', 'certificate_name', 'email', 'phone', 'street',
                'city', 'zip'
            ], post),
            self._section_html("Personal Details", [
                'dob', 'gender', 'nationality', 'country_of_residence', 'time_zone'
            ], post),
            self._section_html("Guardian / Sponsor", [
                'underage_consent', 'guardian_name', 'guardian_relationship',
                'guardian_phone', 'guardian_email', 'has_sponsor', 'sponsor_name',
                'sponsor_relationship', 'sponsor_phone', 'sponsor_email'
            ], post),
            self._section_html("Academic Information", [
                'highest_qualification', 'last_institution', 'graduation_year',
                'gpa', 'prior_attendance', 'prior_institution_name',
                'prior_program', 'prior_dates', 'prior_credits', 'prior_reason',
                'transfer_credit'
            ], post),
            self._section_html("Program Preferences", [
                'academic_level', 'enrollment_load', 'rolling_admission_start',
                'preferred_start_month', 'preferred_start_year',
                'pacing_expectation'
            ], post),
            self._section_html("Faith Information", [
                'is_christian', 'church_affiliation', 'church_name',
                'pastor_name', 'pastor_contact', 'relationship_with_christ',
                'why_study_lcu'
            ], post),
            self._section_html("Online Learning Setup", [
                'internet_access', 'primary_device', 'operating_system',
                'headset_webcam', 'accessibility', 'accessibility_details',
                'communication_channels', 'availability_windows'
            ], post),
            self._section_html("Additional Information", [
                'dismissed', 'dismissed_explanation', 'english_proficiency',
                'hear_about', 'agent_other'
            ], post),
            self._section_html("Consents & Declarations", [
                'privacy_consent', 'esign_consent', 'honor_code',
                'online_policies', 'marketing_consent', 'truthfulness',
                'signature_date'
            ], post),
        ]
        return "".join(parts)

    # -------------------------------------------------------------------------
    # FILE UPLOADS
    # -------------------------------------------------------------------------
    def _upload_files_to_lead(self, lead):
        if not lead:
            return

        for field_name in self.binary_fields:
            file = request.httprequest.files.get(field_name)
            if file:
                lead.sudo().write({
                    field_name: base64.b64encode(file.read())
                })

        for field_name in self.pdf_fields:
            files = request.httprequest.files.getlist(field_name)
            attachment_ids = []
            for file in files:
                if file.filename.lower().endswith('.pdf'):
                    att = request.env['ir.attachment'].sudo().create({
                        'name': file.filename,
                        'type': 'binary',
                        'datas': base64.b64encode(file.read()),
                        'res_model': 'crm.lead',
                        'res_id': lead.id,
                        'mimetype': 'application/pdf'
                    })
                    attachment_ids.append(att.id)

            if attachment_ids:
                lead.sudo().write({
                    field_name: [(6, 0, attachment_ids)]
                })

    # -------------------------------------------------------------------------
    # PARTNER
    # -------------------------------------------------------------------------
    def _get_or_create_partner(self, post):
        email = (post.get('email') or '').strip()
        if not email:
            return False
        return request.env['res.partner'].sudo().search(
            [('email', '=', email)], limit=1
        )

    # -------------------------------------------------------------------------
    # LEAD
    # -------------------------------------------------------------------------
    def _get_or_create_lead(self, post, partner, description):
        email = post.get('email')
        course_id = post.get('Course_details')

        lead = request.env['crm.lead'].sudo().search(
            [('email_from', '=', email)], limit=1
        )
        if lead:
            return lead

        vals = {
            'name': f"Admission Enquiry - {post.get('legal_first_name','')}",
            'email_from': email,
            'phone': post.get('phone'),
            'partner_id': partner.id if partner else False,
            'description': description,
        }

        if course_id:
            course = request.env['slide.channel'].sudo().browse(int(course_id))
            if course:
                vals.update({
                    'course_id': course.id,
                    'expected_revenue': course.product_id.lst_price
                })

        return request.env['crm.lead'].sudo().create(vals)

    # def _create_or_update_student(self, post, lead, partner):
    #     Student = request.env['student.master'].sudo()
    #     email = post.get('email')

    #     # ---------- NAME FALLBACK ----------
    #     first_name = post.get('legal_first_name')
    #     last_name = post.get('legal_last_name')

    #     if first_name or last_name:
    #         name = f"{first_name or ''} {last_name or ''}".strip()
    #     elif partner and partner.name:
    #         name = partner.name
    #     elif email:
    #         name = email.split('@')[0]
    #     else:
    #         name = "Student"

    #     # ---------- SAFE DATE HANDLING ----------
    #     dob = post.get('dob') or False
    #     prior_dates = post.get('prior_dates') or False

    #     student = Student.search([
    #         '|',
    #         ('lead_id', '=', lead.id),
    #         ('email', '=', email)
    #     ], limit=1)

    #     vals = {
    #         # BASIC
    #         'name': name,
    #         'email': email,
    #         'phone': post.get('phone'),
    #         'dob': dob,   # ✅ SAFE
    #         'gender': post.get('gender'),

    #         'country_of_residence': post.get('country_of_residence'),
    #         'nationality': post.get('nationality'),
    #         'time_zone': post.get('time_zone'),

    #         # GUARDIAN
    #         'underage_consent': post.get('underage_consent'),
    #         'guardian_name': post.get('guardian_name'),
    #         'guardian_relationship': post.get('guardian_relationship'),
    #         'guardian_phone': post.get('guardian_phone'),
    #         'guardian_email': post.get('guardian_email'),

    #         # SPONSOR
    #         'has_sponsor': post.get('has_sponsor'),
    #         'sponsor_name': post.get('sponsor_name'),
    #         'sponsor_relationship': post.get('sponsor_relationship'),
    #         'sponsor_phone': post.get('sponsor_phone'),
    #         'sponsor_email': post.get('sponsor_email'),

    #         # ACADEMIC
    #         'highest_qualification': post.get('highest_qualification'),
    #         'last_institution': post.get('last_institution'),
    #         'graduation_year': post.get('graduation_year'),
    #         'gpa': post.get('gpa'),

    #         'prior_attendance': post.get('prior_attendance'),
    #         'prior_institution_name': post.get('prior_institution_name'),
    #         'prior_program': post.get('prior_program'),
    #         'prior_dates': prior_dates,   # ✅ SAFE
    #         'prior_credits': post.get('prior_credits'),
    #         'prior_reason': post.get('prior_reason'),

    #         # RELATIONS
    #         'partner_id': partner.id if partner else False,
    #         'lead_id': lead.id,
    #     }

    #     if student:
    #         student.write(vals)
    #     else:
    #         student = Student.create(vals)

    #     lead.sudo().write({'student_id': student.id})
    #     return student
    def _create_or_update_student(self, post, lead, partner):
        Student = request.env['student.master'].sudo()
        email = post.get('email')

        # ---------- NAME ----------
        first = post.get('legal_first_name')
        last = post.get('legal_last_name')
        name = (
            f"{first or ''} {last or ''}".strip()
            or (partner.name if partner else False)
            or email.split('@')[0]
        )

        student = Student.search([
            '|',
            ('lead_id', '=', lead.id),
            ('email', '=', email)
        ], limit=1)

        # ---------- BASIC ----------
        vals = {
            'name': name,
            'email': email,
            'phone': post.get('phone'),
            'dob': post.get('dob') or False,
            'gender': post.get('gender'),
            'country_of_residence': post.get('country_of_residence'),
            'nationality': post.get('nationality'),
            'time_zone': post.get('time_zone'),
            'highest_qualification': post.get('highest_qualification'),
            'last_institution': post.get('last_institution'),
            'graduation_year': post.get('graduation_year'),
            'gpa': post.get('gpa'),
            'partner_id': partner.id if partner else False,
            'lead_id': lead.id,
        }

        # ---------- GUARDIAN ----------
        if post.get('underage_consent') == 'yes':
            vals.update({
                'underage_consent': 'yes',
                'guardian_name': post.get('guardian_name'),
                'guardian_relationship': post.get('guardian_relationship'),
                'guardian_phone': post.get('guardian_phone'),
                'guardian_email': post.get('guardian_email'),
            })
        else:
            vals.update({
                'underage_consent': 'no',
                'guardian_name': False,
                'guardian_relationship': False,
                'guardian_phone': False,
                'guardian_email': False,
            })

        # ---------- SPONSOR ----------
        if post.get('has_sponsor') == 'yes':
            vals.update({
                'has_sponsor': 'yes',
                'sponsor_name': post.get('sponsor_name'),
                'sponsor_relationship': post.get('sponsor_relationship'),
                'sponsor_phone': post.get('sponsor_phone'),
                'sponsor_email': post.get('sponsor_email'),
            })
        else:
            vals.update({
                'has_sponsor': 'no',
                'sponsor_name': False,
                'sponsor_relationship': False,
                'sponsor_phone': False,
                'sponsor_email': False,
            })

        # ---------- PRIOR ATTENDANCE ----------
        if post.get('prior_attendance') == 'yes':
            vals.update({
                'prior_attendance': 'yes',
                'prior_institution_name': post.get('prior_institution_name'),
                'prior_program': post.get('prior_program'),
                'prior_dates': post.get('prior_dates') or False,
                'prior_credits': post.get('prior_credits'),
                'prior_reason': post.get('prior_reason'),
            })
        else:
            vals.update({
                'prior_attendance': 'no',
                'prior_institution_name': False,
                'prior_program': False,
                'prior_dates': False,
                'prior_credits': False,
                'prior_reason': False,
            })

        # ---------- CREATE / UPDATE ----------
        if student:
            student.write(vals)
        else:
            student = Student.create(vals)

        lead.sudo().write({'student_id': student.id})
        return student

    # -------------------------------------------------------------------------
    # FIRST TIME SUBMISSION
    # -------------------------------------------------------------------------
    @http.route('/shop/address/submit', type='http', methods=['POST'],
                auth='public', website=True, csrf=False)
    def shop_address_submit(self, **post):

        post['communication_channels'] = request.httprequest.form.getlist(
            'communication_channels[]'
        )

        description = self._build_description(post)
        partner = self._get_or_create_partner(post)
        lead = self._get_or_create_lead(post, partner, description)

        # self._create_or_update_student(post, lead, partner)
        self._upload_files_to_lead(lead)
        # 🔹 STEP 2: Create / Update STUDENT
        student = self._create_or_update_student(post, lead, partner)

        # 🔹 STEP 3: COPY PHOTO → STUDENT
        if lead.photo and student:
            student.sudo().write({
                'photo': lead.photo
            })


        request.session['lead_id_from_admission'] = lead.id
        if partner:
            request.session['partner_id'] = partner.id

        order = request.website.sale_get_order(force_create=False)
        if order:
            order.sudo().write({
                'lead_id': lead.id,
                'partner_id': partner.id if partner else False,
                'partner_invoice_id': partner.id if partner else False,
                'partner_shipping_id': partner.id if partner else False,
            })

        return super().shop_address_submit(**post)
    def _section_second_html(self, title, fields, post):
        html = [f"<h3 style='color:#004080;'>{title}</h3>"]
        for key in fields:
            val = post.get(key)
            if val:
                html.append(
                    f"<b>{key.replace('_', ' ').title()}:</b> {val}<br/>"
                )
        return "".join(html)

    def _build_second_description(self, post):

        html = [
            "<h2>🎓 Admission Form – Reapplying Course</h2><hr/>"
        ]
        if post.get('previous_course_id'):
            course = request.env['slide.channel'].sudo().browse(
                int(post.get('previous_course_id'))
            )
            html.append("<h3 style='color:#004080;'>Previous Enrollment Details</h3>")
            html.append(f"<b>Previously Enrolled Course (Lead):</b> {course.name}<br/>")
        if post.get('previous_lead_id'):
            html.append(f"<b>Previous Lead ID:</b> {post.get('previous_lead_id')}<br/>")

        if post.get('previous_course'):
            html.append(
                f"<b>Previous Courses Applied / Purchased:</b> {post.get('previous_course')}<br/>"
            )

        html.append(self._section_second_html(
            "Academic Information",
            [
                'academic_level',
                'enrollment_load',
                'pacing_expectation',
                'rolling_admission_start'
            ],
            post
        ))

        return "".join(html)

    @http.route('/secondtimeregister', type='http',
            auth='public', website=True)
    def second_time_register_form(self, **kw):

        course_id = int(kw.get('course_id', 0))
        course = request.env['slide.channel'].sudo().browse(course_id)

        if not course.exists():
            return request.redirect('/slides')

        partner = (
            request.env.user.partner_id
            if not request.env.user._is_public()
            else False
        )

        old_lead = False
        previous_courses = False

        if partner and partner.email:
            won_stage = request.env['crm.stage'].sudo().search(
                [('name', '=', 'Won')], limit=1
            )

            old_leads = request.env['crm.lead'].sudo().search([
                ('email_from', '=', partner.email),
                ('course_id', '!=', False),
                ('stage_id', '=', won_stage.id),
            ])

            old_lead = old_leads[:1] if old_leads else False
            previous_courses = ', '.join(old_leads.mapped('course_id.name'))

        return request.render(
            'moodle_connector.second_time_register_form',
            {
                'course': course,
                'partner': partner,
                'old_lead': old_lead,
                'previous_course': previous_courses,
                'months': [
                    'january','february','march','april','may','june',
                    'july','august','september','october','november','december'
                ],
                'years': list(range(2020, 2031)),
                'today': date.today().strftime("%Y-%m-%d"),
            }
        )
    # @http.route('/secondtimeregister/submit', type='http',
    #         auth="public", website=True, csrf=False)
    # def second_time_register_submit(self, **post):
    #     course_id = int(post.get('course_id', 0))
    #     course = request.env['slide.channel'].sudo().browse(course_id)

    #     if not course.exists():
    #         return request.redirect('/courses')
        

    #     partner = request.env['res.partner'].sudo().search(
    #         [('email', '=', post.get('email'))], limit=1
    #     )
    #     student = request.env['student.master'].sudo().search(
    #         [('email', '=', post.get('email'))],
    #         limit=1
    #     )
    #     previous_leads = request.env['crm.lead'].sudo().search([
    #         ('email_from', '=', post.get('email')),
    #         ('course_id', '!=', False),
    #     ])

    #     previous_lead = previous_leads[:1] if previous_leads else False
    #     previous_courses = ', '.join(
    #         set(previous_leads.mapped('course_id.name'))
    #     ) if previous_leads else False

    #     lead = request.env['crm.lead'].sudo().create({
    #         'name': f"Admission Enquiry - {post.get('email')}",
    #         'email_from': post.get('email'),
    #         'phone': post.get('phone'),
    #         'partner_id': partner.id if partner else False,
    #         'course_id': course.id,
    #         'description': self._build_second_description(post),
    #         'expected_revenue': (
    #             course.application_product_id.lst_price
    #             if course.application_product_id else 0.0
    #         ),
    #     })

    #     if student:
    #         student.sudo().write({
    #             'previous_lead_id': previous_lead.id if previous_lead else False,
    #             'previous_courses': previous_courses,
    #             'lead_id': lead.id,  # latest application
    #         })
    #     order = request.website.sale_get_order(force_create=True)

    #     if course.application_product_id:
    #         order._cart_update(
    #             product_id=course.application_product_id.id,
    #             add_qty=1
    #         )

    #     order.sudo().write({
    #         'lead_id': lead.id,
    #         'partner_id': partner.id if partner else False,
    #         'partner_invoice_id': partner.id if partner else False,
    #         'partner_shipping_id': partner.id if partner else False,
    #     })

    #     request.session['lead_id_from_admission'] = lead.id
    #     if partner:
    #         request.session['partner_id'] = partner.id

    #     return request.redirect('/shop/checkout')
    @http.route('/secondtimeregister/submit', type='http',
            auth="public", website=True, csrf=False)
    def second_time_register_submit(self, **post):

        # --------------------------------------------------
        # COURSE
        # --------------------------------------------------
        course_id = int(post.get('course_id', 0))
        course = request.env['slide.channel'].sudo().browse(course_id)

        if not course.exists():
            return request.redirect('/slides')

        # --------------------------------------------------
        # BUILD APPLICANT NAME (FIRST + LAST)
        # --------------------------------------------------
        first_name = (post.get('legal_first_name') or '').strip()
        last_name = (post.get('legal_last_name') or '').strip()

        if first_name or last_name:
            applicant_name = f"{first_name} {last_name}".strip()
        else:
            applicant_name = post.get('email')

        # --------------------------------------------------
        # PARTNER
        # --------------------------------------------------
        partner = request.env['res.partner'].sudo().search(
            [('email', '=', post.get('email'))],
            limit=1
        )

        # --------------------------------------------------
        # STUDENT (DO NOT OVERWRITE DETAILS)
        # --------------------------------------------------
        student = request.env['student.master'].sudo().search(
            [('email', '=', post.get('email'))],
            limit=1
        )

        # --------------------------------------------------
        # FETCH PREVIOUS LEADS (READ ONLY)
        # --------------------------------------------------
        previous_leads = request.env['crm.lead'].sudo().search([
            ('email_from', '=', post.get('email')),
            ('course_id', '!=', False),
        ])

        previous_lead = previous_leads[:1] if previous_leads else False

        previous_courses = (
            ', '.join(set(previous_leads.mapped('course_id.name')))
            if previous_leads else False
        )

        # --------------------------------------------------
        # CREATE NEW LEAD (IMPORTANT)
        # --------------------------------------------------
        lead = request.env['crm.lead'].sudo().create({
            'name': f"Admission Enquiry - {applicant_name}",
            'email_from': post.get('email'),
            'phone': post.get('phone'),
            'partner_id': partner.id if partner else False,
            'course_id': course.id,
            'description': self._build_second_description(post),
            'previous_lead_id': previous_lead.id if previous_lead else False,
            'expected_revenue': (
                course.application_product_id.lst_price
                if course.application_product_id else 0.0
            
            ),
        })

        # --------------------------------------------------
        # UPDATE STUDENT MASTER (HISTORY ONLY)
        # --------------------------------------------------
        if student:
            student.sudo().write({
                'previous_lead_id': previous_lead.id if previous_lead else False,
                'previous_courses': previous_courses,
                'lead_id': lead.id,   # latest application
            })
        else:
            # safety fallback (should not usually happen)
            student = request.env['student.master'].sudo().create({
                'name': applicant_name,
                'email': post.get('email'),
                'phone': post.get('phone'),
                'partner_id': partner.id if partner else False,
                'lead_id': lead.id,
                'previous_lead_id': previous_lead.id if previous_lead else False,
                'previous_courses': previous_courses,
            })

        # --------------------------------------------------
        # 🔥 THIS IS THE MISSING LINK (MOST IMPORTANT)
        # --------------------------------------------------
        lead.sudo().write({
            'student_id': student.id
        })


        # --------------------------------------------------
        # CART + CHECKOUT
        # --------------------------------------------------
        order = request.website.sale_get_order(force_create=True)

        if course.application_product_id:
            order._cart_update(
                product_id=course.application_product_id.id,
                add_qty=1
            )

        order.sudo().write({
            'lead_id': lead.id,
            'partner_id': partner.id if partner else False,
            'partner_invoice_id': partner.id if partner else False,
            'partner_shipping_id': partner.id if partner else False,
        })

        # --------------------------------------------------
        # SESSION
        # --------------------------------------------------
        request.session['lead_id_from_admission'] = lead.id
        if partner:
            request.session['partner_id'] = partner.id

        return request.redirect('/shop/checkout')



    # -------------------------------------------------------------------------
    # SHOP ADDRESS EXTENSION
    # -------------------------------------------------------------------------
    @http.route(['/shop/address'], type='http', auth="public", website=True)
    def shop_address(self, **kw):
        response = super().shop_address(**kw)

        response.qcontext.update({
            'courses': request.env['slide.channel'].sudo().search([]),
            'time_zones': pytz.all_timezones,
            'months': [
                'january','february','march','april','may','june',
                'july','august','september','october','november','december'
            ],
            'years': list(range(2020, 2031)),
            'today': date.today().strftime("%Y-%m-%d"),
        })
        return response



