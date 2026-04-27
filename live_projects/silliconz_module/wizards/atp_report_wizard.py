import io
import base64
from odoo import models, fields, _
from odoo.exceptions import UserError

try:
    import xlsxwriter
except ImportError:
    xlsxwriter = None


class AtpReportWizard(models.TransientModel):
    _name = 'atp.report.wizard'
    _description = 'Available-To-Promise Report Wizard'

    product_ids = fields.Many2many(
        'product.product',
        string='Finished Products',
        domain=[('bom_ids', '!=', False)],
        help='Select finished goods to include in ATP report. Leave empty to include all FG with active MOs.',
    )
    warehouse_id = fields.Many2one(
        'stock.warehouse',
        string='Warehouse',
        default=lambda self: self.env['stock.warehouse'].search([], limit=1),
    )
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    mo_state = fields.Selection(
        [('draft_confirmed', 'Draft & Confirmed'), ('draft', 'Draft Only'), ('confirmed', 'Confirmed Only')],
        string='MO Status',
        default='draft_confirmed',
    )

    # ─── Core Data Computation ────────────────────────────────────────────────

    def _get_manufacturing_orders(self):
        """Fetch MOs based on wizard filters."""
        domain = []

        if self.mo_state == 'draft_confirmed':
            domain += [('state', 'in', ['draft', 'confirmed'])]
        elif self.mo_state == 'draft':
            domain += [('state', '=', 'draft')]
        else:
            domain += [('state', '=', 'confirmed')]

        if self.product_ids:
            domain += [('product_id', 'in', self.product_ids.ids)]

        # if self.warehouse_id:
        #     domain += [('picking_type_id.warehouse_id', '=', self.warehouse_id.id)]

        if self.date_from:
            domain += [('date_start', '>=', self.date_from)]

        if self.date_to:
            domain += [('date_start', '<=', self.date_to)]

        mos = self.env['mrp.production'].search(domain, order='product_id, id')
        if not mos:
            raise UserError(_('No Manufacturing Orders found for the selected criteria.'))
        return mos

    def _get_component_stock(self, product, warehouse):
        """Return available qty and free (unreserved) qty for a component."""
        location = warehouse.lot_stock_id if warehouse else self.env['stock.location'].search(
            [('usage', '=', 'internal')], limit=1
        )
        quants = self.env['stock.quant'].search([
            ('product_id', '=', product.id),
            ('location_id', '=', location.id),
        ])
        available_qty = sum(quants.mapped('quantity'))
        reserved_qty = sum(quants.mapped('reserved_quantity'))
        free_qty = available_qty - reserved_qty
        return available_qty, max(free_qty, 0)

    def _get_fg_available(self, product, warehouse):
        """Return available stock of the finished good."""
        location = warehouse.lot_stock_id if warehouse else self.env['stock.location'].search(
            [('usage', '=', 'internal')], limit=1
        )
        quants = self.env['stock.quant'].search([
            ('product_id', '=', product.id),
            ('location_id', '=', location.id),
        ])
        available = sum(quants.mapped('quantity')) - sum(quants.mapped('reserved_quantity'))
        return max(available, 0)

    def _compute_atp_data(self):
        """
        Returns a list of FG-level dicts:
        {
            fg_code, fg_name, bom_name, demand_qty, fg_available, atp_qty,
            components: [
                {sno, component_code, description, uom, qpu, required_qty,
                 available_qty, free_qty, shortage_qty, manufacturer, part_no}
            ],
            total_components, total_shortage
        }
        """
        mos = self._get_manufacturing_orders()
        warehouse = self.warehouse_id

        # Group MOs by product → aggregate demand
        fg_map = {}
        for mo in mos:
            pid = mo.product_id.id
            if pid not in fg_map:
                fg_map[pid] = {
                    'product': mo.product_id,
                    'bom': mo.bom_id,
                    'demand_qty': 0.0,
                    'mo_records': self.env['mrp.production'],
                }
            fg_map[pid]['demand_qty'] += mo.product_qty
            fg_map[pid]['mo_records'] |= mo
            # prefer a bom that is set
            if not fg_map[pid]['bom'] and mo.bom_id:
                fg_map[pid]['bom'] = mo.bom_id

        result = []
        for pid, data in fg_map.items():
            product = data['product']
            bom = data['bom']
            demand_qty = data['demand_qty']

            fg_available = self._get_fg_available(product, warehouse)
            atp_qty = min(fg_available, demand_qty)

            components = []
            total_shortage = 0.0
            sno = 1

            # Gather components from BOM lines
            if bom:
                bom_lines = bom.bom_line_ids
            else:
                # Fallback: aggregate move_raw lines from all MOs
                bom_lines = self.env['mrp.bom.line']
                # We will handle separately below if no BOM

            if bom and bom_lines:
                for line in bom_lines:
                    comp = line.product_id
                    # QPU = qty per unit (bom qty is for bom_qty FG, normalise to 1)
                    qpu = line.product_qty / (bom.product_qty or 1.0)
                    required_qty = qpu * demand_qty
                    available_qty, free_qty = self._get_component_stock(comp, warehouse)
                    shortage_qty = max(required_qty - free_qty, 0)
                    total_shortage += shortage_qty

                    # manufacturer info
                    mfr_info = self.env['product.manufacturer.info'].search([
                        ('product_tmpl_id', '=', comp.product_tmpl_id.id)
                    ], limit=1)
                    manufacturer = mfr_info.manufacturer_id.manufacturer if mfr_info else ''
                    part_no = mfr_info.part_number if mfr_info else ''

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
                        'manufacturer': manufacturer,
                        'part_no': part_no,
                    })
                    sno += 1
            else:
                # No BOM → aggregate raw move lines from MOs
                for mo in data['mo_records']:
                    for move in mo.move_raw_ids.filtered(lambda m: m.state not in ['cancel', 'done']):
                        comp = move.product_id
                        required_qty = move.product_uom_qty
                        available_qty, free_qty = self._get_component_stock(comp, warehouse)
                        shortage_qty = max(required_qty - free_qty, 0)
                        total_shortage += shortage_qty

                        # manufacturer info
                        mfr_info = self.env['product.manufacturer.info'].search([
                            ('product_tmpl_id', '=', comp.product_tmpl_id.id)
                        ], limit=1)
                        manufacturer = mfr_info.manufacturer_id.manufacturer if mfr_info else ''
                        part_no = mfr_info.part_number if mfr_info else ''

                        components.append({
                            'sno': sno,
                            'component_code': comp.default_code or comp.name,
                            'description': comp.name,
                            'uom': comp.uom_id.name,
                            'qpu': required_qty / (demand_qty or 1),
                            'required_qty': required_qty,
                            'available_qty': available_qty,
                            'free_qty': free_qty,
                            'shortage_qty': shortage_qty,
                            'manufacturer': manufacturer,
                            'part_no': part_no,
                        })
                        sno += 1

            result.append({
                'fg_code': product.default_code or product.name,
                'fg_name': product.name,
                'bom_name': (bom.code or bom.product_tmpl_id.name or 'BOM') if bom else 'N/A',
                'demand_qty': demand_qty,
                'fg_available': fg_available,
                'atp_qty': atp_qty,
                'components': components,
                'total_components': len(components),
                'total_shortage': total_shortage,
            })

        return result

    # ─── PDF Report ───────────────────────────────────────────────────────────

    def action_print_pdf(self):
        data = {
            'wizard_id': self.id,
            'warehouse': self.warehouse_id.name or 'All Warehouses',
            'mo_state': self.mo_state,
            'atp_data': self._compute_atp_data(),
        }
        return self.env.ref('silliconz_module.action_atp_report_pdf').report_action(self, data=data)

    # ─── Excel Report ─────────────────────────────────────────────────────────

    def action_print_xlsx(self):
        if not xlsxwriter:
            raise UserError(_('xlsxwriter library is required. Please install it: pip install xlsxwriter'))

        atp_data = self._compute_atp_data()
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})

        # ── Formats ──
        fmt_title = workbook.add_format({
            'bold': True, 'font_size': 14, 'font_color': '#FFFFFF',
            'bg_color': '#1F3864', 'align': 'center', 'valign': 'vcenter',
            'border': 1,
        })
        fmt_header_meta = workbook.add_format({
            'bold': True, 'font_size': 10, 'bg_color': '#D6E4F0',
            'border': 1, 'valign': 'vcenter',
        })
        fmt_meta_val = workbook.add_format({
            'font_size': 10, 'bg_color': '#EBF5FB', 'border': 1,
        })
        fmt_fg_header = workbook.add_format({
            'bold': True, 'font_size': 11, 'font_color': '#FFFFFF',
            'bg_color': '#2E75B6', 'border': 1, 'align': 'center',
        })
        fmt_col_header = workbook.add_format({
            'bold': True, 'font_size': 9, 'font_color': '#FFFFFF',
            'bg_color': '#1F3864', 'border': 1, 'align': 'center',
            'valign': 'vcenter', 'text_wrap': True,
        })
        fmt_cell = workbook.add_format({
            'font_size': 9, 'border': 1, 'valign': 'vcenter',
        })
        fmt_cell_center = workbook.add_format({
            'font_size': 9, 'border': 1, 'align': 'center', 'valign': 'vcenter',
        })
        fmt_cell_num = workbook.add_format({
            'font_size': 9, 'border': 1, 'align': 'center',
            'num_format': '#,##0.##',
        })
        fmt_shortage = workbook.add_format({
            'font_size': 9, 'border': 1, 'align': 'center',
            'bg_color': '#FDECEA', 'font_color': '#C0392B',
            'num_format': '#,##0.##', 'bold': True,
        })
        fmt_ok = workbook.add_format({
            'font_size': 9, 'border': 1, 'align': 'center',
            'bg_color': '#E9F7EF', 'font_color': '#1E8449',
            'num_format': '#,##0.##',
        })
        fmt_total = workbook.add_format({
            'bold': True, 'font_size': 9, 'bg_color': '#EBF5FB',
            'border': 1, 'align': 'right',
        })
        fmt_total_val = workbook.add_format({
            'bold': True, 'font_size': 9, 'bg_color': '#EBF5FB',
            'border': 1, 'align': 'center', 'num_format': '#,##0.##',
        })

        ws = workbook.add_worksheet('ATP Report')
        ws.set_zoom(85)

        # Column widths
        col_widths = [6, 14, 28, 7, 7, 12, 12, 12, 12, 20, 16]
        for i, w in enumerate(col_widths):
            ws.set_column(i, i, w)

        row = 0

        # ── Report Title ──
        ws.merge_range(row, 0, row, 10, 'Available-To-Promise (ATP) Report', fmt_title)
        ws.set_row(row, 28)
        row += 1

        # ── Meta info ──
        meta = [
            ('Warehouse', self.warehouse_id.name or 'All'),
            ('MO Status', dict(self._fields['mo_state'].selection).get(self.mo_state, '')),
            ('Generated By', self.env.user.name),
            ('Date', fields.Date.today().strftime('%d-%m-%Y')),
        ]
        for label, val in meta:
            ws.write(row, 0, label, fmt_header_meta)
            ws.merge_range(row, 1, row, 3, val, fmt_meta_val)
            row += 1
        row += 1

        col_headers = [
            'S.No', 'Component\nCode', 'Description', 'UoM', 'QPU',
            'Required\nQty', 'Available\nQty', 'Free\nQty',
            'Shortage\nQty', 'Manufacturer', 'Part No.',
        ]

        for fg in atp_data:
            # ── FG Summary Header ──
            ws.merge_range(row, 0, row, 10,
                f"FG: {fg['fg_code']} | {fg['fg_name']} | BOM: {fg['bom_name']}",
                fmt_fg_header)
            ws.set_row(row, 18)
            row += 1

            # FG KPIs
            kpis = [
                ('Demand Qty', fg['demand_qty']),
                ('FG Available', fg['fg_available']),
                ('ATP Qty', fg['atp_qty']),
            ]
            for label, val in kpis:
                ws.write(row, 0, label, fmt_header_meta)
                ws.write(row, 1, val, fmt_meta_val)
                row += 1

            # ── Component Table Header ──
            ws.set_row(row, 28)
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
                ws.write(row, 5, comp['required_qty'], fmt_cell_num)
                ws.write(row, 6, comp['available_qty'], fmt_cell_num)
                ws.write(row, 7, comp['free_qty'], fmt_cell_num)
                shortage_fmt = fmt_shortage if comp['shortage_qty'] > 0 else fmt_ok
                ws.write(row, 8, comp['shortage_qty'], shortage_fmt)
                ws.write(row, 9, comp['manufacturer'], fmt_cell)
                ws.write(row, 10, comp['part_no'], fmt_cell)
                row += 1

            # ── Totals Row ──
            ws.merge_range(row, 0, row, 7, f"Total Components: {fg['total_components']}", fmt_total)
            ws.write(row, 8, fg['total_shortage'], fmt_total_val)
            ws.merge_range(row, 9, row, 10, '', fmt_total)
            row += 2  # spacer between FGs

        workbook.close()
        output.seek(0)
        file_data = base64.b64encode(output.read())

        # Create attachment and return download action
        attachment = self.env['ir.attachment'].create({
            'name': 'ATP_Report.xlsx',
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
