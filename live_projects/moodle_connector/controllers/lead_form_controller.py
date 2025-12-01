from odoo import http
from odoo.http import request
import logging
import base64
import pytz
from odoo.addons.website_sale.controllers.main import WebsiteSale

_logger = logging.getLogger(__name__)


class WebsiteSaleController(WebsiteSale):

    @http.route('/shop/address/submit', type='http', methods=['POST'],
                auth='public', website=True, csrf=False, sitemap=False)
    def shop_address_submit(self, **post):
        _logger.info("🎯 Controller Hit - Saving Admission Details to CRM Lead (HTML + File Uploads)")

        # --- Helper to format HTML sections ---
        def section(title, fields):
            html = [f"<h3 style='color:#004080;'>🟦 {title}</h3>"]
            for key in fields:
                val = post.get(key)
                if val:
                    html.append(f"<b>{key.replace('_', ' ').title()}:</b> {val}<br/>")
            return "".join(html)


        state_ids = post.get('state_id')
        orm = request.env['res.partner'].sudo().search([('id', '=', state_ids)])
        state_name = orm.name
        # --- Build formatted HTML Description ---
        description_html = "".join([
            "<h2>🎓 Admission Form Submission</h2><hr/>",
            section("Contact Information", [
                'legal_first_name', 'middle_name', 'legal_last_name', 'preferred_name',
                'certificate_name', 'email', 'phone', 'street', 'city', 'zip',
            ]),
            section("Personal Details", [
                'dob', 'gender', 'nationality', 'country_of_residence', 'time_zone'
            ]),
            section("Guardian / Sponsor", [
                'underage_consent', 'guardian_name', 'guardian_relationship', 'guardian_phone',
                'guardian_email', 'has_sponsor', 'sponsor_name', 'sponsor_relationship',
                'sponsor_phone', 'sponsor_email'
            ]),
            section("Academic Information", [
                'highest_qualification', 'last_institution', 'graduation_year', 'gpa',
                'prior_attendance', 'prior_institution_name', 'prior_program', 'prior_dates',
                'prior_credits', 'prior_reason', 'transfer_credit'
            ]),
            section("Program Preferences", [
                'academic_level', 'enrollment_load', 'rolling_admission_start',
                'preferred_start_month', 'preferred_start_year', 'pacing_expectation'
            ]),
            section("Faith Information", [
                'is_christian', 'church_affiliation', 'church_name', 'pastor_name',
                'pastor_contact', 'relationship_with_christ', 'why_study_lcu'
            ]),
            section("Online Learning Setup", [
                'internet_access', 'primary_device', 'operating_system', 'headset_webcam',
                'accessibility', 'accessibility_details', 'communication_channels',
                'availability_windows'
            ]),
            section("Additional Information", [
                'dismissed', 'dismissed_explanation', 'english_proficiency',
                'hear_about', 'agent_other'
            ]),
            section("Consents & Declarations", [
                'privacy_consent', 'esign_consent', 'honor_code', 'online_policies',
                'marketing_consent', 'truthfulness', 'signature_date'
            ]),
        ])


        # --- Partner handling ---
        partner_name = post.get('name')
        partner_email = post.get('email')
        partner_phone = post.get('phone')

        partner = request.env['res.partner'].sudo().search([('email', '=', partner_email)], limit=1)
        if not partner:
            partner = request.env['res.partner'].sudo().create({
                'name': partner_name,
                'email': partner_email,
                'phone': partner_phone,
            })
            _logger.info(f"👤 Created new partner: {partner.name}")
        else:
            _logger.info(f"🔁 Existing partner found: {partner.name}")



        # --- Create CRM Lead ---
        lead_vals = {
            'name': f"Admission Enquiry - {post.get('legal_first_name', '')} {post.get('legal_last_name', '')}".strip(),
            'partner_id': partner.id,
            'contact_name': partner_name,
            'email_from': partner_email,
            'phone': partner_phone,
            'course_id':post.get('Course_details'),
            'description': description_html,
        }

        # --- Optional: Link selected course ---
        course_id = post.get('Course_details')
        if course_id:
            try:
                course = request.env['slide.channel'].sudo().browse(int(course_id))
                if course and course.product_id:
                    lead_vals['expected_revenue'] = course.product_id.lst_price
                    lead_vals['course_id'] = course.id
                    description_html += f"<br/><br/><b>💰 Course Selected:</b> {course.name} | <b>Fee:</b> {course.product_id.lst_price}"
            except Exception as e:
                _logger.warning(f"⚠️ Error fetching course: {e}")

        lead = request.env['crm.lead'].sudo().create(lead_vals)
        _logger.info(f"✅ Created CRM Lead: {lead.name} (ID: {lead.id})")

        # =======================================================
        # 🖼️ Binary Uploads (Images)
        # =======================================================
        binary_fields = [
            'photo',
            'certificates',
            'government_id',
            'electronic_signature'
        ]

        for field_name in binary_fields:
            file = request.httprequest.files.get(field_name)
            if file:
                try:
                    file_data = base64.b64encode(file.read())
                    lead.sudo().write({field_name: file_data})
                    _logger.info(f"📸 Uploaded binary/image file for {field_name} (Lead ID: {lead.id})")
                except Exception as e:
                    _logger.warning(f"⚠️ Failed to upload binary field {field_name}: {e}")

        # =======================================================
        # 🧾 PDF Uploads (Many2many Attachments)
        # =======================================================
        pdf_fields = [
            'academic_transcript',
            'recommendation_letter',
            'personal_statement',
            'proof_upload',
            'transcript_upload'
        ]

        for field_name in pdf_fields:
            uploaded_files = request.httprequest.files.getlist(field_name)
            if not uploaded_files:
                _logger.debug(f"No files found for {field_name}")
                continue

            attachment_ids = []
            for file in uploaded_files:
                try:
                    filename = file.filename
                    if not filename.lower().endswith('.pdf'):
                        _logger.warning(f"🚫 Skipped non-PDF file: {filename}")
                        continue

                    file_data = file.read()
                    attachment = request.env['ir.attachment'].sudo().create({
                        'name': filename,
                        'type': 'binary',
                        'mimetype': 'application/pdf',
                        'datas': base64.b64encode(file_data),
                        'res_model': 'crm.lead',
                        'res_id': lead.id,
                    })
                    attachment_ids.append(attachment.id)
                    _logger.info(f"📎 Uploaded PDF '{filename}' for {field_name}")
                except Exception as e:
                    _logger.error(f"❌ Error uploading {filename} for {field_name}: {e}")

            if attachment_ids:
                lead.sudo().write({field_name: [(6, 0, attachment_ids)]})
                _logger.info(f"✅ Linked {len(attachment_ids)} PDFs to {field_name}")

        _logger.info("🎉 All images and PDFs uploaded successfully to CRM Lead.")
        return super(WebsiteSaleController, self).shop_address_submit(**post)

    # ===============================================
    # Load Address Form with Dropdowns
    # ===============================================
    @http.route(['/shop/address'], type='http', auth="public", website=True, sitemap=False)
    def shop_address(self, **kw):
        response = super().shop_address(**kw)
        courses = request.env['slide.channel'].sudo().search([])
        time_zones = pytz.all_timezones
        months = [
            'january', 'february', 'march', 'april', 'may', 'june',
            'july', 'august', 'september', 'october', 'november', 'december'
        ]
        years = list(range(2020, 2031))
        response.qcontext.update({
            'courses': courses,
            'time_zones': time_zones,
            'months': months,
            'years': years,
        })
        return response
