from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import date,timedelta
import re
from dateutil.relativedelta import relativedelta
import calendar
import datetime



class res_partner_value(models.Model):

    _inherit = 'res.partner'

    mainvalue_ids = fields.One2many('appointment.time','doctor_id',string='Appointment',ondelete='cascade',)
    monthly_appointment = fields.One2many('day.slot','doctor_name',string='appointment',ondelete='cascade',)




    @api.constrains('mainvalue_ids')
    def function_monthly_appointment(self):
        test = []
        todays_date = datetime.datetime.now() + timedelta(hours=5,minutes=30)
        for rec in self:
            no_of_days = calendar.monthrange(todays_date.year, todays_date.month)[1]
            for record in rec.mainvalue_ids:
                for i in range(todays_date.day -1,no_of_days):
                    x = date(todays_date.year,todays_date.month,i+1)
                    if x.strftime("%A") == record.ava_timing:
                        for each_slot in record.appointment_time:
                            slot_datetime = str(x) + " " + str(each_slot.float_time)
                            departure_time_obj = datetime.datetime.strptime(slot_datetime, '%Y-%m-%d %H:%M')
                            dtimestamp = departure_time_obj.timestamp()
                       
                            appointment_slot = self.env['day.slot'].search([('time_stamp','=',dtimestamp),('doctor_name','=',rec._origin.id)])
                            if not appointment_slot:
                                data = {
                                    'date_time' : x,
                                    'work_shift' : record.shifts,
                                    'doctor_name' : record.doctor_id.id,
                                    'consultation_time': record.consultation_differ.id,
                                    'appointment_time_detail' : each_slot._origin.id,
                                    'seven_days' : record.ava_timing,
                                    'time_available':'available',
                                    'status':'active',
                                    'time_stamp': dtimestamp
                                }
                            
                                creat_slot = self.env['day.slot'].create(data)
                            remove_slot = self.env['day.slot'].search([('consultation_time','!=',record.consultation_differ.id),('doctor_name','=',rec._origin.id),('date_time','=',x)])
                            for remove in remove_slot:
                                remove.time_available = 'not_available'
                                remove.status = 'in_active'

