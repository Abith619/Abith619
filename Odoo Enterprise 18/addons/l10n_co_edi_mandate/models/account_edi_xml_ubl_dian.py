from odoo import models


class AccountEdiXmlUBLDianMandate(models.AbstractModel):
    _inherit = 'account.edi.xml.ubl_dian'
    _description = "UBL DIAN Mandate extension"

    def _get_invoice_line_item_vals(self, line, taxes_vals):
        vals = super()._get_invoice_line_item_vals(line, taxes_vals)
        if line.product_id.l10n_co_dian_mandate_contract:
            scheme_name_mp = line.move_id.l10n_co_dian_mandate_principal._l10n_co_edi_get_carvajal_code_for_identification_type()
            vals['l10n_co_edi_mandate_vals'] = {
                'id_attrs': {
                    'schemeAgencyID': '195',
                    'schemeAgencyName': "CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)",
                    'schemeID': line.move_id.l10n_co_dian_mandate_principal._get_vat_verification_code() if scheme_name_mp == '31' else False,
                    'schemeName': scheme_name_mp,
                },
                'id_out': line.move_id.l10n_co_dian_mandate_principal._get_vat_without_verification_code(),
            }
        return vals

    def _get_invoice_line_vals(self, line, line_id, taxes_vals):
        vals = super()._get_invoice_line_vals(line, line_id, taxes_vals)
        if line.move_id.l10n_co_edi_operation_type == '11':
            vals['id_attrs'] = {'schemeID': '1' if line.product_id.l10n_co_dian_mandate_contract else '0'}
        return vals
