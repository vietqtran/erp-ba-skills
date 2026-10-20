---
name: elbardan-erp-governance-audit
description: "Knowledge base tiếng Việt từ sách \"Enterprise Resource Planning, Corporate Governance and Internal Auditing: An Institutional Perspective\" (Hany Elbardan & Ahmed Othman Rashwan Kholeif, 2017). DÙNG SKILL NÀY khi bạn hoặc một agent cần kiến thức ERP chuẩn để viết/nghiệm thu tài liệu đặc tả: ERP là gì, module & quy trình chuẩn ERP, control assumptions (giả định kiểm soát), RBAC & Segregation of Duties, maker-checker, audit trail, danh mục/master data, tham số hệ thống, báo cáo kiểm soát, quyết định reengineer vs customise, hay checklist elicitation/nghiệm thu. EN: Pull this ERP governance & internal-control knowledge base whenever a BA or agent writes ERP requirement/spec documents and needs standard ERP concepts, control design, permissions/SoD, master data, parameters, reports, or ERP-standard process flows — so specs don't drift from intent, over/under-scope, conflict, or stay too vague to code."
---

<!-- argument-hint: [chủ đề, tên framework, hoặc số chương, vd: control assumptions / SoD / ch06] -->

# ERP, Corporate Governance & Internal Auditing (Elbardan & Kholeif)
**Tác giả**: Hany Elbardan & Ahmed Othman Rashwan Kholeif | **Trang**: ~360 | **Chương**: 12 | **Tạo ngày**: 2026-10-20

Đây là kho kiến thức ERP (khái niệm, kiểm soát, phân quyền, quy trình chuẩn) rút từ một nghiên cứu học thuật 4 tình huống ở Ai Cập (2 công ty, 2 ngân hàng; SAP & Oracle). Giá trị cho BA: sách mô tả rất cụ thể **ERP thực thi kiểm soát thế nào** — đủ chi tiết để biến thành control/non-functional requirements code được.

## Cách dùng skill này
- **Không tham số** — nạp các framework cốt lõi bên dưới để tham chiếu.
- **Theo chủ đề** — hỏi `control assumptions`, `SoD`, `maker-checker`, `CAVAIR`, `reengineer vs customise`... agent sẽ tìm và đọc chương liên quan.
- **Theo chương** — hỏi `ch06` để nạp đúng chương đó.
- **Duyệt** — hỏi "có những chương nào?" để xem Chapter Index.

Khi bạn hỏi một chủ đề không có trong Core Frameworks dưới đây, agent sẽ đọc file chương liên quan trước khi trả lời. Tra cứu nhanh: `cheatsheet.md`; tra thuật ngữ: `glossary.md`; tra kỹ thuật: `patterns.md`.

---

## Core Frameworks & Mental Models

### 1. ERP mang "logic kiểm soát" — nguyên lý nền
ERP không trung lập: mỗi lựa chọn thiết kế của nhà cung cấp thành "luật" ràng buộc người dùng. **Institutional logic** của ERP có nguyên lý = **control**, với ba giả định nền: **standardisation**, **visibility**, **integration**. Hệ quả cho BA:
- Tách **mục tiêu kiểm soát** (giữ nguyên) khỏi **cơ chế thực hiện** (đổi theo hệ thống) — chống tài liệu lệch khỏi yêu cầu gốc.
- Một quy trình phải **auditable** (để lại vết, gắn kiểm soát) *trước khi* cho chạy. "Governance rules vẽ hướng dẫn, ERP thực thi quy trình có tính tới các quy tắc đó."

### 2. Control Assumptions — checklist "đã chuẩn ERP chưa" (11 giả định)
Bộ hợp nhất ở Ch 10 gồm **11 giả định kiểm soát**; mỗi tình huống dùng một tập con (IC 9; NC/NB/IB 10). Dùng làm checklist nghiệm thu từng chức năng, trả lời yes/no + nêu cơ chế:
**integration · standardisation · automation · multiple methods of control · preventive controls · compensating controls · continuous monitoring · data security · centralisation · data consistency · transparency & visibility.** Đừng ép đủ 11 cho chức năng nhỏ — chọn theo vùng rủi ro.

### 3. Bốn loại kiểm soát ERP — phân định code vs config
**Inherent** (có sẵn, không code) · **Configurable** (cấu hình lúc customise) · **Security** (phân quyền + SoD) · **Reporting** (báo cáo chuẩn/ad hoc). Gắn nhãn mỗi kiểm soát trong spec để dev biết việc phải làm. Lưu ý: phần lớn khối lượng customise thực tế rơi vào vùng **reporting**.

