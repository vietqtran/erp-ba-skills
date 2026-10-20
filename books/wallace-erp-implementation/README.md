---
name: wallace-erp-implementation
description: "Kho tri thức ERP từ sách \"ERP: Making It Happen\" (Thomas F. Wallace & Michael H. Kremzar, 2001). DÙNG SKILL NÀY khi bạn hoặc agent cần kiến thức ERP chuẩn để thiết kế chức năng, viết tài liệu/spec code-ready, hoặc rà soát nghiệp vụ — các chủ đề: ERP vs phần mềm (ES), Proven Path triển khai, Sales & Operations Planning (S&OP), master scheduling, MRP/CRP/RCCP, DRP, supplier scheduling/VMI, data integrity (BOM/routing/inventory accuracy, cycle counting), job shop vs flow shop, Quick-Slice, Class A/ABCD, bedrock policies (roles/parameters/feedback/measurements). ENGLISH: Knowledge base from Wallace & Kremzar's \"ERP: Making It Happen\"; use it whenever an ERP Business Analyst or agent needs standard ERP knowledge — ERP vs software, the Proven Path, S&OP, the planning hierarchy (master scheduling, MRP, CRP), DRP, supplier scheduling/VMI, data integrity, job vs flow shop, Quick-Slice, Class A — to design ERP-standard functions and write code-ready specifications."
---

<!-- argument-hint: [chủ đề, tên framework, hoặc số chương vd ch08] -->

# ERP: Making It Happen — The Implementers' Guide to Success
**Tác giả**: Thomas F. Wallace & Michael H. Kremzar | **Trang**: ~370 | **Chương**: 20 file (16 chương + Phụ lục A–D) | **Generated**: 2026-10-20

## Cách dùng skill này
- **Không tham số** — nạp các framework cốt lõi dưới đây để tham chiếu.
- **Theo chủ đề** — hỏi về `S&OP`, `master scheduling`, `data integrity`, `supplier scheduling`... tôi mở đúng chương.
- **Theo chương** — hỏi `ch08` để nạp nguyên chương.
- **Tra cứu** — xem `glossary.md`, `patterns.md`, `cheatsheet.md` (cheatsheet là trang tra nhanh giá trị nhất).

Khi câu hỏi vượt phần Core dưới đây, tôi đọc chương liên quan trước khi trả lời.

---

## Core Frameworks & Mental Models

**ERP ≠ phần mềm.** **Enterprise Resource Planning (ERP)** là tập quy trình nghiệp vụ toàn doanh nghiệp để cân bằng cung–cầu và ra quyết định; phần mềm là **Enterprise System (ES)**. Phần lớn "ERP failure" thực chất chỉ là cài ES mà không đổi quy trình → spec phải mô tả **quy trình + con người**, không chỉ cấu hình. Dùng thang **Class A/B/C/D** (Oliver Wight) để đánh giá "độ chuẩn": A = một bộ số thống nhất xuyên suốt hoạch định → thực thi → tài chính.

**ABCs of Implementation** — ưu tiên theo Pareto: **A = People** (quan trọng nhất) > **B = Data** > **C = Computer**. Khi buộc cắt ngân sách, cắt C trước, giữ A.

**The Proven Path + Three Knobs.** Thành công = **lịch quyết liệt (~18 tháng, <2 năm)** + đi đủ **Proven Path** không skip bước. Quản lý bằng **Three Knobs**: Work · Time · Resources — cố định hai, xoay núm còn lại (company-wide xoay *resource*; Quick-Slice *giảm work*). Nguyên tắc nền: **IMPLEMENTERS = USERS** — người triển khai phải là người vận hành.

**Mô hình 3 phase** (tuần tự, trong mỗi phase chạy task song song): **Phase I Basic ERP** (S&OP, demand mgmt, RCCP, master scheduling, MRP, data integrity; ~9–12 tháng) → **Phase II Supply Chain Integration** (supplier scheduling, DRP, VMI) → **Phase III Extensions** (chiến lược, liên tục). Lập lịch **theo business function, không theo software module**. Phase I chỉ nhận "have-to's".

**ERP Planning Hierarchy** (Phụ lục A) — xương sống "chuẩn ERP", trên dẫn động dưới, dưới feedback lên theo exception:
Business Planning ($) → **S&OP** (VOLUME, theo product family, units) → Demand Management + **RCCP** → **Master Scheduling** (MIX, sản phẩm/đơn, theo tuần; *tổng phải reconcile với S&OP*) → **MRP** (cần BOM + inventory) → **CRP** (cần routing + work center) → **Plant/Supplier Scheduling** → Execution & Feedback. Ranh giới then chốt: **Volume vs Mix**. Trộn hai tầng này là nguồn conflict trong tài liệu.

