---
name: parthasarathy-erp-fundamentals
description: "Kho kiến thức ERP nền tảng từ sách \"Enterprise Resource Planning: A Managerial and Technical Perspective\" của S. Parthasarathy (2007). DÙNG skill này bất cứ khi nào bạn hoặc một agent cần kiến thức ERP chuẩn để thiết kế chức năng ERP-standard hoặc viết tài liệu đặc tả đủ chi tiết để code: ERP là gì & tính tích hợp, các module chuẩn (Finance, HR, Materials Management, Sales & Distribution), quy trình MRP/MRP II, vòng đời triển khai 11 bước, Gap Analysis, lựa chọn phần mềm & vendor, SCM, CRM, mô hình hóa nghiệp vụ bằng UML, controls/audit, master data, phân quyền, tham số hệ thống, báo cáo. English: Knowledge base from Parthasarathy's ERP book — consult when you need standard ERP knowledge to design ERP-standard functions, cover functional scope, or write code-ready specs (ERP concepts, standard modules, MRP/MRP II, implementation lifecycle, software/vendor selection, SCM, CRM, UML business modeling, controls, reports). Là nền kiến thức ERP cho skill erp-ba-core."
---

<!-- argument-hint: [chủ đề, tên framework, hoặc số chương, vd: "MRP", "Gap Analysis", "ch05"] -->

# Enterprise Resource Planning: A Managerial and Technical Perspective
**Tác giả**: S. Parthasarathy (New Age International, 2007) | **Số trang**: ~140 | **Số chương**: 12 | **Tạo ngày**: 2026-10-20

## Cách dùng skill này (How to Use)

- **Không tham số** — nạp các framework ERP cốt lõi bên dưới để tham chiếu nhanh.
- **Với một chủ đề** — hỏi về `MRP`, `Gap Analysis`, `module SD`, `CRM`...; tôi tìm và đọc chương liên quan.
- **Với số chương** — hỏi `ch05`; tôi nạp đúng chương đó.
- **Duyệt** — hỏi "có những chương nào?" để xem toàn bộ Chapter Index.

Khi bạn hỏi một chủ đề chưa có trong phần Core bên dưới, tôi sẽ đọc file chương tương ứng trước khi trả lời. Đây là sách giáo khoa ERP tổng quan (managerial + technical), hữu ích nhất để BA hiểu khái niệm, module, quy trình chuẩn và thuật ngữ ERP — không phải tài liệu cấu hình một sản phẩm cụ thể.

---

## Core Frameworks & Mental Models

**ERP là gì (Ch1).** **Enterprise Resource Planning (ERP)** — hoạch định nguồn lực doanh nghiệp: một phần mềm đóng gói tích hợp mọi phòng ban vào **một chương trình chạy trên một CSDL chung**. Giá trị nằm ở chữ "enterprise" (tích hợp), không phải "planning/resource". Ưu điểm số một là **Integration / automatic data updation** — một giao dịch tự động cập nhật mọi nghiệp vụ liên quan (real-time). Bốn lợi ích trực tiếp: **Business Integration, Flexibility, Better Analysis & Planning, Use of Latest Technology**. Nhớ: ERP là **back-office** (transaction-based), CRM là **front-office**; ERP ghi lại cái đã xảy ra, không "thông minh" như **APS**.
→ *Khi viết spec*: mô tả luồng dữ liệu tự cập nhật liên module, không đặc tả từng chức năng như ốc đảo.

**Tiến hóa & logic hoạch định (Ch2).** Chuỗi IC → BOM → **MRP** → **MRP II** → ERP → ERP II. **MRP (Material Requirements Planning)**: từ **MPS (Master Production Schedule)** dùng **BOM** để "nổ" (explosion) thành purchase/production order cho linh kiện, có tính lead-time & lot-size. Phân biệt **independent demand** (thành phẩm — dự báo) vs **dependent demand** (linh kiện — tính toán). **MRP II** thêm mô phỏng "what-if" và hoạch định theo cả đơn vị lẫn tài chính; ERP thêm cả nguồn lực nhà cung cấp. Sáu chức năng nghiệp vụ lõi của ERP = khung phân rã module.

**Module & bao phủ chức năng (Ch3).** Bốn module phổ biến, dùng danh mục chức năng con làm **checklist "cover đủ"**:
- **Finance** (5): Accounting · Investment mgmt · **Cost controlling** · **Treasury management** · Planning & forecasting.
- **HR**: Managerial (Planning/Organizing/Directing/Controlling) + Operative (Employment/**HRD**/Compensation).
- **Materials Management (MM)** (7): Inventory · MRP · Purchasing · Warehouse · Vendor evaluation · Invoice verification · Product costing.
- **Sales & Distribution (SD)** (6): Selling · Shipping · Billing · **Master Data Management** · Order Management · Pricing. Luồng chuẩn **Sales → Shipping (MM) → Billing (Finance)** — luôn vẽ liên module. Phân loại đơn **Normal vs Abnormal**; áp **ABC analysis** cho tồn kho.
Một ERP đầy đủ cần: phần mềm/module · danh mục (master data) · nghiệp vụ · phân quyền & tham số hệ thống · báo cáo.