### 4. Phân quyền chuẩn ERP: RBAC + SoD + maker-checker
- **RBAC 2 lớp**: *function security* (menu/chức năng được truy cập) + *data security* (phạm vi dữ liệu được xem/sửa). "Chỉ thấy thông tin liên quan công việc" → chống thông đồng.
- **Segregation of Duties (SoD)**: liệt kê cặp vai trò không được đồng nắm (vd nhập liệu + phê duyệt); kèm report dò xung đột SoD chạy định kỳ.
- **Maker-checker**: màn hình không đi tiếp đến khi có *approval + validation*. ERP mặc định có thể thiếu → đặc tả như yêu cầu customisation có chủ đích.
- **Two-factor authentication** cho chức năng rủi ro cao. Giám sát liên tục thay đổi quyền theo luân chuyển nhân sự (rủi ro cao nhất).

### 5. Kiểm soát phòng ngừa > phát hiện — viết thành luật if/else
ERP biến kiểm soát thành preventive. Viết code-able: chặn lệnh sản xuất nếu tồn kho vật tư < định mức; chặn post vào kỳ kế toán đã khóa; chặn post hóa đơn sai mã khách; chặn đặt hàng nhà cung cấp từng giao lỗi. Thiết kế luồng override/ngoại lệ hợp lệ.

### 6. Dữ liệu & danh mục chuẩn (master data + NFR)
- **Single data entry point**: nhập một lần, tự lan sang module; nghiệp vụ phi tài chính tự sinh bút toán.
- **Standard chart of accounts** + định dạng dữ liệu thống nhất → nền của data consistency & consolidation (tránh "nhiều giá trị cho cùng một dữ liệu").
- **CAVAIR** làm tiêu chí nghiệm thu dữ liệu: Complete, Accurate, Valid, Restricted Access.
- **Audit trail** là NFR bắt buộc: lưu ai/khi nào/tại sao, truy ngược về GL & sub-ledger.

### 7. Quyết định Reengineer vs Customise/Localise vs Workaround
Quy trình không customise được / sai / bất hợp lệ → **reengineer** về chuẩn (auditable). Lệch do luật địa phương (thuế) → **customise/localise** có kiểm soát. **Tránh workaround** để giữ thao tác bất hợp lệ — nó phá minh bạch. Luôn ghi rõ lựa chọn + lý do trong tài liệu.

### 8. Vòng đời & con người (yếu tố quyết định thành/bại)
Khác biệt lớn nhất giữa ca thành công (IC, IB) và thất bại (NC, NB): **đưa kiểm soát/kiểm toán vào từ giai đoạn requirements** (chọn module/vendor, user management, verify data migration, super users) + **change management plan** + đào tạo thật + tránh parallel-run không kiểm soát.

### 9. Elicitation có kỷ luật (chống lệch/thừa/thiếu/mơ hồ)
Áp **directed content analysis**: khởi đầu từ template/checklist dựng sẵn từ chuẩn ERP, cho yêu cầu mới của khách nổi lên và bổ sung. Dùng **6 nhóm câu hỏi + bộ câu hỏi theo vai trò** (CIA, auditor, quản lý ERP, vendor, IT, kế toán, GĐ tài chính) làm agenda gửi trước. **Triangulate** ≥2 nguồn + **member check**. Gắn mỗi yêu cầu vào **coding scheme 5 nhóm** — nhãn trống = nghi thiếu chức năng. Luôn hỏi "ai chịu trách nhiệm" (RACI).

### 10. Phản ứng thể chế (quản lý thay đổi)
Truy nguồn mỗi yêu cầu về **coercive** (luật, bắt buộc) / **normative** (chuẩn nghề) / **mimetic** (bắt chước thị trường). Lường phản ứng người dùng theo **5 chiến lược Oliver**: acquiescence → compromise → avoidance → defiance → manipulation, mỗi loại cần tactic change management khác nhau.

---

## Chapter Index

