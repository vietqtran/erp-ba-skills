# ERP topic map across the four books

Use this map to pick the **chapters** to read for a process. Book README/cheatsheet/patterns files are only summaries; the ERP
standard behind a step, control or rule comes from the chapter files. Built from the Topic Index of each book README.

| Code | Book | Folder |
|---|---|---|
| P | Parthasarathy — *Enterprise Resource Planning: A Managerial and Technical Perspective* | `parthasarathy-erp-fundamentals` |
| W | Wallace & Kremzar — *ERP: Making It Happen* | `wallace-erp-implementation` |
| O | O'Leary — *Enterprise Resource Planning Systems* | `oleary-erp-systems-lifecycle` |
| E | Elbardan & Kholeif — *ERP, Internal Auditing and Corporate Governance* | `elbardan-erp-governance-audit` |

Chapter file: `books/<folder>/chapters/chNN-*.md`. Cite as "Wallace ch09", "Elbardan ch08", etc.

## How to read (tiered, to keep context small)

| Tier | What | Command | Size |
|---|---|---|---|
| 1. Index | One-line summary of every chapter of all four books | `python3 books/read.py index` | ~6 KB in total |
| 2. Choose | Pick the process type (§1) → topics → chapters (§2). Cross-check with the index and keep only chapters whose summary fits. Write the shortlist and the reason before reading | this file | — |
| 3. Read | For each chosen chapter: core idea, key takeaways, BA application only | `python3 books/read.py W ch09` | ~30% of a chapter |
| 3+. Deepen | Only when a specific rule or control needs it: add sections, or as a last resort the full chapter | `--add "Khái niệm chính,Bảng tham chiếu"` · `--full` | as needed |

Budget: about 8–12 chapters for one process (RSD, at most 15), about 12–15 for a whole process set (bpmn-kit). Do not open README, cheatsheet,
patterns or glossary files in full; do not read chapters outside the shortlist.

## 1. Process type → topics to read

| Process type | Topics (section 2) |
|---|---|
| Every process / every RSD | Process modelling (UML, swimlanes); Policies, roles, parameters; Control types and preventive controls; RBAC, SoD, maker-checker; Data input controls; Reports and exceptions; Parameters vs customisation |
| Master data | Master data; Data integrity; Data input controls; Parameters vs customisation |
| Supplier contracts, procurement | Supplier scheduling; Requisition-to-pay; Maker-checker and approval hierarchy; SoD |
| Product design, pricing (BOM / routing analogues) | BOM and routing accuracy; Pricing; Make-to-order vs make-to-stock |
| Planning (S&OP, master schedule, capacity) | S&OP; Master scheduling and time fences; Capacity; KPIs |
| Sales, order taking (quote-to-cash) | Quote-to-cash; ATP / order promising; CRM; Pricing; Maker-checker and approval hierarchy |
| Operations, fulfilment, field execution | Feedback ("silence is approval"); Data input at the source; Reports and exceptions |
| Order changes, cancellation, refunds | Change control and time fences; Processing constraints; Maker-checker; SoD; Audit trail |
| Costing, settlement | Finance and cost controlling; Audit trail; Reports and exceptions |
| Receivables, payables, cash | SoD; Maker-checker; Preventive controls; Audit trail; Reports and exceptions |
| Customer service, complaints | CRM; KPIs; Reports and exceptions |
| Period close, reporting | Audit trail; Control assumptions; Reports; Data integrity |

## 2. Topic → chapters

| Topic | Chapters |
|---|---|
| ERP concepts, integration, "one set of numbers" | P ch01 · W ch01, ch17 · O ch01 · E ch01, ch02 |
| Standard modules and cross-module flow | P ch03 · O ch03 |
| Process modelling (UML use case, activity/swimlanes, sequence) | P ch12 |
| Policies: roles, parameters, feedback, who may change what | W ch09 |
| Master scheduling and time fences | W ch09, ch17 |
| Change control (engineering-change style policy) | W ch09 · E ch08 (processing constraints) |
| ATP / order promising | W ch09, ch17 · O ch07, ch11 |
| S&OP, volume vs mix | W ch08, ch17 |
| MPS / MRP / MRP II, dependent demand | P ch02 · W ch17 |
| BOM and routing accuracy | P ch02 · W ch10, ch17, ch18 |
| Capacity planning | W ch12, ch17 |
| Supplier scheduling, VMI, collaborative forecasting | W ch12, ch17 |
| Supply chain management | P ch07 |
| Quote-to-cash, requisition-to-pay | P ch08 |
| CRM (operational / analytical / collaborative) | P ch08 |
| Pricing | P ch03 |
| Finance, treasury, cost controlling | P ch03 |
| Make-to-order / make-to-stock / assemble-to-order | P ch01, ch02 · W ch18 |
| Master data, chart of accounts | P ch03, ch08 · O ch02, ch10 · E ch06, ch10 |
| Data integrity, cycle counting, migration | W ch10 · O ch12 · E ch09, ch10 |
| Data input controls, capture at the source | O ch04 · E ch08 (submission checks) |
| Data acceptance criteria (CAVAIR) | E ch09 |
| Reports, outputs, data warehouse | O ch05, ch12 · P ch08 |
| Exception reports, continuous monitoring | E ch06, ch08, ch10 · W ch17 |
| Feedback loops, "silence is approval" | W ch11, ch12, ch17 |
| KPIs and performance measurement | W ch06, ch11, ch15 · P ch11 |
| Control types (inherent / configurable / security / reporting) | E ch06 |
| Preventive controls written as if/else rules | E ch02, ch06, ch07 |
| Control assumptions checklist | E ch06, ch07, ch08, ch09, ch10 |
| RBAC, data security, access | E ch08, ch09, ch10, ch11 · O ch05, ch12 |
| Segregation of duties | E ch02, ch06, ch07, ch08, ch09, ch10 |
| Maker-checker, approval hierarchy | E ch08, ch09 |
| Audit trail / logs | E ch02, ch06, ch08, ch09 · P ch05, ch08 |
| Internal control (COSO), compliance drivers | E ch01, ch02, ch08, ch09 |
| Parameters / switch settings vs customisation | O ch02, ch10 · W ch04 · P ch04, ch05 |
| Reengineer vs customise vs workaround | E ch06, ch10, ch11 · O ch06, ch09 · P ch05 |
| Requirements elicitation, gap analysis | P ch04, ch05 · E ch05, ch12 |
| RACI, who is accountable | E ch11, ch12 |
| Go-live, cutover, stabilisation | W ch11, ch14 · O ch12 · E ch07, ch08 |
| Training, education, behaviour change | W ch07, ch15 · O ch13 |
| E-commerce, EDI, configuration engine | O ch14 |
| Risk, success and failure factors | O ch15 · E ch09, ch11 |
