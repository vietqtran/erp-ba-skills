# The BA team's RSD frame on Confluence

**Where it comes from.** This frame was derived from 64 specification pages in 15 shared spaces of ignify-co.atlassian.net (survey of 20/10/2026).
The page "Quy trình làm việc BA" requires every RSD to share one section structure. There is no standalone template page; the frame below
is the common part of the approved RSD/URD pages.

**How the kit applies it.** `scripts/confluence_page.py` builds pages in this frame, in two dialects:
- HTML for the Atlassian Rovo MCP (`--dialect adf`);
- storage format for the REST API (`--dialect storage`): status/expand/info/toc macros, `ac:image`, two portrait images in a 2-cell table.

## Reference pages

| Page | Space | What it shows |
|---|---|---|
| [RSD Danh sách yêu cầu thẻ - Checker](https://ignify-co.atlassian.net/wiki/pages/viewpage.action?pageId=95453194) | Card GĐ4 | Two-column use-case table (grey bold labels); coloured status lozenges; mockup + description in 2–3 columns; info panels |
| [[URD] AI Food Daily_01](https://ignify-co.atlassian.net/wiki/pages/viewpage.action?pageId=188121372) | BA | Version table at the top; automatic table of contents; flow table "Bước \| Tên bước \| Tác nhân \| Mô tả" |
| [[RA] RSD(01) - Quy tắc chung](https://ignify-co.atlassian.net/wiki/pages/viewpage.action?pageId=201293965) | Hệ thống quản lý vận hành | Use case with code, active/passive actors, trigger condition |
| [RSD 00 — Tổng quan và mục lục](https://ignify-co.atlassian.net/wiki/pages/viewpage.action?pageId=195461179) | Hệ thống quản lý testcase | A large RSD split into an overview page plus child pages |
| [PTTK template IRM](https://ignify-co.atlassian.net/wiki/pages/viewpage.action?pageId=113868897) | IRM | Many expand blocks to keep a long page short |
| [Quy trình làm việc BA](https://ignify-co.atlassian.net/wiki/pages/viewpage.action?pageId=188186694) | BA | Rule: one shared template, cross review, checklist |
| [TOOL 1 — rsd-generator](https://ignify-co.atlassian.net/wiki/pages/viewpage.action?pageId=197787651) | personal (Bích Ngọc) | Every cell has a source; no guessing, empty cells become questions; check duplicate titles, attach images, read back after publishing |

## Elements and how to produce them

| Element | Used for | Write in Markdown |
|---|---|---|
| Version table `Version \| Lý do \| Date \| Người sửa \| Mô tả` | Page top | Table after the **Phiên bản** line; dates `dd/MM/yyyy` (become Confluence date cells) |
| Document info table, BẢN NHÁP lozenge | Page top | Table `Thông tin \| Nội dung` with row `Trạng thái \| Bản nháp` |
| Automatic table of contents (2 levels) | After the version table | Added automatically; the "Nội dung tài liệu" list only serves the Word file |
| Two-column use-case table | Top of section 1 | Table `Đặc tả use case \| Nội dung`: Tên, Mã, Mô tả (Là… tôi muốn… để…), Tác nhân, Mức độ ưu tiên (High/Medium/Low → coloured lozenge), Điều kiện kích hoạt, Tiền/Hậu điều kiện |
| Any two-column table | Label–value information | First column becomes grey and bold |
| Status lozenges | Document statuses; "needs confirmation" / "proposal" | `*Nháp*`, `*Chờ duyệt*`… (italics); `[Cần xác nhận: CH-xx]` yellow, `[Đề xuất: CH-xx]` purple |
| Expand blocks | Step details (2.3), error table (2.6), rule groups (2.7), examples (2.8), "Cách đọc tài liệu" | `#### Bước n – …`; `**a) Nhóm …**` + table; `**Ví dụ n — …**` + table |
| Panels | Notes (blue); proposed values to confirm (yellow, sections 5 and 10); remarks (section 8) | `> note` becomes a blue panel; sections 5, 8, 10 are handled automatically |
| Colour-coded permission matrix | Section 4 | ✔ / Sửa: green · Duyệt: blue · Một phần, Che: yellow · — / Ẩn: grey |
| Question status column | Section 10 | Tables `Mã \| Câu hỏi \| Ảnh hưởng` get an ĐANG MỞ column |
| Figures | Section 6 | `### Hình n – …` + image. Landscape images stay full width; two consecutive portrait images are paired in 2 columns |

## Pitfalls met when publishing through Rovo MCP (handled by the scripts)

- **Allowed HTML.** Confluence rejects `id` on headings and Confluence storage XML (`<ac:...>`) in the HTML dialect. Use only the HTML patterns from `getContentFormatGuide`.
- **Images.** Upload images as attachments first: `createConfluenceAttachment` returns a curl command whose token lives 5 minutes. Then embed them by media id + `contentId-<page>`.
- **Updates.** An update needs the latest `snapshotToken`. **Do not resend the title** when updating, or Confluence reports a duplicate title.
- **Finding a page.** CQL search does not find pages in personal spaces. Find same-title pages with `listConfluenceContent` per space.
- **Duplicates.** Creating a page with an existing title gets "(2)", "(3)" appended. Rovo MCP has **no page delete operation**, so mistaken pages must be deleted by hand.
- **Space instructions.** Read the space (`getConfluenceSpace`) before writing and apply its instructions, if any.

## Google Docs (workspace-mcp)

- **File access.** The server only reads files inside its own folder, so send the `.docx` as base64.
- **Verification.** The Google Docs API may be disabled in the OAuth project, so do not rely on Docs read tools. Verify with the HTML export of the public link.
- **Table formatting.** Google Docs ignores Word table styles. `scripts/docx_style.py` writes borders and header shading into each table directly.
