from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import datetime,timedelta
import re
class timing_data(models.Model):
    _name='appointment.time'
    # _rec_name = 'namess'

    doctor_id= fields.Many2one('res.partner',string ='Name')
    doctor_detail = fields.Char(string='doctor')
   
    shifts = fields.Selection([('days_shift','Morining Shift'),('evening','Evening Shift')],string='Shift')
    appointment_time = fields.Many2many('many.times',string='Appointment Time',domain="[('miniutes_differ', '=', consultation_differ)]",required=True)
    date_time = fields.Date(string='Date')

    ava_timing = fields.Selection([('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),
    ('Thursday','Thursday'),('Friday','Friday'),('Saturday','Saturday'),('Sunday','Sunday')],string='Select available timings',required=True)

    consultation_differ = fields.Many2one('consultation.hour',string='Consultation Hour',required=True)
    start_time = fields.Char(string='Start Time')
    end_time = fields.Char(string='End Time')
    status = fields.Selection([('active','Active'),('inactive','In Active')],string='Status',default="active")

    @api.onchange('start_time','end_time','consultation_differ')
    def time_slots(self):
        for rec in self:
            if rec.start_time and rec.end_time and rec.consultation_differ:
                if re.search("[0-1][0-9]:[0-5][0-9]|[0-2][0-3]:[0-5][0-9]",rec.start_time) and re.search("[0-1][0-9]:[0-5][0-9]|[0-2][0-3]:[0-5][0-9]",rec.end_time):
                    start = rec.start_time.split(':')
                    starting_time = str(rec.start_time)
                    count = int(start[1])
                    con = rec.consultation_differ.consultation_hour
                    consult_time = con.split(':')
                    end_time = str(rec.end_time)
                    rec.appointment_time = [5,0,0]
                    time_slots = []
                    str_start_time = datetime.strptime(rec.start_time,'%H:%M').time()
                    str_end_time = datetime.strptime(rec.end_time,'%H:%M').time()
                    if str_start_time > str_end_time:
                        raise ValidationError("Start time is Greater than End time")
                    else:
                        for gen in range(100):
                            if gen == 0:
                                resultant_time = datetime.strptime(rec.start_time,'%H:%M').time()
                                data = self.env['many.times'].search([('times_data','=',str(resultant_time.strftime("%I:%M %p"))),('miniutes_differ','=',rec.consultation_differ.consultation_hour)])
                                if data:
                                    time_slots.append(data.id)
                            else:
                                add_time = timedelta(hours=int(start[0]),minutes=int(start[1])) + timedelta(hours=int(consult_time[0]),minutes=int(consult_time[1]))
                                resultant_time = datetime.strptime(str(add_time),'%H:%M:%S').time()
                                starting_time = str(resultant_time)[:-3]
                                start[0] = starting_time[:-3]
                                start[1] = starting_time[3:]
                                if starting_time == end_time:
                                    break
                        
                                data = self.env['many.times'].search([('times_data','=',str(resultant_time.strftime("%I:%M %p"))),('miniutes_differ','=',rec.consultation_differ.consultation_hour)])
                                if data:
                                    time_slots.append(data.id)
                                            # else:
                                            #     create_time = self.env['many.times'].create({'times_data':value,'miniutes_differ':rec.consultation_differ.id})
                                            #     time_slots.append(create_time.id)
                        rec.appointment_time = [(6,0,time_slots)]
                else:
                    raise ValidationError("In Valid formate for Start or End time. Give Railway time Eg: 21:00")
            
            else:
                pass







class time_details(models.Model):
    _name = 'many.times'
    _rec_name = 'times_data'
    
    times_data = fields.Char('Minutes')
    miniutes_differ = fields.Many2one('consultation.hour',string='Consulting Hour')
    float_time = fields.Char('Float Time')
    status = fields.Selection([('active','Active'),('inactive','In Active')],string='Status',default="active")

    
class consultation_details(models.Model):
    _name = 'consultation.hour'
    _rec_name = 'consultation_hour'
    consultation_hour = fields.Char(string='Consultation Hour')




class day_slot(models.Model):
    _name = 'day.slot'
    _rec_name = 'seven_days'

    date_time = fields.Date('Date')

    work_shift = fields.Selection([('days_shift','Days Shift'),('evening','Evening Shift')],string='Shift')
    appointment_time_detail = fields.Many2one('many.times',string='Appointment Time',)
    seven_days = fields.Selection([('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),
    ('Thursday','Thursday'),('Friday','Friday'),('Saturday','Saturday'),('Sunday','Sunday')],string='Select available timings')
    time_stamp = fields.Float(string='Time Stamp')
    consultation_time = fields.Many2one('consultation.hour',string='Consultation Hour',)
    doctor_name= fields.Many2one('res.partner',string ='name')
    # time_available = fields.Many2many('time.available',string='Time Avilable')
    time_available = fields.Selection([('available','Available'),('not_available','Not Available')],string='Time Available Slot')
    status = fields.Selection([('active','Active'),('in_active','In Active')],string='Status')
    payment_status = fields.Boolean(string = 'Paid')   
    payment_timer = fields.Datetime(string = 'payment_timer')   
    payment_time_status = fields.Boolean(string = 'Payment Timer Status')
    day_vals = fields.Integer(string='Time Stamp')
