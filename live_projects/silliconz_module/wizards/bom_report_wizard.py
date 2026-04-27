import io
import base64
from odoo import models, fields, _
from odoo.exceptions import UserError

try:
    import xlsxwriter
except ImportError:
    xlsxwriter = None


class BomConsolidatedReportWizard(models.TransientModel):
    _name = 'bom.consolidated.report.wizard'
    _description = 'All-FG BOM Consolidated Report Wizard'

    product_ids = fields.Many2many(
        'product.product',
        string='Finished Products',
        domain=[('bom_ids', '!=', False)],
        help='Select finished goods. Leave empty to include all FGs with an active BOM.',
    )
    warehouse_id = fields.Many2one(
        'stock.warehouse',
        string='Warehouse',
        default=lambda self: self.env['stock.warehouse'].search([], limit=1),
    )
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    mo_state = fields.Selection(
        [
            ('draft_confirmed', 'Draft & Confirmed'),
            ('draft', 'Draft Only'),
            ('confirmed', 'Confirmed Only'),
            ('all_bom', 'All Active BOMs (No MO Filter)'),
        ],
        string='MO / BOM Source',
        default='draft_confirmed',
    )

    # ─── Helpers ─────────────────────────────────────────────────────────────

    def _get_component_stock(self, product, warehouse):
        location = (
            warehouse.lot_stock_id
            if warehouse
            else self.env['stock.location'].search([('usage', '=', 'internal')], limit=1)
        )
        quants = self.env['stock.quant'].search([
            ('product_id', '=', product.id),
            ('location_id', '=', location.id),
        ])
        available_qty = sum(quants.mapped('quantity'))
        reserved_qty = sum(quants.mapped('reserved_quantity'))
        free_qty = max(available_qty - reserved_qty, 0)
        return available_qty, free_qty

    def _get_fg_available(self, product, warehouse):
        location = (
            warehouse.lot_stock_id
            if warehouse
            else self.env['stock.location'].search([('usage', '=', 'internal')], limit=1)
        )
        quants = self.env['stock.quant'].search([
            ('product_id', '=', product.id),
            ('location_id', '=', location.id),
        ])
        available = sum(quants.mapped('quantity')) - sum(quants.mapped('reserved_quantity'))
        return max(available, 0)

    def _get_manufacturer_info(self, product):
        mfr_infos = self.env['product.manufacturer.info'].search([
            ('product_tmpl_id', '=', product.product_tmpl_id.id)
        ])
        manufacturer = ', '.join(
            m.manufacturer_id.manufacturer for m in mfr_infos if m.manufacturer_id
        )
        part_no = ', '.join(
            m.part_number for m in mfr_infos if m.part_number
        )
        return manufacturer, part_no

    # ─── Core Data ───────────────────────────────────────────────────────────

    def _compute_bom_data(self):
        """
        Returns list of FG-level dicts with full BOM breakdown:
        {
            fg_code, fg_name, bom_name, bom_qty, bom_uom,
            fg_available, fg_cost,
            components: [
                {sno, component_code, description, uom, qpu,
                 available_qty, free_qty, shortage_qty,
                 unit_cost, total_cost,
                 manufacturer, part_no}
            ],
            total_components, total_component_cost, total_shortage_lines
        }
        """
        warehouse = self.warehouse_id

        # ── Source BOMs ──
        if self.mo_state == 'all_bom':
            # Directly from mrp.bom, ignoring MOs
            bom_domain = [('active', '=', True)]
            if self.product_ids:
                product_tmpl_ids = self.product_ids.mapped('product_tmpl_id').ids
                bom_domain += [('product_tmpl_id', 'in', product_tmpl_ids)]
            boms = self.env['mrp.bom'].search(bom_domain)
            if not boms:
                raise UserError(_('No active BOMs found for the selected criteria.'))

            fg_list = []
            for bom in boms:
                product = bom.product_id or bom.product_tmpl_id.product_variant_id
                fg_list.append({
                    'product': product,
                    'bom': bom,
                    'demand_qty': bom.product_qty,
                })
        else:
            # Via MOs (same logic as ATP wizard)
            mo_domain = []
            if self.mo_state == 'draft_confirmed':
                mo_domain += [('state', 'in', ['draft', 'confirmed'])]
            elif self.mo_state == 'draft':
                mo_domain += [('state', '=', 'draft')]
            else:
                mo_domain += [('state', '=', 'confirmed')]

            if self.product_ids:
                mo_domain += [('product_id', 'in', self.product_ids.ids)]
            if self.date_from:
                mo_domain += [('date_start', '>=', self.date_from)]
            if self.date_to:
                mo_domain += [('date_start', '<=', self.date_to)]

            mos = self.env['mrp.production'].search(mo_domain, order='product_id, id')
            if not mos:
                raise UserError(_('No Manufacturing Orders found for the selected criteria.'))

            fg_map = {}
            for mo in mos:
                pid = mo.product_id.id
                if pid not in fg_map:
                    fg_map[pid] = {
                        'product': mo.product_id,
                        'bom': mo.bom_id,
                        'demand_qty': 0.0,
                    }
                fg_map[pid]['demand_qty'] += mo.product_qty
                if not fg_map[pid]['bom'] and mo.bom_id:
                    fg_map[pid]['bom'] = mo.bom_id

            fg_list = list(fg_map.values())

        # ── Build Result ──
        result = []
        for data in fg_list:
            product = data['product']
            bom = data['bom']
            demand_qty = data['demand_qty']

            if not bom:
                continue

            fg_available = self._get_fg_available(product, warehouse)
            fg_cost = product.standard_price or 0.0

            components = []
            total_component_cost = 0.0
            total_shortage_lines = 0
            sno = 1

            for line in bom.bom_line_ids:
                comp = line.product_id
                qpu = line.product_qty / (bom.product_qty or 1.0)
                required_qty = qpu * demand_qty
                available_qty, free_qty = self._get_component_stock(comp, warehouse)
                shortage_qty = max(required_qty - free_qty, 0)

                unit_cost = comp.standard_price or 0.0
                total_cost = unit_cost * required_qty
                total_component_cost += total_cost

                if shortage_qty > 0:
                    total_shortage_lines += 1

                manufacturer, part_no = self._get_manufacturer_info(comp)

                components.append({
                    'sno': sno,
                    'component_code': comp.default_code or comp.name,
                    'description': comp.name,
                    'uom': comp.uom_id.name,
                    'qpu': qpu,
                    'required_qty': required_qty,
                    'available_qty': available_qty,
                    'free_qty': free_qty,
                    'shortage_qty': shortage_qty,
                    'unit_cost': unit_cost,
                    'total_cost': total_cost,
                    'manufacturer': manufacturer,
                    'part_no': part_no,
                })
                sno += 1

            result.append({
                'fg_code': product.default_code or product.name,
                'fg_name': product.name,
                'bom_name': bom.code or bom.product_tmpl_id.name or 'BOM',
                'bom_qty': bom.product_qty,
                'bom_uom': bom.product_uom_id.name,
                'demand_qty': demand_qty,
                'fg_available': fg_available,
                'fg_cost': fg_cost,
                'components': components,
                'total_components': len(components),
                'total_component_cost': total_component_cost,
                'total_shortage_lines': total_shortage_lines,
            })

        if not result:
            raise UserError(_('No BOM data found for the selected criteria.'))

        return result

    # ─── PDF ─────────────────────────────────────────────────────────────────

    def action_print_bom_pdf(self):
        bom_data = self._compute_bom_data()
        mo_state_labels = dict(self._fields['mo_state'].selection)
        data = {
            'wizard_id': self.id,
            'warehouse': self.warehouse_id.name or 'All Warehouses',
            'mo_state_label': mo_state_labels.get(self.mo_state, ''),
            'report_date': fields.Date.today().strftime('%d-%m-%Y'),
            'bom_data': bom_data,
            'currency_symbol': self.env.company.currency_id.symbol or '',
        }
        return self.env.ref('silliconz_module.action_bom_report_pdf').report_action(self, data=data)

    # ─── Excel ───────────────────────────────────────────────────────────────

    def action_print_bom_xlsx(self):
        if not xlsxwriter:
            raise UserError(_('xlsxwriter library is required. Install it via: pip install xlsxwriter'))

        bom_data = self._compute_bom_data()
        currency_symbol = self.env.company.currency_id.symbol or ''
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})

        # ── Formats ──
        fmt_title = workbook.add_format({
            'bold': True, 'font_size': 14, 'font_color': '#FFFFFF',
            'bg_color': '#1B3A5C', 'align': 'center', 'valign': 'vcenter', 'border': 1,
        })
        fmt_meta_label = workbook.add_format({
            'bold': True, 'font_size': 9, 'bg_color': '#D6E4F0', 'border': 1,
        })
        fmt_meta_val = workbook.add_format({
            'font_size': 9, 'bg_color': '#EBF5FB', 'border': 1,
        })
        fmt_fg_header = workbook.add_format({
            'bold': True, 'font_size': 11, 'font_color': '#FFFFFF',
            'bg_color': '#2E75B6', 'border': 1,
        })
        fmt_kpi_label = workbook.add_format({
            'bold': True, 'font_size': 8, 'bg_color': '#D6E4F0',
            'border': 1, 'align': 'center',
        })
        fmt_kpi_val = workbook.add_format({
            'font_size': 10, 'bold': True, 'bg_color': '#EBF5FB',
            'border': 1, 'align': 'center', 'num_format': '#,##0.00',
        })
        fmt_kpi_val_int = workbook.add_format({
            'font_size': 10, 'bold': True, 'bg_color': '#EBF5FB',
            'border': 1, 'align': 'center',
        })
        fmt_col_header = workbook.add_format({
            'bold': True, 'font_size': 8, 'font_color': '#FFFFFF',
            'bg_color': '#1B3A5C', 'border': 1, 'align': 'center',
            'valign': 'vcenter', 'text_wrap': True,
        })
        fmt_cell = workbook.add_format({'font_size': 8, 'border': 1, 'valign': 'vcenter'})
        fmt_cell_center = workbook.add_format({
            'font_size': 8, 'border': 1, 'align': 'center', 'valign': 'vcenter',
        })
        fmt_cell_num = workbook.add_format({
            'font_size': 8, 'border': 1, 'align': 'center', 'num_format': '#,##0.000',
        })
        fmt_cell_qty = workbook.add_format({
            'font_size': 8, 'border': 1, 'align': 'center', 'num_format': '#,##0.00',
        })
        fmt_cell_cost = workbook.add_format({
            'font_size': 8, 'border': 1, 'align': 'right',
            'num_format': f'#,##0.00',
        })
        fmt_shortage = workbook.add_format({
            'font_size': 8, 'border': 1, 'align': 'center',
            'bg_color': '#FDECEA', 'font_color': '#C0392B',
            'num_format': '#,##0.00', 'bold': True,
        })
        fmt_ok = workbook.add_format({
            'font_size': 8, 'border': 1, 'align': 'center',
            'bg_color': '#E9F7EF', 'font_color': '#1E8449',
            'num_format': '#,##0.00',
        })
        fmt_total = workbook.add_format({
            'bold': True, 'font_size': 8, 'bg_color': '#D6E4F0',
            'border': 1, 'align': 'right',
        })
        fmt_total_num = workbook.add_format({
            'bold': True, 'font_size': 8, 'bg_color': '#D6E4F0',
            'border': 1, 'align': 'center', 'num_format': '#,##0.00',
        })
        fmt_total_cost = workbook.add_format({
            'bold': True, 'font_size': 8, 'bg_color': '#D6E4F0',
            'border': 1, 'align': 'right', 'num_format': '#,##0.00',
        })

        ws = workbook.add_worksheet('BOM Consolidated Report')
        ws.set_zoom(85)
        ws.freeze_panes(1, 0)

        # Column widths: S.No | Code | Description | UoM | QPU | Req Qty | Avail | Free | Shortage | Unit Cost | Total Cost | Manufacturer | Part No
        col_widths = [5, 14, 28, 7, 8, 10, 10, 10, 10, 12, 13, 20, 16]
        for i, w in enumerate(col_widths):
            ws.set_column(i, i, w)

        LAST_COL = 12  # 0-indexed, 13 columns total

        row = 0

        # ── Title ──
        ws.merge_range(row, 0, row, LAST_COL,
                       'All-FG BOM Consolidated Report', fmt_title)
        ws.set_row(row, 28)
        row += 1

        # ── Meta ──
        mo_state_labels = dict(self._fields['mo_state'].selection)
        meta = [
            ('Warehouse', self.warehouse_id.name or 'All Warehouses'),
            ('MO / BOM Source', mo_state_labels.get(self.mo_state, '')),
            ('Generated By', self.env.user.name),
            ('Date', fields.Date.today().strftime('%d-%m-%Y')),
        ]
        for label, val in meta:
            ws.write(row, 0, label, fmt_meta_label)
            ws.merge_range(row, 1, row, LAST_COL, val, fmt_meta_val)
            row += 1
        row += 1

        col_headers = [
            'S.No', 'Component\nCode', 'Description', 'UoM', 'QPU',
            'Required\nQty', 'Available\nQty', 'Free\nQty',
            'Shortage\nQty', f'Unit Cost\n({currency_symbol})',
            f'Total Cost\n({currency_symbol})',
            'Manufacturer', 'Part No.',
        ]

        for fg in bom_data:
            # ── FG Header ──
            ws.merge_range(row, 0, row, LAST_COL,
                f"FG: {fg['fg_code']}  |  {fg['fg_name']}  |  BOM: {fg['bom_name']}  |  BOM Qty: {fg['bom_qty']} {fg['bom_uom']}",
                fmt_fg_header)
            ws.set_row(row, 18)
            row += 1

            # ── KPI Row Labels ──
            kpi_labels = ['Demand Qty', 'FG Available', 'FG Std Cost', 'Components', 'Shortage Lines', 'Total BOM Cost']
            kpi_vals = [
                (fg['demand_qty'], fmt_kpi_val),
                (fg['fg_available'], fmt_kpi_val),
                (fg['fg_cost'], fmt_kpi_val),
                (fg['total_components'], fmt_kpi_val_int),
                (fg['total_shortage_lines'], fmt_kpi_val_int),
                (fg['total_component_cost'], fmt_kpi_val),
            ]
            # Labels row
            col_span = LAST_COL / len(kpi_labels)
            positions = [0, 2, 4, 7, 9, 11]
            spans =     [1, 1, 2, 1, 1,  1]
            for i, (lbl, pos, span) in enumerate(zip(kpi_labels, positions, spans)):
                if span > 0:
                    ws.merge_range(row, pos, row, pos + span, lbl, fmt_kpi_label)
                else:
                    ws.write(row, pos, lbl, fmt_kpi_label)
            row += 1
            for i, ((val, fmt), pos, span) in enumerate(zip(kpi_vals, positions, spans)):
                if span > 0:
                    ws.merge_range(row, pos, row, pos + span, val, fmt)
                else:
                    ws.write(row, pos, val, fmt)
            row += 1

            # ── Column Headers ──
            ws.set_row(row, 30)
            for ci, h in enumerate(col_headers):
                ws.write(row, ci, h, fmt_col_header)
            row += 1

            # ── Component Rows ──
            for comp in fg['components']:
                ws.write(row, 0, comp['sno'], fmt_cell_center)
                ws.write(row, 1, comp['component_code'], fmt_cell)
                ws.write(row, 2, comp['description'], fmt_cell)
                ws.write(row, 3, comp['uom'], fmt_cell_center)
                ws.write(row, 4, comp['qpu'], fmt_cell_num)
                ws.write(row, 5, comp['required_qty'], fmt_cell_qty)
                ws.write(row, 6, comp['available_qty'], fmt_cell_qty)
                ws.write(row, 7, comp['free_qty'], fmt_cell_qty)
                ws.write(row, 8, comp['shortage_qty'],
                         fmt_shortage if comp['shortage_qty'] > 0 else fmt_ok)
                ws.write(row, 9, comp['unit_cost'], fmt_cell_cost)
                ws.write(row, 10, comp['total_cost'], fmt_cell_cost)
                ws.write(row, 11, comp['manufacturer'], fmt_cell)
                ws.write(row, 12, comp['part_no'], fmt_cell)
                row += 1

            # ── Totals Row ──
            ws.merge_range(row, 0, row, 8,
                f"Total Components: {fg['total_components']}  |  Shortage Lines: {fg['total_shortage_lines']}",
                fmt_total)
            ws.merge_range(row, 9, row, 10, fg['total_component_cost'], fmt_total_cost)
            ws.merge_range(row, 11, row, LAST_COL, '', fmt_total)
            row += 2  # spacer

        workbook.close()
        output.seek(0)
        file_data = base64.b64encode(output.read())

        attachment = self.env['ir.attachment'].create({
            'name': 'BOM_Consolidated_Report.xlsx',
            'type': 'binary',
            'datas': file_data,
            'res_model': self._name,
            'res_id': self.id,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        })
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'self',
        }