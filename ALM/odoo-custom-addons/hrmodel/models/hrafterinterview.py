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
	_name = 'hrafter.hrafter'
	_rec_name = 'names'
	name = fields.Text(string='Family & Occupation')

	names = fields.Char(string='Applicant Name', required=True)

	bornbrought = fields.Text(string='Born & Brought-up Enivronment')

	friends = fields.Text(string='Friends')

	relatives = fields.Text(string='Relatives')

	school = fields.Text(string='School')

	college = fields.Text(string='College')

	scholarship = fields.Text(string='Scholarship/Loan')

	courses = fields.Text(string='Courses')

	projects = fields.Text(string='Projects')

	extracur = fields.Text(string='Extra-Curricular')

	freetime = fields.Text(string='Free Time Spending/Hobbies/Interests')

	goals = fields.Text(string='Goals/Purpose of Job')

	aboutsociety = fields.Text(string='About Society & People')

	processwork = fields.Text(string='Process or Work Flow / Whats your part in it?')

	reasonfor = fields.Text(string='Reason For change From Current Job')

	relieving = fields.Text(string='Relieving Period')

	current = fields.Text(string='Current Renumeration And Benefits')

	expection = fields.Char(string='Expectation')

	roles = fields.Text(string='Roles And Responsibilites')	
	
	skills = fields.Text(string='Skills')
	
	practical = fields.Text(string='Practiacls Test')
	
	requestand = fields.Text(string='Request And Assurance By Candidate')

	reuestinterview = fields.Text(string='Request And Assurance By Interviewer')	
	
	otherkey = fields.Text(string='Other Key Points (if any)')	