| # | Tiêu đề | Framework chính |
|---|---------|-----------------|
| [ch01](chapters/ch01-introduction.md) | Giới thiệu | Control logic, RQ1–RQ5, ERP = dự án thay đổi tổ chức |
| [ch02](chapters/ch02-erp-internal-auditing-corporate-governance.md) | ERP, Kiểm toán nội bộ & Quản trị công ty | ERP definition, Hakim & Hakim risk, COSO, SoD, Continuous Auditing, CAAT |
| [ch03](chapters/ch03-legitimacy-internal-auditing-practice.md) | Tính chính danh của kiểm toán nội bộ | Isomorphism, Oliver 5 responses, pragmatic/moral legitimacy, 9 khía cạnh IAF |
| [ch04](chapters/ch04-institutional-framework-iaf-adaptation.md) | Khung thể chế cho thích nghi IAF | Institutional logic 4 chiều, coercive/normative/mimetic, loose coupling |
| [ch05](chapters/ch05-interpretive-approach-data-collection.md) | Cách tiếp cận diễn giải (phương pháp) | Directed content analysis, triangulation, case study protocol, member checks |
| [ch06](chapters/ch06-findings-case-study-1-international-company.md) | Tình huống 1 — Công ty quốc tế (IC, SAP) | 9 control assumptions, 4 loại kiểm soát, authorisation profile, reengineer vs localise |
| [ch07](chapters/ch07-case-study-2-national-company.md) | Tình huống 2 — Công ty quốc gia (NC, SAP) | 10 control assumptions, single data entry, preventive if/else, workaround/decoupling |
| [ch08](chapters/ch08-case-study-3-national-bank.md) | Tình huống 3 — Ngân hàng quốc gia (NB, Oracle) | RBAC 2 lớp, maker-checker, approval workflow, processing constraints, parallel-run |
| [ch09](chapters/ch09-case-study-4-international-bank.md) | Tình huống 4 — Ngân hàng quốc tế (IB, Oracle) | Early involvement, CAVAIR, FIM/BIM, black-box test, risk-based audit, CAAT/ACL |
| [ch10](chapters/ch10-cross-case-analysis-discussion.md) | Phân tích đa tình huống | 11 control assumptions hợp nhất, meta-matrix 4 ca, reengineer vs customise |
| [ch11](chapters/ch11-conclusion.md) | Kết luận | Khung thích nghi IAF, integrated internal audit, horizontal vs vertical, risk-based |
| [ch12](chapters/ch12-appendices-protocol-interview-guide.md) | Phụ lục — protocol, câu hỏi, coding scheme | Case study protocol, 6 nhóm câu hỏi, coding scheme 5 nhóm, 5 tiền đề thể chế |

## Topic Index
- **Audit trail / log** → ch02, ch06, ch08, ch09
- **CAVAIR (nghiệm thu dữ liệu)** → ch09
- **Change management / cutover / parallel-run** → ch07, ch08, ch10, ch11
- **Control assumptions (9/10/11)** → ch06, ch07, ch08, ch09, ch10
- **COSO / internal control** → ch01, ch02, ch08
- **Data migration / integrity** → ch09, ch10
- **ERP concept / module / tích hợp** → ch01, ch02, ch08, ch10
- **Elicitation / phỏng vấn / coding scheme** → ch05, ch12
- **Institutional theory / legitimacy / Oliver** → ch01, ch03, ch04, ch10
- **Maker-checker / approval workflow** → ch08, ch09
- **Master data / chart of accounts** → ch06, ch10
- **Preventive controls (if/else)** → ch02, ch06, ch07
- **RACI / ai chịu trách nhiệm** → ch11, ch12
- **RBAC / phân quyền / data security** → ch08, ch09, ch10, ch11
- **Reengineer vs customise/localise** → ch06, ch10, ch11
- **Reports / exception / continuous monitoring** → ch06, ch08, ch10, ch12
- **Risk-based auditing / risk map** → ch09, ch11
- **Segregation of Duties (SoD)** → ch02, ch06, ch07, ch08, ch09, ch10
- **SOX / Basel / PCI DSS / compliance driver** → ch02, ch08, ch09, ch10

## Supporting Files
- [glossary.md](glossary.md) — thuật ngữ chính (EN + gloss tiếng Việt), xếp theo chữ cái
- [patterns.md](patterns.md) — các mẫu kỹ thuật thiết kế chức năng/kiểm soát chuẩn ERP
- [cheatsheet.md](cheatsheet.md) — quy tắc quyết định, bảng đánh đổi, ngưỡng, dấu hiệu cảnh báo (tra trước)

---

## Dùng cùng skill `erp-ba-core`
Skill này là **kiến thức nền ERP** (background knowledge). Nó bổ trợ cho skill viết tài liệu BA `erp-ba-core` (thư mục anh em `../erp-ba-core`): khi `erp-ba-core` cần tra "chuẩn ERP" cho một khái niệm/kiểm soát/quy trình (ví dụ cần biết control assumptions, SoD, maker-checker, CAVAIR, cách quyết định reengineer vs customise), hãy đọc skill này để lấy khung chuẩn, rồi áp vào template tài liệu của `erp-ba-core`.

## Scope & Limits
Skill chỉ phủ nội dung sách (nghiên cứu học thuật về *thích nghi của kiểm toán nội bộ sau ERP*, bối cảnh Ai Cập, SAP & Oracle). Đây **không** phải tài liệu triển khai SAP/Oracle chính thức, cũng không thay cho kiến thức nghiệp vụ ngành cụ thể (xây dựng, logistics...). Các sơ đồ/bảng ma trận trong nguồn (Fig 4.x, 6.1, 10.x) bị công cụ trích xuất làm phẳng nên được tái dựng từ văn xuôi xung quanh, không sao chép bố cục gốc; tham chiếu chéo mục trong sách có vài chỗ lỗi biên tập (đã bỏ qua). Để code trong codebase thực tế, kết hợp với công cụ/chuẩn của dự án.
