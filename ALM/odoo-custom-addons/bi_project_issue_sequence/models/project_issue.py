# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class project_issue(models.Model):
    _inherit = 'project.task'

    sequence_name = fields.Char(string="Sequence",readonly=True)

    @api.model
    def create(self,vals):
    	if vals.get('sequence_name', _('New')) == _('New'):
            vals['sequence_name'] = self.env['ir.sequence'].next_by_code('project.task') or _('New')
    	res = super(project_issue, self).create(vals)
    	return res


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
