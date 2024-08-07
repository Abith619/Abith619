# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from email.policy import default
from inspect import signature
from odoo import api, fields, models, _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta 
from odoo.exceptions import  ValidationError
import qrcode
import base64
from io import BytesIO



class medical_patient(models.Model):
    
    _name = 'medical.patient'
    _rec_name = 'patient_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # @api.onchange('patient_id')
    # def _onchange_patient(self):
    #     '''
    #     The purpose of the method is to define a domain for the available
    #     purchase orders.
    #     '''
    #     address_id = self.patient_id
    #     self.partner_address_id = address_id

    def no_fees(self):
        orm = self.env['medical.doctor'].search([('patient','=',self.patient_id.id)])
        # raise ValidationError(orm)
        orm.update({
            'no_fees':True})
    
    @api.onchange('patient_id')
    def on_patient(self):
        patient_orm = self.env['res.partner'].search([('id','=',self.patient_id.id)])
        orm_city = self.env['res.city'].search([('name','=',patient_orm.city)])
        self.update({
            'reg_type':'dir',
            'contact_no':patient_orm.mobile,
            'sex':patient_orm.patient_gender,
            'contact_number':patient_orm.whatsapp,
            'name':patient_orm.doctor_idxs,
            'date_of_birth':patient_orm.dob_contact,
            'occupation':patient_orm.designation,
            'designation':patient_orm.experience,
            'address':patient_orm.street,
            'city':orm_city,
            'state':patient_orm.state_id,
            'pin_code':patient_orm.zip,
            'country':patient_orm.country_id,
            'marital_status':patient_orm.marital_status,
            'treatment_for':patient_orm.treatment_for,
            'abroad_addr':patient_orm.abroad_addr,
            })
        patient_orm.write({'roles_selection':'patient',
        'mobile':self.contact_no,
        'patient_gender':self.sex,
        'is_patient':True,
        })

    def print_report(self):
        return self.env.ref('basic_hms.report_print_patient_card').report_action(self)

    @api.depends('date_of_birth')
    def onchange_age(self):
        for rec in self:
            if rec.date_of_birth:
                d1 = rec.date_of_birth
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years) + "y" +" "+ str(rd.months) + "m" +" "+ str(rd.days) + "d"
            else:
                rec.age = "Age"

    qr_type = fields.Selection([('n',''),('qr','QR Scan')], string='QR')
    whatsapp_check=fields.Boolean()
    stages= fields.Selection([('draft',"New"),('on',"On Process"),('done',"Done")])
    patient_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient Name", required= True)
    name = fields.Char(string ="Patient ID",readonly=True)
    blood_pressure = fields. Float(string="Blood Pressure")
    last_name = fields.Char('Last Name')
    date_of_birth = fields.Date(string="Date of Birth")
    sex = fields.Selection([('m', 'Male'),('f', 'Female')], string ="Sex",required= True)
    age = fields.Char(compute=onchange_age,string="Age",store=True,readonly=False)
    critical_info = fields.Text(string="Patient Critical Information")
    photo = fields.Binary(string="Picture")
    blood_type = fields.Selection([('A', 'A'),('B', 'B'),('AB', 'AB'),('O', 'O')], string ="Blood Type")
    rh = fields.Selection([('-+', '+'),('--', '-')], string ="Rh")
    marital_status = fields.Selection([('s','Single'),('m','Married'),('w','Widowed'),('d','Divorced'),('x','Seperated')],string='Marital Status')
    deceased = fields.Boolean(string='Deceased')
    date_of_death = fields.Datetime(string="Date of Death")
    cause_of_death = fields.Char(string='Cause of Death')
    receivable = fields.Float(string="Receivable", readonly=True)
    current_insurance_id = fields.Many2one('medical.insurance',string="Insurance")
    partner_address_id = fields.Many2one('res.partner', string="Address", )
    primary_care_physician_id = fields.Many2one('medical.physician', string="Primary Care Doctor")
    patient_status = fields.Char(string="Hospitalization Status",readonly=True)
    patient_disease_ids = fields.One2many('medical.patient.disease','patient_id')
    patient_psc_ids = fields.One2many('medical.patient.psc','patient_id')
    excercise = fields.Boolean(string='Excercise')
    excercise_minutes_day = fields.Integer(string="Minutes/Day")
    sleep_hours = fields.Integer(string="Hours of sleep")
    sleep_during_daytime = fields.Boolean(string="Sleep at daytime")
    number_of_meals = fields.Integer(string="Meals per day")
    coffee = fields.Boolean('Coffee')
    coffee_cups = fields.Integer(string='Cups Per Day')
    eats_alone = fields.Boolean(string="Eats alone")
    soft_drinks = fields.Boolean(string="Soft drinks(sugar)")
    salt = fields.Boolean(string="Salt")
    diet = fields.Boolean(string=" Currently on a diet ")
    diet_info = fields.Integer(string=' Diet info ')
    general_info = fields.Text(string="Info")
    lifestyle_info = fields.Text('Lifestyle Information')
    smoking = fields.Boolean(string="Smokes")
    smoking_number = fields.Integer(string="Cigarretes a day")
    ex_smoker = fields.Boolean(string="Ex-smoker")
    second_hand_smoker = fields.Boolean(string="Passive smoker")
    age_start_smoking = fields.Integer(string="Age started to smoke")
    age_quit_smoking = fields.Integer(string="Age of quitting")
    drug_usage = fields.Boolean(string='Drug Habits')
    drug_iv = fields.Boolean(string='IV drug user')
    ex_drug_addict = fields.Boolean(string='Ex drug addict')
    age_start_drugs = fields.Integer(string='Age started drugs')
    age_quit_drugs = fields.Integer(string="Age quit drugs")
    alcohol = fields.Boolean(string="Drinks Alcohol")
    ex_alcohol = fields.Boolean(string="Ex alcoholic")
    age_start_drinking = fields.Integer(string="Age started to drink")
    age_quit_drinking = fields.Integer(string="Age quit drinking")
    alcohol_beer_number = fields.Integer(string="Beer / day")
    alcohol_wine_number = fields.Integer(string="Wine / day")
    alcohol_liquor_number = fields.Integer(string="Liquor / day")
    cage_ids = fields.One2many('medical.patient.cage','patient_id')
    sex_oral = fields.Selection([('0','None'),
                                 ('1','Active'),
                                 ('2','Passive'),
                                 ('3','Both')],string='Oral Sex')
    sex_anal = fields.Selection([('0','None'),
                                 ('1','Active'),
                                 ('2','Passive'),
                                 ('3','Both')],string='Anal Sex')
    prostitute = fields.Boolean(string='Prostitute')
    sex_with_prostitutes = fields.Boolean(string=' Sex with prostitutes ')
    sexual_preferences = fields.Selection([
            ('h', 'Heterosexual'),
            ('g', 'Homosexual'),
            ('b', 'Bisexual'),
            ('t', 'Transexual'),
        ], 'Sexual Orientation', sort=False)
    sexual_practices = fields.Selection([
            ('s', 'Safe / Protected sex'),
            ('r', 'Risky / Unprotected sex'),
        ], 'Sexual Practices', sort=False)
    sexual_partners = fields.Selection([
            ('m', 'Monogamous'),
            ('t', 'Polygamous'),
        ], 'Sexual Partners', sort=False)
    sexual_partners_number = fields.Integer('Number of sexual partners')
    first_sexual_encounter = fields.Integer('Age first sexual encounter')
    anticonceptive = fields.Selection([
            ('0', 'None'),
            ('1', 'Pill / Minipill'),
            ('2', 'Male condom'),
            ('3', 'Vasectomy'),
            ('4', 'Female sterilisation'),
            ('5', 'Intra-uterine device'),
            ('6', 'Withdrawal method'),
            ('7', 'Fertility cycle awareness'),
            ('8', 'Contraceptive injection'),
            ('9', 'Skin Patch'),
            ('10', 'Female condom'),
        ], 'Anticonceptive Method', sort=False)
    sexuality_info = fields.Text('Extra Information')
    motorcycle_rider = fields.Boolean('Motorcycle Rider', help="The patient rides motorcycles")
    helmet = fields.Boolean('Uses helmet', help="The patient uses the proper motorcycle helmet")
    traffic_laws = fields.Boolean('Obeys Traffic Laws', help="Check if the patient is a safe driver")
    car_revision = fields.Boolean('Car Revision', help="Maintain the vehicle. Do periodical checks - tires,breaks ...")
    car_seat_belt = fields.Boolean('Seat belt', help="Safety measures when driving : safety belt")
    car_child_safety = fields.Boolean('Car Child Safety', help="Safety measures when driving : child seats, proper seat belting, not seating on the front seat, ....")
    home_safety = fields.Boolean('Home safety', help="Keep safety measures for kids in the kitchen, correct storage of chemicals, ...")
    fertile = fields.Boolean('Fertile')
    menarche = fields.Integer('Menarche age')
    menopausal = fields.Boolean('Menopausal')
    menopause = fields.Integer('Menopause age')
    menstrual_history_ids = fields.One2many('medical.patient.menstrual.history','patient_id')
    breast_self_examination = fields.Boolean('Breast self-examination')
    mammography = fields.Boolean('Mammography')
    pap_test = fields.Boolean('PAP test')
    last_pap_test = fields.Date('Last PAP test')
    colposcopy = fields.Boolean('Colposcopy')
    mammography_history_ids = fields.One2many('medical.patient.mammography.history','patient_id')
    pap_history_ids = fields.One2many('medical.patient.pap.history','patient_id')
    colposcopy_history_ids = fields.One2many('medical.patient.colposcopy.history','patient_id')
    pregnancies = fields.Integer('Pregnancies')
    premature = fields.Integer('Premature')
    stillbirths = fields.Integer('Stillbirths')
    abortions = fields.Integer('Abortions')
    pregnancy_history_ids = fields.One2many('medical.patient.pregnency','patient_id')
    family_history_ids = fields.Many2many('medical.family.disease',string="Family Disease Lines")
    perinatal_ids = fields.Many2many('medical.preinatal')
    ex_alcoholic = fields.Boolean('Ex alcoholic')
    currently_pregnant = fields.Boolean('Currently Pregnant')
    born_alive = fields.Integer('Born Alive')
    gpa = fields.Char('GPA')
    works_at_home = fields.Boolean('Works At Home')
    colposcopy_last = fields.Date('Last colposcopy')
    mammography_last = fields.Date('Last mammography')
    ses = fields.Selection([
            ('None', ''),
            ('0', 'Lower'),
            ('1', 'Lower-middle'),
            ('2', 'Middle'),
            ('3', 'Middle-upper'),
            ('4', 'Higher'),
        ], 'Socioeconomics', help="SES - Socioeconomic Status", sort=False)
    education = fields.Selection([('o','None'),('1','Incomplete Primary School'),
                                  ('2','Primary School'),
                                  ('3','Incomplete Secondary School'),
                                  ('4','Secondary School'),
                                  ('5','University')],string='Education Level')
    housing = fields.Selection([
            ('None', ''),
            ('0', 'Shanty, deficient sanitary conditions'),
            ('1', 'Small, crowded but with good sanitary conditions'),
            ('2', 'Comfortable and good sanitary conditions'),
            ('3', 'Roomy and excellent sanitary conditions'),
            ('4', 'Luxury and excellent sanitary conditions'),
        ], 'Housing conditions', help="Housing and sanitary living conditions", sort=False)
    works = fields.Boolean('Works')
    hours_outside = fields.Integer('Hours outside home', help="Number of hours a day the patient spend outside the house")
    hostile_area = fields.Boolean('Hostile Area')
    notes = fields.Text(string="Extra info")
    sewers = fields.Boolean('Sanitary Sewers')
    water = fields.Boolean('Running Water')
    trash = fields.Boolean('Trash recollection')
    electricity = fields.Boolean('Electrical supply')
    gas = fields.Boolean('Gas supply')
    telephone = fields.Boolean('Telephone')
    television = fields.Boolean('Television')
    internet = fields.Boolean('Internet')
    single_parent= fields.Boolean('Single parent family')
    domestic_violence = fields.Boolean('Domestic violence')
    working_children = fields.Boolean('Working children')
    teenage_pregnancy = fields.Boolean('Teenage pregnancy')
    sexual_abuse = fields.Boolean('Sexual abuse')
    drug_addiction = fields.Boolean('Drug addiction')
    school_withdrawal = fields.Boolean('School withdrawal')
    prison_past = fields.Boolean('Has been in prison')
    prison_current = fields.Boolean('Is currently in prison')
    relative_in_prison = fields.Boolean('Relative in prison', help="Check if someone from the nuclear family - parents sibblings  is or has been in prison")
    fam_apgar_help = fields.Selection([
            ('None', ''),
            ('0', 'None'),
            ('1', 'Moderately'),
            ('2', 'Very much'),
        ], 'Help from family',
            help="Is the patient satisfied with the level of help coming from the family when there is a problem ?", sort=False)
    fam_apgar_discussion = fields.Selection([
            ('None', ''),
            ('0', 'None'),
            ('1', 'Moderately'),
            ('2', 'Very much'),
        ], 'Problems discussion',
            help="Is the patient satisfied with the level talking over the problems as family ?", sort=False)
    fam_apgar_decisions = fields.Selection([
            ('None', ''),
            ('0', 'None'),
            ('1', 'Moderately'),
            ('2', 'Very much'),
        ], 'Decision making',
            help="Is the patient satisfied with the level of making important decisions as a group ?", sort=False)
    fam_apgar_timesharing = fields.Selection([
            ('None', ''),
            ('0', 'None'),
            ('1', 'Moderately'),
            ('2', 'Very much'),
        ], 'Time sharing',
            help="Is the patient satisfied with the level of time that they spend together ?", sort=False)
    fam_apgar_affection = fields.Selection([
            ('None', ''),
            ('0', 'None'),
            ('1', 'Moderately'),
            ('2', 'Very much'),
        ], 'Family affection',
            help="Is the patient satisfied with the level of affection coming from the family ?", sort=False)
    fam_apgar_score = fields.Integer('Score', help="Total Family APGAR 7 - 10 : Functional Family 4 - 6  : Some level of disfunction \n"
                                          "0 - 3  : Severe disfunctional family \n")
    lab_test_ids = fields.One2many('medical.patient.lab.test','patient_id')
    fertile = fields.Boolean('Fertile')
    menarche_age  = fields.Integer('Menarche age')
    menopausal = fields.Boolean('Menopausal')
    pap_test_last = fields.Date('Last PAP Test')
    colposcopy = fields.Boolean('Colpscopy')
    gravida = fields.Integer('Pregnancies')
    # medical_vaccination_ids = fields.One2many('medical.vaccination','medical_patient_vaccines_id')
    # medical_appointments_ids = fields.One2many('medical.appointment','patient_id',string='Appointments')
    lastname = fields.Char('Last Name')
    report_date = fields.Date('Date',default = datetime.today().date())
    # medication_ids = fields.One2many('medical.patient.medication1','medical_patient_medication_id')
    deaths_2nd_week = fields.Integer('Deceased after 2nd week')
    deaths_1st_week = fields.Integer('Deceased after 1st week')
    full_term = fields.Integer('Full Term')
    ses_notes = fields.Text('Notes')
    patient_photo = fields.Binary(string='Photo', widget='image')
    appoinment_by = fields.Many2one('res.users',string='Appointment By',readonly=True,default=lambda self: self.env.user)