**S&OP** — "tay nắm của ban lãnh đạo", có thể là phần quan trọng nhất của ERP; chu kỳ tháng 5 bước kết thúc bằng Executive S&OP Meeting ≤2 giờ; **single-number forecast** (một dự báo chính thức). Phần mềm không hỗ trợ thì vẫn phải làm (spreadsheet). Là early win; multiplant vẫn làm đồng loạt & sớm.

**Data integrity trước, không trong/sau.** Phân loại **forgiving vs unforgiving**; dồn sức vào unforgiving. Ngưỡng trước go-live: **inventory ≥95%** (đẩy 98–99%), **BOM/routings/open orders ≥98%**, counting tolerance 0–5%. Đạt bằng **cycle counting** (control group ~100 item/tuần) + limited access + transaction đơn giản + zero-defects attitude. BOM phải complete (shipment-stopper), structured (modular/planning bills), integrated (một nguồn sự thật). Dưới ngưỡng → **đừng bật MS/MRP/DRP**.

**Go-live = pilot, không big bang.** Ba pilot: Computer → Conference room ("play Murphy / Make It Fail") → **Live pilot** (chứng minh works + **user sign-off**). **Parallel** chỉ dùng cho accounting. "**Silence is approval**": mỗi role sinh **anticipated delay report** khi biết sẽ trễ → closed loop.

**Five Bedrock Policies** (Process Definition): S&OP, demand management, master scheduling, material planning, engineering change. Mỗi policy — và trong spec, **mỗi chức năng** — phải nêu: **roles** (ai đổi gì ở time zone nào) · **parameters** (order qty, safety stock/time, scrap/shrinkage, time fences, hedges) · **feedback flows** · **performance measurements** · **business rules**. Đây chính là cấu phần "phân quyền/tham số hệ thống" của tài liệu ERP chuẩn.

**Education = behavior change**, không chỉ fact transfer; đạt **critical mass ≥80%** trước go-live; "đừng train trước khi educate"; **bulletproofing** (trả lời mọi câu hỏi hóc búa) = mô hình vòng verify tài liệu.

**Quick-Slice** — khi đã có ES / cần payback nhanh / nguy cơ sống còn: chọn 1 product line tác động cao, triển khai đầy đủ ERP cho nó, pilot ~120 ngày, pilot = cutover; bỏ F&A, thêm physical process improvement (cells/kanban); S&OP cho tất cả family.

**Job shop vs flow shop** quyết định bộ chức năng lập lịch: job shop cần routing nhiều nguyên công + back scheduling + dispatch list + CRP + input-output; flow shop dùng lịch trình tự đơn giản (có thể không cần routing chính thức).

---

## Chapter Index

| # | Chương | Framework chính |
|---|--------|-----------------|
| [ch01](chapters/ch01-enterprise-resource-planning.md) | ERP là gì | ERP vs ES, MRP→MRPII→ERP, Class ABCD, ABCs, universal mfg equation |
| [ch02](chapters/ch02-the-implementation-challenge.md) | Thách thức triển khai | Catch-22, Proven Path, Three Knobs, 18 tháng, IMPLEMENTERS=USERS |
| [ch03](chapters/ch03-company-wide-implementation-overview.md) | Triển khai toàn công ty | 3 phase, schedule by function, staggered multiplant |
| [ch04](chapters/ch04-software.md) | Phần mềm | ES, bolt-on, switches, big bang, change-request control |
| [ch05](chapters/ch05-getting-ready.md) | Chuẩn bị | Audit I, first-cut education, vision, cost/benefit, Go/No-Go |
| [ch06](chapters/ch06-project-launch.md) | Khởi động dự án | Project leader, steering committee, torchbearer, performance goals |
| [ch07](chapters/ch07-initial-education.md) | Đào tạo ban đầu | Behavior change, education vs training, critical mass, bulletproofing |
| [ch08](chapters/ch08-sales-and-operations-planning.md) | S&OP | Volume vs mix, monthly 5-step, single-number forecast |
| [ch09](chapters/ch09-process-definition.md) | Định nghĩa quy trình | Five bedrock policies, customer meeting point, ATP, rolling 90-day |
| [ch10](chapters/ch10-data-integrity.md) | Toàn vẹn dữ liệu | Forgiving/unforgiving, cycle counting, BOM/routing accuracy |
| [ch11](chapters/ch11-going-on-the-air-basic-erp.md) | Go-live Phase I | 3 cách triển khai, 3 loại pilot, silence is approval |
| [ch12](chapters/ch12-supply-chain-integration-phase-ii.md) | Chuỗi cung ứng (II) | Supplier scheduling, DRP, VMI, finite scheduling, input-output |
| [ch13](chapters/ch13-quick-slice-erp-overview.md) | Quick-Slice tổng quan | Quick-Slice, three knobs, window of risk |
| [ch14](chapters/ch14-quick-slice-erp-implementation.md) | Quick-Slice triển khai | 5 tiêu chí chọn slice, cells, kanban, pilot=cutover |
| [ch15](chapters/ch15-operating-erp.md) | Vận hành ERP | Operating committee, ABCD Checklist, re-certification, Lean |
| [ch16](chapters/ch16-the-strategic-future-phase-iii.md) | Tương lai chiến lược (III) | Time & knowledge, zero inventory, B2B/bullwhip, factoid |
| [ch17](chapters/ch17-appendix-a-fundamentals-of-erp.md) | Phụ lục A — Nền tảng ERP | Planning hierarchy, S&OP/MS/MRP/CRP/RCCP, ATP, one set of numbers |
| [ch18](chapters/ch18-appendix-b-job-shop-vs-flow-shop.md) | Phụ lục B — Job/Flow shop | Job vs flow, back scheduling, dispatch list, cellular |
| [ch19](chapters/ch19-appendix-c-sample-implementation-plan.md) | Phụ lục C — Kế hoạch mẫu | Detailed implementation plan, cycle counting |
| [ch20](chapters/ch20-appendix-d-erp-support-resources.md) | Phụ lục D — Nguồn lực | APICS, Oliver Wight, MRP II Standard System |

