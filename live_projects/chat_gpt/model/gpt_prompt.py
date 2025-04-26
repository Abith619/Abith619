from odoo import fields, models, api
from datetime import date, datetime,timedelta
from odoo.exceptions import ValidationError, UserError
from openai import OpenAI

class GptPrompt(models.Model):
    _name = "gpt.prompt"
    _rec_name = 'question'

    token = fields.Char("Token")
    question = fields.Char('Question')
    prompt = fields.Text(string='Prompt ', default=f'I want You to Be Act as A Rasa Bot Superviser .Create the below files for this question: for Rasa bot training.You  Must Maintain The nlu File Structure.Use Postgresql for Db Queries And Get Partner_id from Tracker.File Structure : [*nlu.yml[Create This file structue  : nlu_startintent :[intent] example : |[15 examples]]nlu_end*stories.yml[Create This file structue  : stories_startstory: [story Title]steps:-[steps]stories_end],*Actions. py[write custom action  : Action_startClassClassname:[queris in postgresql]Action_end].].')

    @api.model
    def generate_project(self):
        client = OpenAI(
            api_key=self.token or "your-fallback-api-key"
        )

        user_message = f"{self.prompt}\n{self.question}"

        try:
            completion = client.chat.completions.create(
                model="gpt-4o",  # Use "gpt-4o" or "gpt-4o-mini" if available
                messages=[
                    {"role": "system", "content": "You are a helpful assistant generating Rasa training data."},
                    {"role": "user", "content": user_message},
                ],
                temperature=0.7,
                max_tokens=1000,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )

            paragraph = completion.choices[0].message.content.strip()

            # Now parsing the response
            nlu = ((paragraph.split("nlu_startintent:"))[1].split("nlu_end"))[0]
            story = ((paragraph.split("stories_start"))[1].split("stories_end"))[0]
            api_data = ((paragraph.split("Action_start"))[1].split("Action_end"))[0]
            intent = ((nlu.split("intent:")[1]).split("examples:"))[0]
            story_title = ((story.split("story:"))[1].split("steps:"))[0]
            action = (story.split("action:"))[-1]

            data = {
                'intent': intent.strip(),
                'example_set': nlu.strip(),
                'story_title': story_title.strip(),
                'story_set': story.strip(),
                'action_api': api_data.strip(),
                'intent_domain': intent.strip(),
                'action_domain': action.strip(),
            }
            self.env['rasa.intent'].create(data)

        except Exception as e:
            raise ValidationError(f"Error generating project: {e}")