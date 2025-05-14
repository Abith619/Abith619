from odoo import models, _


class CustomerStatementCustomHandler(models.AbstractModel):
    _name = 'account.customer.statement.report.handler'
    _inherit = 'account.partner.ledger.report.handler'
    _description = 'Customer Statement Custom Handler'

    def _custom_options_initializer(self, report, options, previous_options):
        super()._custom_options_initializer(report, options, previous_options)

        options['buttons'].append({
            'name': _('Send'),
            'action': 'action_send_statements',
            'sequence': 90,
            'always_show': True,
        })
