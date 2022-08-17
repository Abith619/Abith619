from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import Warning, ValidationError

class manylabs(models.Model):
    _name = 'lab.many'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

class manylabs_data(models.Model):
    _name = 'lab.many.data'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

class manylabs_form(models.Model):
    _name = 'lab.many.form'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')
    date= fields.Datetime(string="Date of Lab/Scan")

class lab_test_form(models.Model):
    _name = 'lab.test.form'

    name = fields.Char(string='Name')
    date= fields.Datetime(string="Date of Lab/Scan")
    patient_id = fields.Many2one('res.partner', string='Patient')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')

class lab_test_data(models.Model):
    _name = 'lab.test.data'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

class lab_test_data_form(models.Model):
    _name = 'lab.test.data.form'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

class lab_test_data_form_many(models.Model):
    _name = 'lab.test.data.form.many'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

class lab_test_data_form_many_data(models.Model):
    _name = 'lab.test.data.form.many.data'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

class lab_test_data_form_many_form(models.Model):
    _name = 'lab.test.data.form.many.form'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

class lab_test_data_form_many_form_many(models.Model):
    _name = 'lab.test.data.form.many.form.many'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

class lab_test_hospital(models.Model):
    _name = 'lab.test.hospital'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

class lab_test_hospital_data(models.Model):
    _name = 'lab.test.hospital.data'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

# class lab_test_hospital_form(models.Model):
#     _name = 'lab.test.hospital.form'

#     name = fields.Char(string='Name')

class lab_test_hospital_form_many(models.Model):
    _name = 'lab.test.hospital.form.many'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

class lab_test_hospital_form_many_data(models.Model):
    _name = 'lab.test.hospital.form.many.data'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

class lab_test_hospital_form_many_form(models.Model):
    _name = 'lab.test.hospital.form.many.form'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

class lab_test_hospital_form_many_form_data(models.Model):
    _name = 'lab.test.hospital.form.many.form.data'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

class lab_hospital_test(models.Model):
    _name = 'lab.hospital.test'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

class lab_hospital_test_data(models.Model):
    _name = 'lab.hospital.test.data'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

class lab_hospital_test_form(models.Model):
    _name = 'lab.hospital.test.form'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

class Immunology_test(models.Model):
    _name = 'immunology.test'

    patient_id = fields.Many2one('res.partner', string='Patient')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    date= fields.Datetime(string="Date of Lab/Scan")
    range = fields.Char(string='Range')

class LabsScansd(models.Model):
    _name='lab.scan.form'
    _rec_name = 'request'

    request = fields.Char('ID Number', readonly = True)
    patient_id = fields.Many2one('res.partner', string='Patient Name')
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price')
    range = fields.Char(string='Range')
    test_range = fields.Char(string='Tested Range')
    date= fields.Datetime(string="Date of Lab/Scan")
    write_date=fields.Date(string='Date')
    ebook_id = fields.Char(string='Patient ID')
    # appoinment_by=fields.Many2one('res.users',string='Appointment By',default=lambda self: self.env.user,readonly='1')

    company_id=fields.Many2one('res.company',string='Branch',readonly=True,default=lambda self: self.env['res.company']._company_default_get('medical.doctor'))

    hemo_coag12 = fields.Many2many('lab.many', string="HAEMATOLOGY")
    hemo_coag1 = fields.Many2many('lab.many.data', string='Urine')
    hemo_coag2 = fields.Many2many('lab.many.form', string='Stool Analysis')
    lab_test_hos = fields.Many2many('lab.test.form', string='Semen')
    lab_test_hos_data = fields.Many2many('lab.test.data', string='Serology')
    lab_test_hos_form = fields.Many2many('lab.test.data.form', string='Bio Chemistry')
    lab_liver = fields.Many2many('lab.test.hospital.data', string='Endocrinology')
    lab_enzymes = fields.Many2many('lab.test.data.form.many',string='Liver Function')
    lab_lipid = fields.Many2many('lab.test.data.form.many.data',string='Enzymes')
    lab_protein = fields.Many2many('lab.test.data.form.many.form',string='Lipid')
    lab_checkup = fields.Many2many('lab.test.data.form.many.form.many',string='Lipoproteins')
    lab_endocrinology = fields.Many2many('lab.test.hospital', string='Master Health Check up')
    lab_immunology = fields.Many2many('lab.test.hospital.form.many', string='Tumour Makers')
    lab_tumour = fields.Many2many('lab.test.hospital.form.many.data',string='Drug Assays')
    lab_drug = fields.Many2many('lab.test.hospital.form.many.form',string='Serology Torch')
    lab_serology = fields.Many2many('lab.test.hospital.form.many.form.data',string='Leptospirosis')
    lab_leptospirosis = fields.Many2many('lab.hospital.test',string='HIV TEST')
    lab_hiv = fields.Many2many('lab.hospital.test.data',string='Hepatitis Panel')
    lab_hepatis = fields.Many2many('lab.hospital.test.form',string='X-Ray Digital')
    lab_immune_test = fields.Many2many('immunology.test',string='Immunology')

    def lab_button(self):
            return {
    'name': "Lab Details",
    'domain':[('patient_id', '=', self.patient_id.id)],
    'view_mode': 'tree,form',
    'res_model': 'lab.scan.form',
    'view_type': 'form',
    'type': 'ir.actions.act_window',
    }
