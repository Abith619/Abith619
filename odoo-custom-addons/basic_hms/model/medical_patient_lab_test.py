from odoo import api, fields, models, _
from datetime import date,datetime
from odoo.exceptions import Warning

class medical_patient_lab_test(models.Model):
    _name = 'medical.patient.lab.test'
    _rec_name = 'request'

    request = fields.Char('Request', readonly = True)
    date =  fields.Datetime('Date', default = fields.Datetime.now)
    lab_test_owner_partner_id = fields.Many2one('res.partner', 'Owner Name')
    urgent =  fields.Boolean('Urgent',)
    owner_partner_id = fields.Many2one('res.partner')
    state = fields.Selection([('draft', 'New'),('tested', 'Waiting'), ('cancel', 'Cancel'),('ontest', 'On Testing')], readonly= True, default = 'draft')
    medical_test_type_id = fields.Many2one('medical.test_type', 'Test',required = True)
    test_types = fields. Many2one('medical.lab.test.units',string='Test Types',required = True)
    test_amount = fields.Float(string="Test Amount", related='test_types.code')
    patient_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string='Patient',required=True)
    doctor_id = fields.Many2one('res.partner',domain=[('is_doctor','=',True)],string='Doctor',required=True)
    insurer_id = fields.Many2one('medical.insurance','Insurer')
    invoice_to_insurer = fields.Boolean('Invoice to Insurance')
    lab_res_created = fields.Boolean(default  =  False) 
    is_invoiced = fields.Boolean(copy=False,default = False)
    units= fields.Many2one('test.units', string="Units",related='test_types.units')
    normal_range = fields.Float(related='test_types.normal_range')
    normal_ranges = fields.Char(related='test_types.normal_ranges')
    reports= fields.One2many('scan.test.document','scan_t',string="Documents")

    def update_result(self):
        self.state = 'ontest'



    @api.onchange('units','normal_range')
    def _range(self):
        lines=[(5,0,0)]
        val={
            'test_unit':self.units,
            'normal_ranges':self.normal_ranges
        }
        lines.append((0,0,val))
        self.reports = lines

    # @api.onchange('test_types')
    # def _range_change(self):
    #     for rec in self:
    #         lines = [(5, 0, 0)]
    #         for line in self.test_types.test_line:

    #             val={
    #                 'normal_range': line.product.id,
    #                 'quantity':line.quantity,
    #                 'uom':line.uom,
    #             }
    #             lines.append((0,0,val))
    #         rec.requisitionline=lines
        



    @api.onchange('medical_test_type_id')
    def onchange_test(self):
        for rec in self:
            return {'domain':{'test_types':[('test', '=', rec.medical_test_type_id.id)]}}
            
    @api.model
    def create(self, vals):
        vals['request'] = self.env['ir.sequence'].next_by_code('test_seq')
        result = super(medical_patient_lab_test, self).create(vals)
        orm = self.env['patient.bills'].search([('patient_name','=',result.patient_id.id)],order='id desc', limit=1)
        lines=[]
        value={
            'name':'Lab Payment',
            'date':datetime.now(),
            'bill_amount':result.test_amount,
        }
        lines.append((0,0,value))
        orm.write({'bills_lines':lines})


        labscan = self.env['medical.doctor'].search([('patient','=',result.patient_id.id)])
        lab_lines=[]
        values={
            'lab_scan_alot':result.id,
            'date':datetime.now()
            }
        lab_lines.append((0,0,values))
        labscan.write({'history_surgery':lab_lines})

        return result 

        # lines=[]
        # bill={
        #     'name':'Lab Payment',
        #     'date':datetime.now(),
        #     'bill_amount':self.test_amount,
        # }
        # lines.append((0,0,bill))
        # bills = self.env['patient.bills'].search([('patient_name','=',self.patient_id.id)])
        # bills.update({
        #     'bills_lines':lines
        #     })




    def cancel_lab_test(self):
        self.write({'state': 'cancel'})

    def create_lab_test(self):
        res_ids = []
        for browse_record in self:
            result = {}
            medical_lab_obj = self.env['medical.lab']
            res=medical_lab_obj.create({
                                        'name': self.env['ir.sequence'].next_by_code('ltest_seq'),
                                       'patient_id': browse_record.patient_id.id,
                                       'date_requested':browse_record.date or False,
                                       'test_id':browse_record.medical_test_type_id.id or False,
                                       'requestor_physician_id': browse_record.doctor_id.id or False,
                                       })
            res_ids.append(res.id)
            if res_ids:                     
                imd = self.env['ir.model.data']
                action = imd.xmlid_to_object('basic_hms.action_medical_lab_form')
                list_view_id = imd.xmlid_to_res_id('basic_hms.medical_lab_tree_view')
                form_view_id  =  imd.xmlid_to_res_id('basic_hms.medical_lab_form_view')
                result = {
                                'name': action.name,
                                'help': action.help,
                                'type': action.type,
                                'views': [ [list_view_id,'tree' ],[form_view_id,'form']],
                                'target': action.target,
                                'context': action.context,
                                'res_model': action.res_model,
                                'res_id':res.id,
                                
                            }

            if res_ids:
                    result['domain'] = "[('id','=',%s)]" % res_ids

        return result




class Testdocuments(models.Model):
    _name ="scan.test.document"

    scan_t = fields.Many2one('medical.patient.lab.test',string="Doctor")
    report_name = fields.Char(string="Report Name")
    normal_range = fields.Float( string="Normal Range")
    normal_ranges = fields.Char( string="Normal Range",rewuired=True)
    tested_range = fields.Char(string="Tested Range")
    test_unit = fields.Many2one('test.units',string="Unit")
    attachments = fields.Many2many('ir.attachment',string="Attachment")




