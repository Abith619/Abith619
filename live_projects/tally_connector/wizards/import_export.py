from odoo import models, fields, api, _
import xml.etree.ElementTree as ET
import requests, re
from odoo.exceptions import UserError, ValidationError

class TallyIntegrationWizard(models.TransientModel):
    _name = "tally.integration.wizard"
    _description = "Tally Integration Wizard"

    company_id : fields.Many2one = fields.Many2one(
        'res.company',
        string="Company",
        required=True,
        help="Company in which you want to import data."
    )

    tally_account : fields.Many2one = fields.Many2one("tally.config", string="Tally Configuration", required=True)

    # Accounts
    import_ledgers = fields.Boolean("Ledgers", help="Import all the ledgers of Tally into Odoo as Chart of Accounts.")
    import_groups = fields.Boolean("Groups", help="Import all the groups of Tally into Odoo as Account Groups.")

    # Journal Entries
    import_journal_entries = fields.Boolean("Journal Entries", help="Import all journal entries between dates.")
    journal_start_date = fields.Date("Start Date")
    journal_end_date = fields.Date("End Date")

    # Inventory
    import_stock_items = fields.Boolean("Stock Items", help="Import stock items into Odoo as Products.")
    import_stock_categories = fields.Boolean("Stock Categories", help="Import stock categories into Odoo as Product Categories.")
    import_uom = fields.Boolean("Unit of Measure", help="Import unit of measures from Tally.")
    import_godowns = fields.Boolean("Godowns", help="Import godowns into Odoo as Stock Locations.")

    # Sale Orders
    import_sale_orders = fields.Boolean("Sale Orders", help="Import sale vouchers as Sale Orders between dates.")
    sale_start_date = fields.Date("Start Date")
    sale_end_date = fields.Date("End Date")

    def action_import(self):
        if self.import_ledgers:
            self._import_ledgers()
        if self.import_groups:
            self._import_groups()
        if self.import_journal_entries:
            self._import_journal_entries()
        if self.import_stock_items:
            self._import_stock_items()
        if self.import_stock_categories:
            self._import_stock_categories()
        if self.import_uom:
            self._import_uom()
        if self.import_godowns:
            self._import_godowns()
        if self.import_sale_orders:
            self._import_sale_orders()

    @staticmethod
    def sanitize_name(name):
        name = name.strip()
        name = re.sub(r'[\/&]', ' ', name)
        name = re.sub(r'\s+', ' ', name)
        return name

    @staticmethod
    def make_valid_code(name, existing_codes=set()):
        code = re.sub(r'[^0-9a-zA-Z\.]', '', name)
        if code and code[0].isdigit():
            code = 'A' + code
        if not code:
            code = 'Ledger001'
        code = code[:10]

        # Ensure uniqueness by appending numbers if duplicate
        orig_code = code
        counter = 1
        while code in existing_codes:
            suffix = str(counter)
            code = (orig_code[:10-len(suffix)] + suffix)
            counter += 1

        existing_codes.add(code)
        return code

    tally_request = f"""
            <ENVELOPE>
                <HEADER>
                    <VERSION>1</VERSION>
                    <TALLYREQUEST>Export Data</TALLYREQUEST>
                    <TYPE>Collection</TYPE>
                    <ID>Ledger Collection</ID>
                </HEADER>
                <BODY>
                    <DESC>
                        <STATICVARIABLES>
                            <SVCURRENTCOMPANY>BWS</SVCURRENTCOMPANY>
                        </STATICVARIABLES>
                        <TDL>
                            <TDLMESSAGE>
                                <COLLECTION NAME="Ledger Collection">
                                    <TYPE>Ledger</TYPE>
                                    <FETCH>Name,Parent</FETCH>
                                </COLLECTION>
                            </TDLMESSAGE>
                        </TDL>
                    </DESC>
                </BODY>
            </ENVELOPE>
        """

    godown_request = f"""
            <ENVELOPE>
                <HEADER>
                    <VERSION>1</VERSION>
                    <TALLYREQUEST>Export Data</TALLYREQUEST>
                    <TYPE>Collection</TYPE>
                    <ID>Godown Collection</ID>
                </HEADER>
                <BODY>
                    <DESC>
                        <STATICVARIABLES>
                            <SVCURRENTCOMPANY>BWS</SVCURRENTCOMPANY>
                        </STATICVARIABLES>
                        <TDL>
                            <TDLMESSAGE>
                                <COLLECTION NAME="Godown Collection">
                                    <TYPE>Godown</TYPE>
                                    <FETCH>Name,Parent</FETCH>
                                </COLLECTION>
                            </TDLMESSAGE>
                        </TDL>
                    </DESC>
                </BODY>
            </ENVELOPE>
        """

    stock_group = f"""
            <ENVELOPEVELOPE>
                <HEADER>
                    <VERSION>1</VERSION>
                    <TALLYREQUEST>Export Data</TALLYREQUEST>
                    <TYPE>Collection</TYPE>
                    <ID>Stock Group Collection</ID>
                </HEADER>
                <BODY>
                    <DESC>
                        <STATICVARIABLES>
                            <SVCURRENTCOMPANY>BWS</SVCURRENTCOMPANY>
                        </STATICVARIABLES>
                        <TDL>
                            <TDLMESSAGE>
                                <COLLECTION NAME="Stock Group Collection">
                                    <TYPE>Stock Group</TYPE>
                                    <FETCH>Name,Parent</FETCH>
                                </COLLECTION>
                            </TDLMESSAGE>
                        </TDL>
                    </DESC>
                </BODY>
            </ENVELOPEVELOPE>
        """

    # === Below methods are placeholders for actual import logic === #
    def _import_ledgers(self):
        ledger_mapping = {
            "Bank Accounts": "asset_cash",
            "Cash-in-Hand": "asset_cash",
            "Deposits (Asset)": "asset_current",
            "Loans & Advances (Asset)": "asset_current",
            "Sundry Debtors": "asset_receivable",
            "Stock-in-Hand": "asset_current",
            "Fixed Assets": "asset_non_current",
            "Investments": "asset_non_current",
            "Misc. Expenses (ASSET)": "asset_non_current",

            "Sundry Creditors": "liability_payable",
            "Duties & Taxes": "liability_current",
            "Provisions": "liability_current",
            "Loans (Liability)": "liability_non_current",
            "Bank OD A/c": "liability_non_current",
            "Suspense A/c": "liability_current",

            "Capital Account": "equity",
            "Reserves & Surplus": "equity",

            "Sales Accounts": "income",
            "Sales": "income",
            "Direct Incomes": "income",
            "Indirect Incomes": "income_other",

            "Purchase Accounts": "expense_direct_cost",
            "Direct Expenses": "expense_direct_cost",
            "Indirect Expenses": "expense",
        }
        skip_ledgers = ["profit & loss a/c", "profit loss a c", "balance sheet"]

        # 2️⃣ Send Request to Tally
        try:
            tally_url = f"{self.tally_account.host}:{self.tally_account.port}"
            response = requests.post(tally_url, data=self.tally_request.encode("utf-8"))
            response.raise_for_status()
            xml_text = response.text
            xml_text = xml_text.replace("&amp;#4;", "")
            xml_text = re.sub(r'&#\d+;', '', xml_text)
        except Exception as e:
            raise UserError(_("Error connecting to Tally: %s") % str(e))
        # 3️⃣ Parse XML Response
        try:
            root = ET.fromstring(xml_text)
        except Exception as a:
            raise UserError(_("Error parsing Tally response: %s") % str(a))
        for ledger in root.findall(".//DATA//COLLECTION//LEDGER"):
            name_raw = ledger.attrib.get("NAME")
            parent_elem = ledger.find("PARENT")

            name = self.sanitize_name(name_raw.strip())
            code = self.make_valid_code(name.strip())
            parent = parent_elem.text.strip() if parent_elem is not None else None

            if not name or name.lower() in skip_ledgers:
                continue

            account_type = ledger_mapping.get(parent, None)
            if not account_type:
                if "sales" in name.lower():
                    account_type = "income"
                elif "purchase" in name.lower():
                    account_type = "expense_direct_cost"
                elif "capital" in name.lower() or "equity" in name.lower():
                    account_type = "equity"
                else:
                    account_type = "asset_current"

            existing = self.env["account.account"].search([("name", "=", name)], limit=1)
            if not existing:
                self.env["account.account"].create({
                    "name": name,
                    "code": code,
                    "account_type": account_type,
                })
            else:
                existing.write({"account_type": account_type})

        return True

    def _import_godowns(self):
        try:
            tally_url = f"{self.tally_account.host}:{self.tally_account.port}"
            response = requests.post(tally_url, data=self.godown_request.encode("utf-8"))
            response.raise_for_status()
            xml_text = response.text
            xml_text = xml_text.replace("&amp;#4;", "")
            xml_text = re.sub(r'&#\d+;', '', xml_text)
            root = ET.fromstring(xml_text)
        except Exception as e:
            raise UserError(f"Error reading XML: {e}")

        Godown = self.env['stock.location']

        for godown in root.findall(".//DATA//COLLECTION//GODOWN"):
            godown_name = godown.attrib.get("NAME")
            parent_name = godown.find("PARENT")
            if not godown_name:
                raise ValidationError("No Godown name found from Tally Request")

            # Skip "Primary" (root in Tally), Odoo already has main Stock
            if godown_name.strip().lower() == "primary":
                raise ValidationError("primary")

            # Find parent location (map "Primary" to Odoo's main stock)
            parent_id = False
            if parent_name and parent_name.strip().lower() != "primary":
                parent_loc = Godown.search([('name', '=', parent_name)], limit=1)
                parent_id = parent_loc.id if parent_loc else False
            else:
                parent_id = self.env.ref("stock.stock_location_stock").id

            Godown.create({
                'name': godown_name,
                'location_id': parent_id,
                'usage': 'internal',
                'company_id': self.env.company.id,
            })

        return True

    def _import_groups(self):
        group_request = f"""
            <ENVELOPE>
                <HEADER>
                    <VERSION>1</VERSION>
                    <TALLYREQUEST>Export Data</TALLYREQUEST>
                    <TYPE>Collection</TYPE>
                    <ID>Group Collection</ID>
                </HEADER>
                <BODY>
                    <DESC>
                        <STATICVARIABLES>
                            <SVCURRENTCOMPANY>{self.tally_account.company_name}</SVCURRENTCOMPANY>
                        </STATICVARIABLES>
                        <TDL>
                            <TDLMESSAGE>
                                <COLLECTION NAME="Group Collection">
                                    <TYPE>Group</TYPE>
                                    <FETCH>Name,Parent,ISBILLWISEON,ISCOSTCENTRESON</FETCH>
                                </COLLECTION>
                            </TDLMESSAGE>
                        </TDL>
                    </DESC>
                </BODY>
            </ENVELOPE>
        """

        tally_url = f"{self.tally_account.host}:{self.tally_account.port}"
        try:
            response = requests.post(tally_url, data=group_request.encode("utf-8"))
            response.raise_for_status()
            xml_text = response.text.replace("&amp;#4;", "")
            xml_text = re.sub(r'&#\d+;', '', xml_text)
            root = ET.fromstring(xml_text)
        except Exception as e:
            raise UserError(f"Error fetching accounting groups from Tally: {e}")

        # 2️⃣ Parse Groups
        groups = []
        for g in root.findall(".//DATA//COLLECTION//GROUP"):
            group_name = (g.attrib.get("NAME") or "").strip()
            parent_name = (g.find("PARENT") or "").strip()
            is_billwise = g.find("ISBILLWISEON") == "Yes"
            is_cost_centre = g.find("ISCOSTCENTRESON") == "Yes"

            if group_name:
                groups.append({
                    "name": group_name,
                    "parent_name": parent_name,
                    "billwise": is_billwise,
                    "cost_centre": is_cost_centre
                })

        # 3️⃣ Create / Update in Odoo
        AccountGroup = self.env['account.group']  # Odoo group model
        existing_groups = {g.name: g for g in AccountGroup.search([])}

        for g in groups:
            parent = existing_groups.get(g['parent_name']) if g['parent_name'] else None

            if g['name'] in existing_groups:
                # Update parent if changed
                existing_groups[g['name']].write({
                    'parent_id': parent.id if parent else False
                })
            else:
                # Create new group
                group = AccountGroup.create({
                    'name': g['name'],
                    'parent_id': parent.id if parent else False
                })
                existing_groups[g['name']] = group

        return True

    def _import_journal_entries(self):
        journal_request = f"""
            <ENVELOPE>
                <HEADER>
                    <VERSION>1</VERSION>
                    <TALLYREQUEST>Export Data</TALLYREQUEST>
                    <TYPE>Collection</TYPE>
                    <ID>Journal Voucher Collection</ID>
                </HEADER>
                <BODY>
                    <DESC>
                        <STATICVARIABLES>
                            <SVCURRENTCOMPANY>{self.tally_account.company_name}</SVCURRENTCOMPANY>
                        </STATICVARIABLES>
                        <TDL>
                            <TDLMESSAGE>
                                <COLLECTION NAME="Journal Voucher Collection">
                                    <TYPE>Voucher</TYPE>
                                    <FETCH>VOUCHERTYPENAME,DATE,LEDGERENTRIES.LIST,NARRATION,AMOUNT</FETCH>
                                    <FILTERS>
                                        <EXP>$$VoucherTypeName = "Journal"</EXP>
                                    </FILTERS>
                                </COLLECTION>
                            </TDLMESSAGE>
                        </TDL>
                    </DESC>
                </BODY>
            </ENVELOPE>
        """

        tally_url = f"{self.tally_account.host}:{self.tally_account.port}"
        try:
            response = requests.post(tally_url, data=journal_request.encode("utf-8"))
            response.raise_for_status()
            xml_text = response.text.replace("&amp;#4;", "")
            xml_text = re.sub(r'&#\d+;', '', xml_text)
            root = ET.fromstring(xml_text)
        except Exception as e:
            raise UserError(f"Error fetching journal entries from Tally: {e}")

        # 2️⃣ Parse vouchers
        AccountMove = self.env['account.move']
        AccountMoveLine = self.env['account.move.line']
        Account = self.env['account.account']
        Partner = self.env['res.partner']

        for voucher in root.findall(".//DATA//COLLECTION//VOUCHER"):
            date_str = voucher.findtext("DATE")  # Tally date YYYYMMDD
            date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}" if date_str else None
            narration = voucher.findtext("NARRATION") or ""
            voucher_type = voucher.findtext("VOUCHERTYPENAME") or "Journal"

            # 3️⃣ Create account.move in Odoo
            move_vals = {
                'move_type': 'entry',
                'date': date,
                'ref': voucher_type,
                'journal_id': self.env['account.journal'].search([('type', '=', 'general')], limit=1).id,
                'line_ids': []
            }

            for line in voucher.findall(".//LEDGERENTRIES.LIST"):
                ledger_name = line.findtext("LEDGERNAME") or "Unknown"
                debit = float(line.findtext("AMOUNT") or 0)
                credit = 0.0
                if debit < 0:
                    credit = abs(debit)
                    debit = 0.0

                # Find account in Odoo
                account = Account.search([('name', '=', ledger_name)], limit=1)
                if not account:
                    account = Account.create({'name': ledger_name, 'user_type_id': self.env.ref('account.data_account_type_other').id})

                # Optional: link partner
                party_name = line.findtext("PARTYNAME")
                partner = None
                if party_name:
                    partner = Partner.search([('name', '=', party_name)], limit=1)
                    if not partner:
                        partner = Partner.create({'name': party_name})

                move_vals['line_ids'].append((0, 0, {
                    'account_id': account.id,
                    'partner_id': partner.id if partner else False,
                    'name': narration,
                    'debit': debit,
                    'credit': credit,
                }))

            if move_vals['line_ids']:
                AccountMove.create(move_vals)

        return True

    def _import_stock_items(self):
        stock_item_request = f"""
        <ENVELOPE>
            <HEADER>
                <VERSION>1</VERSION>
                <TALLYREQUEST>Export Data</TALLYREQUEST>
                <TYPE>Collection</TYPE>
                <ID>Stock Item Collection</ID>
            </HEADER>
            <BODY>
                <DESC>
                    <STATICVARIABLES>
                        <SVCURRENTCOMPANY>{self.tally_account.company_name}</SVCURRENTCOMPANY>
                    </STATICVARIABLES>
                    <TDL>
                        <TDLMESSAGE>
                            <COLLECTION NAME="Stock Item Collection">
                                <TYPE>Stock Item</TYPE>
                                <FETCH>Name,Parent,StockCategory,Units,Alias</FETCH>
                            </COLLECTION>
                        </TDLMESSAGE>
                    </TDL>
                </DESC>
            </BODY>
        </ENVELOPE>
        """

        try:
            tally_url = f"{self.tally_account.host}:{self.tally_account.port}"
            response = requests.post(tally_url, data=stock_item_request.encode("utf-8"))
            response.raise_for_status()
            xml_text = response.text
            xml_text = xml_text.replace("&amp;#4;", "")
            xml_text = re.sub(r'&#\d+;', '', xml_text)
            root = ET.fromstring(xml_text)
        except Exception as e:
            raise UserError(f"Error reading XML: {e}")

        # 2️⃣ Parse Stock Items
        stock_items = []
        for item in root.findall(".//DATA//COLLECTION//STOCKITEM"):
            name = (item.attrib.get("NAME") or "").strip()
            parent_name = (item.find("PARENT") or "").strip()
            category_name = (item.find("StockCategory") or "").strip()
            unit_name = (item.find("Units") or "").strip()
            aliases = [n.text.strip() for n in item.findall(".//NAME.LIST/NAME") if n.text]

            stock_items.append({
                "name": name,
                "parent_name": parent_name,
                "category_name": category_name,
                "unit_name": unit_name,
                "aliases": aliases
            })

        # 3️⃣ Map to Odoo models
        ProductTemplate = self.env['product.template']
        ProductCategory = self.env['product.category']
        UOM = self.env['uom.uom']

        # Preload existing categories and units
        existing_categories = {c.name: c for c in ProductCategory.search([])}
        existing_uoms = {u.name: u for u in UOM.search([])}

        for item in stock_items:
            # Determine category
            category = existing_categories.get(item['parent_name'])
            if not category and item['parent_name']:
                category = ProductCategory.create({'name': item['parent_name']})
                existing_categories[item['parent_name']] = category

            # Determine UOM
            uom = existing_uoms.get(item['unit_name'])
            if not uom and item['unit_name']:
                uom = UOM.create({'name': item['unit_name'], 'category_id': 1})  # default category
                existing_uoms[item['unit_name']] = uom

            # Check if product exists
            product = ProductTemplate.search([('name', '=', item['name'])], limit=1)
            if product:
                # Update existing
                product.write({
                    'categ_id': category.id if category else False,
                    'uom_id': uom.id if uom else False,
                    'uom_po_id': uom.id if uom else False
                })
            else:
                # Create new product
                ProductTemplate.create({
                    'name': item['name'],
                    'categ_id': category.id if category else False,
                    'uom_id': uom.id if uom else False,
                    'uom_po_id': uom.id if uom else False
                })

        return True

    def _import_stock_categories(self):
        try:
            tally_url = f"{self.tally_account.host}:{self.tally_account.port}"
            response = requests.post(tally_url, data=self.stock_group.encode("utf-8"))
            response.raise_for_status()
            xml_text = response.text
            xml_text = xml_text.replace("&amp;#4;", "")
            xml_text = re.sub(r'&#\d+;', '', xml_text)
            root = ET.fromstring(xml_text)
        except Exception as e:
            raise UserError(f"Error reading XML: {e}")

        ProductCategory = self.env['product.category']
        existing_categories = {c.name: c for c in ProductCategory.search([])}

        for group in root.findall(".//DATA//COLLECTION//STOCKGROUP"):
            group_name = (group.attrib.get("NAME") or "").strip()
            parent_elem = group.find("PARENT")
            parent_name = parent_elem.text.strip() if parent_elem is not None and parent_elem.text else ""

            if not group_name:
                raise ValidationError("No Stock Group name found")

            # Determine parent category in Odoo
            parent = existing_categories.get(parent_name) if parent_name else None

            if group_name in existing_categories:
                # Update parent if changed
                category = existing_categories[group_name]
                category.parent_id = parent.id if parent else False
            else:
                # Create new category
                category = ProductCategory.create({
                    'name': group_name,
                    'parent_id': parent.id if parent else False,
                })
                existing_categories[group_name] = category

        return True

    def _import_uom(self):
        uom_request = f"""
            <ENVELOPE>
                <HEADER>
                    <VERSION>1</VERSION>
                    <TALLYREQUEST>Export Data</TALLYREQUEST>
                    <TYPE>Collection</TYPE>
                    <ID>Unit Collection</ID>
                </HEADER>
                <BODY>
                    <DESC>
                        <STATICVARIABLES>
                            <SVCURRENTCOMPANY>{self.tally_account.company_name}</SVCURRENTCOMPANY>
                        </STATICVARIABLES>
                        <TDL>
                            <TDLMESSAGE>
                                <COLLECTION NAME="Unit Collection">
                                    <TYPE>Unit</TYPE>
                                    <FETCH>Name,Symbol</FETCH>
                                </COLLECTION>
                            </TDLMESSAGE>
                        </TDL>
                    </DESC>
                </BODY>
            </ENVELOPE>
        """
        try:
            tally_url = f"{self.tally_account.host}:{self.tally_account.port}"
            response = requests.post(tally_url, data=uom_request.encode("utf-8"))
            response.raise_for_status()
            xml_text = response.text
            xml_text = xml_text.replace("&amp;#4;", "")
            xml_text = re.sub(r'&#\d+;', '', xml_text)
            root = ET.fromstring(xml_text)
        except Exception as e:
            raise UserError(f"Error reading XML: {e}")

        uoms = []
        for unit in root.findall(".//DATA//COLLECTION//UNIT"):
            name = (unit.attrib.get("NAME") or "").strip()
            symbol = (unit.find("Symbol") or "").strip()
            if name:
                uoms.append({
                    "name": name,
                    "symbol": symbol
                })

        # 3️⃣ Create or Update Odoo UOMs
        UOM = self.env['uom.uom']
        existing_uoms = {u.name: u for u in UOM.search([])}

        for u in uoms:
            if u['name'] in existing_uoms:
                # Update symbol if needed
                existing_uoms[u['name']].write({
                    'name': u['name'],
                    'uom_type': 'reference',  # default type
                    'active': True,
                })
            else:
                # Create new UOM
                UOM.create({
                    'name': u['name'],
                    'category_id': 1,  # Default category; you may create separate categories
                    'uom_type': 'reference',
                    'active': True,
                })

        return True

    def _import_sale_orders(self):
        sale_request = f"""
            <ENVELOPE>
                <HEADER>
                    <VERSION>1</VERSION>
                    <TALLYREQUEST>Export Data</TALLYREQUEST>
                    <TYPE>Collection</TYPE>
                    <ID>Sales Voucher Collection</ID>
                </HEADER>
                <BODY>
                    <DESC>
                        <STATICVARIABLES>
                            <SVCURRENTCOMPANY>{self.tally_account.company_name}</SVCURRENTCOMPANY>
                        </STATICVARIABLES>
                        <TDL>
                            <TDLMESSAGE>
                                <COLLECTION NAME="Sales Voucher Collection">
                                    <TYPE>Voucher</TYPE>
                                    <FETCH>VOUCHERTYPENAME,DATE,PARTYNAME,LEDGERENTRIES.LIST,ALLINVENTORYENTRIES.LIST</FETCH>
                                    <FILTERS>
                                        <EXP>$$VoucherTypeName = "Sales"</EXP>
                                    </FILTERS>
                                </COLLECTION>
                            </TDLMESSAGE>
                        </TDL>
                    </DESC>
                </BODY>
            </ENVELOPE>
        """

        try:
            tally_url = f"{self.tally_account.host}:{self.tally_account.port}"
            response = requests.post(tally_url, data=sale_request.encode("utf-8"))
            response.raise_for_status()
            xml_text = response.text
            xml_text = xml_text.replace("&amp;#4;", "")
            xml_text = re.sub(r'&#\d+;', '', xml_text)
            root = ET.fromstring(xml_text)
        except Exception as e:
            raise UserError(f"Error reading XML: {e}")

        # 2️⃣ Parse Sale Orders
        SaleOrder = self.env['sale.order']
        SaleOrderLine = self.env['sale.order.line']
        Product = self.env['product.product']
        Partner = self.env['res.partner']
        StockLocation = self.env['stock.location']
        AccountTax = self.env['account.tax']

        # Preload warehouses / godowns mapping
        godown_mapping = {loc.name: loc.id for loc in StockLocation.search([])}
        tax_mapping = {tax.name: tax.id for tax in AccountTax.search([])}

        for voucher in root.findall(".//DATA//COLLECTION//VOUCHER"):
            # Basic info
            date_str = voucher.findtext("DATE")  # Tally date YYYYMMDD
            date_order = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}" if date_str else None
            party_name = voucher.findtext("PARTYNAME") or "Unknown Customer"

            # Customer
            partner = Partner.search([('name', '=', party_name)], limit=1)
            if not partner:
                partner = Partner.create({'name': party_name})

            # Sale order
            existing_order = SaleOrder.search([
                ('partner_id', '=', partner.id),
                ('date_order', '=', date_order)
            ], limit=1)

            if existing_order:
                order = existing_order
            else:
                order = SaleOrder.create({
                    'partner_id': partner.id,
                    'date_order': date_order,
                    'partner_invoice_id': partner.id,
                    'partner_shipping_id': partner.id,
                })

            # Sale lines
            for line in voucher.findall(".//ALLINVENTORYENTRIES.LIST"):
                item_name = line.findtext("STOCKITEMNAME") or "Unknown Product"
                qty = float(line.findtext("ACTUALQTY") or 0)
                rate = float(line.findtext("RATE") or 0)

                # Product
                product = Product.search([('name', '=', item_name)], limit=1)
                if not product:
                    product = Product.create({
                        'name': item_name,
                        'type': 'product',
                        'sale_ok': True,
                        'purchase_ok': True
                    })

                # Map Godown → Odoo Stock Location
                godown_name = line.findtext("GODOWNNAME") or ""
                location_id = godown_mapping.get(godown_name)

                # Map Taxes
                taxes = []
                for tax_elem in line.findall(".//TAX/LedgerName"):
                    tax_name = tax_elem.text.strip() if tax_elem.text else ""
                    tax_id = tax_mapping.get(tax_name)
                    if tax_id:
                        taxes.append(tax_id)

                # Create / update order line
                existing_line = order.order_line.filtered(lambda l: l.product_id.id == product.id and l.location_id.id == location_id)
                if existing_line:
                    existing_line.write({
                        'product_uom_qty': existing_line.product_uom_qty + qty,
                        'price_unit': rate
                    })
                else:
                    SaleOrderLine.create({
                        'order_id': order.id,
                        'product_id': product.id,
                        'product_uom_qty': qty,
                        'price_unit': rate,
                        # 'location_id': location_id,
                        'tax_id': [(6, 0, taxes)] if taxes else False,
                    })

        return True

