from odoo import models, fields, api

class mri_test_study(models.Model):
    _name = 'mri.test.study'

    name = fields.Char('1.5 MRI Study')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

class doppler_studies(models.Model):
    _name = 'doppler.studies'

    name = fields.Char('Doppler Studies')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

class Robotic_clinical_studies(models.Model):
    _name = 'robotic.clinical.studies'

    name = fields.Char('Fully Robotic Clinical Lab')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

class CT_studies(models.Model):
    _name = 'ct.studies'

    name = fields.Char('CT Studies')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

class Other_studies(models.Model):
    _name = 'other.studies'

    name = fields.Char('Other Studies')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

class CT_Angiogram(models.Model):
    _name = 'ct.angiogram'

    name = fields.Char('CT Angiogram')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

class UltraSound_studies(models.Model):
    _name = 'ultra.sound.studies'

    name = fields.Char('Ultrasound Study')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

class CT_Guided_Intervention(models.Model):
    _name = 'ct.guided.intervention'

    name = fields.Char('CT Guided Intervention')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

class Scan_test(models.Model):
    _name = 'scan.test'

    name = fields.Char('Scan Test')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

    mri_test = fields.Many2many('mri.test.study', string='MRI Test')
    doppler_test = fields.Many2many('doppler.studies', string='Doppler Test')
    robotic_clinical_test = fields.Many2many('robotic.clinical.studies', string='Robotic Clinical Test')
    ct_test = fields.Many2many('ct.studies', string='CT Test')
    other_test = fields.Many2many('other.studies', string='Other Test')
    ct_angiogram = fields.Many2many('ct.angiogram', string='CT Angiogram')
    ultra_sound_test = fields.Many2many('ultra.sound.studies', string='Ultrasound Test')
    ct_guided_intervention = fields.Many2many('ct.guided.intervention', string='CT Guided Intervention')
    