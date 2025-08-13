from odoo import models, api, fields
from openai import OpenAI
from odoo.exceptions import ValidationError
import requests
import base64
import string
from zlib import compress
import re

PREVIEW_HTML = "<h3 style='text-align:center;'>Preview only!<br/>Download source code for details</h3><p>" \
               "<a href='{}/{}' target='_blank'>" \
               "<img style='max-width:95%;height:auto' src='http://www.plantuml.com/plantuml/png/{}'></img>" \
               "</a></p>"

maketrans = bytes.maketrans
plantuml_alphabet = string.digits + string.ascii_uppercase + string.ascii_lowercase + '-_'
base64_alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
b64_to_plantuml = maketrans(base64_alphabet.encode('utf-8'), plantuml_alphabet.encode('utf-8'))

def get_url(plantuml_text):
    zipped_str = compress(plantuml_text.encode('utf-8'))
    compressed_string = zipped_str[2:-4]
    return base64.b64encode(compressed_string).translate(b64_to_plantuml).decode('utf-8')

class ChatGptModel(models.Model):
    _name = 'chat.model'
    _rec_name = 'select_type'

    select_type = fields.Selection([('requirements','Requirements'),('roles','Roles and Activities')], string='Select Intent', default='requirements', required=True)

    # Project Requirements

    project_input = fields.Many2one('dynamic.prompt',string='Project',domain="[('select_type','=','requirements')]")
    desc_input = fields.Char(string='Project Description', related='project_input.description')

    project_inputs = fields.Char(string='Project')
    desc_inputs = fields.Many2one('dynamic.prompt',string='Project Description',domain="[('select_type','=','requirements')]")

    uml_code = fields.Html(string='UML PNG')
    uml_code_char = fields.Text(string='UML Code')
    uml_diagram = fields.Binary(string='Mind-Map')
    uml_link = fields.Text(string='Uml Link')

    response_line = fields.One2many('chat.response','related_id',string='Module Requirements')
    sub_model_line = fields.One2many('chat.submodel','related_id',string='Sub Models')
    fields_line = fields.One2many('chat.fields','related_id',string='Sub Models')

    # Roles and Activities

    designation = fields.Many2one('dynamic.prompt', string='Designation',domain="[('select_type','=','roles')]")
    prompt = fields.Char(string='Prompt', related='designation.content')

    designations = fields.Char(string='Designation')
    prompts = fields.Many2one('dynamic.prompt',string='Prompt',domain="[('content','!=',False)]")

    roles_line = fields.One2many('chat.roles', 'related_id', string='Roles')
    activity_line = fields.One2many('chat.activity', 'related_id', string='Activities')
    action_line = fields.One2many('chat.actions', 'related_id', string='Actions')

    def generate_bot(self):
        return {
            'name': "Generate Activity",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'create.bot',
            'context': {
                'default_related_id': self.id,
                'default_select_relate': 'action',
                },
            'target': 'new'
        }

    def generate_bot_1(self):
        return {
            'name': "Generate Activity",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'create.bot',
            'context': {
                'default_related_id': self.id,
                'default_select_relate': 'field',
                },
            'target': 'new'
        }

    def generate_actions(self):
        lists=[(5,0,0)]
        for i in self.activity_line:
            if i.select_activity == True:
                client = OpenAI(
                    api_key=self.prompts.api_key
                )

                completions = client.chat.completions.create(
                    model=self.prompts.model,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant generating action lists."},
                        {"role": "user", "content": f"List the Actions required for {self.designations} with {i.roles} roles of {i.activity} activity, generate in bullet points only, do not generate Description"},
                    ],
                    temperature=self.prompts.temperature,
                    max_tokens=self.prompts.max_tokens,
                    top_p=self.prompts.top_p,
                    frequency_penalty=self.prompts.frequency_penalty,
                    presence_penalty=self.prompts.presence_penalty,
                )


                paragraph = completions.choices[0].text.strip()

                pattern = r"[.\-\d\•\:]+"
                sentences = re.split(pattern, paragraph)

                modules = []
                for sentence in sentences:
                    modules.append(sentence.strip())

                while("" in modules):
                    modules.remove("")

                for action in modules:
                    data = {
                            'related_id' : self.id,
                            'activity' : i.activity,
                            'actions' : action,
                        }
                    lists.append((0,0,data))

        self.action_line = lists
        return {
            'name': "Generate Activity",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'create.bot',
            'context': {
                'default_related_id': self.id,
                'default_select_relate': 'activity',
                },
            'target': 'new'
        }

    def generate_activity(self):
        lists=[(5,0,0)]
        for i in self.roles_line:
            if i.select_roles == True:
                client = OpenAI(
                    api_key=self.prompts.api_key
                )

                completions = client.chat.completions.create(
                    model=self.prompts.model,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant generating lists of activities."},
                        {"role": "user", "content": f"List the activities required for {self.designations} with {i.roles} role, generate in bullet points only, do not generate Description"},
                    ],
                    temperature=self.prompts.temperature,
                    max_tokens=self.prompts.max_tokens,
                    top_p=self.prompts.top_p,
                    frequency_penalty=self.prompts.frequency_penalty,
                    presence_penalty=self.prompts.presence_penalty,
                )

                paragraph = completions.choices[0].text.strip()

                pattern = r"[.\-\d\•\:]+"
                sentences = re.split(pattern, paragraph)

                modules = []
                for sentence in sentences:
                    modules.append(sentence.strip())

                while("" in modules):
                    modules.remove("")

                for activity in modules:
                    data = {
                            'related_id' : self.id,
                            'roles' : i.roles,
                            'activity' : activity,
                        }
                    lists.append((0,0,data))

        self.activity_line = lists
        return {
            'name': "Generate Activity",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'create.bot',
            'context': {
                'default_related_id': self.id,
                'default_select_relate': 'role',
                    },
            'target': 'new'
        }

    @api.constrains('designations','prompts')
    def generate_roles_act(self):
        if self.prompts:
            headings = [(5,0,0)]
            client = OpenAI(
                api_key=self.prompts.api_key
            )

            completions = client.chat.completions.create(
                model=self.prompts.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant generating dictionary-formatted bullet points."},
                    {"role": "user", "content": f"List the topics of {self.designations} with {self.prompts.content} as Description in Dictionary format: with Bullet Points"},
                ],
                temperature=self.prompts.temperature,
                max_tokens=self.prompts.max_tokens,
                top_p=self.prompts.top_p,
                frequency_penalty=self.prompts.frequency_penalty,
                presence_penalty=self.prompts.presence_penalty,
            )

            paragraph = completions.choices[0].text.strip()

            array = paragraph.split('•')

            result_list = []

            for item in array:
                if item != "":
                    try:
                        key = item.split(':')[0]
                        value = item.split(':')[1]
                        result_list.append([key, value])
                    except IndexError:
                        raise ValidationError('Please Try Again')

            result_obj = dict(result_list)

            for roles,descr in result_obj.items():
                data = {
                        'related_id' : self.id,
                        'roles' : roles,
                        'description' : descr,
                        }
                headings.append((0,0,data))

            self.roles_line = headings

    def generate_uml_diagram(self):
        if self.project_inputs:
            modules = [f"""@startwbs \n * {self.desc_inputs.prompt_input,self.desc_inputs} \n"""]
            models = ['@endwbs']

            for i in self.response_line:
                if i.select_models == True:
                    modules.append('** '+i.modules_name+'\n')
                    for j in self.sub_model_line:
                        if j.select_models == True:
                            if i.modules_name == j.modules_name:
                                modules.append("*** "+j.model_name+'\n')
                                for k in self.fields_line:
                                    if j.model_name == k.model_name:
                                        modules.append('**** '+k.fields_name+'\n')
            fields = modules+models
            new_list = [string.replace(',', '').replace('(', '').replace(')', '').replace("'", '').replace(',', '') for string in fields]
            str1 = " "
            uml_str = str1.join(new_list)
            self.uml_code_char = uml_str

        elif self.designations:
            modules = [f"""@startwbs \n * {self.prompts.content,self.designations} \n"""]
            models = ['@endwbs']

            for i in self.roles_line:
                if i.select_roles == True:
                    modules.append('** '+i.roles+'\n')
                    for j in self.activity_line:
                        if j.select_activity == True:
                            if i.roles == j.roles:
                                modules.append("*** "+j.activity+'\n')
                                for k in self.action_line:
                                    if j.activity == k.activity:
                                        modules.append('**** '+k.actions+'\n')
            fields = modules+models
            new_list = [string.replace(',', '').replace('(', '').replace(')', '').replace("'", '').replace(',', '') for string in fields]
            str1 = " "
            uml_str = str1.join(new_list)
            self.uml_code_char = uml_str

        api_url = "http://www.plantuml.com/plantuml/png/{}".format(get_url(self.uml_code_char))
        self.uml_link = api_url
        image = base64.b64encode(requests.get(api_url).content)

        self.uml_diagram = image

    @api.constrains('project_inputs','desc_input')
    def generate_project(self):
        if self.project_inputs:
            headings = [(5,0,0)]

            client = OpenAI(
                api_key=self.desc_inputs.api_key
            )

            completions = client.chat.completions.create(
                model=self.desc_inputs.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant generating model lists in bullet points without descriptions."},
                    {"role": "user", "content": f"List the required Models for {self.project_inputs} Project with {self.desc_inputs} as description in bullet points Only, Do not Generate Description."},
                ],
                temperature=self.desc_inputs.temperature,
                max_tokens=self.desc_inputs.max_tokens,
                top_p=self.desc_inputs.top_p,
                frequency_penalty=self.desc_inputs.frequency_penalty,
                presence_penalty=self.desc_inputs.presence_penalty,
            )

            paragraph = completions.choices[0].text.strip()

            pattern = r"[.\-\d\•\:]+"
            sentences = re.split(pattern, paragraph)

            modules = []
            for sentence in sentences:
                modules.append(sentence.strip())

            while("" in modules):
                modules.remove("")

            for module in modules:
                data = {
                    'related_id' : self.id,
                    'modules_name' : module
                }
                headings.append((0,0,data))
            self.response_line = headings

    def generate_models(self):

        headings = [(5,0,0)]
        for i in self.response_line:
            if i.select_models == True:
                client = OpenAI(
                    api_key=self.desc_inputs.api_key
                )

                completions = client.chat.completions.create(
                    model=self.desc_inputs.model,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant generating lists of sub-model names in bullet points only, without any descriptions."},
                        {"role": "user", "content": f"List the required Sub-Model names for {self.desc_inputs.prompt_input} Module titles in bullet points Only. Do not Generate Description."},
                    ],
                    temperature=self.desc_inputs.temperature,
                    max_tokens=self.desc_inputs.max_tokens,
                    top_p=self.desc_inputs.top_p,
                    frequency_penalty=self.desc_inputs.frequency_penalty,
                    presence_penalty=self.desc_inputs.presence_penalty,
                )
                paragraph = completions.choices[0].text.strip()

                pattern = r"[.\-\d\•\:]+"
                sentences = re.split(pattern, paragraph)

                modules = []
                for sentence in sentences:
                    modules.append(sentence.strip())

                while("" in modules):
                    modules.remove("")

                for module in modules:
                    data = {
                        'related_id' : self.id,
                        'modules_name' : i.modules_name,
                        'model_name' : module
                    }
                    headings.append((0,0,data))
        self.sub_model_line = headings
        return {
            'name': "Generate Activity",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'create.bot',
            'context': {
                'default_related_id': self.id,
                'default_select_relate': 'module',
                    },
            'target': 'new'
        }

    def generate_fields(self):

        headings = [(5,0,0)]
        for i in self.sub_model_line:
            if i.select_models == True:
                client = OpenAI(
                    api_key=self.desc_inputs.api_key
                )

                completions = client.chat.completions.create(
                    model=self.desc_inputs.model,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant generating field names in bullet points only, without any descriptions."},
                        {"role": "user", "content": f"List the required field names for {i.model_name} Model titles in bullet points Only. Do not generate descriptions."},
                    ],
                    temperature=self.desc_inputs.temperature,
                    max_tokens=self.desc_inputs.max_tokens,
                    top_p=self.desc_inputs.top_p,
                    frequency_penalty=self.desc_inputs.frequency_penalty,
                    presence_penalty=self.desc_inputs.presence_penalty,
                )

                paragraph = completions.choices[0].text.strip()

                pattern = r"[.\-\d\•\:]+"
                sentences = re.split(pattern, paragraph)

                modules = []
                for sentence in sentences:
                    modules.append(sentence.strip())

                while("" in modules):
                    modules.remove("")

                for module in modules:
                    data = {
                        'related_id' : self.id,
                        'model_name' : i.model_name,
                        'fields_name' : module
                    }
                    headings.append((0,0,data))

        self.fields_line = headings
        return {
            'name': "Generate Activity",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'create.bot',
            'context': {
                'default_related_id': self.id,
                'default_select_relate': 'model',
                    },
            'target': 'new'
        }

