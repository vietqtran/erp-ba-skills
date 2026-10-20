# Writing guide: business-reader RSD from one BPMN process

The **document is written in Vietnamese**. Its readers are BAs, key users and customers, not developers.
Approved sample: `examples/tour-operator/rsd/BP-13/`. Frame: `templates/rsd-template.md`.

## Where content comes from

The main source is `<project>/docs/BP-xx-*.md` together with `<project>/defs/bpxx_*.py`; both come from the same definition.
Also read the documents of the processes this one calls or is called from (`upstream`, `downstream`, call-activity steps),
so that sections 1.4 and 1.8 agree in both directions.

| BPMN definition | RSD section |
|---|---|
| `objective`, `scope`, `out_of_scope`, `trigger`, `outcome` | 1.1, 1.3, 1.4, 1.6 and the use-case table |
| `kpis` | 1.2 |
| `lanes`, `pools` | 1.7, 4.1 |
| `nodes` (tasks, events) | 2.2, 2.3. **Renumber as Bước 1…n in flow order**; never use the T1/G1/S1 ids |
| XOR/AND gateways | 2.4 (conditions in plain words) |
| `messages` | 3.6 |
| `documents` | 3.3, 3.2 (statuses in Vietnamese) |
| `postings` | 3.5 |
| `controls` (Cxx-nn) | 7. Recode as KS-01… and list the QT/TN/TS that implement each one |
| `parameters` | 5. Codes TS-01…, each with "Ảnh hưởng" and "Ai thay đổi" |
| `questions` | 10. Codes CH-01…, grouped by who must answer |
| `references` | 11 (book title + chapter, no paths) |

Some things are not in the BPMN but are standard ERP practice. **Add them and mark them `[Đề xuất: CH-xx]`**, with a matching
question in section 10:
- timeouts (customer or supplier not answering, payment overdue);
- error cases;
- segregation of duties and approval limits;
- who may see sensitive data;
- missing BPMN branches.

Any figure without a source gets `[Cần xác nhận: CH-xx]`. Never invent a source.

## ERP standard from the books (required)

The four books in `books/` are the reference for what "standard ERP" means. The BPMN gives the flow; the books give the controls,
policies and rules around it.

Read in tiers (`books/TOPICS.md`, "How to read"). This avoids reading whole books, which is slow and fills the context.

1. **Index.** Run `python3 books/read.py index` for the one-line summary of every chapter (~6 KB for all four books).
2. **Choose.**
   - In `books/TOPICS.md`, pick the process type and its topics. Always include the "Every process" topics.
   - Map the topics to chapters and keep about 8–12 whose index summary fits.
   - Write this shortlist and the reasons at the top of `book-notes.md` **before** reading.
3. **Read.** For each chosen chapter, run `python3 books/read.py <P|W|O|E> chNN`. It prints the core idea, key takeaways and
   BA application, about 30% of the chapter. Use `--add "Khái niệm chính,Bảng tham chiếu"` or `--full` only when a specific rule needs it.
   Never open README, cheatsheet, patterns or glossary files in full.
4. **Record.** Fill `<RSD dir>/book-notes.md` from `templates/book-notes.md`: topic, key point, where the RSD applies it, chapter file.
   It needs at least 8 rows from at least 3 books. It is a working file and is not published.
4. Apply the notes in the RSD:
   - every KS row in section 7 has a "Căn cứ" cell (book chapter, or law/standard), and at least half cite a book;
   - rules in section 2.7 cite their KS or chapter;
   - section 11 lists the chapters actually used (at least 3 books).
5. Cite as "Elbardan ch08", "Wallace ch09" in table cells, and as "Ch. 8" rows per book in section 11.
   `scripts/check.py` checks that every cited chapter exists.

## Writing rules

- **Never include:**
  - file paths or file names;
  - technical field names (snake_case);
  - English status codes (DRAFT…) or technical ID schemes (BR-, PRM-, MSG-, ROLE-…);
  - sequence diagrams or data models.

  `scripts/check.py` catches these.
- **Use one code scheme:** Bước n, QT-, TS-, KS-, TN-, BC-, NT-, CH- (two digits). Every code mentioned must be defined in a table row.
- **Document statuses** go in italics (`*Chờ duyệt*`), so they become coloured lozenges on Confluence.
- **Error messages:** quote the exact sentence the user sees, with `{parameters}`. No MSG codes.
- **Formulas** are written in words. Always add 2–3 worked examples with concrete numbers, and reuse them in the acceptance criteria.
- **Acceptance criteria** use Cho trước / Khi / Thì with concrete data. Cover the main flow, exceptions, permissions and boundaries.
- **Laws:** cite texts that are in force and add "cần kiểm tra lại hiệu lực khi áp dụng". Postings and tax: "kế toán xác nhận".
- **Lists** need a blank line before them (pandoc).
- **Section titles and column names** must stay exactly as in the template; the scripts rely on them.

## Diagrams (`diagrams/`, Mermaid; labels in Vietnamese)

Copy `<project>/png/BP-xx-*.png` to `images/h01-bpmn.png`. The other diagrams are `.mmd` files coloured by role
(`templates/diagrams/role-colors.mmd`). Labels are Vietnamese with no technical codes, at most about 20 nodes per diagram.
File names are English.

| File | Content |
|---|---|
| `h02-context` | External parties ↔ ERP modules (flowchart LR) |
| `h03-flow-phase-…`, `h04-flow-phase-…` | Steps per phase (flowchart TD, nodes "n. Vai trò: việc"). **No lane subgraphs**: Mermaid lays lanes out badly, and the real swimlanes are already in figure 1 |
| `h05-decision-…` … `h08-decision-…` | Decision diagrams for the points with several conditions (pricing, approval, invoice/refund handling) |
| `h09-state-…` … `h11-state-…` | Status life cycle of the main documents (stateDiagram-v2) |

The number of diagrams depends on the process; simple processes may have fewer. Run `scripts/render-diagrams.sh`, open the PNGs,
and fix any diagram that looks cluttered.