## Topic Index

- **ABCs / People-Data-Computer** → ch01, ch05
- **ATP / order promising** → ch09, ch17
- **behavior change / education** → ch07, ch15
- **BOM / routing accuracy** → ch10, ch17, ch18
- **bolt-on / software** → ch04
- **Class A / ABCD Checklist** → ch01, ch15
- **cost/benefit / Go-No-Go** → ch05
- **CRP / capacity** → ch12, ch17
- **cutover / pilot / go-live** → ch11, ch14
- **cycle counting / data integrity** → ch10, ch19
- **DRP / distribution** → ch03, ch12
- **ERP vs ES** → ch01, ch04, ch17
- **finite scheduling** → ch12
- **job shop vs flow shop** → ch18, ch12
- **master scheduling / time fences** → ch09, ch17
- **MRP** → ch01, ch17
- **performance goals / KPI / measurements** → ch06, ch11, ch15
- **policies (roles/parameters/feedback)** → ch09
- **Proven Path / phases** → ch02, ch03
- **Quick-Slice** → ch02, ch13, ch14
- **S&OP / volume vs mix** → ch08, ch17
- **silence is approval / feedback** → ch11, ch12
- **supplier scheduling** → ch12, ch17
- **Three Knobs** → ch02, ch06, ch13
- **vision statement / charter** → ch05
- **VMI / collaborative forecasting** → ch12
- **Quick-Slice cells / kanban** → ch14, ch18

## Supporting Files

- [glossary.md](glossary.md) — thuật ngữ ERP chuẩn (English + gloss tiếng Việt), theo bảng chữ cái.
- [patterns.md](patterns.md) — kỹ thuật triển khai (When / How / Trade-offs).
- [cheatsheet.md](cheatsheet.md) — **file giá trị nhất**: ngưỡng, cây quyết định, bảng đánh đổi, quy tắc "Khi X → làm Y".

## Dùng cùng skill erp-ba-core

Skill này là **kiến thức nền ERP** (background knowledge) cho skill viết tài liệu `erp-ba-core` (thư mục anh em `../erp-ba-core`). Khi `erp-ba-core` cần hiểu một quy trình/chức năng ERP chuẩn (S&OP, master scheduling, MRP, supplier scheduling, data integrity, roles/parameters/feedback, go-live gate...), hãy tham chiếu chương tương ứng ở đây để spec "chuẩn ERP" và code-ready, không bị thiếu/thừa/mâu thuẫn chức năng.

---

## Scope & Limits

Skill chỉ phủ nội dung cuốn sách (triển khai ERP sản xuất theo trường phái Oliver Wight/APICS, bản 2001). Thuật ngữ và framework giữ nguyên tên gốc tiếng Anh. Mọi sơ đồ/bảng trong sách là văn bản trích từ PDF (pdftotext) — một số figure bị làm phẳng đã được tái dựng từ phần văn xuôi và có ghi chú trong chương; không dùng thay cho bản gốc khi cần số liệu chính xác tuyệt đối. Để áp vào sản phẩm/ngành cụ thể (xây dựng, kế toán, logistic...), kết hợp với kiến thức ngành và skill `erp-ba-core`.
