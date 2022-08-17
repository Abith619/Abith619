# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import date
import re
from dateutil.relativedelta import relativedelta
from datetime import datetime, date, timedelta
from odoo import models, fields, api, _
from odoo.exceptions import Warning, UserError
import pytz

class Model(models.Model):
	_name = 'afterin.afterin'
	_rec_name = 'names'
	names = fields.Char(string='Applicant Name', required=True)
	name = fields.Selection([('Excellent', 'Excellent'), ('Good', 'Good'), ('Moderate', 'Moderate'), ('Bad', 'Bad')] , string='Hospitality (Eg:offering water,coffee,sending off)')

	ourbehaviour = fields.Selection([('Excellent', 'Excellent'), ('Good', 'Good'), ('Moderate', 'Moderate'), ('Bad', 'Bad')] ,string='Behaviour/Approach')

	emailphone = fields.Selection([('Excellent', 'Excellent'), ('Good', 'Good'), ('Moderate', 'Moderate'), ('Bad', 'Bad')] ,string='Clarity on our Email/Phone Communication')

	timing = fields.Selection([('Excellent', 'Excellent'), ('Good', 'Good'), ('Moderate', 'Moderate'), ('Bad', 'Bad')] ,string='Our communication on Schedules/Times/Venue')

	doubts = fields.Selection([('Excellent', 'Excellent'), ('Good', 'Good'), ('Moderate', 'Moderate'), ('Bad', 'Bad')] ,string='Our Response to your Queries/Doubts')        

	conduct = fields.Selection([('Excellent', 'Excellent'), ('Good', 'Good'), ('Moderate', 'Moderate'), ('Bad', 'Bad')] ,string='Our Professionalism & Conduct')  

	office = fields.Selection([('Excellent', 'Excellent'), ('Good', 'Good'), ('Moderate', 'Moderate'), ('Bad', 'Bad')] ,string='Office Reachability(Eg:Teavel Access Like Bus,Auto,etc)')

	officeoutside = fields.Selection([('Excellent', 'Excellent'), ('Good', 'Good'), ('Moderate', 'Moderate'), ('Bad', 'Bad')] ,string='Office Outside Enivronment')  

	officesafety = fields.Selection([('Excellent', 'Excellent'), ('Good', 'Good'), ('Moderate', 'Moderate'), ('Bad', 'Bad')] ,string='Office outside Safety')  

	officeinside = fields.Selection([('Excellent', 'Excellent'), ('Good', 'Good'), ('Moderate', 'Moderate'), ('Bad', 'Bad')] ,string='Office Inside Environment')  

	specify = fields.Text(string='(please specify,if any)')  


	specifyifany = fields.Text(string='(please specify,if any)')  
