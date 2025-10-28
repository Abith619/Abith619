# 🧩 Tally ↔ Odoo Integration (tally_connector)

This module integrates **Tally ERP** with **Odoo** to seamlessly synchronize accounting, inventory, and sales data between both systems.

It enables two-way communication between **Tally** (via XML/HTTP interface) and **Odoo** models (via ORM and REST RPC), ensuring consistent financial and stock information.

---

## 🚀 Features

### ✅ Data Import from Tally → Odoo
- **Chart of Accounts** – Import account groups and ledgers into Odoo’s accounting.
- **Stock Items / Products** – Sync Tally stock items into Odoo products.
- **Units of Measure (UoM)** – Create matching UoMs in Odoo for items imported from Tally.
- **Godowns / Warehouses** – Map Tally godowns to Odoo warehouses or stock locations.
- **Sales Orders** – Import customer sale orders from Tally into Odoo.
- **Purchase Orders** – Import vendor purchase orders from Tally into Odoo.
- **Journals & Entries** – Bring Tally journal vouchers into Odoo accounting journals.
- **Taxes** – Map Tally tax ledgers to Odoo tax records.

### 🔄 Optional: Export from Odoo → Tally
- Push invoices, credit notes, and journal entries back to Tally.

---

## ⚙️ Installation

1. **Activate developer mode** in Odoo.
2. Copy the `tally_connector` folder to your Odoo `addons/` path:
   ```bash
   /odoo/custom_addons/tally_connector/

| Tally Field | Odoo Model        | Description              |
| ----------- | ----------------- | ------------------------ |
| `GROUP`     | `account.group`   | Account hierarchy        |
| `LEDGER`    | `account.account` | Chart of Accounts        |
| `STOCKITEM` | `product.product` | Product master data      |
| `GODOWN`    | `stock.location`  | Warehouse/stock location |
| `UNIT`      | `uom.uom`         | Unit of measure          |
| `SALEORDER` | `sale.order`      | Customer sales orders    |
| `PURCHASEORDER` | `purchase.order` | Vendor purchase orders  |
| `JOURNALVOUCHER` | `account.move` | Journal vouchers         |
| `TAX` | `account.tax` | Tax master data          |

