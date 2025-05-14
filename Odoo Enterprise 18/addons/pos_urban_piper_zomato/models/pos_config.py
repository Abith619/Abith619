from odoo import models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    def _get_total_tax_tag(self):
        if self.company_id.country_id.code == 'IN':
            return 'total_excluded'
        return super()._get_total_tax_tag()

    def get_item_ref_id(self, product):
        return f'{product.id}-{self.env["ir.config_parameter"].sudo().get_param("database.uuid")[0:5]}'

    def prepare_taxes_data(self, pos_products):
        tax_lst = super().prepare_taxes_data(pos_products)
        if self.env.ref('pos_urban_piper_zomato.pos_delivery_provider_zomato', False) in self.urbanpiper_delivery_provider_ids:
            for tax in pos_products.taxes_id:
                if tax.type_tax_use == 'sale' and tax.tax_group_id.with_context(lang="en_US").name == 'GST':
                    product = pos_products.filtered(lambda p: tax.id in p.taxes_id.ids)
                    tax_lines = tax.flatten_taxes_hierarchy()
                    sgst_group = self.env['account.chart.template'].with_company(self.company_id).ref("sgst_group")
                    cgst_group = self.env['account.chart.template'].with_company(self.company_id).ref("cgst_group")
                    for tax in tax_lines:
                        if tax.tax_group_id in [sgst_group, cgst_group]:
                            tax_lst.append(
                                {
                                    'code': ('CGST' if tax.tax_group_id == cgst_group else 'SGST') + '_P',
                                    'title': 'CGST' if tax.tax_group_id == cgst_group else 'SGST',
                                    'description': f'{tax.amount}% {tax.tax_group_id.with_context(lang="en_US").name} on product price.',
                                    'active': True,
                                    'structure': {
                                        'value': tax.amount
                                    },
                                    'item_ref_ids': [self.get_item_ref_id(p) for p in product]
                                }
                            )
        return tax_lst

    def _add_line_to_fiscal_position(self, fiscal_position):
        super()._add_line_to_fiscal_position(fiscal_position)
        if self.company_id.country_code == 'IN':
            tax_line_to_remove = fiscal_position.tax_ids.filtered(lambda l: l.tax_src_id.amount != 5 or l.tax_src_id.tax_group_id.name != 'GST')
            fiscal_position.tax_ids -= tax_line_to_remove
