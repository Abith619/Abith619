from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BoothWebsite(models.Model):
    _inherit = 'event.booth.category'

    quantity_details = fields.Html(string='Quantity Details')

class EventBoothInherit(models.Model):
    _inherit = 'event.booth'

    sales_person = fields.Selection(
        [('jackie', 'Jackie Hooker'), ('jean', 'Jean Michel'), ('Garrett', 'Garrett Brunnquell'),
        ('Jessica', 'Jessica Collins'), ('Bobby', 'Bobby Fulcher'), ('Joseph', 'Joseph Dunleavy'),
        ('Mont', "Mont'a McAdory"), ('Meinen', 'Jessica Meinen'), ('Marlena', 'Marlena Fineberg'),
        ('Kyle', 'Kyle Ewanic'), ('Sean', 'Sean McDonough'), ('other', 'Others')],
        string='Sales Person')
    sales_persons : fields.Many2one = fields.Many2one('sales.person.custom', string='Sales Person')

class EventRegistrationCustom(models.Model):
    _inherit = 'event.registration'

    sales_person = fields.Selection(
        [('jackie', 'Jackie Hooker'), ('jean', 'Jean Michel'), ('Garrett', 'Garrett Brunnquell'),
        ('Jessica', 'Jessica Collins'), ('Bobby', 'Bobby Fulcher'), ('Joseph', 'Joseph Dunleavy'),
        ('Mont', "Mont'a McAdory"), ('Meinen', 'Jessica Meinen'), ('Marlena', 'Marlena Fineberg'),
        ('Kyle', 'Kyle Ewanic'), ('Sean', 'Sean McDonough'), ('other', 'Others')],
        string='Sales Person')
    sales_persons : fields.Many2one = fields.Many2one('sales.person.custom', string='Sales Person')

class EventBoothRegistrationCustom(models.Model):
    _inherit = 'event.booth.registration'

    sales_person = fields.Selection(
        [('jackie', 'Jackie Hooker'), ('jean', 'Jean Michel'), ('Garrett', 'Garrett Brunnquell'),
        ('Jessica', 'Jessica Collins'), ('Bobby', 'Bobby Fulcher'), ('Joseph', 'Joseph Dunleavy'),
        ('Mont', "Mont'a McAdory"), ('Meinen', 'Jessica Meinen'), ('Marlena', 'Marlena Fineberg'),
        ('Kyle', 'Kyle Ewanic'), ('Sean', 'Sean McDonough'), ('other', 'Others')],
        string='Sales Person')
    sales_persons : fields.Many2one = fields.Many2one('sales.person.custom', string='Sales Person')
