---
name: oleary-erp-systems-lifecycle
description: "Kho tri thức ERP từ sách \"Enterprise Resource Planning Systems: Systems, Life Cycle, Electronic Commerce, and Risk\" của Daniel E. O'Leary (2000, Cambridge University Press). DÙNG skill này khi bạn hoặc agent cần kiến thức nền ERP để viết/kiểm tra tài liệu đặc tả: ERP là gì, module chuẩn (FI/CO/MM/PP/SD/HR), master data & danh mục, khung MAPs (Models/Artifacts/Processes), thiết kế quy trình chuẩn ERP, data input controls, báo cáo & đầu ra, phân quyền & tham số hệ thống, business case, big bang vs phased, rủi ro, go-live, đào tạo, EDI/thương mại điện tử. Knowledge base from O'Leary's ERP book — consult whenever a BA or agent needs ERP domain knowledge (what ERP is, standard modules, standard processes, ERP terminology, controls, master data, permissions, parameters, reports, implementation life cycle, risk) to design ERP-standard functions or write code-ready specifications."
---

<!-- argument-hint: [chủ đề, tên framework, hoặc số chương vd ch05] -->

# Enterprise Resource Planning Systems: Systems, Life Cycle, Electronic Commerce, and Risk
**Tác giả**: Daniel E. O'Leary | **Số trang**: ~220 | **Số chương**: 15 | **Tạo ngày**: 2026-10-20

## Cách dùng skill này
- **Không tham số** — nạp các framework cốt lõi bên dưới để tham chiếu nhanh.
- **Với một chủ đề** — hỏi về `master data`, `big bang`, `data input controls`, `risk`... tôi tìm và đọc chương liên quan.
- **Với số chương** — hỏi `ch05`, tôi nạp đúng chương đó.
- **Duyệt** — hỏi "có những chương nào?" để xem Chapter Index.

Khi bạn hỏi một chủ đề không có trong "Core Frameworks" dưới đây, tôi đọc chương tương ứng trước khi trả lời. Đây là tri thức nền (background knowledge) — không phải quản trị dự án phần mềm nói chung mà là các vấn đề *đặc thù ERP*.

---

## Core Frameworks & Mental Models

### Nền tảng tư duy (áp cho mọi đặc tả)
- **Eight Value-Creation Mechanisms** — tám cơ chế ERP tạo giá trị: (1) tích hợp toàn doanh nghiệp, (2) nhúng **best practices**, (3) chuẩn hóa tổ chức, (4) xóa **information asymmetry** (bất đối xứng thông tin), (5) thông tin real-time, (6) truy cập đồng thời, (7) cộng tác nội bộ, (8) cộng tác liên tổ chức. *Dùng để*: biện minh mỗi yêu cầu — nếu một chức năng không hiện thực hóa cơ chế nào thì nghi "thừa chức năng". Giá trị ERP = tích hợp + một nguồn dữ liệu + real-time, KHÔNG phải số lượng tính năng (Ch 1).
- **MAPs — Models, Artifacts, Processes** — xương sống của MỌI spec chức năng: nêu rõ **Models** (mô hình dữ liệu/tổ chức + *giả định* bắt buộc, vd mỗi đơn vị phải là cost/profit center), **Artifacts** (chứng từ + danh mục/master data), **Processes** (luồng liên chức năng). Thiết kế trái giả định của model ⇒ conflict khi code (Ch 3, 10).
- **Enter once + Relational normalization**: mỗi dữ liệu nhập một lần tại nguồn; master data chuẩn hóa thành bảng + khóa tham chiếu, không trường phẳng lặp lại. Ưu tiên **switch setting** (tham số) trước khi đề xuất tùy biến mã — tùy biến tốn chi phí 3 lần (sửa/nâng cấp/hỗ trợ) (Ch 2, 4).