#inherit fields
    adoption_agreement = fields.Boolean()
    family_details = fields.Boolean() 
    area=fields.Char(string="Area")
    city=fields.Many2one('res.city',string="City")

    fees = fields.Float(string="Fees")
    contact_no = fields.Char(string="Contact No", required= True)
    contact_number=fields.Char(string="Whatsapp Number")
    date1 = fields.Datetime(string="Date", default=fields.Datetime.now())
    fess = fields.Float(string="Consultation Fee",default=150)
    doctors = fields.Many2one('res.partner',string="Doctor Allocation",domain=[('is_doctor','=',True)],track_visibility='onchange')
    height = fields.Float(string="Height in Cms")
    weight = fields.Float(string="Weight in Kgs")
    occupation = fields.Char(string="Occupation")
    designation = fields.Char(string="Designation")
    
    father_name = fields.Selection([('1','Father'),('2','Husband'),('3','Mother'),('4','Wife'),('5','Gaurdian'),('6','Relative')])
    father_occupation = fields.Char(string="Father Occupation")
    address = fields.Char(string="Address")
    state=fields.Many2one('res.country.state',string="State" ,domain="[('country_id', '=', country)]")
    country=fields.Many2one('res.country',string="Country")
    pincode = fields.Integer(string="Pincode")
    Phone_mobile = fields.Integer(string="Phone / Mobile")
    email = fields.Char(string="Email")
    office_address = fields.Char(string="Office Address")
    offPhone_mobile = fields.Integer(string="Office Phone")
    offemail = fields.Char(string="Office Email")
    treatment = fields.Many2one('medical.pathology',string="Treatment for")
    duration_ailmenmts = fields.Char(string="Duration of Ailment")
    early_treatment = fields.Char(string="Early Treatments if any Furnish details")
    duration_treatment = fields.Char(string="Duration of Earlier Treatments taken")
    operations_details = fields.Char(string="Operation if any furnish details")
    name_father=fields.Char(string="Name")
    pin_code=fields.Char(string="Pin Code")
    # reg_type=fields.Selection([('dir',"Direct"),('on',"Online"),('app',"Appointment"),('rev',"Review"),('stop',"Stopped"),('cam','Camp')],string="Registration Type")
    patient_movement = fields.Datetime()
    treatment_for=fields.Many2one('medical.pathology',string="Treatment For")
    patient_signs_symptoms = fields.Many2many('medical.symptoms',string="Signs/Symptoms")
    related_field = fields.Char(string='Appointment ID')
    # company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company'].browse(self.env['res.company']._company_default_get('medical.prescription.order')))

    # company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company']
	# .browse(self.env['res.company']._company_default_get('medical.patient')))

    company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company']._company_default_get('medical.patient'))
    patient_waiting = fields.Char(string="Waiting Time",compute='waiting')
    patient_activity = fields.Selection([('wait',"Waiting"),('doctor',"Doctor Assigned"),('doc','Diet Assigned'),
                                         ('lab','Lab Bill Assigned'),('pres','Pharmacy Bill Assigned'),('scan','Scan Bill Assigned'),
                                         ('labs','Lab Test Completed'),('scans','Scan Test Completed'),
                                         ('bill',"Pharmacy Bill Assigned"),('discontinued','Discontinued'),('completed',"Completed")],default='wait',track_visibility='always')

    status_report = fields.Selection([('file','File'),('consult','Consultation'),('br','BR')])
    file_num = fields.Char(string='File ID')
    qr_code = fields.Binary("QR Code", attachment=True, compute='generate_qr_code')
    barcode = fields.Char("Barcode")
    review_type = fields.Selection([('direct','Direct'),('courier','Courier')], string='Review Type')
    reg_type=fields.Selection([('dir',"Direct"),('on',"Online")],string="Registration Type")
    online_type = fields.Selection([('app',"Appointment"),('rev',"Review"),('package','Package'),('stop',"Stopped"),('cam','Camp')], string='Online Type')
    direct_type = fields.Selection([('app',"Appointment"),('rev',"Review"),('package','Package'),('stop',"Stopped"),('cam','Camp')], string='Direct Type')


    abroad_addr = fields.Char(string='Abroad Address')

    appoint_times = fields.Many2one('many.times', string='Time')
    days_slot = fields.Many2one('day.slot', string='Day Slot')

    @api.constrains('patient_photo')
    def image_upload(self):
        partner_id = self.env['res.partner'].search([('name','=',self.patient_id.name)],limit=1)
        partner_id.write({
            'image_1920':self.patient_photo
        })
        ebook_id = self.env['medical.doctor'].search([('patient','=',self.patient_id.id)],limit=1)
        if ebook_id:
            ebook_id.write({
                'image1':self.patient_photo
            })

    @api.onchange('doctors','dates','appoint_times')
    def time_slot_master(self):
        val=[]
        for i in self:
            data_appointment = self.env['day.slot'].search([('doctor_name','=',i.doctors.id),('date_time','=',i.dates),('appointment_time_detail','=',i.appoint_times.id)])
            for m in data_appointment:
                val.append(m.id)
            return {'domain':{'days_slot':[('id','=',val)]}}


    @api.onchange('doctors','dates',)
    def function_onchange(self):
        lin = []
        for i in self:
            data = self.env['day.slot'].search([('doctor_name','=',i.doctors.id),('date_time','=',i.dates)])
            for j in data:
                if i.doctors.id and i.dates:
                    lin.append(j.appointment_time_detail.id)
        return {'domain':{'appoint_times':[('id','=',lin)]}}

    @api.onchange('appoint_times')
    def check_data(self):
        for rec in self:
            if rec.doctors and rec.dates:
                slots = self.env['medical.patient'].search([('doctors','=',rec.doctors.id),('dates','=',rec.dates),('appoint_times','=',rec.appoint_times.id)])
                if len(slots) >= 1:
                    raise ValidationError(" Already Appointment Fixed")
                else:
                    pass



    name_age_sex = fields.Char(string='Patient Name', compute='concatinate_name_age')
    def concatinate_name_age(self):
        if self.age:
            ages = self.age.split()[0]
        else:
            ages = 'Age'
        var = dict(self._fields['sex'].selection).get(self.sex)
        self.name_age_sex = '{} /{}/{}'.format(self.patient_id.name,ages,var)


    @api.onchange('whatsapp_check')
    def number_swaps(self):
        if self.whatsapp_check == True:
            self.contact_number = self.contact_no


    # @api.onchange('bp')
    def generate_qr_code(self):
        for rec in self:
            p_details={
                'Patient Id':rec.name,
                'Patient Name':rec.patient_id.name,
                'Doctor Name' :rec.doctors.name,
                'Date':rec.dates,
                'Registration Type':rec.reg_type

            }
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(p_details)
            qr.make(fit=True)
            img = qr.make_image()
            temp = BytesIO()
            img.save(temp, format="PNG")
            qr_image = base64.b64encode(temp.getvalue())
            self.qr_code = qr_image


    

    @api.depends('write_date')
    def waiting(self):
        for rec in self:
            orm_time=self.env['medical.doctor'].search([('patient','=',rec.patient_id.id)])
            consult_time = orm_time.wait_date
            if consult_time:
                time_waited = str(consult_time - rec.write_date)
                # raise ValidationError(f"{consult_time} {rec.write_date} {type(str(time_waited))}")
                time_data = time_waited.split(':')
                rec.patient_waiting = f"{time_data[0]}:{time_data[1]}"
            else:
                rec.patient_waiting = "00:00"

    write_date=fields.Datetime(string='Registration Time',default=datetime.now())


    # @api.onchange('dates','doctors')
    # def roll(self):
    #     date_today=self.dates
    #     today=datetime.now().date()
    #     if date_today != False:
    #         if date_today < today:
    #             raise ValidationError("Date should be greater than today's date")
    #     vals=self.env['medical.patient'].search_count([('dates','=',date_today),('doctors','=',self.doctors.id)])
    #     if vals >= 20:
    #         raise ValidationError("Appointment Slots are full")

    # @api.onchange('appointment_from')
    # def date_appointment(self):
    #     l1 = []

    #     all_slots = ['09:00 Am - 10:00 Am','10:00 Am - 11:00 Am','11:00 Am - 12:00 Pm',"12:00 Pm - 01:00 Pm","02:00 Pm - 03:00 Pm","03:00 Pm - 04:00 Pm","04:00 Pm - 05:00 Pm","05:00 Pm - 06:00 Pm","06:00 Pm - 07:00 Pm"]
    #     value=self.env['medical.patient'].search([('dates','=',self.dates),('doctors','=',self.doctors.id),('appointment_from','=',self.appointment_from)])
    #     if len(value) >= 3:
    #         empty=self.env['medical.patient'].search([('dates','=',self.dates),('doctors','=',self.doctors.id)])
    #         for i in empty:
    #             slots = i.appointment_from
    #             l1.append(slots)
    #             booked_slots = [i for i in all_slots if i not in l1]
    #             raise ValidationError("Please Select from Available Slots: {}".format(booked_slots))
    
    @api.onchange('height','weight')
    def _calculate_bmi(self):
        bmi = 0
        for rec in self:
            if rec.height and rec.weight:
                bmi = rec.weight/(rec.height/100)**2
            else:
                rec.bmi_value = 0.0
            if bmi <= 18.5:
                status = "Underweight"
            elif bmi >= 18.5 and bmi <= 25:
                status = "Normal"
            elif bmi==0.00:
                status=" "
            else:
                status = "Obesity"
            self.bmi_value = f"{bmi:.{2}f} {status}" 

    bmi_value= fields.Char(string="BMI")
    

    aboutinfor = fields.Selection([('newspaper','News Paper'),('radio','Radio'),
    ('ouremployee','Our Employee'),('friend','Friend / Referral'),('ref','Ref.Doctor'),('Adwall','Ad.Wall'),
    ('tv','Tv Program'),('magazine','Magazine'),('camp','Camp'),('youtube','Youtube'),('others','Others')],
    string='How you came to know about Daisy Health Care (p) Ltd.,?')
    signatures=fields.Char(string="Signature")
    data_value = fields.Many2many('medical.feedback', string="How you came to know about Daisy Hospital.")
    

    fix_appoinment=fields.One2many('fix.appointment','fix',string="Appoinment Slot")
    dates= fields.Date(string="Date")
    appointment_from=fields.Selection([('09:00 Am - 10:00 Am','09:00 Am - 10:00 Am'),('10:00 Am - 11:00 Am','10:00 Am - 11:00 Am'),('11:00 Am - 12:00 Pm',"11:00 Am - 12:00 Pm"),
    ('12:00 Pm - 01:00 Pm','12:00 Pm - 01:00 Pm'),('02:00 Pm - 03:00 Pm','02:00 Pm - 03:00 Pm'),('03:00 Pm - 04:00 Pm','03:00 Pm - 04:00 Pm'),('04:00 Pm - 05:00 Pm','04:00 Pm - 05:00 Pm'),
    ('05:00 Pm - 06:00 Pm','05:00 Pm - 06:00 Pm'),('06:00 Pm - 07:00 Pm','06:00 Pm - 07:00 Pm')],string='Appointment Slot')
    payment = fields.Float(string="Payments")


    

    @api.model
    def create(self,val):
        appointment = self._context.get('appointment_id')

        # patient_orm = self.env['res.partner'].search([('id','=',val['patient_id'])])
        # patient_orm.write({'is_patient':True,
        # # 'mobile':val.contact_no,
        # # 'gender':val.sex
        # })

        res_partner_obj = self.env['res.partner']

        if appointment:
            val_1 = {'name': self.env['res.partner'].browse(val['name']).name}
            patient= res_partner_obj.create(val_1)
            val.update({'name': patient.id,'image_1920':val.patient_photo,
            'roles_selection':'patient'})
            
        if val.get('date_of_birth'):
            dt = val.get('date_of_birth')
            d1 = datetime.strptime(str(dt), "%Y-%m-%d").date()
            d2 = datetime.today().date()
            rd = relativedelta(d2, d1)
            age = str(rd.years) + "y" +" "+ str(rd.months) + "m" +" "+ str(rd.days) + "d"
            val.update({'age':age} )

        patient_id  = self.env['ir.sequence'].next_by_code('medical.patient')
        if patient_id:
            val.update({
                        'name':patient_id,
                     
                       })
        result = super(medical_patient, self).create(val)

        orm = self.env['res.partner'].search([('name','=',result.patient_id.name)])
        # raise ValidationError(orm)
        orm.write({
            'roles_selection':'patient',
            'mobile':result.contact_no,
            'patient_gender':result.sex,
            'is_patient':True,
            'whatsapp':result.contact_number,
            'phone':result.contact_no,
            'experience':result.designation,
            'doctor_idxs':result.name,
            'dob_contact':result.date_of_birth,
            'street':result.address,
            'city':result.city.name,
            'state_id':result.state,
            'zip':result.pin_code,
            'country_id':result.country,
            'designation':result.occupation,
            'experience':result.designation,
            'marital_status':result.marital_status,
            'treatment_for':result.treatment_for,
            'abroad_addr':result.abroad_addr,
            'image_1920':result.patient_photo,

        })

        return result


        # appointment = self._context.get('appointment_id')
        # res_partner_obj = self.env['res.partner']
        # patient_orm = self.env['res.partner'].search([('id','=',val['patient_id'])])
        # patient_orm.write({'is_patient':True,})
        
        # if appointment:
        #     val_1 = {'name': self.env['res.partner'].browse(val['patient_id']).name}
        #     patient= res_partner_obj.create(val_1)
        #     val.update({'patient_id': patient.id})
        # if val.get('date_of_birth'):
        #     dt = val.get('date_of_birth')
        #     d1 = datetime.strptime(str(dt), "%Y-%m-%d").date()
        #     d2 = datetime.today().date()
        #     rd = relativedelta(d2, d1)
        #     age = str(rd.years) + "y" +" "+ str(rd.months) + "m" +" "+ str(rd.days) + "d"
        #     val.update({'age':age} )
        # else:
        #     pass

        # patient_ids  = self.env['ir.sequence'].next_by_code('medical.patient')
        # if patient_ids:
        #     val.update({
        #                 'name':patient_ids,
        #                })
        # result = super(medical_patient, self).create(val)
        # return result


    def payment_button(self):
        return {
    'name': "Register Payments",
    'domain':[('patient_id', '=', self.patient_id.id)],
    'view_mode': 'tree,form',
    'res_model': 'register.payment',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }


    def payment_count(self):
        for k in self:

            payment_count = self.env['register.payment'].search_count([('patient_id', '=', k.patient_id.id)])
            k.payment= payment_count
    payment = fields.Integer(string="Payments",compute='payment_count')

    def send_msg(self):
        return {'type': 'ir.actions.act_window',
                'name': 'Whatsapp Message',
                'res_model': 'whatsapp.wizard',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_user_id': self.patient_id.id,
                'default_mobile':self.contact_number,
                'default_message':"Hi "+self.patient_id.name+",\n\nYour Have registrated With  "+self.doctors.name+" on "+str(self.dates)+"\nFeedback : https://www.google.co.in/webhp?hl=en&sa=X&ved=0ahUKEwji0JG87J_4AhVVv2MGHcWkCuwQPAgI"+"\n\nThank You,\nDaisy Hospital",
                }}

