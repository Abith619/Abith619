from odoo import api,fields, models

class PbiDashboard(models.Model):
    _name = 'pbi.dashboard'
    _description = "power bi report"

    name = fields.Char(string="name")
    report_id = fields.Char(string="report ID")
    embedurl = fields.Char(string="Embed URL")
    workspace_id : fields.Many2one = fields.Many2one('pbi.workspace', string='workspace')
    report_type = fields.Char(string="report type")
    access_token = fields.Char(string="access token",compute='_compute_access_token')
    access_users : fields.Many2many = fields.Many2many('res.users','pbi_dashboard_access_user_rel',string='access users')
    is_admin = fields.Boolean(string="is admin",compute='checkadmin')
    filters_visible = fields.Boolean(string="filters visible",default=True)
    # _sql_constraints = [
    #     ('unique_dashboard_report_id', 'unique(report_id)', 'report_id. should be unique.'),
    #     ]


    def checkadmin(self):
        if self.user_has_groups('base.group_erp_manager') or self.user_has_groups('powerbi.group_powerbi_admin'):
            self.is_admin = True
        else:
            self.is_admin = False
    @api.depends('workspace_id')
    def _compute_access_token(self):
        self.access_token = self.workspace_id.connection_id.access_id

