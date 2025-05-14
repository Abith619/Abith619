# -*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class L10nChWorkLocation(models.Model):
    _inherit = 'l10n.ch.location.unit'

    active = fields.Boolean(default=True)
    in_house_id = fields.Char(string="InHouseID")
    bur_ree_number = fields.Char(required=False)
    dpi_number = fields.Char(required=False)
    canton = fields.Selection(required=False)
    municipality = fields.Char(required=False)
