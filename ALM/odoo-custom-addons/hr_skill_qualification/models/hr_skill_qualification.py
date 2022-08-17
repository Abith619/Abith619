# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from datetime import date


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    techskill_ids = fields.One2many(
        'emp.tech.skills', 'employee_id', 'Technical Skills')
    nontechskill_ids = fields.One2many(
        'emp.nontech.skills', 'employee_id', 'Non-Technical Skills')
    education_ids = fields.One2many(
        'employee.education', 'employee_id', 'Education')
    certification_ids = fields.One2many(
        'employee.certification', 'employee_id', 'Certification')
    profession_ids = fields.One2many(
        'employee.profession', 'employee_id', 'Professional Experience')


class EmployeeTechSkills(models.Model):
    _name = 'emp.tech.skills'
    _description = 'Employee Tech Skills'

    applicant_id = fields.Many2one('hr.applicant', 'applicant')
    employee_id = fields.Many2one('hr.employee', 'Employee')
    tech_id = fields.Many2one(
        'tech.tech', 'Technical Skills', ondelete="cascade")
    levels = fields.Selection([('basic', 'Basic'),
                               ('medium', 'Medium'),
                               ('advance', 'Advance')], 'Levels')


class TechTech(models.Model):
    _name = 'tech.tech'
    _description = 'Tech Tech'

    name = fields.Char()
    sequence = fields.Integer("Sequence")

    _sql_constraints = [
        ('tech_unique', 'unique (name)',
         'The name of the Technologies already exixts!'),
        ('seq_uniq', 'unique (sequence)', "Sequence name already exists!")
    ]

    @api.multi
    def unlink(self):
        """
        his method is called user tries to delete a skill which
        is already in use by an employee.
        --------------------------------------------------------
        @param self : object pointer
        """
        tech_skill = self.env['emp.tech.skills'].search(
            [('tech_id', 'in', self.ids)])
        if tech_skill:
            raise UserError(
                _('You are trying to delete a Skill which is referenced by an Employee.'))
        return super(TechTech, self).unlink()


class EmployeeNonTechSkills(models.Model):
    _name = 'emp.nontech.skills'
    _description = 'Employee Non Tech Skills'

    applicant_id = fields.Many2one('hr.applicant', 'Applicant')
    employee_id = fields.Many2one('hr.employee', 'Employee')
    nontech_id = fields.Many2one(
        'nontech.nontech', 'Non-Technical Skills', ondelete="cascade")
    levels = fields.Selection([('basic', 'Basic'),
                               ('medium', 'Medium'),
                               ('advance', 'Advance')], 'Levels')


class NontechNontech(models.Model):
    _name = 'nontech.nontech'
    _description = 'Nontech Nontech'

    name = fields.Char()
    sequence = fields.Integer("Sequence")

    _sql_constraints = [
        ('nontech_unique', 'unique (name)',
         'The name of the Non Technical skills must be unique!'),
        ('seq_uniq', 'unique (sequence)', "Sequence name already exists!")
    ]

    @api.multi
    def unlink(self):
        """
        This method is called user tries to delete a skill which
        is already in use by an employee.
        --------------------------------------------------------
        @param self : object pointer
        """
        tech_skill = self.env['emp.nontech.skills'].search(
            [('nontech_id', 'in', self.ids)])
        if tech_skill:
            raise UserError(
                _('You are trying to delete a Skill \
                    which is referenced by an Employee.'))
        return super(NontechNontech, self).unlink()


class EmployeeEducation(models.Model):
    _name = 'employee.education'
    _description = 'Employee Education'

    applicant_id = fields.Many2one('hr.applicant', 'applicant')
    employee_id = fields.Many2one('hr.employee', 'Employee')
    type_id = fields.Many2one('hr.recruitment.degree',
                              "Degree", ondelete="cascade")
    institute_id = fields.Many2one(
        'hr.institute', 'Institutes', ondelete="cascade")
    score = fields.Char()
    qualified_year = fields.Date()
    doc = fields.Binary('Transcripts')
    subject = fields.Char(string='Subject')


class HrInstitute(models.Model):
    _name = 'hr.institute'
    _description = 'Hr Institute'

    name = fields.Char()
    country_id = fields.Many2one('res.country', 'Country')
    state_id = fields.Many2one('res.country.state', 'State')


class RecruitmentDegree(models.Model):
    _inherit = "hr.recruitment.degree"

    name = fields.Char("Degree")
    sequence = fields.Integer(
        "Sequence", default=1, help="Gives the sequence \
        order when displaying a list of degrees.")

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
         'The name of the Degree of Recruitment must be unique!'),
        ('seq_uniq', 'unique (sequence)', "Sequence name already exists!")
    ]


