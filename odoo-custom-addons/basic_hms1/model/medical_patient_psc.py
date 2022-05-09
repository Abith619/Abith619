# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
# classes under  menu of laboratry 

class medical_patient_psc(models.Model):
    _name = 'medical.patient.psc'
    _rec_name = 'patient_id'

    @api.model
    def default_get(self,fields):
        result = super(medical_patient_psc, self).default_get(fields)
        
        result.update({
                        'user_id':self._uid,
                       })
        return result

    appointment_id = fields.Many2one('medical.appointment',"Appointment")
    patient_id = fields.Many2one('medical.patient','Patient', required = True) 
    evaluation_start = fields.Datetime('Date ', required = True, default=fields.Datetime.now)
    psc_total = fields.Integer('PCS Total')
    user_id = fields.Many2one('res.users','Healh Professional', default=lambda self: self.env.user)
    notes = fields.Text('Notes')
    #selection field 
    psc_aches_pains = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Complains of aches and pains')
    psc_absent_from_school = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Absent from school')
    psc_act_as_younger = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Acts younger than children his or her age')
    psc_acts_as_driven_by_motor = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Acts as if driven by a motor')
    psc_afraid_of_new_situations = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Is afraid of new situations')
    psc_blames_others = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Blames others for his or her troubles')
    psc_daydreams_too_much = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Daydreams too much')
    psc_distracted_easily = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Distracted easily')
    psc_does_not_get_people_feelings = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Does not get people feelings')
    psc_does_not_listen_to_rules = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Does not listen to rules')
    psc_does_not_show_feelings = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Does not show feelings')
    psc_down_on_self = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Is down on him or herself')
    psc_feels_hopeless = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Feels hopeless')
    psc_feels_is_bad_child = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Feels he or she is bad')
    psc_fidgety =fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Fidgety, unable to sit still')
    psc_fights_with_others = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Fights with other children')
    psc_gets_hurt_2 = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Gets hurt frequently')
    psc_having_less_fun = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Seems to be having less fun')
    psc_irritable_angry = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Is irritable, angry')
    psc_less_interested_in_friends = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Less interested in friends')
    psc_less_interest_in_school = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Less interested in school')
    psc_refuses_to_share = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Refuses to share')
    psc_sad_unhappy = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Feels sad, unhappy')
    psc_school_grades_dropping = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'School grades dropping')
    psc_spend_time_alone = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Spends more time alone')
    psc_takes_things_from_others = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Takes things that do not belong to him or her')
    psc_takes_unnecesary_risks = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Takes unnecessary risks')
    psc_teases_others = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Teases others')
    psc_tires_easily = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Tires easily, has little energy')
    psc_trouble_concentrating = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Has trouble concentrating')
    psc_trouble_sleeping = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Has trouble sleeping')
    psc_trouble_with_teacher = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Has trouble with teacher')
    psc_gets_hurt_often = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Gets hurt often')
    psc_visit_doctor_finds_ok = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Visits the doctor with doctor finding nothing wrong')
    psc_wants_to_be_with_parents = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Wants to be with you more than before')
    psc_worries_a_lot = fields.Selection([('0', 'Never'),('1', 'Sometimes'),('2', 'Often')], 'Worries a lot')
    
    @api.onchange('psc_aches_pains', 
                  'psc_absent_from_school',
                   'psc_act_as_younger', 'psc_acts_as_driven_by_motor',
                    'psc_afraid_of_new_situations', 
                    'psc_blames_others','psc_teases_others',
                     'psc_daydreams_too_much', 'psc_tires_easily',
                     'psc_distracted_easily','psc_trouble_concentrating',
                     'psc_trouble_sleeping','psc_trouble_with_teacher',
                     'psc_visit_doctor_finds_ok', 'psc_wants_to_be_with_parents',
                     'psc_worries_a_lot',
                      'psc_does_not_get_people_feelings', 'psc_does_not_listen_to_rules', 
                      'psc_does_not_show_feelings', 'psc_down_on_self',
                       'psc_feels_hopeless','psc_feels_is_bad_child',
                       'psc_fidgety','psc_fights_with_others', 
                       'psc_gets_hurt_often', 'psc_having_less_fun', 'psc_irritable_angry', 
                      'psc_less_interested_in_friends', 'psc_less_interest_in_school',
                       'psc_refuses_to_share', 'psc_sad_unhappy', 
                       'psc_school_grades_dropping', 'psc_spend_time_alone', 
                       'psc_takes_things_from_others', 'psc_takes_unnecesary_risks', )
    def onchange_selections(self):
        self.psc_total = int(self.psc_aches_pains)+int(self.psc_absent_from_school) + int(self.psc_act_as_younger) +int(self.psc_acts_as_driven_by_motor)  + int(self.psc_afraid_of_new_situations) +int(self.psc_blames_others) + int(self.psc_teases_others) + int(self.psc_daydreams_too_much)+int(self.psc_tires_easily)+ int(self.psc_distracted_easily)+ int(self.psc_trouble_concentrating)+ int(self.psc_trouble_sleeping)+ int(self.psc_trouble_with_teacher)+ int(self.psc_visit_doctor_finds_ok)++int(self.psc_wants_to_be_with_parents) + int(self.psc_worries_a_lot)+ int(self.psc_does_not_get_people_feelings)+int(self.psc_down_on_self)+ int(self.psc_feels_hopeless)+ int(self.psc_feels_is_bad_child)+int(self.psc_fidgety)+ int(self.psc_fights_with_others)+ int(self.psc_gets_hurt_often)+ int(self.psc_having_less_fun)+ int(self.psc_irritable_angry) + int(self.psc_less_interested_in_friends)+int(self.psc_less_interest_in_school)+ int(self.psc_refuses_to_share)+ int(self.psc_sad_unhappy) +int(self.psc_school_grades_dropping) + int(self.psc_spend_time_alone) + int(self.psc_takes_things_from_others)+int(self.psc_takes_unnecesary_risks)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:    








