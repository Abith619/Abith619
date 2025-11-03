from odoo import models, fields, api
from odoo.exceptions import ValidationError
import requests, base64, json, html
import logging

_logger = logging.getLogger(__name__)

class MoodleConfig(models.Model):
    _name = 'moodle.config'
    _rec_name = 'name'
    _description = 'Moodle Account Configuration'

    name = fields.Char(string='Name', required=True)
    url = fields.Char(string='URL', required=True)
    token = fields.Char(string='Token', required=True)

    category = fields.Boolean(string='Categories')
    course = fields.Boolean(string='Courses')
    user = fields.Boolean(string='Users')

    def test_moodle(self):
        for rec in self:
            # Ensure proper URL formatting
            base_url = rec.url.rstrip('/')
            token = rec.token

            # Example endpoint — use a harmless function for testing (core_webservice_get_site_info)
            endpoint = f"{base_url}/webservice/rest/server.php"
            params = {
                'wstoken': token,
                'wsfunction': 'core_webservice_get_site_info',
                'moodlewsrestformat': 'json'
            }

            try:
                response = requests.get(endpoint, params=params, timeout=10)
                response.raise_for_status()

                data = response.json()

                if 'exception' in data:
                    raise ValidationError(f"Connection failed: {data.get('message', 'Invalid token or API error')}")

                site_name = data.get('sitename', 'Unknown site')
                version = data.get('version', 'Unknown version')
                raise ValidationError(f"✅ Moodle connection successful!\nSite: {site_name}\nVersion: {version}")

            except requests.exceptions.RequestException as e:
                raise ValidationError(f"Connection failed: {str(e)}")
            except ValueError:
                raise ValidationError("Invalid JSON response from Moodle server.")

    def fetch_contents(self):
        for rec in self:
            base_url = rec.url.rstrip('/')
            endpoint = f"{base_url}/webservice/rest/server.php"

            def _call_moodle(wsfunction, extra_params=None):
                """Helper for Moodle API calls"""
                params = {
                    'wstoken': rec.token,
                    'wsfunction': wsfunction,
                    'moodlewsrestformat': 'json'
                }
                if extra_params:
                    params.update(extra_params)
                res = requests.get(endpoint, params=params, timeout=15)
                try:
                    data = res.json()
                except ValueError:
                    raise ValidationError("Invalid JSON response from Moodle.")

                if isinstance(data, dict) and 'exception' in data:
                    raise ValidationError(f"Moodle API Error: {data.get('message', '')}")
                return data
            results = {}

        category_tags = []
        if rec.category:
                data = _call_moodle('core_course_get_categories')
                CategoryGroup = self.env['slide.channel.tag.group']
                Tag = self.env['slide.channel'].search([('id', '=', 1)], limit=1)
                TagModel = self.env['slide.channel.tag']

                for cat in data:
                    if not isinstance(cat, dict):
                        continue

                    name = cat.get('name')
                    category_id = cat.get('id')

                    existing_group = CategoryGroup.search([('id', '=', 2)], limit=1)
                    if not existing_group:
                        continue
                    category_tags.append({
                        'name': name,
                        'group_id': existing_group.id,
                        'moodle_id': category_id,
                    })
                    # Check if this tag already exists (to avoid duplicates)
                    existing_tag = TagModel.search([
                        ('name', '=', name),
                        ('group_id', '=', existing_group.id)
                    ], limit=1)

                    if not existing_tag:
                        new_tag = TagModel.create({
                            'name': name,
                            'group_id': existing_group.id,
                            'moodle_id': category_id,
                        })
                        category_tags.append(new_tag.id)
                    if category_tags:
                        Tag.write({'tag_ids': [(6, 0, category_tags)]})

                results['categories'] = data

        if rec.course:
            data = _call_moodle('core_course_get_courses')
            SlideChannel = self.env['slide.channel']
            SlideSlide = self.env['slide.slide']
            Tag = self.env['slide.channel.tag']
            CategoryGroup= self.env['slide.channel.tag.group']

            for course in data:
                if not isinstance(course, dict):
                    continue
                moodle_course_id = course.get('id')
                name = course.get('fullname', f"Moodle Course {moodle_course_id}")
                summary = course.get('summary', '')
                category_id = course.get('categoryid')
                category_group = Tag.search([('moodle_id', '=', category_id)], limit=1)
                # --- Check if Odoo course already exists ---
                existing_course = SlideChannel.search([('moodle_course_id', '=', moodle_course_id)], limit=1)
                course_vals = {
                    'name': name,
                    'description': summary or '',
                    'moodle_course_id': moodle_course_id,
                    'tag_ids': [(6, 0, [category_group.id])] if category_group else False,
                    'website_published': True,
                }

                if existing_course:
                    existing_course.write(course_vals)
                    _logger.info(f"Updated existing course: {name} (Moodle ID: {moodle_course_id})")
                    slide_channel = existing_course
                else:
                    slide_channel = SlideChannel.create(course_vals)
                    _logger.info(f"Created new course: {name} (Moodle ID: {moodle_course_id})")


                # --- Fetch course sections & contents ---
                content_data = _call_moodle('core_course_get_contents', {'courseid': moodle_course_id})
                if not isinstance(content_data, list):
                    continue

                SlideSlide = self.env['slide.slide']
                sequence_counter = 0  # ✅ maintain order across sections and contents

                for section in content_data:
                    section_name = section.get('name') or 'Untitled Section'
                    modules = section.get('modules', [])

                    # --- Create or update section slide (acts as category) ---
                    existing_section_slide = SlideSlide.search([
                        ('name', '=', section_name),
                        ('channel_id', '=', slide_channel.id),
                        ('is_category', '=', True),
                    ], limit=1)

                    section_slide_vals = {
                        'name': section_name,
                        'channel_id': slide_channel.id,
                        'is_category': True,
                        'sequence': sequence_counter,
                    }

                    if existing_section_slide:
                        existing_section_slide.write(section_slide_vals)
                        section_slide = existing_section_slide
                    else:
                        section_slide = SlideSlide.create(section_slide_vals)

                    sequence_counter += 1  # increment for next section

                    # --- Process each module inside section ---
                    for module in modules:
                        mod_name = module.get('name') or 'Unnamed Content'
                        mod_type = module.get('modname', 'other')
                        mod_summary = module.get('description', '')
                        mod_url = module.get('url')
                        content_list = module.get('contents', [])

                        mime_type = file_url = file_name = None
                        if content_list and isinstance(content_list, list):
                            content_item = content_list[0]
                            file_url = content_item.get('fileurl')
                            file_name = content_item.get('filename')
                            mime_type = content_item.get('mimetype')

                        # --- Determine slide type ---
                        slide_type_map = {
                            'resource': 'document',
                            'file': 'document',
                            'page': 'article',
                            'url': 'video',
                            'quiz': 'quiz',
                            'assignment': 'quiz',
                            'book': 'article',
                            'lesson': 'article',
                            'label': 'article',
                            'forum': 'article',
                        }

                        if mime_type:
                            if 'pdf' in mime_type:
                                slide_type = 'document'
                            elif 'image' in mime_type:
                                slide_type = 'infographic'
                            elif 'video' in mime_type:
                                slide_type = 'video'
                            elif any(x in mime_type for x in ['sheet', 'excel', 'csv']):
                                slide_type = 'document'
                            elif any(x in mime_type for x in ['presentation', 'powerpoint', 'ppt']):
                                slide_type = 'document'
                            elif any(x in mime_type for x in ['word', 'document', 'msword', 'officedocument']):
                                slide_type = 'document'
                            elif 'text' in mime_type or 'html' in mime_type:
                                slide_type = 'article'
                            elif mod_type in ['quiz', 'assignment']:
                                slide_type = 'quiz'
                            elif mod_type in ['forum', 'page', 'lesson', 'label', 'book']:
                                slide_type = 'article'
                            else:
                                slide_type = slide_type_map.get(mod_type, 'article')
                        else:
                            slide_type = slide_type_map.get(mod_type, 'article')

                        # --- Prepare base slide values ---
                        slide_vals = {
                            'name': mod_name,
                            'channel_id': slide_channel.id,
                            'slide_category': slide_type,
                            'description': mod_summary or '',
                            'category_id': section_slide.id,
                            'website_published': True,
                            'sequence': sequence_counter,
                        }

                        # --- Attach file or URL ---
                        if file_url:
                            token = rec.token
                            if token and 'token=' not in file_url:
                                if '?' in file_url:
                                    file_url = f"{file_url}&token={token}"
                                else:
                                    file_url = f"{file_url}?token={token}"

                            try:
                                response = requests.get(file_url, timeout=10)
                                if response.status_code == 200:
                                    file_content = base64.b64encode(response.content)
                                    slide_vals.update({
                                        'source_type': 'local_file',
                                        'image_binary_content': file_content,
                                        'url': file_url,
                                    })
                                else:
                                    slide_vals.update({'source_type': 'external', 'url': file_url})
                            except Exception as e:
                                _logger.error(f"Error downloading file from Moodle: {e}")
                                slide_vals.update({'source_type': 'external', 'url': file_url})
                        else:
                            slide_vals.update({'source_type': 'external', 'url': mod_url})

                        # --- Handle Moodle 'Book' content type ---
                        if mod_type == 'book':
                            html_content = ''
                            for content in module.get('contents', []):
                                if content.get('type') == 'file':
                                    file_url = content.get('fileurl')
                                    break

                            if file_url:
                                token = rec.token
                                if token and 'token=' not in file_url:
                                    file_url = f"{file_url}?token={token}"
                                try:
                                    response = requests.get(file_url, timeout=10)
                                    if response.status_code == 200:
                                        html_content = response.text
                                    else:
                                        _logger.warning(f"Failed to fetch HTML from Moodle Book: {response.status_code}")
                                except Exception as e:
                                    _logger.error(f"Error fetching Moodle Book HTML: {e}")

                            slide_vals.update({
                                'source_type': 'external',
                                'html_content': html_content,
                                'url': False,
                            })

                        # --- Handle Moodle 'Quiz' type ---
                        if mod_type == 'quiz':
                            slide_vals.update({
                                'slide_category': 'quiz',
                                'source_type': 'external',
                                'html_content': False,
                            })

                        # --- Create or update slide ---
                        existing_slide = SlideSlide.search([
                            ('name', '=', mod_name),
                            ('channel_id', '=', slide_channel.id),
                        ], limit=1)
                        if existing_slide:
                            existing_slide.write(slide_vals)
                        else:
                            SlideSlide.create(slide_vals)

                        sequence_counter += 1  # ✅ maintain correct order

                # Store result
                results['courses'] = data

        if rec.user:
            courses = self.env['slide.channel'].search([('moodle_course_id', '!=', False)])
            for course in courses:
                moodle_course_id = course.moodle_course_id
                _logger.info(f"Fetching enrolled users for Moodle course ID {moodle_course_id}...")
                try:
                    enrolled_users = _call_moodle('core_enrol_get_enrolled_users', {
                        'courseid': moodle_course_id
                    })
                except Exception as e:
                    _logger.info(f"Failed to fetch enrolled users for course {moodle_course_id}: {e}")
                    enrolled_users = []

                User = self.env['res.partner']
                Users = self.env['res.users']
                ChannelPartner = self.env['slide.channel.partner']

                # Get Portal group reference once
                portal_group = self.env.ref('base.group_portal', raise_if_not_found=False)

                for user in enrolled_users:
                    user_email = user.get('email')
                    if not user_email:
                        _logger.info(f"Skipping user with missing email: {user}")
                        continue

                    # Step 1️⃣: Create or update partner (res.partner)
                    existing_partner = User.search([('email', '=', user_email)], limit=1)
                    partner_vals = {
                        'name': f"{user.get('firstname', '')} {user.get('lastname', '')}".strip(),
                        'email': user_email,
                        'is_company': False,
                    }

                    if existing_partner:
                        existing_partner.write(partner_vals)
                        odoo_partner = existing_partner
                    else:
                        odoo_partner = User.create(partner_vals)
                        _logger.info(f"Created new partner: {odoo_partner.email}")

                    # Step 2️⃣: Create or update system user (res.users)
                    existing_user = Users.search([('login', '=', user_email)], limit=1)
                    if not existing_user:
                        user_data = {
                            'name': odoo_partner.name,
                            'login': user_email,
                            'partner_id': odoo_partner.id,
                            'active': True,
                            # Optional: Assign company if multi-company setup
                            'company_id': self.env.company.id,
                        }
                        new_user = Users.with_context(no_reset_password=True).create(user_data)

                        # Assign to Portal group (read-only learners)
                        if portal_group:
                            new_user.groups_id = [(6, 0, [portal_group.id])]
                            _logger.info(f"Assigned {new_user.login} to Portal group")


                    # Step 3️⃣: Link partner to course (as attendee)
                    existing_attendee = ChannelPartner.search([
                        ('channel_id', '=', course.id),
                        ('partner_id', '=', odoo_partner.id)
                    ], limit=1)

                    if not existing_attendee:
                        ChannelPartner.create({
                            'channel_id': course.id,
                            'partner_id': odoo_partner.id,
                            'completion': 0.0,
                        })
                        _logger.info(f"Added attendee {odoo_partner.email} to course {course.name}")
                    else:
                        _logger.info(f"{odoo_partner.email} is already enrolled in {course.name}")

                _logger.info(f"✅ Synced enrolled users for course '{course.name}' ({moodle_course_id})")


