from odoo import models, fields


class MrpProduction(models.Model):
    _inherit = 'mrp.production'
    sale_order_id = fields.Many2one('sale.order',string="Sale Order",ondelete='cascade')
    customer_po_reference = fields.Char(string="Customer PO Reference", related='sale_order_id.customer_po_reference')
    material_request_id = fields.Many2one("material.request",string="Material Request")
    material_request_count = fields.Integer(string="Material Requests", compute="_compute_material_request_count")
    def _compute_material_request_count(self):
        for rec in self:
            rec.material_request_count = self.env['material.request'].search_count([
                ('mo_id', '=', rec.id)
            ])

    def action_view_material_requests(self):
        self.ensure_one()
        material_requests = self.env['material.request'].search([
            ('mo_id', '=', self.id)
        ])
        if len(material_requests) == 1:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Material Request',
                'res_model': 'material.request',
                'view_mode': 'form',
                'res_id': material_requests.id,
            }
        return {
            'type': 'ir.actions.act_window',
            'name': 'Material Requests',
            'res_model': 'material.request',
            'view_mode': 'list,form',
            'domain': [('mo_id', '=', self.id)],
        }

    def action_confirm(self):
        res = super().action_confirm()

        for production in self:

            if production.material_request_id:
                continue

            analytic_acc_id = False
            if hasattr(production, 'analytic_account_id') and production.analytic_account_id:
                analytic_acc_id = production.analytic_account_id.id
            elif production.sale_order_id and hasattr(production.sale_order_id, 'analytic_account_id') and production.sale_order_id.analytic_account_id:
                analytic_acc_id = production.sale_order_id.analytic_account_id.id
            else:
                acc = self.env['account.analytic.account'].search([], limit=1)
                analytic_acc_id = acc.id if acc else False

            material_request = self.env['material.request'].create({
                "requester_id": self.env.user.id,
                "sale_order_id": production.sale_order_id.id,
                "mo_id": production.id,
                "source_location_id": production.location_src_id.id,
                "destination_location_id": production.location_dest_id.id,
                "product_id": production.product_id.id,
                "expected_date": getattr(production, 'date_start', fields.Datetime.now()) or fields.Datetime.now(),
                "analytic_account_id": analytic_acc_id,
            })

        
            for move in production.move_raw_ids:
                mfg_ids_val = False
                part_ids_val = False
                if move.product_id.manufacturer_line_ids:
                    mfg_ids_val = move.product_id.manufacturer_line_ids[0].manufacturer_id.id
                    part_ids_val = move.product_id.manufacturer_line_ids[0].id

                self.env['material.request.line'].create({
                    "request_id": material_request.id,
                    "product_id": move.product_id.id,
                    "description": move.product_id.display_name,
                    "requested_qty": move.product_uom_qty,
                    "uom_id": move.product_uom.id,
                    "destination_location_id": production.location_dest_id.id,
                    "manufacturer_ids": mfg_ids_val,
                    "manufacturer_part_number_ids": part_ids_val,
                })

            production.material_request_id = material_request.id

        return res