### Quyết định & lựa chọn
- **Four Business Case Rationales** (Ch 7): technology / business process / strategic / competitive. CHỈ process & strategic cho mục tiêu đo được ⇒ chuyển thành **acceptance criteria** (vd đóng sổ 24→6 ngày). Lý do chỉ Y2K/"đối thủ có" ⇒ phải bổ sung.
- **Technology enabled vs Clean slate** (Ch 6): chọn phần mềm trước rồi thiết kế trong giới hạn (nhanh/rẻ/khả thi, bị ràng buộc) VS thiết kế tự do rồi fit phần mềm (độc nhất, tốn kém, rủi ro bất khả thi). Ghi rõ vị trí dự án TRƯỚC khi viết spec quy trình.
- **Requirements vs Gap Analysis** (Ch 8): rà soát yêu cầu đối với MAPs, gắn nhãn ưu tiên + độ mịn (granularity); luôn kèm mục **non-functional** (cost, time, nhân sự triển khai, bảo trì, nâng cấp). Chốt factor/weight TRƯỚC demo. Demo scripted hai pha để lộ gap.
- **Small-r vs Big-R Reengineering** (Ch 9): đổi tổ chức × đổi phần mềm. Quy trình generic (tài chính, back office) ⇒ theo chuẩn (small-r); chỉ sửa phần mềm cho quy trình tạo giá trị khác biệt.
- **Group-choice rules cho MAPs chung** (Ch 10): Majority Vote / **Borda Rule** / Pareto Optimality / Dictatorship. Mỗi danh mục dùng chung (vendor, customer, product, chart of accounts) là quyết định chuẩn hóa cấp doanh nghiệp: ghi nguồn chuẩn, ai chịu chi phí đổi, tỷ lệ local tự cấu hình (~1%).

### Nhập liệu, đầu ra, triển khai
- **Five Reengineering Sources of Data-Input** + **data input controls** (Ch 4): "nhập một lần" BẮT BUỘC kèm input controls (ràng buộc, kiểm tra, xác nhận) vì hệ không còn redundancy. Ghi rõ *ai* nhập (vai trò tại nguồn), *ở đâu*, *bao nhiêu lần* = thông tin role/quyền. **Screens-to-Transactions**: tỉ lệ màn hình ERP/legacy × volume để dự báo độ khó + đo "fit".
- **Four Output Alternatives** (Ch 5): standard reports/queries, customized reports, intranet, data warehouse. Query thường được xử lý như transaction ⇒ **capacity-plan đầu ra** trước go-live. Thiết kế màn hình chính theo **vai trò** (role-specific portal), phân tầng expert vs casual. Mỗi module liệt kê báo cáo chuẩn + ad hoc.
- **Big Bang vs Phased** (Ch 11): contingency theo size/complexity, hierarchy/control, số module × module fit. Cần cross-module (ATP) ngay ⇒ big bang. Luôn test **interface giữa các module** (SVT), không chỉ từng module.

### Sau go-live, đào tạo, rủi ro
- **Stabilization + metric-vs-goal** (Ch 12): 3-9 tháng hiệu năng tụt; lập support organization; mỗi benefit = **metric** có baseline + owner + quy về ERP (không chỉ goal); soát implementation compromise (security, báo cáo); dùng Deloitte checklist (Yes/No) làm acceptance criteria hậu triển khai.
- **Training** (Ch 13): gắn vào mọi giai đoạn, cho cả user lẫn implementor; trong giờ làm + **super users** + **script-based materials** (dẫn từng bước qua trọn giao dịch = nguồn viết user story có ngữ cảnh); ngân sách ≥10%.
- **E-commerce building blocks** (Ch 14): ERP (thông tin) + EDI/WFT + user access. **Configuration engine** chặn lỗi đầu vào ("không cho đặt nếu còn lỗi"); EDI cho volume lớn, WFT cho originator ít; ERP-to-ERP cần chung MAPs; MIT cần "một PO/một invoice".
- **Risk Matrix** (Ch 15): giai đoạn vòng đời × (technical/business/organizational). Ưu tiên **organizational > business > technical**. Đặc tả **volume requirement** cụ thể + network/computing capacity khớp (bài học FoxMeyer 10.000 vs 420.000).

---

## Chapter Index