# https://bwslcu.moodlecloud.com/webservice/rest/server.php?wstoken=ae3e0d8606017fe44bd3b3ce12365bb7&wsfunction=mod_quiz_get_attempt_data&moodlewsrestformat=json&attemptid=6&page=0

    def export_contents(self):
        """Export Odoo eLearning courses and contents to Moodle safely and idempotently."""

        for rec in self:
            base_url = rec.url.rstrip('/')
            endpoint = f"{base_url}/webservice/rest/server.php"
            token = rec.token

            def _call_moodle(wsfunction, extra_params=None):
                """Helper for Moodle REST API calls with error handling"""
                params = {
                    'wstoken': token,
                    'wsfunction': wsfunction,
                    'moodlewsrestformat': 'json',
                }
                if extra_params:
                    params.update(extra_params)
                res = requests.post(endpoint, data=params, timeout=30)
                try:
                    data = res.json()
                except ValueError:
                    raise ValidationError("Invalid JSON response from Moodle.")

                if isinstance(data, dict) and data.get('exception'):
                    _logger.error(f"❌ Moodle API Error: {data}")
                    raise ValidationError(f"Moodle API Error: {data.get('message')}")
                return data

            _logger.warning("🚀 Starting export of Odoo courses to Moodle...")

            SlideChannel = self.env['slide.channel']
            SlideSlide = self.env['slide.slide']
            odoo_courses = SlideChannel.search([('website_published', '=', True)])

            if not odoo_courses:
                _logger.warning("⚠️ No published Odoo courses found to export.")
                continue

            # Fetch Moodle categories and courses once for reuse
            moodle_categories = _call_moodle('core_course_get_categories')
            moodle_courses = _call_moodle('core_course_get_courses')

            for course in odoo_courses:
                _logger.warning(f"📤 Exporting course: {course.name}")
                course_shortname = course.name[:20].replace(' ', '_')
                course_fullname = course.name

                # --- Determine or create category ---
                category_id = 1
                if course.tag_ids:
                    cat_name = course.tag_ids[0].name
                    match = next((c for c in moodle_categories if c.get('name') == cat_name), None)
                    if not match:
                        _logger.warning(f"📂 Creating category '{cat_name}' in Moodle...")
                        created = _call_moodle('core_course_create_categories', {
                            'categories[0][name]': cat_name,
                            'categories[0][parent]': 0,
                        })
                        if isinstance(created, list) and created:
                            category_id = created[0].get('id', 1)
                            moodle_categories.append(created[0])
                    else:
                        category_id = match['id']

                # --- Match or create course ---
                match_course = next(
                    (c for c in moodle_courses if c.get('shortname') == course_shortname or c.get('fullname') == course_fullname),
                    None
                )

                if match_course:
                    moodle_course_id = match_course['id']
                    _logger.warning(f"🔁 Updating existing Moodle course (ID {moodle_course_id}): {course.name}")
                    _call_moodle('core_course_update_courses', {
                        'courses[0][id]': moodle_course_id,
                        'courses[0][fullname]': course_fullname,
                        'courses[0][shortname]': course_shortname,
                        'courses[0][categoryid]': category_id,
                        'courses[0][summary]': html.escape(course.description or ''),
                        'courses[0][format]': 'topics',
                        'courses[0][visible]': 1,
                    })
                    _logger.info(f"✅ Successfully updated '{course.name}' → Moodle ID {moodle_course_id}")
                    course.moodle_course_id = moodle_course_id
                else:
                    _logger.warning(f"➕ Creating new Moodle course: {course.name}")
                    created = _call_moodle('core_course_create_courses', {
                        'courses[0][fullname]': course_fullname,
                        'courses[0][shortname]': course_shortname,
                        'courses[0][categoryid]': category_id,
                        'courses[0][summary]': html.escape(course.description or ''),
                        'courses[0][format]': 'topics',
                        'courses[0][visible]': 1,
                    })
                    if isinstance(created, list) and created:
                        moodle_course_id = created[0]['id']
                        course.moodle_course_id = moodle_course_id
                        moodle_courses.append(created[0])
                        _logger.info(f"✅ Successfully created '{course.name}' → Moodle ID {moodle_course_id}")
                    else:
                        raise ValidationError(f"Failed to create course '{course.name}' in Moodle.\nResponse: {created}")