**Lựa chọn phần mềm (Ch4).** Quy trình 4 giai đoạn: Phase 1 dựng **requirements profile** → "Top Ten List" (<3 tuần); Phase 2 lọc còn **2–4** ứng viên (<1 tháng); Phase 3 **demo do khách điều khiển** bằng danh sách **50–100 chức năng** bắt buộc + đàm phán; Phase 4 implementation planning. **Cost Benefit Analysis** là analysis để *quyết định*, bất lợi thì **dừng dự án** — không phải justification. Trọng số chọn vendor: Reputation 26% · Functionality 24% · Project cost 23% · Complete solution 16% · Future maintenance 11%.

**Triển khai (Ch5).** Ba cách: **Big Bang / Location-wise / Module-wise**. Ba góc nhìn: **Organizational / Business / Technological**. Vòng đời **11 bước**: Project Planning → Vendor Identification → Evaluation → **Gap Analysis** → Reengineering → **Customization** → Team Training → Testing → Going Live → End-User Training → Maintenance. Nguyên tắc: **"fit the organization around the software"**, **không bao giờ sửa base**, customize càng cao lợi ích càng thấp. **BPR** (Michael Hammer) = "radical redesign". ERP có thể **không để lại chứng từ**, sinh dữ liệu tự động, lỗi lan rộng → bắt buộc đặc tả **audit trail, control procedure, phân quyền** trong NFR. **Benefits realization** qua 3 cấp, mất vài tháng tới ~1 năm. Ghi **CSF** và cam kết lãnh đạo vào phần giả định/ràng buộc.

**Mở rộng & công nghệ (Ch6–10).** **OS/nền tảng** là NFR nền (Unix/Windows/Linux; tính **TCO**, migration = dự án 6 pha META Group ~7 tháng). **SCM (Supply Chain Management)**: 4 yếu tố (Location/Production/Inventory/Transportation), 3 dòng chảy (product/information/financial — thông tin chảy ngược chiều hàng), 3 cấp quyết định (strategic/tactical/operational); ERP sinh giao dịch, SCM tối ưu — bổ sung nhau. **CRM**: 3 thành phần **Operational/Analytical/Collaborative** + 3 góc nhìn Business/Technology/Customer; chiến lược trước, công nghệ sau; quy trình **Quote-to-Cash**, **Requisition-to-Pay**. **.NET/business rules**: ERP hiện đại = chuẩn hóa + **tách validation rules khỏi processing rules** (dynamic choreography), loosely coupled, managed code. **Vendors**: SAP dẫn đầu (~25%); chọn theo **ngành dọc + ít tùy biến nhất**.

**Mô hình hóa để code được (Ch12).** **UML** là ngôn ngữ chung giữa business analyst và system analyst. 5 phần tử: **business actor** (ngoài) · **business worker/role** (trong) · **business entity** · **business use case** · organizational unit. 4 sơ đồ ↔ 4 góc nhìn: **Use Case** (bối cảnh & actor) · **Activity + swimlanes** (luồng & ai làm gì) · **Class** (entity & quan hệ) · **Sequence** (tương tác các bước). Hiểu quy trình trước → reengineering; không hiểu → chỉ automation. Mỗi chức năng ERP nên có đủ bộ sơ đồ này — đúng mức "chi tiết để code ngay".

---

## Chapter Index