class ChatGptResponse(models.Model):
    _name = 'chat.response'

    related_id = fields.Many2one('chat.model', string='Related',ondelete='cascade')
    modules_name = fields.Char(string='Modules')
    select_models = fields.Boolean(string='Select')

class ChatGPTsubModels(models.Model):
    _name = 'chat.submodel'

    related_id = fields.Many2one('chat.model', string='Related',ondelete='cascade')
    modules_name = fields.Char(string='Modules')
    model_name = fields.Char(string='Sub-Models')
    select_models = fields.Boolean(string='Select')

class ChatGptResponseFields(models.Model):
    _name = 'chat.fields'

    related_id = fields.Many2one('chat.model', string='Related',ondelete='cascade')
    fields_name = fields.Char(string='Fields')
    model_name = fields.Char(string='Sub-Models')
    select_fields = fields.Boolean(string='Select')

class ChatRolesGenerate(models.Model):
    _name = 'chat.roles'

    roles = fields.Char(string='Roles')
    description = fields.Char(string='Description')
    related_id = fields.Many2one('chat.model', string='Related')
    select_roles = fields.Boolean(string='Select')

class ChatActivitiesGenerate(models.Model):
    _name = 'chat.activity'

    activity = fields.Char(string='Activities')
    related_id = fields.Many2one('chat.model', string='Related')
    select_activity = fields.Boolean(string='Select')
    roles = fields.Char(string='Role')

class ChatActions(models.Model):
    _name = 'chat.actions'

    related_id = fields.Many2one('chat.model', string='Related')
    select_activity = fields.Boolean(string='Select')
    actions = fields.Char(string='Actions')
    activity = fields.Char(string='Activity')
