# AbSafe ERP — Product Build Plan

> A multi-industry, customizable ERP product built on **Django (REST API)** +
> **React**, delivered as a configurable core platform that adapts to each
> client's vertical and requirements — with a modern, "next-level" UI.

---

## 1. Product Vision

**AbSafe ERP** is a single, modular ERP platform that runs the **end-to-end
operations** of a business — and is **customized per client** instead of being a
rigid one-size-fits-all tool.

- **One core, many verticals.** A shared platform (auth, data, workflow, reporting)
  with industry packs layered on top.
- **Configurable, not hard-coded.** Clients differ in fields, workflows, and
  documents — so the platform is driven by configuration and a customization layer.
- **Backend ERP + customer-facing website** for each client.
- **Beautiful, fast UI** that feels like a modern SaaS product, not legacy ERP.

### Target Industries (Vertical Packs)
Manufacturing · Healthcare · POS/Retail · Restaurant & Hotels · Consulting ·
Real Estate · Logistics · Textile · Food · Trading · Printing · Education ·
General Service-Based Businesses.

### Core Modules (shared across verticals)
CRM · Sales · Purchase · Inventory · Manufacturing · Quality · Maintenance ·
HR · Accounting.

---

## 2. Strategy: Build a Core, Sell Verticals

Do **not** build 13 ERPs. Build **one core + thin vertical packs**.

```
                ┌─────────────────────────────┐
                │      AbSafe Core Platform     │
                │  Auth · Tenancy · Workflow ·  │
                │  Documents · Reporting · API  │
                └─────────────┬───────────────┘
                              │
   ┌──────────┬──────────┬────┴─────┬──────────┬──────────┐
   │  CRM     │  Sales   │ Inventory│   Mfg    │Accounting│  ... (core modules)
   └──────────┴──────────┴──────────┴──────────┴──────────┘
                              │
   ┌──────────────┬───────────┴───────────┬──────────────┐
   │ Manufacturing│   Healthcare Pack     │ Restaurant   │ ... (vertical packs)
   │     Pack     │  (patients, imaging)  │  Pack (KOT)  │
   └──────────────┴───────────────────────┴──────────────┘
```

