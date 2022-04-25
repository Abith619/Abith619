# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_patient_evaluation(models.Model):
	_name = 'medical.patient.evaluation'
	_rec_name = 'medical_patient_id' 

	patient_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Patient")
	medical_patient_id = fields.Many2one('medical.patient',string="Patient",required=True)
	start_evaluation = fields.Datetime(string="Start Evaluation")
	physician_partner_id = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string="Doctor")
	end_evaluation = fields.Datetime(string="End of Evaluation")
	evaluation_type= fields.Selection([
			('a', 'Ambulatory'),
			('e', 'Emergency'),
			('i', 'Inpatient'),
			('pa', 'Pre-arranged appointment'),
			('pc', 'Periodic control'),
			('p', 'Phone call'),
			('t', 'Telemedicine'),
		], string='Type')
	chief_complaint = fields.Char('Chief Complaint')
	information_source = fields.Char('Source')
	reliable_info = fields.Boolean('Reliable')
	present_illness = fields.Text(string='Present Illness')
   
	weight = fields.Float(string='Weight (kg)',help='Weight in Kilos')
	height = fields.Float(string='Height (cm)')
	abdominal_circ = fields.Float(string='Abdominal Circumference')
	hip = fields.Float(string='Hip')
	bmi = fields.Float(string='Body Mass Index')
	whr = fields.Float(string='WHR')
	head_circumference = fields.Float(string='Head Circumference')
	malnutrition = fields.Boolean('Malnutrition')
	dehydration = fields.Boolean('Dehydration')
	tag = fields.Integer(
			string='Last TAGs',
			help='Triacylglycerol(triglicerides) level. Can be approximative'
		)
	is_tremor = fields.Boolean(
			string='Tremor',
			help='Check this box is the patient shows signs of tremors',
		)
	mood = fields.Selection([
			('n', 'Normal'),
			('s', 'Sad'),
			('f', 'Fear'),
			('r', 'Rage'),
			('h', 'Happy'),
			('d', 'Disgust'),
			('e', 'Euphoria'),
			('fl', 'Flat'),
		], string='Mood')
	glycemia = fields.Float(
			string='Glycemia',
			help='Last blood glucose level. Can be approximative.')
	evaluation_summary = fields.Text(string='Evaluation Summary')
	temperature = fields.Float(string='Temperature (celsius)',
									help='Temperature in celcius')
	osat = fields.Integer(string='Oxygen Saturation',
							   help='Oxygen Saturation(arterial).')
	bpm = fields.Integer(string='Heart Rate',
							  help='Heart rate expressed in beats per minute')
	loc_eyes = fields.Selection([
			('1', 'Does not Open Eyes'),
			('2', 'Opens eyes in response to painful stimuli'),
			('3', 'Opens eyes in response to voice'),
			('4', 'Opens eyes spontaneously'),
		], string='Glasgow - Eyes')
	loc_verbal = fields.Selection([
			('1', 'Make no sounds'),
			('2', 'Incomprehensible Sounds'),
			('3', 'Utters inappropriate words'),
			('4', 'Confused,disoriented'),
			('5', 'Oriented, converses normally'),
		], string='Glasgow - Verbal')
	loc_motor = fields.Selection([
			('1', 'Make no movement'),
			('2', 'Extension to painful stimuli decerebrate response'),
			('3', 'Abnormal flexion to painful stimuli decerebrate response'),
			('4', 'Flexion/Withdrawal to painful stimuli '),
			('5', 'Localizes painful stimuli'),
			('6', 'Obeys commands'),
		], string='Glasgow - Motor')
	violent = fields.Boolean('Violent Behaviour')
	orientation = fields.Boolean('Orientation')
	memory = fields.Boolean('Memory')
	knowledge_current_events = fields.Boolean('Knowledge of Current Events')
	judgment = fields.Boolean('Jugdment')
	symptom_proctorrhagia = fields.Boolean('Polyphagia')
	abstraction = fields.Boolean('Abstraction')
	vocabulary = fields.Boolean('Vocabulary')
	symptom_pain = fields.Boolean('Pain')
	symptom_pain_intensity = fields.Integer('Pain intensity')
	symptom_arthralgia = fields.Boolean('Arthralgia')
	symptom_abdominal_pain = fields.Boolean('Abdominal Pain')
	symptom_thoracic_pain = fields.Boolean('Thoracic Pain')
	symptom_pelvic_pain = fields.Boolean('Pelvic Pain')
	symptom_hoarseness = fields.Boolean('Hoarseness')
	symptom_sore_throat = fields.Boolean('Sore throat')
	symptom_ear_discharge = fields.Boolean('Ear Discharge')
	symptom_chest_pain_excercise = fields.Boolean('Chest Pain on excercise only')
	symptom_astenia = fields.Boolean('Astenia')
	symptom_weight_change = fields.Boolean('Sudden weight change')
	symptom_hemoptysis = fields.Boolean('Hemoptysis')
	symptom_epistaxis = fields.Boolean('Epistaxis')
	symptom_rinorrhea = fields.Boolean('Rinorrhea')
	symptom_vomiting = fields.Boolean('Vomiting')
	symptom_polydipsia = fields.Boolean('Polydipsia')
	symptom_polyuria = fields.Boolean('Polyuria')
	symptom_vesical_tenesmus = fields.Boolean('Vesical Tenesmus')
	symptom_dysuria = fields.Boolean('Dysuria')
	symptom_myalgia = fields.Boolean('Myalgia')
	symptom_cervical_pain = fields.Boolean('Cervical Pain')
	symptom_lumbar_pain = fields.Boolean('Lumbar Pain')
	symptom_headache = fields.Boolean('Headache')
	symptom_odynophagia = fields.Boolean('Odynophagia')
	symptom_otalgia = fields.Boolean('Otalgia')
	symptom_chest_pain = fields.Boolean('Chest Pain')
	symptom_orthostatic_hypotension = fields.Boolean('Orthostatic hypotension')
	symptom_anorexia = fields.Boolean('Anorexia')
	symptom_abdominal_distension = fields.Boolean('Abdominal Distension')
	symptom_hematemesis = fields.Boolean('Hematemesis')
	symptom_gingival_bleeding = fields.Boolean('Gingival Bleeding')
	symptom_nausea = fields.Boolean('Nausea')
	symptom_dysphagia = fields.Boolean('Dysphagia')
	symptom_polyphagia = fields.Boolean('Polyphagia')
	symptom_nocturia = fields.Boolean('Nocturia')
	symptom_pollakiuria = fields.Boolean('Pollakiuiria')
	symptom_mood_swings = fields.Boolean('Mood Swings')
	symptom_pruritus = fields.Boolean('Pruritus')
	symptom_disturb_sleep = fields.Boolean('Disturbed Sleep')
	symptom_orthopnea = fields.Boolean('Orthopnea')
	symptom_paresthesia = fields.Boolean('Paresthesia')
	symptom_dizziness = fields.Boolean('Dizziness')
	symptom_tinnitus = fields.Boolean('Tinnitus')
	symptom_eye_glasses = fields.Boolean('Eye glasses')
	symptom_diplopia = fields.Boolean('Diplopia')
	symptom_dysmenorrhea = fields.Boolean('Dysmenorrhea')
	symptom_metrorrhagia = fields.Boolean('Metrorrhagia')
	symptom_vaginal_discharge = fields.Boolean('Vaginal Discharge')
	symptom_diarrhea = fields.Boolean('Diarrhea')
	symptom_rectal_tenesmus = fields.Boolean('Rectal Tenesmus')
	symptom_sexual_dysfunction = fields.Boolean('Sexual Dysfunction')
	symptom_stress = fields.Boolean('Stressed-out')
	symptom_insomnia = fields.Boolean('Insomnia')
	symptom_dyspnea = fields.Boolean('Dyspnea')
	symptom_amnesia = fields.Boolean('Amnesia')
	symptom_paralysis = fields.Boolean('Paralysis')
	symptom_vertigo = fields.Boolean('Vertigo')
	symptom_syncope = fields.Boolean('Syncope')
	symptom_blurry_vision = fields.Boolean('Blurry vision')
	symptom_photophobia = fields.Boolean('Photophobia')
	symptom_amenorrhea = fields.Boolean('Amenorrhea')
	symptom_menorrhagia = fields.Boolean('Menorrhagia')
	symptom_urethral_discharge = fields.Boolean('Urethral Discharge')
	symptom_constipation = fields.Boolean('Constipation')
	symptom_melena = fields.Boolean('Melena')
	symptom_xerostomia = fields.Boolean('Xerostomia')
	calculation_ability = fields.Boolean('Calculation Ability')
	object_recognition = fields.Boolean('Object Recognition')
	praxis = fields.Boolean('Praxis')
	edema = fields.Boolean('Edema')
	petechiae = fields.Boolean('Petechiae')
	acropachy = fields.Boolean('Acropachy')
	miosis = fields.Boolean('Miosis')
	cough = fields.Boolean('Cough')
	arritmia = fields.Boolean('Arritmias')
	heart_extra_sounds = fields.Boolean('Heart Extra Sounds')
	ascites = fields.Boolean('Ascites')
	bronchophony = fields.Boolean('Bronchophony')
	cyanosis = fields.Boolean('Cyanosis')
	hematoma = fields.Boolean('Hematomas')
	nystagmus = fields.Boolean('Nystagmus')
	mydriasis = fields.Boolean('Mydriasis')
	palpebral_ptosis = fields.Boolean('Palpebral Ptosis')
	heart_murmurs = fields.Boolean('Heart Murmurs')
	jugular_engorgement = fields.Boolean('Tremor')
	lung_adventitious_sounds = fields.Boolean('Lung Adventitious sounds')
	increased_fremitus = fields.Boolean('Increased Fremitus')
	jaundice = fields.Boolean('Jaundice')
	breast_lump = fields.Boolean('Breast Lumps')
	nipple_inversion = fields.Boolean('Nipple Inversion')
	peau_dorange = fields.Boolean('Peau d orange')
	hypotonia = fields.Boolean('Hypotonia')
	masses = fields.Boolean('Masses')
	goiter = fields.Boolean('Goiter')
	xerosis = fields.Boolean('Xerosis')
	decreased_fremitus = fields.Boolean('Decreased Fremitus')
	lynphadenitis = fields.Boolean('Linphadenitis')
	breast_asymmetry = fields.Boolean('Breast Asymmetry')
	nipple_discharge = fields.Boolean('Nipple Discharge')
	gynecomastia = fields.Boolean('Gynecomastia')
	hypertonia = fields.Boolean('Hypertonia')
	pressure_ulcers = fields.Boolean('Pressure Ulcers')
	alopecia = fields.Boolean('Alopecia')
	erithema = fields.Boolean('Erithema')
	diagnosis_id = fields.Many2one('medical.pathology','Presumptive Diagnosis')
	ldl = fields.Integer(
			string='Last LDL',
			help='Last LDL Cholesterol reading. Can be approximative'
		)
	visit_type  = fields.Selection([('new','New Health Condition'),('follow','FollowUp'),('chronic','Chronic Condition ChechUp'),('child','Well Child Visit'),('women','Well Woman Visit'),('man','Well Man Visit')],string="Visit")
	urgency  = fields.Selection([('a', 'Normal'), ('b', 'Urgent'), ('c', 'Medical Emergency')],string='Urgency')
	systolic = fields.Integer('Systolic Pressure')
	diastolic = fields.Integer('Diastolic Pressure')
	respiratory_rate = fields.Integer('Respiratory Rate')
	signs_and_symptoms_ids = fields.One2many('medical.signs.and.sympotoms','patient_evaluation_id','Signs and Symptoms')
	hba1c = fields.Float('Glycated Hemoglobin')
	cholesterol_total = fields.Integer('Last Cholesterol')
	hdl = fields.Integer('Last HDL')
	ldl = fields.Integer('Last LDL')
	tags = fields.Integer('Last TAGs')
	loc = fields.Integer('Level of Consciousness')
	info_diagnosis = fields.Text(string='Information on Diagnosis')
	directions = fields.Text(string='Treatment Plan')
	user_id = fields.Many2one('res.users','Doctor user ID',readonly=True)
	medical_appointment_date_id = fields.Many2one('medical.appointment','Appointment Date')
	next_appointment_id = fields.Many2one('medical.appointment','Next Appointment')
	derived_from_physician_id = fields.Many2one('medical.physician','Derived from Doctor')
	derived_to_physician_id = fields.Many2one('medical.physician','Derived to Doctor')
	secondary_conditions_ids = fields.One2many('medical.secondary_condition','patient_evaluation_id','Secondary Conditions')
	diagnostic_hypothesis_ids = fields.One2many('medical.diagnostic_hypotesis','patient_evaluation_id','Procedures')
	procedure_ids = fields.One2many('medical.directions','patient_evaluation_id','Procedures')