| # | Tiêu đề | Framework chính |
|---|-------|----------------|
| [ch01](chapters/ch01-introduction-to-erp.md) | Giới thiệu về ERP | 4 lợi ích ERP; Integration; back/front-office; APS |
| [ch02](chapters/ch02-evolution-of-erp.md) | Sự tiến hóa của ERP | MRP; MRP II; MPS→BOM explosion; ERP II; 3 manufacturing strategies |
| [ch03](chapters/ch03-erp-modules.md) | Các module của ERP | Finance/HR/MM/SD; ABC analysis; 3 motives tồn kho |
| [ch04](chapters/ch04-erp-software-selection.md) | Lựa chọn phần mềm ERP | Quy trình 4 phase; requirements profile; cost-benefit; trọng số vendor |
| [ch05](chapters/ch05-erp-implementation.md) | Triển khai ERP | 11 phases; Gap Analysis; Customization; BPR; CSF; benefits realization |
| [ch06](chapters/ch06-operating-system-impact.md) | Tác động của Hệ điều hành | Functions of OS; TCO; META 6-phase migration |
| [ch07](chapters/ch07-supply-chain-management.md) | Quản trị Chuỗi cung ứng (SCM) | 4 elements; 3 flows; 3 cấp quyết định; ERP vs SCM |
| [ch08](chapters/ch08-erp-and-crm.md) | ERP và CRM | 3 components CRM; 3 dimensions; data mining/warehouse |
| [ch09](chapters/ch09-erp-and-dotnet.md) | ERP và .NET | ERP hoàn hảo; managed code; CLR/CIL; business rules |
| [ch10](chapters/ch10-erp-vendors.md) | Các nhà cung cấp ERP | mySAP ERP 4 solutions; SAP R/3; vendor mapping |
| [ch11](chapters/ch11-erp-case-studies.md) | Các tình huống triển khai | Case template; KPI trước/sau; Big Bang; ETO |
| [ch12](chapters/ch12-business-modeling-uml.md) | Mô hình hóa nghiệp vụ bằng UML | 5 notation; 4 diagram; swimlanes; use case |

## Topic Index

- **ABC analysis / tồn kho** → ch03, ch07
- **APS / cycle time / lead-time** → ch01
- **Audit trail / controls / phân quyền** → ch05, ch08
- **BOM / component explosion** → ch02, ch11
- **BPR / reengineering** → ch05, ch12
- **Benefits realization** → ch05
- **Business rules / .NET / managed code / CLR** → ch09
- **CAD / CAM** → ch07
- **Case studies / KPI** → ch11
- **Change management** → ch05, ch06, ch11
- **Cost Benefit Analysis** → ch04
- **CRM (Operational/Analytical/Collaborative)** → ch08
- **Customization** → ch04, ch05
- **Data mining / data warehouse / OLAP** → ch08
- **Dependent vs independent demand** → ch02
- **ERP concepts / Integration** → ch01
- **ERP II** → ch02
- **Finance module / Treasury / Cost controlling** → ch03
- **Gap Analysis** → ch05
- **HR module / HRD** → ch03
- **Implementation lifecycle (11 phases)** → ch05
- **Make-to-order / stock / assemble-to-order** → ch01, ch02
- **Master Data Management** → ch03, ch08
- **Materials Management (MM)** → ch03
- **MPS / MRP / MRP II** → ch02
- **Operating System / TCO / migration** → ch06
- **Pricing strategies** → ch03
- **Quote-to-Cash / Requisition-to-Pay** → ch08
- **Requirements profile / elicitation** → ch04
- **Sales & Distribution (SD)** → ch03
- **SCM (Supply Chain Management)** → ch07
- **SCM (Software Configuration Management)** → ch05
- **Selection process (4 phases)** → ch04
- **SOAP / XML Web services** → ch09
- **UML (use case / activity / class / sequence / swimlanes)** → ch12
- **Vendor selection / SAP / mySAP ERP** → ch04, ch10

## Supporting Files

- [glossary.md](glossary.md) — ~50 thuật ngữ ERP (Anh + gloss Việt + định nghĩa).
- [patterns.md](patterns.md) — 15 kỹ thuật/quy trình chuẩn ERP dạng When/How/Trade-offs.
- [cheatsheet.md](cheatsheet.md) — quy tắc quyết định, bảng đánh đổi, ngưỡng/con số, tells & smells, checklist bao phủ module.

## Dùng cùng skill erp-ba-core

Skill này là **nền kiến thức ERP** (background knowledge) cho skill viết tài liệu BA **`erp-ba-core`** (thư mục anh em `../erp-ba-core`). Khi `erp-ba-core` cần tra khái niệm ERP, module chuẩn, quy trình chuẩn, thuật ngữ, hoặc checklist bao phủ chức năng/controls/master data/báo cáo, hãy đọc skill này. Ở đây chỉ cung cấp *kiến thức*; việc dựng template tài liệu, checklist nghiệm thu và vòng lặp verify thuộc về `erp-ba-core`.

---

## Scope & Limits

Skill chỉ bao phủ nội dung cuốn sách (ERP tổng quan, cấp quản trị + kỹ thuật, bối cảnh ~2007; một số ví dụ công nghệ như .NET/SAP R/3 đã cũ). Dùng cho *kiến thức ERP chuẩn*, không thay cho cấu hình sản phẩm cụ thể hay quy định ngành/địa phương. Lưu ý trích xuất: nhiều Figure và vài tiêu đề mục bị làm phẳng/mất khi chuyển PDF→text; các chương có ghi chú rõ chỗ hình bị dẹt và không bịa chi tiết hình. Với đặc tả thực thi trong dự án, kết hợp skill `erp-ba-core` và công cụ/ngữ cảnh dự án của bạn.
