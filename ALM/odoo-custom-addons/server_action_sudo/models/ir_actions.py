# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).
from odoo import models, fields, api


class ServerAction(models.Model):
    _inherit = 'ir.actions.server'

    execute_silently = fields.Boolean(default=False)
    execute_sudo = fields.Boolean(default=False)
    sudo_id = fields.Many2one(
        comodel_name='res.users',
        string='Sudo User',
        help='If left blank default sudo uers will be used.'
    )

    @api.model
    def run_action_object_write(self, action, eval_context=None):
        """ Write server action.

         - 1. evaluate the value mapping
         - 2. depending on the write configuration:

          - `current`: id = active_id
          - `other`: id = from reference object
          - `expression`: id = from expression evaluation
        """
        res = {}
        if action.execute_sudo:
            if action.sudo_id:
                action = action.sudo(action.sudo_id.id)
            else:
                action = action.sudo()

        for exp in action.fields_lines:
            res[exp.col1.name] = exp.eval_value(
                eval_context=eval_context
            )[exp.id]

        if self._context.get('onchange_self'):
            record_cached = self._context['onchange_self']
            for field, new_value in res.items():
                record_cached[field] = new_value
        else:
            record = self.env[action.model_id.model].browse(
                self._context.get('active_id')
            )

            if action.execute_silently:
                record._write(res)
            else:
                record.write(res)

    @api.model
    def run_action_object_create(self, action, eval_context=None):
        """ Create and Copy server action.

         - 1. evaluate the value mapping
         - 2. depending on the write configuration:

          - `new`: new record in the base model
          - `copy_current`: copy the current record (id = active_id)
                            + gives custom values
          - `new_other`: new record in target model
          - `copy_other`: copy the current record (id from reference object)
            + gives custom values
        """
        res = {}
        if action.execute_sudo:
            if action.sudo_id:
                action = action.sudo(action.sudo_id.id)
            else:
                action = action.sudo()

        for exp in action.fields_lines:
            res[exp.col1.name] = exp.eval_value(
                eval_context=eval_context
            )[exp.id]

        res = self.env[action.crud_model_id.model].create(res)

        if action.link_field_id:
            record = self.env[action.model_id.model].browse(
                self._context.get('active_id'))
            if action.execute_silently:
                record._write({action.link_field_id.name: res.id})
            else:
                record.write({action.link_field_id.name: res.id})