#assign doc create e book

    def assign_button(self):
       
    	return {
            'type': 'ir.actions.act_window',
            'name': 'Register Payment',
            'res_model': 'register.wizard',
            'target': 'new',
            'view_mode': 'form',
            'view_type': 'form',
            'context': {       
                    'default_patient_id':self.patient_id.id ,
                    'default_age':self.age, 
                    'default_sex':self.sex,
                    'default_doctors':self.doctors.id,
                    'default_contact_no':self.contact_no,
                    'default_contact_number':self.contact_number,
                    'default_marital_status':self.marital_status,
                    'default_address':self.address,
                    'default_father_name':self.father_name,
                    'default_name_father':self.name_father,
                    'default_occupation':self.occupation,
                    'default_office_address':self.office_address,
                    'default_height':self.height,
                    'default_weight':self.weight,
                    'default_bmi_value':self.bmi_value,
                    'default_name':self.name,
                    'default_treatment':self.treatment.id,
                    'default_fees':self.fees,
                    'default_duration_ailments':self.duration_ailmenmts,
                    'default_doctor_changes':True,
                    'default_reg_type':self.reg_type,
                    'default_designation':self.designation,
                    'default_adoption_details':False,
                },}
 

#one2many new 

class FixAppointment(models.Model):
    _name = "fix.appointment"

    fix= fields.Many2one('medical.patient')
    date= fields.Datetime(string="Date")
    doctors_id = fields. Many2one('res.partner',domain=[('is_doctor','=',True)],string="Doctor")
    days=fields.Selection([('monday','MONDAY'),('tuesday','TUESDAY'),('wednesday','WEDNESDAY'),('thursday','THURSDAY'),('friday','FRIDAY'),('saturday','SATURDAY'),('sunday','SUNDAY')],string='Day')
    period = fields.Selection([('mor',"MORINING"),('eve',"EVENING")],string= "Session")
    appointment_from=fields.Selection([('s1',"9:30 Am - 10:30 Am"),('s2',"10:30 Am - 11:30 Am"),('s3',"11:30 Am - 12:30 Pm "),
    ('s4',"1:30 Pm - 2:30 Pm "),('s5',"2:30Pm - 3:30 Pm"),('s6',"3:30 Pm - 4:30 Pm "),('s7',"4:30 Pm - 5:30 pm"),('s8',"5:30 Pm - 6:30 Pm")],
    string='Appointment Slot')
