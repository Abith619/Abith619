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
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Scan Test')
    patient_id = fields.Many2one('res.partner', string='Patient')
    ip_name = fields.Many2one('in.patient',string='Name')
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

    patient_activity = fields.Selection([('wait',"Waiting"),('doctor',"Doctor Assigned"),('doc','Diet Assigned'),
                                         ('lab','Lab Bill Assigned'),('pres','Pharmacy Bill Assigned'),('scan','Scan Bill Assigned'),
                                         ('labs','Lab Test Completed'),('scans','Scan Test Completed'),
                                         ('bill',"Pharmacy Bill Assigned"),('discontinued','Discontinued'),('completed',"Completed")],default='wait',track_visibility='onchange')
    num_days = fields.Selection([('e','ebook'),('1','Day1'),('2','Day2'),('3','Day3'),('4','Day4'),('5','Day5'),
                                ('6','Day6'),('7','Day7'),('8','Day8'),('9','Day9'),('10','Day10')])
    doctor_id = fields.Many2one('res.partner', string='Doctor Name',domain=[('is_doctor','=',True)])

    select_mri = fields.Boolean(string='M.R.I STUDY')
    select_doppler = fields.Boolean(string='DOPPLER STUDIES')
    select_other = fields.Boolean(string='OTHER STUDIES')
    select_angio = fields.Boolean(string='C.T ANGIOGRAM')
    select_us = fields.Boolean(string='ULTRASOUND STUDY')
    select_robotic = fields.Boolean(string='FULLY ROBITIC CLINICAL LAB')
    select_ct_study = fields.Boolean(string='C.T STUDY')
    select_ct_intervention = fields.Boolean(string='C.T GUIDED INTERVENTION')

    
    @api.constrains('patient_id')
    def write_lab(self):
        orm_e = self.env['medical.doctor'].search([('patient','=',self.patient_id.id)])
        orm_e.write({'patient_activity' : 'scan'})
        
        orm_count = self.env['patient.bills'].search_count([('patient_name','=',self.patient_id.id)])
        if orm_count > 1:
            scan_assign = self.env['patient.bills'].search([('patient_name','=',self.patient_id.id)])[-1]
            scan_assign.write({'patient_activity' : 'scan',
            'scan_date':datetime.now(),})
        else:
            scan_assign = self.env['patient.bills'].search([('patient_name','=',self.patient_id.id)])
            scan_assign.write({'patient_activity' : 'scan',
            'scan_date':datetime.now()})
        orm = self.env['medical.patient'].search([('patient_id','=',self.patient_id.id)])
        orm.write({'patient_activity' : 'scan'})
        
        orm = self.env['res.partner'].search([('name','=',self.patient_id.name)])
        orm.update({
            'patient_activity':'scan',
        })
        self.patient_activity = 'scan'
    
    def document_button(self):
        # self.patient_activity = 'scans'
        
        return{
            'name': "Document Upload",
            'domain':[('name', '=', self.patient_id.name)],
            'view_mode': 'form',
            'res_model': 'document.type.line',
            'view_type': 'form',
            'type': 'ir.actions.act_window',
            'context': {
            'default_name': self.patient_id.name,
            'default_attach_types':'scan',
                },
            'target': 'new'
        }
    
    def scan_button(self):
            return {
    'name': "Scan Details",
    'domain':[('name', '=', self.patient_id.name),('attach_types','=','scan')],
    'view_mode': 'tree,form',
    'res_model': 'document.type.line',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }
