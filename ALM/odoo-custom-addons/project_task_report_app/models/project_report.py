# -*- coding: utf-8 -*-

from openerp import api, fields, models, _

class ProjectDetails(models.TransientModel):
	_name = 'project.details'
	_description = "Project Report Details"

	user_id = fields.Many2one('res.users', string='User', required=True)
	start_date = fields.Date(string='Start Date', required=True)
	end_date = fields.Date(string='End Date', required=True)
	stage_id = fields.Many2one('project.task.type', string="Stage", required=True)

	@api.multi
	def print_report(self):
		project_id = self.env.context.get('active_id')
		data = {
			'ids': self.ids,
			'model': self._name,
			'form': {
			    'project_id':project_id,
				'user_id': self.user_id.id,
				'start_date': self.start_date,
				'end_date':self.end_date,
				'stage_id':self.stage_id.id,
			},
		}
		return self.env.ref('project_task_report_app.project_report_action').report_action(self, data=data)

class ProjectTaskReport(models.AbstractModel):
	_name = 'report.project_task_report_app.template_report'
	_description = "Project Report"

	@api.model
	def _get_report_values(self, docids, data=None):
		user_id = data['form']['user_id']
		start_date = data['form']['start_date'] 
		end_date = data['form']['end_date']
		stage_id = data['form']['stage_id']
		project_id = data['form']['project_id']
		docs = []

		task_ids = self.env['project.task'].search([('user_id','=',user_id),('project_id','=',project_id),('stage_id','=',stage_id),('date_assign','>=',start_date),('date_assign','<=',end_date)])
		for task in task_ids:
			docs.append({
				'name': task.name,
				'user_id': task.user_id.name,
				'stage': task.stage_id.name,
				'planned_hours':task.planned_hours,
				'total_hours_spent':task.total_hours_spent,
				'remaining_hours':task.remaining_hours,
				'date_assign':task.date_assign.date(),
				'date_deadline':task.date_deadline,
			})
		return {
			'doc_ids': data['ids'],
			'doc_model': data['model'],
			'docs': docs,
			'start_date':start_date,
			'end_date':end_date,
			'project_id':self.env['project.project'].browse(project_id),
			'stage_id':self.env['project.task.type'].browse(stage_id),
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: