from odoo import models, fields, api
from odoo.exceptions import ValidationError
import requests, base64
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

            if rec.category:
                data = _call_moodle('core_course_get_categories')
                CategoryGroup = self.env['slide.channel.tag.group']
                Tag = self.env['slide.channel'].search([('id', '=', 1)], limit=1)

                for cat in data:
                    if not isinstance(cat, dict):
                        continue

                    name = cat.get('name')
                    category_id = cat.get('id')

                    existing_group = CategoryGroup.search([('id', '=', 2)], limit=1)
                    if not existing_group:
                        continue

                    # Check if this tag already exists (to avoid duplicates)
                    existing_tag = self.env['slide.channel.tag'].search([
                        ('name', '=', name),
                        ('group_id', '=', existing_group.id)
                    ], limit=1)

                    if not existing_tag:
                        Tag.write({
                            'tag_ids': [(0, 0, {
                                'name': name,
                                'group_id': existing_group.id,
                            })]
                        })

                results['categories'] = data
            if rec.course:
                data = _call_moodle('core_course_get_courses')
                SlideChannel = self.env['slide.channel']
                SlideSlide = self.env['slide.slide']
                CategoryGroup = self.env['slide.channel.tag.group']

                for course in data:
                    if not isinstance(course, dict):
                        continue

                    moodle_course_id = course.get('id')
                    name = course.get('fullname', f"Moodle Course {moodle_course_id}")
                    summary = course.get('summary', '')
                    category_id = course.get('categoryid')

                    # --- Find or create related category ---
                    category = CategoryGroup.search([('moodle_id', '=', category_id)], limit=1) if category_id else False

                    # --- Check if Odoo course already exists ---
                    existing_course = SlideChannel.search([('moodle_course_id', '=', moodle_course_id)], limit=1)
                    course_vals = {
                        'name': name,
                        'description': summary or '',
                        'moodle_course_id': moodle_course_id,
                        'tag_ids': [(6, 0, [category.id])] if category else False,
                        'website_published': True,
                    }

                    if existing_course:
                        existing_course.write(course_vals)
                        slide_channel = existing_course
                    else:
                        slide_channel = SlideChannel.create(course_vals)

                    # --- Fetch course sections & contents ---
                    content_data = _call_moodle('core_course_get_contents', {'courseid': moodle_course_id})
                    # test_response = _call_moodle('core_course_get_contents', {'courseid': 9})
                    if not isinstance(content_data, list):
                        continue
                    # response_list = []
                    # for i in test_response:
                    #     response_list.append(i)
                    # raise ValidationError(response_list)
                    for section in content_data:
                        section_name = section.get('name') or 'Untitled Section'
                        modules = section.get('modules', [])

                        existing_section_slide = SlideSlide.search([
                            ('name', '=', section_name),
                            ('channel_id', '=', slide_channel.id),
                        ], limit=1)

                        section_slide_vals = {
                            'name': section_name,
                            'channel_id': slide_channel.id,
                            'is_category': True,
                        }
                        if not existing_section_slide:
                            section_slide = SlideSlide.create(section_slide_vals)
                        else:
                            section_slide = existing_section_slide

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

                            # --- Slide type mapping ---
                            # These are valid Odoo 'slide_type' values
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

                            # --- Infer from MIME type ---
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

                            # --- Prepare slide values ---
                            slide_vals = {
                                'name': mod_name,
                                'channel_id': slide_channel.id,
                                'slide_category': slide_type,
                                'description': mod_summary or '',
                                'website_published': True,
                            }

                            # --- Set URL or file link ---
                            if file_url:
                                # Download and attach file into Odoo
                                token = rec.token
                                if token and 'token=' not in file_url:
                                    if '?' in file_url:
                                        file_url = f"{file_url}&token={token}"
                                    else:
                                        file_url = f"{file_url}?token={token}"

                                response = requests.get(file_url)
                                if response.status_code == 200:
                                    file_content = base64.b64encode(response.content)
                                    slide_vals.update({
                                        'source_type': 'local_file',
                                        'image_binary_content': file_content,
                                        'url': file_url,
                                    })
                            else:
                                slide_vals.update({
                                    'source_type': 'external',
                                    'url': mod_url,
                                })
                            if mod_type == 'book':
                                for content in module.get('contents', []):
                                    if content.get('type') == 'file':
                                        file_url = content.get('fileurl')
                                        break
                                html_content = ''
                                if file_url:
                                    token = rec.token
                                    url_with_token = f"{file_url}?token={token}"
                                    if token and 'token=' not in file_url:
                                        try:
                                            response = requests.get(url_with_token, timeout=10)
                                            if response.status_code == 200:
                                                html_content = response.text
                                            else:
                                                _logger.warning(f"Failed to fetch HTML from {url_with_token}: {response.status_code}")
                                        except Exception as e:
                                            _logger.error(f"Error fetching HTML from Moodle Book URL: {e}")
                                    # raise ValidationError(html_content)
                                slide_vals.update({
                                    'source_type': 'external',
                                    'html_content': html_content,
                                    'url': False,
                                })

                            if mod_type == 'quiz':
                                # raise ValidationError(mod_type)
                                slide_vals.update({
                                    'slide_category': 'quiz',
                                    'source_type': 'external',
                                    'html_content': False,
                                    # 'question_ids': [((0, 0, {
                                    #     'question': mod_name,
                                    #     'slide_id': section_slide.id,
                                    #     'answer_ids': [(0, 0, {
                                    #         'text_value': 'Answer 1',
                                    #     })]
                                    # }))],
                                })

                            existing_slide = SlideSlide.search([
                                ('name', '=', mod_name),
                                ('channel_id', '=', slide_channel.id),
                            ], limit=1)

                            if existing_slide:
                                existing_slide.write(slide_vals)
                            else:
                                SlideSlide.create(slide_vals)

                results['courses'] = data


            # summary = "\n".join([f"✅ {k.capitalize()}: {len(v)} fetched & synced" for k, v in results.items()])
            # if not summary:
            #     summary = "No options selected for fetching data."
            # raise ValidationError(summary)