class EmployeeCertification(models.Model):
    _name = 'employee.certification'
    _description = 'Employee Certification'

    applicant_id = fields.Many2one('hr.applicant', 'applicant')
    employee_id = fields.Many2one('hr.employee', 'Employee')
    course_id = fields.Many2one('cert.cert', 'Course Name', ondelete="cascade")
    levels = fields.Char('Bands/Levels of Completion')
    year = fields.Date('Year of completion')
    doc = fields.Binary('Certificates')


class CertCert(models.Model):
    _name = 'cert.cert'
    _description = 'Cert Cert'

    name = fields.Char('Course Name')
    sequence = fields.Integer("Sequence")

    _sql_constraints = [
        ('cert_unique', 'unique (name)',
         'The name of the Certifications must be unique!'),
        ('seq_uniq', 'unique (sequence)', "Sequence name already exists!")
    ]


class EmployeeProfession(models.Model):
    _name = 'employee.profession'
    _description = 'Employee Profession'

    applicant_id = fields.Many2one('hr.applicant', 'applicant')
    employee_id = fields.Many2one('hr.employee', 'Employee')
    job_id = fields.Many2one('hr.job', 'Job Title')
    location = fields.Char()
    from_date = fields.Date('Start Date')
    to_date = fields.Date('End Date')
    doc = fields.Binary('Experience Certificates')

    _sql_constraints = [
        ('to_date_greater', 'check(to_date > from_date)',
         'Start Date of Professional Experience \
         should be less than End Date!'),
    ]

    @api.constrains('from_date', 'to_date')
    def check_from_date(self):
        """
        This method is called when future Start date is entered.
        --------------------------------------------------------
        @param self : object pointer
        """
        # date = fields.Datetime.now()
        today = date.today()
        if (self.from_date > today) or (self.to_date > today):
            raise ValidationError(
                'Future Start Date or End Date \
                in Professional experience is not acceptable!!')


class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    techskill_ids = fields.One2many(
        'emp.tech.skills', 'applicant_id', 'Technical Skills')
    nontechskill_ids = fields.One2many(
        'emp.nontech.skills', 'applicant_id', 'Non-Technical Skills')
    education_ids = fields.One2many(
        'employee.education', 'applicant_id', 'Education')
    certification_ids = fields.One2many(
        'employee.certification', 'applicant_id', 'Certification')
    profession_ids = fields.One2many(
        'employee.profession', 'applicant_id', 'Professional Experience')

    @api.multi
    def create_employee_from_applicant(self):
        """ Create an hr.employee from the hr.applicants """
        employee = False
        for applicant in self:
            address_id = contact_name = False
            if applicant.partner_id:
                address_id = applicant.partner_id.address_get(['contact'])[
                    'contact']
                contact_name = applicant.partner_id.name_get()[0][1]
            if applicant.job_id and (applicant.partner_name or contact_name):
                applicant.job_id.write(
                    {'no_of_hired_employee':
                        applicant.job_id.no_of_hired_employee + 1})
                employee = self.env['hr.employee'].create({
                    'name': applicant.partner_name or contact_name,
                    'job_id': applicant.job_id.id,
                    'address_home_id': address_id,
                    'department_id': applicant.department_id.id or False,
                    'address_id': applicant.company_id and applicant.company_id.partner_id and applicant.company_id.partner_id.id or False,
                    'work_email': applicant.department_id and applicant.department_id.company_id and applicant.department_id.company_id.email or False,
                    'work_phone': applicant.department_id and applicant.department_id.company_id and applicant.department_id.company_id.phone or False,
                    'techskill_ids': [(6, 0, self.techskill_ids.ids)],
                    'nontechskill_ids': [(6, 0, self.nontechskill_ids.ids)],
                    'education_ids': [(6, 0, self.education_ids.ids)],
                    'certification_ids': [(6, 0, self.certification_ids.ids)],
                    'profession_ids': [(6, 0, self.profession_ids.ids)],
                })
                applicant.write({'emp_id': employee.id})
                applicant.job_id.message_post(
                    body=_(
                        'New Employee %s Hired') % applicant.partner_name if applicant.partner_name else applicant.name,
                    subtype="hr_recruitment.mt_job_applicant_hired")
                employee._broadcast_welcome()
            else:
                raise UserError(
                    _('You must define an Applied Job and a Contact Name for this applicant.'))
        employee_action = self.env.ref('hr.open_view_employee_list')
        dict_act_window = employee_action.read([])[0]
        if employee:
            dict_act_window['res_id'] = employee.id
        dict_act_window['view_mode'] = 'form,tree'
        return dict_act_window