#      Count in Smart Button
    def scan_count(self):
        for res in self :
            count_d = self.env['document.type.line'].search_count([('name', '=', res.patient_id.name),('attach_types','=','scan')])
            self.scan_recs= count_d

    scan_recs = fields.Integer(compute='scan_count',string="Scan Details")

    @api.model
    def create(self, vals):
        vals['request'] = self.env['ir.sequence'].next_by_code('scan.test') or 'SCAN'
        result = super(Scan_test, self).create(vals)

        mri_test = self.env['mri.test.study'].search([])
        doppler_test = self.env['doppler.studies'].search([])
        other_test = self.env['other.studies'].search([])
        ct_angiogram = self.env['ct.angiogram'].search([])
        ultra_sound_test = self.env['ultra.sound.studies'].search([])
        robotic_clinical_test = self.env['robotic.clinical.studies'].search([])
        ct_test = self.env['ct.studies'].search([])
        ct_guided_intervention = self.env['ct.guided.intervention'].search([])

        if result.num_days == 'e':
            orm = self.env['patient.bills'].search([('patient_name','=',result.patient_id.id)],order='id desc', limit=1)
            scan = self.env['scan.menu']
            scan_test = self.env['medical.doctor'].search([('patient','=',result.patient_id.id)])
            lines=[]
            scan_lines = []
            if result.select_mri == True:
                for i in mri_test:
                    valuez={
                        'name': i.name,
                        'date':datetime.now(),
                        'bill_amount': i.price
                    }
                    lines.append((0, 0, valuez))
                    values={
                        'patient_id':result.patient_id.id,
                        'ebook_id':result.ebook_id,
                        'test_name':i.name
                    }
                    scan.create(values)
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':i.name,
                    }
                    scan_lines.append((0,0,valuee))
            else:
                for rec in result.mri_test:
                    valuez={
                        'name': rec.name,
                        'date':datetime.now(),
                        'bill_amount': rec.price
                    }
                    lines.append((0, 0, valuez))
                    values={
                        'patient_id':result.patient_id.id,
                        'ebook_id':result.ebook_id,
                        'test_name':rec.name
                    }
                    scan.create(values)
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_lines.append((0,0,valuee))
            if result.select_doppler == True:
                for i in doppler_test:
                    valuez={
                        'name': i.name,
                        'date':datetime.now(),
                        'bill_amount': i.price
                        }
                    lines.append((0, 0, valuez))
                    values={
                        'patient_id':result.patient_id.id,
                        'ebook_id':result.ebook_id,
                        'test_name':i.name
                    }
                    scan.create(values)
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':i.name,
                    }
                    scan_lines.append((0,0,valuee))
            else:
                for rec in result.doppler_test:
                    valuez={
                        'name': rec.name,
                        'date':datetime.now(),
                        'bill_amount': rec.price
                    }
                    lines.append((0, 0, valuez))
                    values={
                        'patient_id':result.patient_id.id,
                        'ebook_id':result.ebook_id,
                        'test_name':rec.name
                    }
                    scan.create(values)
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_lines.append((0,0,valuee))
            if result.select_robotic == True:
                for i in robotic_clinical_test:
                    valuez={
                        'name': i.name,
                        'date':datetime.now(),
                        'bill_amount': i.price
                    }
                    lines.append((0, 0, valuez))
                    values={
                        'patient_id':result.patient_id.id,
                        'ebook_id':result.ebook_id,
                        'test_name':i.name
                    }
                    scan.create(values)
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':i.name,
                    }
                    scan_lines.append((0,0,valuee))
            else:
                for rec in result.robotic_clinical_test:
                    valuez={
                        'name': rec.name,
                        'date':datetime.now(),
                        'bill_amount': rec.price
                    }
                    lines.append((0, 0, valuez))
                    values={
                        'patient_id':result.patient_id.id,
                        'ebook_id':result.ebook_id,
                        'test_name':rec.name
                    }
                    scan.create(values)
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_lines.append((0,0,valuee))
            if result.select_ct_study == True:
                for i in ct_test:
                    valuez={
                        'name': i.name,
                        'date':datetime.now(),
                        'bill_amount': i.price
                    }
                    lines.append((0, 0, valuez))
                    values={
                        'patient_id':result.patient_id.id,
                        'ebook_id':result.ebook_id,
                        'test_name':i.name
                    }
                    scan.create(values)
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':i.name,
                    }
                    scan_lines.append((0,0,valuee))
            else:
                for rec in result.ct_test:
                    valuez={
                        'name': rec.name,
                        'date':datetime.now(),
                        'bill_amount': rec.price
                    }
                    lines.append((0, 0, valuez))
                    values={
                        'patient_id':result.patient_id.id,
                        'ebook_id':result.ebook_id,
                        'test_name':rec.name
                    }
                    scan.create(values)
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_lines.append((0,0,valuee))
            if result.select_other == True:
                for i in other_test:
                    valuez={
                        'name': i.name,
                        'date':datetime.now(),
                        'bill_amount': i.price
                    }
                    lines.append((0, 0, valuez))
                    values={
                        'patient_id':result.patient_id.id,
                        'ebook_id':result.ebook_id,
                        'test_name':i.name
                    }
                    scan.create(values)
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':i.name,
                    }
                    scan_lines.append((0,0,valuee))
            else:
                for rec in result.other_test:
                    valuez={
                        'name': rec.name,
                        'date':datetime.now(),
                        'bill_amount': rec.price
                    }
                    lines.append((0, 0, valuez))
                    values={
                        'patient_id':result.patient_id.id,
                        'ebook_id':result.ebook_id,
                        'test_name':rec.name
                    }
                    scan.create(values)
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_lines.append((0,0,valuee))
            if result.select_angio == True:
                for i in ct_angiogram:
                    valuez={
                        'name': i.name,
                        'date':datetime.now(),
                        'bill_amount': i.price
                    }
                    lines.append((0, 0, valuez))
                    values={
                        'patient_id':result.patient_id.id,
                        'ebook_id':result.ebook_id,
                        'test_name':i.name
                    }
                    scan.create(values)
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':i.name,
                    }
                    scan_lines.append((0,0,valuee))
            else:
                for rec in result.ct_angiogram:
                    valuez={
                        'name': rec.name,
                        'date':datetime.now(),
                        'bill_amount': rec.price
                    }
                    lines.append((0, 0, valuez))
                    values={
                        'patient_id':result.patient_id.id,
                        'ebook_id':result.ebook_id,
                        'test_name':rec.name
                    }
                    scan.create(values)
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_lines.append((0,0,valuee))
            if result.select_us == True:
                for i in ultra_sound_test:
                    valuez={
                        'name': i.name,
                        'date':datetime.now(),
                        'bill_amount': i.price
                    }
                    lines.append((0, 0, valuez))
                    values={
                        'patient_id':result.patient_id.id,
                        'ebook_id':result.ebook_id,
                        'test_name':i.name
                    }
                    scan.create(values)
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':i.name,
                    }
                    scan_lines.append((0,0,valuee))
            else:
                for rec in result.ultra_sound_test:
                    valuez={
                        'name': rec.name,
                        'date':datetime.now(),
                        'bill_amount': rec.price
                    }
                    lines.append((0, 0, valuez))
                    values={
                        'patient_id':result.patient_id.id,
                        'ebook_id':result.ebook_id,
                        'test_name':rec.name
                    }
                    scan.create(values)
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_lines.append((0,0,valuee))
            if result.select_ct_study == True:
                for i in ct_guided_intervention:
                    valuez={
                        'name': i.name,
                        'date':datetime.now(),
                        'bill_amount': i.price
                    }
                    lines.append((0, 0, valuez))
                    values={
                        'patient_id':result.patient_id.id,
                        'ebook_id':result.ebook_id,
                        'test_name':i.name
                    }
                    scan.create(values)
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':i.name,
                    }
                    scan_lines.append((0,0,valuee))
            else:
                for rec in result.ct_guided_intervention:
                    valuez={
                        'name': rec.name,
                        'date':datetime.now(),
                        'bill_amount': rec.price
                    }
                    lines.append((0, 0, valuez))
                    values={
                        'patient_id':result.patient_id.id,
                        'ebook_id':result.ebook_id,
                        'test_name':rec.name
                    }
                    scan.create(values)
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_lines.append((0,0,valuee))
            orm.write({'scan_bill':lines,
            'scan_date':datetime.now()})
            scan_test.write({'scan_test':scan_lines})
        
        if result.num_days == '1':
            orm = self.env['patient.bills'].search([('patient_name','=',result.patient_id.id)],order='id desc', limit=1)
            scan = self.env['in.patient'].search([('patient_id','=',result.patient_id.id)])
            scan_test = self.env['medical.doctor'].search([('patient','=',result.patient_id.id)])
            scan_menu = self.env['scan.menu']
            scan_lines=[]
            lines=[]
            scan_doc=[]
            if result.select_mri == True:
                for rec in mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_doppler == True:
                for rec in doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_robotic == True:
                for rec in robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_study == True:
                for rec in ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_other == True:
                for rec in other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_angio == True:
                for rec in ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_us == True:
                for rec in ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_intervention == True:
                for rec in ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            
            scan.write({'scan_line':scan_lines})
            orm.write({'inpatient_scan':lines})
            scan_test.write({'scan_test':scan_doc})
            
        elif result.num_days == '2':
            orm = self.env['patient.bills'].search([('patient_name','=',result.patient_id.id)],order='id desc', limit=1)
            scan = self.env['in.patient'].search([('patient_id','=',result.patient_id.id)])
            scan_test = self.env['medical.doctor'].search([('patient','=',result.patient_id.id)])
            scan_lines=[]
            lines=[]
            scan_doc=[]
            if result.select_mri == True:
                for rec in mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_doppler == True:
                for rec in doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_robotic == True:
                for rec in robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_study == True:
                for rec in ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_other == True:
                for rec in other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_angio == True:
                for rec in ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_us == True:
                for rec in ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_intervention == True:
                for rec in ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            
            scan.write({'scan_line_two':scan_lines})
            orm.write({'inpatient_scan':lines})
            scan_test.write({'scan_test':scan_doc})
            
        elif result.num_days == '3':
            orm = self.env['patient.bills'].search([('patient_name','=',result.patient_id.id)],order='id desc', limit=1)
            scan = self.env['in.patient'].search([('patient_id','=',result.patient_id.id)])
            scan_test = self.env['medical.doctor'].search([('patient','=',result.patient_id.id)])
            scan_lines=[]
            lines=[]
            scan_doc=[]
            if result.select_mri == True:
                for rec in mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_doppler == True:
                for rec in doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_robotic == True:
                for rec in robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_study == True:
                for rec in ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_other == True:
                for rec in other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_angio == True:
                for rec in ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_us == True:
                for rec in ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_intervention == True:
                for rec in ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            
            scan.write({'scan_line_three':scan_lines})
            orm.write({'inpatient_scan':lines})
            scan_test.write({'scan_test':scan_doc})
            
        elif result.num_days == '4':
            orm = self.env['patient.bills'].search([('patient_name','=',result.patient_id.id)],order='id desc', limit=1)
            scan = self.env['in.patient'].search([('patient_id','=',result.patient_id.id)])
            scan_test = self.env['medical.doctor'].search([('patient','=',result.patient_id.id)])
            scan_lines=[]
            lines=[]
            scan_doc=[]
            if result.select_mri == True:
                for rec in mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_doppler == True:
                for rec in doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_robotic == True:
                for rec in robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_study == True:
                for rec in ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_other == True:
                for rec in other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_angio == True:
                for rec in ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_us == True:
                for rec in ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_intervention == True:
                for rec in ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            
            scan.write({'scan_line_four':scan_lines})
            orm.write({'inpatient_scan':lines})
            scan_test.write({'scan_test':scan_doc})
            
        elif result.num_days == '5':
            orm = self.env['patient.bills'].search([('patient_name','=',result.patient_id.id)],order='id desc', limit=1)
            scan = self.env['in.patient'].search([('patient_id','=',result.patient_id.id)])
            scan_test = self.env['medical.doctor'].search([('patient','=',result.patient_id.id)])
            scan_lines=[]
            lines=[]
            scan_doc=[]
            if result.select_mri == True:
                for rec in mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_doppler == True:
                for rec in doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_robotic == True:
                for rec in robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_study == True:
                for rec in ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_other == True:
                for rec in other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_angio == True:
                for rec in ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_us == True:
                for rec in ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_intervention == True:
                for rec in ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            
            scan.write({'scan_line_five':scan_lines})
            orm.write({'inpatient_scan':lines})
            scan_test.write({'scan_test':scan_doc})
            
        elif result.num_days == '6':
            orm = self.env['patient.bills'].search([('patient_name','=',result.patient_id.id)],order='id desc', limit=1)
            scan = self.env['in.patient'].search([('patient_id','=',result.patient_id.id)])
            scan_test = self.env['medical.doctor'].search([('patient','=',result.patient_id.id)])
            scan_lines=[]
            lines=[]
            scan_doc=[]
            if result.select_mri == True:
                for rec in mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_doppler == True:
                for rec in doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_robotic == True:
                for rec in robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_study == True:
                for rec in ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_other == True:
                for rec in other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_angio == True:
                for rec in ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_us == True:
                for rec in ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_intervention == True:
                for rec in ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            
            scan.write({'scan_line_six':scan_lines})
            orm.write({'inpatient_scan':lines})
            scan_test.write({'scan_test':scan_doc})
            
        elif result.num_days == '7':
            orm = self.env['patient.bills'].search([('patient_name','=',result.patient_id.id)],order='id desc', limit=1)
            scan = self.env['in.patient'].search([('patient_id','=',result.patient_id.id)])
            scan_test = self.env['medical.doctor'].search([('patient','=',result.patient_id.id)])
            scan_lines=[]
            lines=[]
            scan_doc=[]
            if result.select_mri == True:
                for rec in mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_doppler == True:
                for rec in doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_robotic == True:
                for rec in robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_study == True:
                for rec in ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_other == True:
                for rec in other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_angio == True:
                for rec in ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_us == True:
                for rec in ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_intervention == True:
                for rec in ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            
            scan.write({'scan_line_seven':scan_lines})
            orm.write({'inpatient_scan':lines})
            scan_test.write({'scan_test':scan_doc})
            
        elif result.num_days == '8':
            orm = self.env['patient.bills'].search([('patient_name','=',result.patient_id.id)],order='id desc', limit=1)
            scan = self.env['in.patient'].search([('patient_id','=',result.patient_id.id)])
            scan_test = self.env['medical.doctor'].search([('patient','=',result.patient_id.id)])
            scan_lines=[]
            lines=[]
            scan_doc=[]
            if result.select_mri == True:
                for rec in mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_doppler == True:
                for rec in doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_robotic == True:
                for rec in robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_study == True:
                for rec in ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_other == True:
                for rec in other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_angio == True:
                for rec in ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_us == True:
                for rec in ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_intervention == True:
                for rec in ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            
            scan.write({'scan_line_eight':scan_lines})
            orm.write({'inpatient_scan':lines})
            scan_test.write({'scan_test':scan_doc})
            
        elif result.num_days == '9':
            orm = self.env['patient.bills'].search([('patient_name','=',result.patient_id.id)],order='id desc', limit=1)
            scan = self.env['in.patient'].search([('patient_id','=',result.patient_id.id)])
            scan_test = self.env['medical.doctor'].search([('patient','=',result.patient_id.id)])
            scan_lines=[]
            lines=[]
            scan_doc=[]
            if result.select_mri == True:
                for rec in mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_doppler == True:
                for rec in doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_robotic == True:
                for rec in robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_study == True:
                for rec in ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_other == True:
                for rec in other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_angio == True:
                for rec in ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_us == True:
                for rec in ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_intervention == True:
                for rec in ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            
            scan.write({'scan_line_nine':scan_lines})
            orm.write({'inpatient_scan':lines})
            scan_test.write({'scan_test':scan_doc})
            
        elif result.num_days == '10':
            orm = self.env['patient.bills'].search([('patient_name','=',result.patient_id.id)],order='id desc', limit=1)
            scan = self.env['in.patient'].search([('patient_id','=',result.patient_id.id)])
            scan_test = self.env['medical.doctor'].search([('patient','=',result.patient_id.id)])
            scan_lines=[]
            lines=[]
            scan_doc=[]
            if result.select_mri == True:
                for rec in mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.mri_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_doppler == True:
                for rec in doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.doppler_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_robotic == True:
                for rec in robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.robotic_clinical_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_study == True:
                for rec in ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_other == True:
                for rec in other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.other_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_angio == True:
                for rec in ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_angiogram:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_us == True:
                for rec in ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ultra_sound_test:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            if result.select_ct_intervention == True:
                for rec in ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            else:
                for rec in result.ct_guided_intervention:
                    valuee={
                    'date':datetime.now(),
                    'scan_id':result.id,
                    'name':rec.name,
                    }
                    scan_doc.append((0,0,valuee))
                    values={
                        'date':datetime.now(),
                        'scan_id':result.id,
                        'name':rec.name,
                        'range_normal':rec.range,
                        }
                    valuez={
                    'name': rec.name,
                    'date':datetime.now(),
                    'bill_amount': rec.price
                        }
                    scan_lines.append((0,0,values))
                    lines.append((0, 0, valuez))
            
            scan.write({'scan_line_ten':scan_lines})
            orm.write({'inpatient_scan':lines})
            scan_test.write({'scan_test':scan_doc})
            
        return result
    
class scanDetails(models.Model):
    _name = 'scan.menu'
    _rec_name = 'patient_id'
    
    patient_id = fields.Many2one('res.partner', string='Patient Name')
    request = fields.Char(string='ID Number')
    ebook_id = fields.Char(string='Patient ID')
    range = fields.Char(string='Range')
    test_range = fields.Char(string='Tested Range')
    test_name = fields.Char(string='Test')
    patient_activity = fields.Selection([('wait',"Doctor Assigned"),('doc','Diet Assigned'),('lab','Lab Assigned'),
                                         ('pres','Prescription'),('scan','Scan Assigned'),('labs','Lab Completed'),
                                         ('scans','Scan Completed'),('bill',"Pharmacy Bill Assigned"),
                                         ('completed',"Completed")],default='wait')
    