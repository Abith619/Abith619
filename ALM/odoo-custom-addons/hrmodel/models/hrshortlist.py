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
	_name = 'hrshort.hrshort'
	_rec_name = 'names'

	name = fields.Char(string='Key Influencing Points')

	names = fields.Char(string='Applicant Name', required=True)

	rec = fields.Char(string='Recommendation on Designation,Department,Roles And Responsibilites')

	jus = fields.Char(string='Recommendation on Renumeration And Benefits With Justification')

	feedback = fields.Char(string='Feedback')

	managementfeed = fields.Char(string='Feedback')

	finalfeed = fields.Char(string='Feedback')