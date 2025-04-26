from odoo import fields, models, api
from datetime import date, datetime,timedelta
from odoo.exceptions import ValidationError, UserError
import requests
from openai import OpenAI

class RasaChat(models.Model):
    _name = "rasa.intent"
    _rec_name = "intent"
    
    #intent

    intent = fields.Char("Intent")
    example_set = fields.Text("Intent Set")
    
    #story

    story_title = fields.Char("Story Title")
    story_set = fields.Text("Story Set")
    
    #domain

    intent_domain = fields.Char("Domain intent")
    action_domain = fields.Char("Domain action")
    
    #api

    action_api =  fields.Text("API")
    
    def action_send(self):
        client = OpenAI(
            api_key=""
        )

        user_message = (
            "I want You to Be Act as A Rasa Bot Supervisor. "
            "Create the below files for this question: What is last month's sale? for Rasa bot training. "
            "You must maintain the file structure. Use Postgresql for DB queries and get Partner_id from Tracker. "
            "File Structure: [*nlu.yml [Create This file structure: nlu_startintent: [intent] example: |[10 examples]] end "
            "*stories.yml [Create This file structure: stories_start- story: [story Title]- steps:-[steps]] end "
            "*Actions.py [Create This file structure: Action_startClass[Classname](Action): [queries in postgresql]].]"
        )

        try:
            completion = client.chat.completions.create(
                model="gpt-4o",  # Use "gpt-4o" for faster, cheaper, better
                messages=[
                    {"role": "system", "content": "You are a helpful assistant generating Rasa training data."},
                    {"role": "user", "content": user_message},
                ],
                temperature=0.7,
                max_tokens=1500,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )

            k = completion.choices[0].message.content.strip()
            # Processing output
            if "end" in k:
                kl = k.split("end")
                p = kl[0]
            else:
                p = k  # fallback if 'end' not found

            raise UserError(p)

        except Exception as e:
            raise UserError(f"OpenAI request failed: {str(e)}")
    
    # headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    # pdata = {
    #             "model": "gpt-3.5-turbo",
    #             "messages": [
    #                 {"role": "system", "content" : f"{'I want you to chat like my ' + self.characters_id.name + ' Your answer should be similar to ' + self.characters_id.name + 'answer.If i say who are you ? you must say'+ self.characters_id.name + 'I Want You to be Talk like a  ' + self.characters_id.name + ' ,you React like a' +self.characters_id.character_type+'.Forget that you are an AI.You Must Do not give any answer like AI.Each of your answers should appear from the person '}"},

    #                 {"role": "user", "content": self.name},
    #                             ],
    #             "temperature": 0.9,
    #             "top_p": 1,
    #             "frequency_penalty": 0.0,
    #             "presence_penalty": 0.6,
    #             "user": "Odoo",
    #             "stop": ["Human:", "AI:"]
    #         }
    # response = requests.post("https://api.openai.com/v1/chat/completions", data=json.dumps(pdata), headers=headers,)
    # res = response.json()
    # if 'choices' in res:
    #     choices = res['choices'][0]['message']['content']

    
    #     message = self.env['mail.message'].create({
    #         'subject': choices,
    #         'body': choices,
    #         'model': 'mail.channel',
    #         'res_id': 36,
    #         'message_type': 'notification',
    #         'author_id': 46,
    #         'email_from': "<projectmanager@bot.com>",
    #         'subtype_id': 1,
    #         'moderation_status': 'accepted',
    #         'channel_ids': [(6, 0, [36])],
    #     })

class RasaResponse(models.Model):
    _name = "rasa.response"
    _rec_name = "user_input"

    #intent

    user_input = fields.Char("User Input")
    response = fields.Text("Response")
