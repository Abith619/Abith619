import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class SaleOrderLeadAttach(models.Model):
    _inherit = 'sale.order'

    lead_id = fields.Many2one('crm.lead', string="CRM Lead")

    def action_confirm(self):
        res = super(SaleOrderLeadAttach, self).action_confirm()

        for order in self:
            partner_email = (order.partner_id.email or "").strip().lower()
            lead_email = (order.lead_id.email_from or "").strip().lower()

            if order.lead_id and partner_email == lead_email and order.lead_id.stage_id.name == 'New':
                order.lead_id.sudo().write({'payment_status': 'paid'})
                _logger.info("LEAD %s PAYMENT STATUS updated to PAID from Sale Order %s",order.lead_id.id, order.name)
        
            if order.lead_id and order.lead_id.stage_id.name == 'Approved':
                lead_course_product = order.lead_id.course_id.product_id.product_tmpl_id
                order_products = order.order_line.product_id.product_tmpl_id

                if lead_course_product == order_products:
                    won_stage = self.env['crm.stage'].search(
                        [('name', '=', 'Won')], limit=1
                    )
                    if won_stage:
                        order.lead_id.sudo().write({'stage_id': won_stage.id})
                        _logger.info(
                            "LEAD %s Stage moved to WON from Sale Order %s",
                            order.lead_id.id, order.name
                        )

        return res

        