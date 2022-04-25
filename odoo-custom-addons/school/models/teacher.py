from odoo.exceptions import ValidationError
from odoo import models, fields, api

#                       Teacher Field, Form
class TeacherRecord(models.Model):
    _name = "teacher.teacher"   
    _inherit=('mail.thread')
    _description= "School teacher"
    name = fields.Many2one('res.partner',string='Name', required=True) 
    teacher_age = fields.Integer(string='Age')    
    teacher_dob = fields.Date(string="Date of Birth")    
    gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')    
    teacher_blood_group = fields.Selection([('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'), ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')], string='Blood Group')
    nationality = fields.Many2one('res.country', string='Nationality')
    bill_no=fields.Float(string="Bill No : ")

#      Value(Required)-Condition
    @api.constrains('bill_no')
    def check_bill_no(self):
        if self.bill_no == 0.00:
            raise ValidationError("Bill No. must be greater than 0")

#               sum(total)
    total=fields.Integer(string='TotalAmount', compute='sum')
    @api.onchange('techer_line')
    @api.depends("total")
    def sum(self):
        b = []
        for i in self:
            for j in i.techer_line:
                b.append(j.total1)
        i.total = sum(b)

#           E-Mail 
    def action_send_email(self):
        self.ensure_one()
        compose_form_id = False
        return {
        'name': 'Compose Email',
        'type': 'ir.actions.act_window',
        'view_mode': 'form',
        'res_model': 'mail.compose.message',
        'views': [(compose_form_id, 'form')],
        'view_id': compose_form_id,
        'target': 'new',
    }

#           Print Report & PDF
    @api.multi
    def print_report(self):
        data={
            'from_date':self.from_date,
            'to_date':self.to_date
        }
        test = self.env['teacher.teacher'].search([('id','=',self.name.id)])
        if test.total <= 500:
            raise ValidationError("You can't print report")
        else:
            return self.env.ref('teacher.action_student_id_card').report_action(self, data=data)

# Value-Check
    @api.multi
    def rolls(self):
        test = self.env['teacher.teacher'].search([('id','=',self.name.id)])
        v = type(test.total)    
        raise ValidationError(v)

#       Set Age Condition
    @api.constrains('teacher_age')
    def age(self):
        if self.teacher_age <= 18:
            raise ValidationError("Please provide valid age  ?")

#                       State-Confirm
    def action_confirm(self):
        for rec in self:
            rec.state='confirm'

#                        State-Paid
    def action_paid(self):
        for i in self:
            i.state='paid'

#                               Invoice
    def invoices_button(self):
            return{
        'name': "Paid ",
        'type': 'ir.actions.act_window',
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'account.invoice',
        'view_id': self.env.ref('account.invoice_form').id,
        'context': {
            'default_partner_id': self.name.id,
        },
        'target': 'new'
    }

#       Condition_for required Field in add_line
    @api.constrains('techer_line')
    def val(self):
        for i in self.techer_line:
            if not i.gender:
                raise ValidationError('Please Enter Required Fields')

#           StaGes
    state =fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirm'),('inpayment','Inpayment'),
        ('paid','Paid'),('cancelled','Cancelled')
        ],string='Status',track_visibility='always', default='draft')
#       Stages for Kanban View
    def _expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]
#       Condition in Stages
    def write(self, values):
        if 'state' in values.keys():
            if self.state == 'paid':
                raise ValidationError(("After paid  You can't move !"))
        return super(TeacherRecord, self).write(values)

#           One2many 
    techer_line=fields.One2many('teacher.teacher.line','teach')

class TeacherLine(models.Model):
    _name="teacher.teacher.line"
    student_field_1 = fields.Many2one('res.users',string="Users")
    nationality = fields.Many2one('res.country', string='Nationality')
    gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender', required=True)
    teach = fields.Many2one('teacher.teacher',string="Teacher")
    amount=fields.Float(string="Salary")
    tax=fields.Many2many("account.tax",string="Tax")
    total1 = fields.Float(string='Total', store=True, compute='_get_sum', tracking=4)
    
#            Sum of Product
    @api.depends('amount','tax')
    def _get_sum(self):
        for rec in self:
            rec.update({
                'total1': rec.amount + sum(tax.amount for tax in rec.tax)
            })