**Ship order (don't boil the ocean):**
1. Core platform + 3 modules (CRM, Sales, Inventory) → usable for *Trading*.
2. Add Purchase + Accounting → usable for most *Service/Trading* businesses.
3. Add Manufacturing + Quality + Maintenance → *Manufacturing/Textile/Printing*.
4. Add HR → complete back office.
5. Then layer vertical packs one at a time, **driven by your first paying client
   in that vertical** (never build a vertical speculatively).

---

## 3. Technical Architecture

### 3.1 Stack
- **Backend:** Python 3.12+, **Django 5 + Django REST Framework**.
- **Frontend:** **React 18 + TypeScript + Vite**.
- **Database:** **PostgreSQL** (JSONB for custom fields, strong relational core).
- **Async/queues:** **Celery + Redis** (emails, reports, stock recompute, integrations).
- **Auth:** JWT (access/refresh) via `djangorestframework-simplejwt`; RBAC permissions.
- **Search:** PostgreSQL full-text first; OpenSearch/Elasticsearch later if needed.
- **Files/media:** S3-compatible object storage.
- **Realtime (optional):** Django Channels / WebSockets for notifications & POS.
- **Caching:** Redis.
- **API docs:** OpenAPI via `drf-spectacular`.

### 3.2 Multi-Tenancy (critical decision)
Choose one early — it shapes everything:

| Approach | How | Best when |
|----------|-----|-----------|
| **Shared DB, tenant_id column** (Row-level) | Every table has `company_id`; filtered by middleware | Simpler ops, many small tenants — **recommended start** |
| **Schema-per-tenant** (`django-tenants`) | Postgres schema per client | Stronger isolation, mid-size tenants |
| **DB-per-tenant** | Separate database per client | Few large/enterprise clients, strict isolation |

> **Recommendation:** Start with **shared DB + `company_id` + strict query
> scoping** (a base manager that always filters by tenant). It's the fastest path
> to revenue and migrates to schema-per-tenant later if a big client demands it.

### 3.3 The Customization Layer (your real differentiator)
Clients always want "one more field" / "a different workflow." Build for it from day 1:

- **Custom fields** — JSONB column + a `FieldDefinition` model per entity so admins
  add fields without code.
- **Configurable workflows** — a state-machine engine (states + transitions +
  guards) defined in data, not hard-coded `if` statements.
- **Document templates** — configurable invoices/POs/quotes (HTML → PDF via WeasyPrint).
- **Numbering sequences** — per-company, per-document configurable sequences.
- **Feature flags / module toggles** per tenant.
- **Approval rules** — configurable approval chains (amount thresholds, roles).
- **Webhooks + REST API** so clients integrate their own tools.

### 3.4 Repository Structure (monorepo recommended)
```
absafe-erp/
├── backend/
│   ├── absafe/                # Django project (settings, urls, celery)
│   ├── core/                  # tenancy, auth, RBAC, audit, custom-fields, workflow
│   ├── modules/
│   │   ├── crm/  sales/  purchase/  inventory/
│   │   ├── manufacturing/  quality/  maintenance/
│   │   └── hr/  accounting/
│   ├── verticals/             # thin packs: healthcare/, restaurant/, realestate/ ...
│   └── tests/
├── frontend/
│   ├── src/
│   │   ├── app/               # routing, layout, providers
│   │   ├── components/ui/     # design system (shared)
│   │   ├── features/          # one folder per module (crm, sales, ...)
│   │   ├── lib/ (api client, hooks, auth)
│   │   └── verticals/
│   └── ...
├── infra/                     # docker-compose, IaC, CI/CD
└── docs/
```

---

## 4. Core Module Scope (End-to-End Processes)

Each module lists the key entities and the **happy-path flow** to implement first.

### 4.1 CRM
- Entities: Lead, Contact, Account/Company, Opportunity, Activity, Pipeline/Stage.
- Flow: **Lead → Qualify → Opportunity (pipeline) → Quotation → Won → hand to Sales.**
- Features: Kanban pipeline, activities/reminders, email log, lead scoring (later).

### 4.2 Sales
- Entities: Quotation, Sales Order, Delivery, Customer Invoice, Price List, Discount.
- Flow: **Quotation → Sales Order → confirm → Delivery (stock out) → Invoice → Payment.**
- Ties into Inventory (reservation) and Accounting (invoice/journal).

### 4.3 Purchase
- Entities: RFQ, Purchase Order, Vendor, Goods Receipt, Vendor Bill.
- Flow: **Requisition → RFQ → PO → Receipt (stock in) → Vendor Bill → Payment.**
- Reorder rules link to Inventory.

### 4.4 Inventory
- Entities: Product, Variant, Warehouse, Location, Stock Move, Lot/Serial, Adjustment.
- Flow: **Receipt / Delivery / Internal transfer**, real-time on-hand, valuation
  (FIFO/avg), reorder rules, barcode support.
- Foundation for Sales, Purchase, Manufacturing.

### 4.5 Manufacturing
- Entities: BOM, Routing/Work Center, Manufacturing Order, Work Order, Component consumption.
- Flow: **MO created → reserve components → work orders → produce → consume
  components, create finished goods.**
- Links Inventory (moves), Quality (checks), Maintenance (machines).

### 4.6 Quality
- Entities: Quality Control Point, Inspection, Check, Non-conformance, CAPA.
- Flow: **Trigger (receipt/MO/delivery) → inspection → pass/fail → NCR → corrective action.**

### 4.7 Maintenance
- Entities: Equipment/Asset, Maintenance Request, Preventive Schedule, Work Order.
- Flow: **Request (corrective) or schedule (preventive) → assign → execute → close.**
- Tracks downtime, links to Manufacturing work centers.

### 4.8 HR
- Entities: Employee, Department, Job Position, Attendance, Leave, Payroll (phase 2).
- Flow: **Onboard employee → attendance/leave → (payroll) → offboard.**

### 4.9 Accounting
- Entities: Chart of Accounts, Journal, Journal Entry, Invoice, Bill, Payment, Tax,
  Bank Reconciliation, Financial Reports.
- Flow: **Source docs (invoices/bills/payments) → automatic journal entries →
  ledgers → P&L, Balance Sheet, Trial Balance, tax reports.**
- **Build last among core** — it's the most regulated and integration-heavy; every
  other module posts into it.

> **Integration principle:** modules talk through **documents and stock/journal
> moves**, not direct table writes. e.g. confirming a Sales Order *emits* a stock
> reservation and (on invoice) an accounting entry.

---

## 5. Vertical Packs (thin add-ons on the core)

Each pack = a few extra models + screens + workflow config. Examples:

| Vertical | Key additions |
|----------|---------------|
| **Manufacturing** | Advanced BOM, shop-floor terminal, OEE |
| **Healthcare** | Patients, appointments, EMR-lite, optional DICOM/imaging, billing |
| **POS / Retail** | Offline-capable POS, sessions, cash control, barcode |
| **Restaurant / Hotels** | Table/room management, KOT, menu/recipe, reservations |
| **Consulting** | Projects, timesheets, billable hours, retainers |
| **Real Estate** | Properties, units, leases, rent schedules, maintenance |
| **Logistics** | Shipments, routes, fleet, tracking, freight billing |
| **Textile** | Size/color matrix variants, fabric lots, production stages |
| **Food** | Batch/expiry tracking, recipes, traceability |
| **Trading** | Multi-currency, landed costs, margin tracking |
| **Printing** | Job estimation, plates/materials, prepress workflow |
| **Education** | Students, courses, admissions, fees, attendance |
| **Service-based** | Service contracts, SLA, ticketing, scheduling |

---

## 6. "Next-Level" UI/UX Design System

The UI is a major selling point — make it feel like a premium modern SaaS.

### 6.1 Frontend foundation
- **React + TypeScript + Vite**.
- **Tailwind CSS** + a component library: **shadcn/ui** (Radix primitives) — clean,
  accessible, fully themeable.
- **TanStack Query** (server state) + **TanStack Table** (data grids) +
  **React Hook Form + Zod** (forms/validation).
- **Recharts / visx** for dashboards; **dnd-kit** for Kanban/drag-drop.
- **Zustand** for light client state; **React Router**.

### 6.2 Design language
- **Per-tenant theming** — brand color, logo, light/dark mode via CSS variables.
- **App shell:** collapsible sidebar, global command palette (⌘K), global search,
  notification center.
- **Consistent record pages:** list (filter/sort/saved views) → detail (tabs,
  activity timeline, smart buttons) → form (inline validation, autosave).
- **Dashboards** per module + role-based home screen with KPIs.
- **Kanban, calendar, Gantt, and pivot/report views** as reusable view types.
- **Responsive + PWA** so POS/shop-floor/field use works on tablets.
- **Micro-interactions:** skeleton loaders, optimistic updates, toasts, empty states.
- **Accessibility (WCAG AA)** and keyboard-first navigation.

### 6.3 Reusable "ERP view" components
Build these once, reuse across all modules:
`DataTableView`, `KanbanView`, `CalendarView`, `FormBuilder` (config-driven),
`DetailLayout`, `KpiCard`, `ChartCard`, `FilterBar`, `ImportExportDialog`,
`DocumentPreview`.

---

## 7. Cross-Cutting Foundations (build into the core early)

- **RBAC & permissions** — roles, groups, record rules (per-tenant).
- **Audit log** — who changed what, when (compliance + trust).
- **Notifications** — in-app + email; configurable per event.
- **Reporting engine** — saved filters, exports (Excel/PDF/CSV), scheduled reports.
- **Import/Export** — CSV/Excel mapping wizard for onboarding client data.
- **Internationalization** — multi-language, multi-currency, multi-company.
- **Background jobs** — Celery for heavy tasks.
- **Observability** — structured logging, Sentry, health checks, metrics.
- **Security** — tenant isolation tests, rate limiting, secrets vault, encrypted PII.
- **Testing** — pytest + factory_boy (backend), Vitest + Playwright (frontend e2e).
- **CI/CD** — lint, type-check, tests on every PR; Docker images; staged deploys.

---

## 8. Delivery Roadmap (phased)

### Phase 0 — Foundations (Weeks 1–4)
- Monorepo, Docker, CI/CD, PostgreSQL.
- Auth, multi-tenancy, RBAC, audit log, custom-fields engine, workflow engine.
- Frontend app shell + design system + API client.
- **Outcome:** empty but production-grade platform you can log into per tenant.

### Phase 1 — Trading-ready MVP (Weeks 5–12)
- Inventory + Products, CRM, Sales, Purchase.
- Basic dashboards, PDF documents, import wizard.
- **Outcome:** sellable to Trading / Service businesses. **Find your first client here.**

### Phase 2 — Back office (Weeks 13–20)
- Accounting (CoA, invoices, bills, payments, core reports) + HR (employees, leave, attendance).
- **Outcome:** complete order-to-cash + procure-to-pay + basic HR.

### Phase 3 — Operations (Weeks 21–30)
- Manufacturing + Quality + Maintenance.
- **Outcome:** sellable to Manufacturing / Textile / Printing / Food.

### Phase 4 — Verticals & client website (ongoing)
- Client-facing website module + each vertical pack, **driven by signed clients**.
- POS pack, Restaurant pack, Healthcare pack, etc., one at a time.

> **Golden rule:** every vertical and big feature should be pulled by a **paying
> client**, not pushed speculatively. Use services revenue to fund the product.

---

## 9. Business & Monetization Notes

- **Pricing:** per-tenant SaaS subscription (per user / per module tier) + one-time
  **implementation & customization** fee + ongoing support retainer.
- **Customization revenue:** custom fields/workflows via config (cheap to deliver);
  bespoke modules quoted as projects.
- **Hosting:** managed cloud hosting as recurring revenue; optional on-prem for
  enterprise/healthcare.
- **Moat:** the configurable core + polished UI + accumulated vertical packs.

---

## 10. Immediate Next Actions

1. **Lock the multi-tenancy decision** (recommended: shared DB + `company_id`).
2. **Scaffold the monorepo** (backend Django + DRF, frontend React+TS, Docker, CI).
3. **Build the core**: auth, tenancy, RBAC, custom-fields, workflow, app shell, design system.
4. **Ship Phase 1 (Inventory + CRM + Sales + Purchase)** and get a pilot client.
5. **Iterate vertical packs** as clients sign.

---

_This is a living document — revise scope and sequencing as real clients validate
each module and vertical._