#      Count in Smart Button
    def lab_count(self):
        for res in self :
            count_d = self.env['lab.scan.form'].search_count([('patient_id', '=', res.patient_id.id)])
            self.lab_recs= count_d

    lab_recs = fields.Integer(compute='lab_count',string="Lab Details")

    @api.model
    def create(self, vals):
        vals['request'] = self.env['ir.sequence'].next_by_code('lab.scan.form') or 'LAB'
        result = super(LabsScansd, self).create(vals)
        
        orm = self.env['patient.bills'].search([('patient_name','=',result.patient_id.id)],order='id desc', limit=1)
        lines=[]
        
        for rec in result.hemo_coag12:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.hemo_coag1:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.hemo_coag2:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.lab_test_hos:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.lab_test_hos_data:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.lab_test_hos_form:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.lab_enzymes:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.lab_lipid:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.lab_protein:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.lab_checkup:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.lab_endocrinology:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.lab_immunology:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.lab_tumour:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.lab_drug:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.lab_serology:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.lab_leptospirosis:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.lab_hiv:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.lab_hepatis:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.lab_immune_test:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        for rec in result.lab_liver:
            valuez={
                'name': rec.name,
                'date':datetime.now(),
                'bill_amount': rec.price
            }
            lines.append((0, 0, valuez))
        orm.write({'lab_bill':lines})

        labscan = self.env['medical.doctor'].search([('patient','=',result.patient_id.id)])
        lab_lines=[]
        
        for rec in result.hemo_coag12:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.hemo_coag1:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.hemo_coag2:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.lab_test_hos:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.lab_test_hos_data:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.lab_test_hos_form:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.lab_enzymes:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.lab_lipid:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.lab_protein:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.lab_checkup:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.lab_endocrinology:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.lab_immunology:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.lab_tumour:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.lab_drug:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.lab_serology:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.lab_leptospirosis:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.lab_hiv:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.lab_hepatis:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.lab_immune_test:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                }
            lab_lines.append((0,0,values))
        for rec in result.lab_liver:
            values={
                'date':datetime.now(),
                'lab_type':result.id,
                'name':rec.name,
                
                }
            lab_lines.append((0,0,values))

        labscan.write({'lab_test_line':lab_lines})


        return result
    

    hemo_coag = fields.Boolean("HAEMATOLOGY & COAGULATION - BLOOD")
    hemo = fields.Boolean("HAEMOGRAM (CBC)")
    hb = fields.Boolean("HB")
    rbc = fields.Boolean("RBC")
    pvc = fields.Boolean("PVC")
    mcv = fields.Boolean(string='MCV')
    mch = fields.Boolean(string='MCH')
    mchc = fields.Boolean(string='MCHC')
    td = fields.Boolean(string='TC')
    dc = fields.Boolean(string='DC')
    esr = fields.Boolean(string='ESR')

    mantoux = fields.Boolean(string='Mantoux')
    abs = fields.Boolean(string='Abs.Eosinophil Count')
    qbc_mp = fields.Boolean(string='QBC MP & MF test')
    smear = fields.Boolean(string='Smear Study')
    blood_group= fields.Boolean(string='Blood Group & Rh')
    coombs_test = fields.Boolean(string='Coombs Test-Direct')
    coombs_test_val = fields.Boolean(string='Coombs Test-InDirect')
    antibody = fields.Boolean(string='Rh Antibody Titre')
    reticulo = fields.Boolean(string='Reticulocyte Count')
    elctrophro = fields.Boolean(string='HB Electrophoresis')
    vitamin = fields.Boolean(string='Vitamin B12')
    follac = fields.Boolean(string='Follc Acid')
    platelet = fields.Boolean(string='Platelet Count')
    bt = fields.Boolean(string='BT')
    ct = fields.Boolean(string='CT')
    pt = fields.Boolean(string='PT')
    ptt = fields.Boolean(string='aPTT')
    protein = fields.Boolean(string='Protein C')
    proteins = fields.Boolean(string='Protein S')
    anthithrobin = fields.Boolean(string='Antithrombin III')
    factor = fields.Boolean(string='Factor V Leiden')
    fibrinogen = fields.Boolean(string='Fibrinogen')
    dimer = fields.Boolean(string='D- Dimer')
    urine = fields.Boolean(string='Urine')
    analysis = fields.Boolean(string='Urine Analysis')
    pregnancy = fields.Boolean(string='Pregnanct Test')
    culture = fields.Boolean(string='Culture & Sensitivity')
    microalbum = fields.Boolean(string='Microalbuminuria')
    hrs = fields.Boolean(string='24Hrs')
    spot = fields.Boolean(string='Spot')
    stone = fields.Boolean(string='Stone Analysis')
    sugar = fields.Boolean(string='Sugar')
    albumin = fields.Boolean(string='Albumin')
    stool_analysis = fields.Boolean(string='Stool Analysis')
    routine_anal = fields.Boolean(string='Routine Analysis')
    occult = fields.Boolean(string='Occult Blood')
    semen = fields.Boolean(string='SEMEN')
    routine_analysis = fields.Boolean(string='Routine Analysis')
    sensitivity = fields.Boolean(string='Culture & Sensitivity')
    serology = fields.Boolean(string='SEROLOGY-BLOOD')
    widal = fields.Boolean(string='Widal')
    dengue = fields.Boolean(string='Dengue Ab lgG &igM')
    letospira = fields.Boolean(string='Letospira lgM ELISA')
    anti = fields.Boolean(string='ANTI TB')
    igg = fields.Boolean(string='IgG')
    igm = fields.Boolean(string='IgM')
    iga = fields.Boolean(string='IgA')
    brucella = fields.Boolean(string='Brucella Abs')
    aso = fields.Boolean(string='ASO')
    ra = fields.Boolean(string='RA')
    crp = fields.Boolean(string='CRP')
    anti_ccp = fields.Boolean(string='Anti CCP')
    vdrl = fields.Boolean(string='VDRL TPHA')
    fta_abs = fields.Boolean(string='FTA-ABS')
    iggg = fields.Boolean(string='IgG')
    igmm = fields.Boolean(string='IgM')
    ebv_abs = fields.Boolean(string='EBV Abs')





    biochemistry = fields.Boolean("BIOCHEMISTRY-BLOOD")
    blood_sugar = fields.Boolean("BLOOD SUGAR")
    f = fields.Boolean("F")
    r = fields.Boolean("R")
    blood_sugar_pp = fields.Boolean(string='Blood Sugar PP')
    onehrs = fields.Boolean(string='1.1/2hrs')
    twohrs = fields.Boolean(string='2hrs')
    gtt = fields.Boolean(string='GTT')
    hba1c = fields.Boolean(string='Hb A1c')

    blood_urea = fields.Boolean(string='Blood Urea')
    creatinine = fields.Boolean(string='Creatnine')
    uric_acid = fields.Boolean(string='Uric Acid')
    cholestral = fields.Boolean(string='Cholesterol')
    calceium = fields.Boolean(string='Calcium')
    phosphrous = fields.Boolean(string='Phosphorous')
    megnisium = fields.Boolean(string='Magnesium')
    elctrolytes = fields.Boolean(string='Electrolytes')
    copper = fields.Boolean(string='Copper')
    ceruloplasmin = fields.Boolean(string='Ceruloplasmin')
    total_protein = fields.Boolean(string='Total Proteins')
    albumin = fields.Boolean(string='Albumin')
    protein = fields.Boolean(string='Protein EPP')
    g6pd = fields.Boolean(string='G 6 PD')
    iron = fields.Boolean(string='Iron')
    tibc = fields.Boolean(string='TIBC')
    ferritin = fields.Boolean(string='Ferritin')
    gfr = fields.Boolean(string='GFR')
    liver = fields.Boolean(string='LIVER FUNCTION')
    billrubin = fields.Boolean(string='Total Billrubin')
    sgot = fields.Boolean(string='SGOT')
    sgpt = fields.Boolean(string='SGPT')
    phosphatase = fields.Boolean(string='AIL.Phosphatase')
    gamma = fields.Boolean(string='Gamma GT')
    proteinss = fields.Boolean(string='Total Protein')
    enzymes = fields.Boolean(string='enzymes')
    cpk = fields.Boolean(string='CPK')
    cpkmb = fields.Boolean(string='CPK MB')
    troponin = fields.Boolean(string='Troponin T')
    troponin_i = fields.Boolean(string='Troponin I')
    ldh = fields.Boolean(string='LDH')
    amylase = fields.Boolean(string='Amylase')
    lipase = fields.Boolean(string='Lipase')
    acid_phosphate = fields.Boolean(string='Acid Phosphatase')
    lipid_profile = fields.Boolean(string='LIPID PROFILE')
    total_cholestral = fields.Boolean(string='Total Cholesterol')
    hdl_cholestral = fields.Boolean(string='HDL Cholesterol')
    vldl_cholestral = fields.Boolean(string='VLDL Cholesterol')
    trigly = fields.Boolean(string='Triglycerides')
    lipoprotein = fields.Boolean(string='LIPOPROTEINS')
    lipoprotein_data = fields.Boolean(string='Lipoprotein a(Lpa)')
    homocystine = fields.Boolean(string='Homocystine')
    apolipo = fields.Boolean(string='Apoliprotein A')
    apolipoprotein = fields.Boolean(string=' Apoliprotein B')
    lemptoigg = fields.Boolean(string='Lepto IgG')
    lemptoigm = fields.Boolean(string='Lepto IgM')



    endorcrinology = fields.Boolean("ENDOCRINOLOGY - BLOOD")
    ft3 = fields.Boolean("FT3")
    ft4 = fields.Boolean("FT4")
    tsh = fields.Boolean("TSH")
    t3 = fields.Boolean(string='T3')
    t4 = fields.Boolean(string='T4')
    tshh = fields.Boolean(string='TSH')
    tg_antibody = fields.Boolean(string='Tg Antibodies')
    tpo = fields.Boolean(string='TPO Ab')
    throglobin = fields.Boolean(string='Thyroglobulin')

    lh = fields.Boolean(string='LH')
    fshh = fields.Boolean(string='FSH')
    proiactin = fields.Boolean(string='Proiactin')
    estraodial = fields.Boolean(string='Estradiol')
    estraodialfree = fields.Boolean(string='Estradiol-Free')
    trible = fields.Boolean(string='Trible Screening')
    progestrone = fields.Boolean(string='Progestrone')
    progestrone17oh = fields.Boolean(string='17 OH Progestrone')
    testoster = fields.Boolean(string='Testosterone')
    testosterone = fields.Boolean(string='Free Testosterone  ')
    dheas = fields.Boolean(string='DHEAS')
    growth_hormone = fields.Boolean(string='Growth Hormone')
    cortisol = fields.Boolean(string='Cortisol AM PM')
    acth = fields.Boolean(string='ACTH')
    pth = fields.Boolean(string='PTH(intact)')
    insulin = fields.Boolean(string='Insulin CD F')
    pp = fields.Boolean(string='PP')
    peptide = fields.Boolean(string='C-Peptide')
    f = fields.Boolean(string='F')
    pp = fields.Boolean(string='PP')
    dual_mark = fields.Boolean(string='Dual Marker test')
    amh = fields.Boolean(string='AMH')
    immunology = fields.Boolean(string='IMMUNOLOGY-BLOOD')
    fixation = fields.Boolean(string='Immuno Fixation.EPP(IFE)')
    total_igg = fields.Boolean(string='Total IgG')
    igaa = fields.Boolean(string='IgA')
    igmm = fields.Boolean(string='IgM')
    total_igee = fields.Boolean(string='Total IgE')
    ana = fields.Boolean(string='ANA')
    dsdna = fields.Boolean(string=' ds DNA')
    canca = fields.Boolean(string='c ANCA')
    panca = fields.Boolean(string='p ANCA')
    c3 = fields.Boolean(string='C3')
    c4 = fields.Boolean(string='C4')
    cardiolipin = fields.Boolean(string='Cardiolipin Ab')
    iggg = fields.Boolean(string='IgG')
    igmmm = fields.Boolean(string='IgM')
    anticcp = fields.Boolean(string='Anti CCP')
    vitamind3 = fields.Boolean(string='VITAMIN D3(25-OH)')
    vitamind  = fields.Boolean(string='VITAMIN D3(125-OH)')
    tumour_maker = fields.Boolean(string='TUMOURS MAKERS')
    cea = fields.Boolean(string='CEA')
    afp = fields.Boolean(string='AFP')
    beta_hcg = fields.Boolean(string='Beta HCG')
    ca125 = fields.Boolean(string='CA 1-25-(Ovary)')
    ca199 = fields.Boolean(string='CA 19-9 -(GI TRACK)')
    ca153 = fields.Boolean(string='CA 15-3-(Breast)')
    b2globulin = fields.Boolean(string='B2 Microglobulin')
    psa = fields.Boolean(string='PSA')
    freepsa = fields.Boolean(string=' Free PSA')
    d33 = fields.Boolean(string='D-3')
    drug_assays = fields.Boolean(string='DRUG ASSAYS')
    phentoin = fields.Boolean(string='Phenytoin')
    carbamaz = fields.Boolean(string='Carbamazepine')
    valporic = fields.Boolean(string='Valporic Acid')
    pheno = fields.Boolean(string='Phenobarbital')



    serology = fields.Boolean("SEROLOGY - BLOOD TORCH PANNEL")
    torch_igg = fields.Boolean("ToRch IgG Pannel")
    torch_igm = fields.Boolean("ToRch IgM Pannel")
    toxiplass = fields.Boolean(string='Toxiplasma')
    toxiplassgg = fields.Boolean(string='IgG')
    toxiplassmm = fields.Boolean(string='IgM')
    rupella = fields.Boolean(string='Rubella')
    rupellagg = fields.Boolean(string='IgG')
    rupellamm = fields.Boolean(string='IgM')

    cmv = fields.Boolean(string='C.M.V')
    cmvgg = fields.Boolean(string='IgG')
    cmvmm = fields.Boolean(string='IgM')
    hsv1 = fields.Boolean(string='H.S.V I')
    hsv1gg = fields.Boolean(string='IgG')
    hsv1mm = fields.Boolean(string='IgM')
    hsv2 = fields.Boolean(string='H.S.V II')
    hsv2gg = fields.Boolean(string='IgG')
    hsv2mm = fields.Boolean(string='IgM')
    sperm_antibody = fields.Boolean(string='Anti Sperm Antibody')
    chiamydia = fields.Boolean(string='Chiamydia Ab')
    leptospir = fields.Boolean(string='LEPTOSPIROSIS')
    dfm = fields.Boolean(string='DFM')
    blood = fields.Boolean(string='Blood')
    urine = fields.Boolean(string='Urine')
    csf = fields.Boolean(string='C.S.F')
    letospira = fields.Boolean(string='Leptospira IgM ELISA')
    hivtest = fields.Boolean(string='HIV/AIDS TESTS')
    hivtest1 = fields.Boolean(string='HIV I&II By ELISA')
    hivtest2 = fields.Boolean(string='HIV I&II By Western blot')
    hivtest3 = fields.Boolean(string='HIV Proviral')
    hivtest4 = fields.Boolean(string='HIV Viral Load')
    hivtest5 = fields.Boolean(string='CD4/CD8 Count')
    hepatitis = fields.Boolean(string='HEPATITIS PANEL')
    antihav = fields.Boolean(string='Anti HAV')
    ig = fields.Boolean(string='IgM')
    im = fields.Boolean(string='IgM')
    hbsag = fields.Boolean(string='HBs Ag (ELISA)')
    antihbs = fields.Boolean(string='Anti HBs')
    totalmg = fields.Boolean(string='Total')
    igmsm = fields.Boolean(string='IgM')
    hbeag = fields.Boolean(string='Hbe Ag')
    antihbe = fields.Boolean(string='Anti Hbe')
    antihbss = fields.Boolean(string='Anti Hbs(Quantitative)')
    antihcv = fields.Boolean(string='Anti HCV')
    antidelta = fields.Boolean(string='Anti Delta IgM')
    antihevigm = fields.Boolean(string='Anti HEV IgM')
    xrays = fields.Boolean(string='X-RAYS DIGITAL')
    cheastpa = fields.Boolean(string='Chest PA View')
    sinuses = fields.Boolean(string='Sinuses')
    cervicalspine = fields.Boolean(string='Cervical Spine AP&Lat')
    lsspain = fields.Boolean(string='L.S.Spain AP & Lat')
    treadmill = fields.Boolean(string='Tread Mill')
    echo = fields.Boolean(string='ECHO')
    doppler = fields.Boolean(string='Colour Doppler')
    mammography = fields.Boolean(string='Mammography')
    others = fields.Boolean(string='Others...........')
    ecg = fields.Boolean(string='ECG    ')
    pftultra = fields.Boolean(string='PFT ULTRASOUND SCAN')
    specify = fields.Boolean(string='specify.........')
    wellwomen = fields.Boolean(string='Well-Women Check Up')
    mhc = fields.Boolean(string='MHC-Gold')
    mhcplatinum = fields.Boolean(string='MHC-Platinum')

