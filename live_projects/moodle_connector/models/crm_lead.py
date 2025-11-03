from odoo import models, fields
from odoo.exceptions import ValidationError

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    course_id = fields.Many2one('slide.channel', string="Course Applied For", help="The course for which the lead has applied")

    def action_approve_lead(self):
        template = self.env.ref('custom_course.email_template_approve_lead', raise_if_not_found=False)
        approved_stage = self.env['crm.stage'].search([('name', '=', 'Qualified')], limit=1)
        if not approved_stage:
            approved_stage = self.env['crm.stage'].create({'name': 'Qualified', 'sequence': 3})
        for lead in self:
            if template:
                mail_id = template.sudo().send_mail(lead.id, force_send=True)
                if mail_id and approved_stage:
                    lead.stage_id = approved_stage.id
        # raise ValidationError(mail_id)
        return True

    def action_reject_lead(self):
        template = self.env.ref('custom_course.email_template_reject_lead', raise_if_not_found=False)
        rejected_stage = self.env['crm.stage'].search([('name', '=', 'Rejected')], limit=1)
        if not rejected_stage:
            rejected_stage = self.env['crm.stage'].create({'name': 'Rejected', 'sequence': 5})
        for lead in self:
            if template:
                mail_id = template.sudo().send_mail(lead.id, force_send=True)
                if mail_id and rejected_stage:
                    lead.stage_id = rejected_stage
        return True
        
