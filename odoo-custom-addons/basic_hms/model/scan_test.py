from odoo import models, fields, api
from datetime import datetime

class mri_test_study(models.Model):
    _name = 'mri.test.study'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char('1.5 MRI Study')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

class doppler_studies(models.Model):
    _name = 'doppler.studies'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char('Doppler Studies')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

class Robotic_clinical_studies(models.Model):
    _name = 'robotic.clinical.studies'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char('Fully Robotic Clinical Lab')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

class CT_studies(models.Model):
    _name = 'ct.studies'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char('CT Studies')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

class Other_studies(models.Model):
    _name = 'other.studies'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char('Other Studies')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

class CT_Angiogram(models.Model):
    _name = 'ct.angiogram'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char('CT Angiogram')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

class UltraSound_studies(models.Model):
    _name = 'ultra.sound.studies'

    patient_id = fields.Many2one('res.partner', string='Patient')    
    name = fields.Char('Ultrasound Study')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

class CT_Guided_Intervention(models.Model):
    _name = 'ct.guided.intervention'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char('CT Guided Intervention')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

class Scan_test(models.Model):
    _name = 'scan.test'
    _rec_name = 'request'

    name = fields.Char('Scan Test')
    patient_id = fields.Many2one('res.partner', string='Patient')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')
    request = fields.Char('ID Number', readonly = True)
    write_date=fields.Date(string='Date')
    ebook_id = fields.Char(srting='Patient ID')
    company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company']._company_default_get('medical.doctor'))

    mri_test = fields.Many2many('mri.test.study', string='MRI Test')
    doppler_test = fields.Many2many('doppler.studies', string='Doppler Test')
    robotic_clinical_test = fields.Many2many('robotic.clinical.studies', string='Robotic Clinical Test')
    ct_test = fields.Many2many('ct.studies', string='CT Test')
    other_test = fields.Many2many('other.studies', string='Other Test')
    ct_angiogram = fields.Many2many('ct.angiogram', string='CT Angiogram')
    ultra_sound_test = fields.Many2many('ultra.sound.studies', string='Ultrasound Test')
    ct_guided_intervention = fields.Many2many('ct.guided.intervention', string='CT Guided Intervention')
    patient_activity = fields.Selection([('wait',"Doctor Assigned"),('doc','Diet Assigned'),
                                         ('lab','Lab Assigned'),('pres','Prescription'),('scan','Scan Assigned'),
                                         ('labs','Lab Completed'),('scans','Scan Completed'),
                                         ('bill',"Pharmacy Bill Assigned"),('completed',"Completed")],default='wait')

    def document_button(self):
        self.patient_activity = 'scans'
        orm = self.env['medical.patient'].search([('patient_id','=',self.patient_id.id)])
        orm.write({'patient_activity':'scans'})
        orm1 = self.env['medical.doctor'].search([('patient','=',self.patient_id.id)])
        orm1.write({'patient_activity':'scans'})
        return{
            'name': "Document Upload",
            'domain':[('patient_id', '=', self.patient_id.id)],
            'view_mode': 'form',
            'res_model': 'document.type.line',
            'view_type': 'form',
            'type': 'ir.actions.act_window',
            'context': {
            'default_patient_id': self.patient_id.id
            },
            'target': 'new'
        }
    
    def scan_button(self):
            return {
    'name': "Scan Details",
    'domain':[('patient_id', '=', self.patient_id.id)],
    'view_mode': 'tree,form',
    'res_model': 'document.type.line',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }
#      Count in Smart Button
    def scan_count(self):
        for res in self :
            count_d = self.env['document.type.line'].search_count([('patient_id', '=', res.patient_id.id)])
            self.scan_recs= count_d

    scan_recs = fields.Integer(compute='scan_count',string="Scan Details")

    @api.model
    def create(self, vals):
        vals['request'] = self.env['ir.sequence'].next_by_code('scan.test') or 'SCAN'
        result = super(Scan_test, self).create(vals)
        
        orm = self.env['patient.bills'].search([('patient_name','=',result.patient_id.id)],order='id desc', limit=1)
        lines=[]
        
        for rec in result.mri_test:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))

        for rec in result.doppler_test:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))

        for rec in result.robotic_clinical_test:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))

        for rec in result.ct_test:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))

        for rec in result.other_test:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))

        for rec in result.ct_angiogram:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))

        for rec in result.ultra_sound_test:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))

        for rec in result.ct_guided_intervention:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        orm.write({'scan_bill':lines})

        scan_test = self.env['medical.doctor'].search([('patient','=',result.patient_id.id)])
        scan_lines=[]

        for rec in result.mri_test:
            values={
                'date':datetime.now(),
                'scan_id':result.id,
                'name':rec.name,
                }
            scan_lines.append((0,0,values))
        for rec in result.doppler_test:
            values={
                'date':datetime.now(),
                'scan_id':result.id,
                'name':rec.name,
                }
            scan_lines.append((0,0,values))

        for rec in result.robotic_clinical_test:
            values={
                'date':datetime.now(),
                'scan_id':result.id,
                'name':rec.name,
                }
            scan_lines.append((0,0,values))

        for rec in result.ct_test:
            values={
                'date':datetime.now(),
                'scan_id':result.id,
                'name':rec.name,
                }
            scan_lines.append((0,0,values))

        for rec in result.other_test:
            values={
                'date':datetime.now(),
                'scan_id':result.id,
                'name':rec.name,
                }
            scan_lines.append((0,0,values))

        for rec in result.ct_angiogram:
            values={
                'date':datetime.now(),
                'scan_id':result.id,
                'name':rec.name,
                }
            scan_lines.append((0,0,values))

        for rec in result.ultra_sound_test:
            values={
                'date':datetime.now(),
                'scan_id':result.id,
                'name':rec.name,
                }
            scan_lines.append((0,0,values))

        for rec in result.ct_guided_intervention:
            values={
                'date':datetime.now(),
                'scan_id':result.id,
                'name':rec.name,
                }
            scan_lines.append((0,0,values))

        scan_test.write({'scan_test':scan_lines})


        return result