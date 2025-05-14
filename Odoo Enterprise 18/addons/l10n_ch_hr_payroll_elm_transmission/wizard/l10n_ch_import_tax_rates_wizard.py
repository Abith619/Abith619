# -*- coding: utf-8 -*-
import base64
import logging
import requests
import zipfile
import io

from odoo import api, fields, models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class L10nChTaxRateImportWizardInherit(models.TransientModel):
    _inherit = 'l10n.ch.tax.rate.import.wizard'
    _description = 'Swiss Payroll: Extended tax rate import wizard (website download)'

    import_mode = fields.Selection(selection=[('manual', 'Manual File Import'),
                                              ('automatic', 'Automatic Import')], required=True, default='automatic')

    canton_mode = fields.Selection([
        ('all', 'Import every canton'),
        ('single', 'Import one canton'),
    ], string='Canton Importation',
       default='all',
       required=True,
       help="Select whether to import tax rates for all cantons at once, or for a single canton.")
    canton = fields.Selection([
        ('AG', 'AG'), ('AI', 'AI'), ('AR', 'AR'), ('BE', 'BE'), ('BL', 'BL'), ('BS', 'BS'),
        ('FR', 'FR'), ('GE', 'GE'), ('GL', 'GL'), ('GR', 'GR'), ('JU', 'JU'), ('LU', 'LU'),
        ('NE', 'NE'), ('NW', 'NW'), ('OW', 'OW'), ('SG', 'SG'), ('SH', 'SH'), ('SO', 'SO'),
        ('SZ', 'SZ'), ('TG', 'TG'), ('TI', 'TI'), ('UR', 'UR'), ('VD', 'VD'), ('VS', 'VS'),
        ('ZG', 'ZG'), ('ZH', 'ZH'),
    ], string='Canton',
       default='GE',
       help="Canton for which to download the official tax file (only relevant if you choose 'Import one canton').")
    year = fields.Integer(
        string='Tax Year',
        default=lambda self: fields.Date.today().year,
        required=True,
        help='Year for which to download the tax rate file'
    )

    def action_import_from_website(self):
        """
        1. Build the URL based on whether we want a single canton or all cantons.
        2. Download the ZIP from ESTV.
        3. Extract all .txt files inside it, attach them to this wizard record.
        4. Call the original `action_import_file()` to parse + import as usual.
        """
        self.ensure_one()
        url = self._build_estv_download_url()
        _logger.info("Downloading Swiss tax ZIP from %s", url)

        # 2) Download the ZIP
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
        except Exception as e:
            raise UserError(_("Could not download file from URL"))

        zip_bytes = io.BytesIO(response.content)
        try:
            with zipfile.ZipFile(zip_bytes, 'r') as z:
                for file_name in z.namelist():
                    if file_name.lower().endswith('.txt'):
                        txt_bytes = z.read(file_name)
                        self.env['ir.attachment'].create({
                            'name': file_name,
                            'res_model': self._name,
                            'res_id': self.id,
                            'datas': base64.b64encode(txt_bytes),
                            'mimetype': 'text/plain',
                        })
                        _logger.info("Attached file %s to wizard", file_name)
        except zipfile.BadZipFile:
            raise UserError(_("Downloaded file is not a valid ZIP or is corrupted."))

        return self.action_import_file()

    def _build_estv_download_url(self):
        """
        Return the official ESTV URL based on year + whether we want all or single canton.
        """
        year_str = str(self.year)
        short_year_str = year_str[-2:]
        canton_lower = (self.canton or '').lower()

        if self.canton_mode == 'all':
            # e.g. 2025 =>
            # https://www.estv.admin.ch/dam/estv/fr/dokumente/qst/schweiz/qst-ch-tar2025txt-fr.zip.download.zip/qst-ch-tar2025txt-fr.zip
            url = (
                "https://www.estv.admin.ch/dam/estv/fr/dokumente/qst/schweiz/"
                "qst-ch-tar{year_str}txt-fr.zip.download.zip/qst-ch-tar{year_str}txt-fr.zip"
            ).format(year_str=year_str)
        else:
            # Single canton approach
            # https://www.estv.admin.ch/dam/estv/fr/dokumente/qst/2025/qst-loehne/qst-tar25ar-fr.zip.download.zip/qst-tar25ar-fr.zip
            url = (
                "https://www.estv.admin.ch/dam/estv/fr/dokumente/qst/{year_str}/qst-loehne/"
                "qst-tar{short_year_str}{canton_lower}-fr.zip.download.zip/"
                "qst-tar{short_year_str}{canton_lower}-fr.zip"
            ).format(
                year_str=year_str,
                short_year_str=short_year_str,
                canton_lower=canton_lower
            )
        return url