| # | Tiêu đề | Framework chính |
|---|---------|-----------------|
| [ch01](chapters/ch01-introduction.md) | Giới thiệu | Eight Value-Creation Mechanisms, ERP Life-Cycle Model |
| [ch02](chapters/ch02-systems-technology-background.md) | Nền tảng hệ thống & công nghệ | As Is/To Be, Best Practices vs Obliteration, Switch Setting |
| [ch03](chapters/ch03-erp-systems-background.md) | Nền tảng hệ thống ERP | MAPs, Best of Breed, BOPSE |
| [ch04](chapters/ch04-erp-data-input.md) | Nhập liệu đầu vào | Five Reengineering Sources, Screens-to-Transactions |
| [ch05](chapters/ch05-erp-output-capabilities.md) | Năng lực đầu ra | Four Output Alternatives, ERP Portals |
| [ch06](chapters/ch06-technology-enabled-vs-clean-slate-reengineering.md) | Technology Enabled vs Clean Slate | Technology Enabled, Clean Slate, Sequencing |
| [ch07](chapters/ch07-deciding-to-go-erp.md) | Quyết định triển khai ERP | Four Business Case Rationales, Wagle's 5-Step NPV |
| [ch08](chapters/ch08-choosing-an-erp-system.md) | Lựa chọn hệ thống ERP | Requirements Analysis, Gap Analysis, Weighted Evaluation |
| [ch09](chapters/ch09-change-processes-or-software.md) | Đổi quy trình hay đổi phần mềm | Small-r vs Big-R, Reengineering Policy |
| [ch10](chapters/ch10-choosing-standard-maps.md) | Chọn MAPs chuẩn | MAPs, Majority/Borda/Pareto/Dictatorship |
| [ch11](chapters/ch11-big-bang-versus-phased.md) | Big Bang vs Phased | Big Bang, Phased, Waved, SVT, Contingency |
| [ch12](chapters/ch12-after-going-live.md) | Sau go-live | Stabilization, Implementation Compromise, Balanced Scorecard |
| [ch13](chapters/ch13-training.md) | Đào tạo | Super Users, Script-based, Training the Implementor |
| [ch14](chapters/ch14-erp-electronic-commerce.md) | ERP & thương mại điện tử | EDI/WFT, Configuration Engine, VMI, BTO, MIT |
| [ch15](chapters/ch15-erp-risk-success-failure.md) | Rủi ro ERP | Risk Matrix, Technical/Business/Organizational risk |

## Topic Index
- **As Is / To Be** → ch02, ch08, ch09
- **Available to Promise (ATP)** → ch07, ch11
- **Báo cáo & đầu ra / reports / data warehouse** → ch05, ch12
- **Best of breed / vendor selection** → ch03, ch08
- **Big bang / phased / waved** → ch11
- **Business case / rationale / NPV** → ch07
- **Data input controls / nhập liệu** → ch04
- **Data conversion / migration** → ch12
- **E-commerce / EDI / WFT / configuration engine** → ch14
- **Life cycle ERP** → ch01, ch07–ch13
- **MAPs (Models, Artifacts, Processes)** → ch03, ch08, ch10
- **Master data / danh mục / chuẩn hóa** → ch02, ch10
- **Modules chuẩn (FI/CO/MM/PP/SD/HR)** → ch03
- **Phân quyền / security / portal** → ch05, ch12, ch14
- **Reengineering (small-r/big-R, clean slate)** → ch06, ch09
- **Risk / success & failure factors** → ch15
- **Stabilization / sau go-live** → ch12
- **Switch setting / tham số hệ thống** → ch02, ch10
- **Training / super users** → ch13
- **Value creation / integration** → ch01

## Supporting Files
- [glossary.md](glossary.md) — thuật ngữ ERP (song ngữ Anh-Việt, sắp xếp ABC).
- [patterns.md](patterns.md) — các kỹ thuật/mẫu thiết kế (When / How / Trade-offs).
- [cheatsheet.md](cheatsheet.md) — luật quyết định, bảng đánh đổi, ngưỡng số, module chuẩn (file giá trị nhất).

---

## Dùng cùng skill erp-ba-core
Skill này là **tri thức nền ERP** (background knowledge base) cho skill viết tài liệu BA **erp-ba-core** (thư mục anh em `../erp-ba-core`). Khi erp-ba-core cần đối chiếu một chức năng với chuẩn ERP — đặt tên module, dựng MAPs, chọn input controls, thiết kế báo cáo/phân quyền/tham số, hay nghiệm thu checklist — hãy tra skill này để lấy thuật ngữ, framework và luật quyết định đã được chuẩn hóa từ sách O'Leary.

## Scope & Limits
Skill chỉ phủ nội dung cuốn sách (ERP tới ~2000: SAP R/3, Oracle Applications, BAAN, PeopleSoft, J.D. Edwards). Một số hình và bảng trong bản PDF gốc bị mất nội dung đồ họa khi trích xuất (chỉ còn caption); các chương mô tả ý nghĩa từ văn bản xung quanh thay vì tái dựng hình, và ghi chú rõ chỗ bảng bị khuyết số liệu thay vì bịa. Để áp vào codebase/sản phẩm cụ thể, kết hợp với skill erp-ba-core và công cụ dự án.
