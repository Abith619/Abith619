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

    # ------------------------------------------------------------------------------------
    # Build HTML Description For Lead
    # ------------------------------------------------------------------------------------
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

    # ------------------------------------------------------------------------------------
    # Upload all binaries + PDFs to CRM Lead
    # ------------------------------------------------------------------------------------
    def _upload_files_to_lead(self, lead):
        if not lead:
            return

        _logger.info("Uploading all files to CRM Lead %s", lead.id)

        # ---------------- Binary Uploads ----------------
        for field_name in self.binary_fields:
            file = request.httprequest.files.get(field_name)
            if file:
                try:
                    data = base64.b64encode(file.read())
                    lead.sudo().write({field_name: data})
                    _logger.info("Uploaded binary/image for %s to Lead %s", field_name, lead.id)
                except Exception as e:
                    _logger.warning("Binary upload failed for %s: %s", field_name, e)

        # ---------------- PDF Uploads (multi-upload) ----------------
        for field_name in self.pdf_fields:
            uploaded_files = request.httprequest.files.getlist(field_name)
            if not uploaded_files:
                _logger.debug("No files provided for %s", field_name)
                continue

            attachment_ids = []
            for file in uploaded_files:
                try:
                    filename = file.filename
                    if not filename.lower().endswith('.pdf'):
                        _logger.warning("Skipped non-PDF file: %s", filename)
                        continue

                    data = base64.b64encode(file.read())

                    attachment = request.env['ir.attachment'].sudo().create({
                        'name': filename,
                        'type': 'binary',
                        'mimetype': 'application/pdf',
                        'datas': data,
                        'res_model': 'crm.lead',
                        'res_id': lead.id,
                    })
                    attachment_ids.append(attachment.id)

                    _logger.info("Uploaded PDF '%s' for %s", filename, field_name)

                except Exception as e:
                    _logger.error("Failed PDF upload (%s) for field %s: %s", filename, field_name, e)

            if attachment_ids:
                lead.sudo().write({field_name: [(6, 0, attachment_ids)]})
                _logger.info("Linked %d PDFs to field %s", len(attachment_ids), field_name)

        _logger.info("File upload complete for Lead %s", lead.id)

    # ------------------------------------------------------------------------------------
    # Partner Handling
    # ------------------------------------------------------------------------------------
    def _get_or_create_partner(self, post):
        email = (post.get('email') or '').strip()
        if not email:
            return None

        partner = request.env['res.partner'].sudo().search([('email', '=', email)], limit=1)
        if partner:
            return partner

        # Do NOT create new partner — requirement says reuse only
        return None

    # ------------------------------------------------------------------------------------
    # Lead Handling
    # ------------------------------------------------------------------------------------
    def _get_or_create_lead(self, post, partner, description_html):
        email = (post.get('email') or '').strip()
        course = post.get('Course_details')

        _logger.info("course Value", course)

        lead = request.env['crm.lead'].sudo().search([('email_from', '=', email)], limit=1)
        if lead:
            return lead

        vals = {
            'name': f"Admission Enquiry - {post.get('legal_first_name', '')} {post.get('legal_last_name', '')}",
            'email_from': email,
            'phone': post.get('phone'),
            'partner_id': partner.id if partner else False,
            'description': description_html,
            'course_id': course
        }

        # Link course
        course_id = post.get('Course_details')
        if course_id:
            course = request.env['slide.channel'].sudo().browse(int(course_id))
            if course :
                _logger.info("Linking Course %s to Lead", course.name)
                vals['course_id'] = course.id
                vals['expected_revenue'] = course.product_id.lst_price

        return request.env['crm.lead'].sudo().create(vals)

    @http.route('/shop/address/submit', type='http', methods=['POST'], auth='public', website=True, csrf=False)
    def shop_address_submit(self, **post):
        _logger.info("Admission Submit Hit — Creating/Updating Lead")

        com_channels = request.httprequest.form.getlist('communication_channels[]')
        post['communication_channels'] = com_channels

        description = self._build_description(post)

        partner = self._get_or_create_partner(post)
        lead = self._get_or_create_lead(post, partner, description)

        # ---- Upload all files ----
        try:
            self._upload_files_to_lead(lead)
        except Exception:
            _logger.exception("File upload block failed")

        # ---- Save into session ----
        try:
            if partner:
                request.session['partner_id'] = partner.id
            request.session['lead_id_from_admission'] = lead.id
        except Exception:
            _logger.exception("Failed to store partner/lead in session")

        # ---- Attach lead/partner to cart ----
        try:
            order = request.website.sale_get_order(force_create=False)
            if order:
                write_vals = {
                    'lead_id': lead.id,
                }
                if partner:
                    write_vals.update({
                        'partner_id': partner.id,
                        'partner_invoice_id': partner.id,
                        'partner_shipping_id': partner.id,
                    })
                order.sudo().write(write_vals)
        except Exception:
            _logger.exception("Failed attaching partner/lead to cart")

        return super(WebsiteSaleController, self).shop_address_submit(**post)

    # ------------------------------------------------------------------------------------
    # Checkout Route — Apply Session Partner
    # ------------------------------------------------------------------------------------
    @http.route(['/shop/checkout'], type='http', auth="public", website=True)
    def shop_checkout(self, try_skip_step=None, **query_params):
        partner_id = request.session.get('partner_id')

        if partner_id:
            try:
                order = request.website.sale_get_order(force_create=False)
                if order:
                    partner = request.env['res.partner'].sudo().browse(partner_id)
                    order.sudo().write({
                        'partner_id': partner.id,
                        'partner_invoice_id': partner.id,
                        'partner_shipping_id': partner.id,
                    })
            except Exception:
                _logger.exception("Failed enforcing session partner on checkout")

        return super(WebsiteSaleController, self).shop_checkout(try_skip_step=try_skip_step, **query_params)

    # ------------------------------------------------------------------------------------
    # Shop Address (adds dynamic fields)
    # ------------------------------------------------------------------------------------
    @http.route(['/shop/address'], type='http', auth="public", website=True)
    def shop_address(self, **kw):
        response = super().shop_address(**kw)

        courses = request.env['slide.channel'].sudo().search([])
        time_zones = pytz.all_timezones
        months = [
            'january','february','march','april','may','june',
            'july','august','september','october','november','december'
        ]
        years = list(range(2020, 2031))

        today = date.today().strftime("%Y-%m-%d")

        response.qcontext.update({
            'courses': courses,
            'time_zones': time_zones,
            'months': months,
            'years': years,
            'today': today,
        })

        return response
