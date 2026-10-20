# Book notes — BP-13 Thay đổi, hủy booking và hoàn tiền

Working file (not published). It records the ERP standard taken from the books and where the RSD applies it.

- Process type (books/TOPICS.md §1): Order changes, cancellation, refunds; plus "Every process / every RSD"
- Topics: change control and time fences, processing constraints, maker-checker, SoD, audit trail, preventive controls,
  data input controls, reports and exceptions, feedback loops, parameters vs customisation, process modelling

## Shortlist (written before reading; about 8–12 chapters, at most 15)

| Chapter | Why (from the index summary) | Read with |
|---|---|---|
| Wallace ch09 | Five bedrock policies (roles, parameters, feedback), ATP — time fences and change policy | default + Bảng tham chiếu |
| Wallace ch10 | Forgiving vs unforgiving data | default |
| Wallace ch12 | Supplier scheduling, "silence is approval" | default |
| Wallace ch17 | ERP fundamentals: exception-driven feedback, one set of numbers | default |
| Elbardan ch02 | SoD, internal control basics | default |
| Elbardan ch06 | Four control types, audit trail, reporting controls | default |
| Elbardan ch07 | Preventive controls as if/else, multiple methods of control | default + Bảng tham chiếu |
| Elbardan ch08 | Maker-checker, approval hierarchy, processing constraints, RBAC | default + Khái niệm chính |
| Elbardan ch09 | Two-factor authentication, access risks | default |
| Parthasarathy ch08 | Quote-to-cash flow across modules | default |
| Parthasarathy ch12 | Actors vs workers, swimlane activity diagrams | default |
| O'Leary ch02 | Switch settings (parameters) before customisation | default |
| O'Leary ch04 | Data input controls, capture at the source | default |
| O'Leary ch05 | Outputs and reports | default |

## Notes

| # | Topic | Key point (paraphrased) | Applied in the RSD | Source |
|---|---|---|---|---|
| 1 | Time fences | Policies state who may change the schedule in which time zone; time fences must be configurable | Mốc ngày trước khởi hành quyết định mức phí (TS-01, QT-08, QT-09) | Wallace ch09 — books/wallace-erp-implementation/chapters/ch09-process-definition.md |
| 2 | Change control | Engineering-change policy: classify changes; who initiates, who sets the effective date, who executes | Phiếu yêu cầu thay đổi, phiên bản booking (mục 1.1, QT-24, KS-06) | Wallace ch09 — books/wallace-erp-implementation/chapters/ch09-process-definition.md |
| 3 | Processing constraints | Block add/update/delete/cancel beyond a control point; approved transactions hit all accounts at once | Khóa sửa trực tiếp booking (QT-02); cập nhật nguyên tử ở Bước 10 (QT-23) | Elbardan ch08 — books/elbardan-erp-governance-audit/chapters/ch08-case-study-3-national-bank.md |
| 4 | Preventive controls | Write preventive controls as if/else rules in the system; avoid workarounds outside the system | Phí hủy do hệ thống tính, không sửa tay (KS-01, QT-07); báo cáo đổi ngoài hệ thống (BC-03) | Elbardan ch07 — books/elbardan-erp-governance-audit/chapters/ch07-case-study-2-national-company.md |
| 5 | Maker-checker, approval hierarchy | The screen does not proceed without approval + validation; "submit for approval" routes to the right level | Duyệt giảm phí theo hạn mức (KS-02, QT-12); hóa đơn điều chỉnh luôn duyệt (KS-04) | Elbardan ch08 — books/elbardan-erp-governance-audit/chapters/ch08-case-study-3-national-bank.md |
| 6 | Multiple methods of control | One person enters, one approves, one confirms | Ba người khác nhau: lập yêu cầu, duyệt hoàn, lập lệnh chi (KS-05, TN-03 … TN-05) | Elbardan ch07 — books/elbardan-erp-governance-audit/chapters/ch07-case-study-2-national-company.md |
| 7 | Segregation of duties | List incompatible duty pairs; review SoD conflicts periodically and when a user's duties change | Bảng tách nhiệm vụ TN-01 … TN-08; rà soát hằng tháng (BC-06) | Elbardan ch02 — books/elbardan-erp-governance-audit/chapters/ch02-erp-internal-auditing-corporate-governance.md |
| 8 | Audit trail | Record who, when and why, traceable to GL and sub-ledgers | Lưu vết mọi thao tác (mục 8); phiên bản trước/sau (KS-06) | Elbardan ch06 — books/elbardan-erp-governance-audit/chapters/ch06-findings-case-study-1-international-company.md |
| 9 | Control types and reporting controls | Four control types; reporting controls (exceptions, reconciliation) are specified up front, not after go-live | Báo cáo ngoại lệ BC-03; phân loại kiểm soát ở mục 7 | Elbardan ch06 — books/elbardan-erp-governance-audit/chapters/ch06-findings-case-study-1-international-company.md |
| 10 | Feedback, "silence is approval" | Suppliers must report anticipated problems; no reply must not be read as acceptance | Hạn NCC phản hồi và leo thang (TS-15, KS-03); NCC từ chối (mục 2.6) | Wallace ch12 — books/wallace-erp-implementation/chapters/ch12-supply-chain-integration-phase-ii.md |
| 11 | Exception-driven feedback loop | Planner → scheduler → sales → customer when a promise cannot be kept | Các mốc hẹn giờ ở mục 2.4; thông báo khi quá hạn (mục 3.7) | Wallace ch17 — books/wallace-erp-implementation/chapters/ch17-appendix-a-fundamentals-of-erp.md |
| 12 | Data input controls | State who enters what, where, when; add an explicit confirmation step when an action does not complete itself | Thời điểm nhận yêu cầu và bằng chứng khách xác nhận (QT-03, QT-04) | O'Leary ch04 — books/oleary-erp-systems-lifecycle/chapters/ch04-erp-data-input.md |
| 13 | Unforgiving data | Data needing high accuracy (money, quantities) gets the most control effort | Số tiền hoàn, chỗ, phí phạt do hệ thống tính và kiểm tra (QT-35, QT-40) | Wallace ch10 — books/wallace-erp-implementation/chapters/ch10-data-integrity.md |
| 14 | Parameters vs customisation | Use switch settings before code changes; list parameters and defaults per function | Mục 5 tham số TS-01 … TS-24 | O'Leary ch02 — books/oleary-erp-systems-lifecycle/chapters/ch02-systems-technology-background.md |
| 15 | Two-factor authentication | Strong authentication for high-risk functions; access changes on staff rotation are the top access risk | Xác thực 2 lớp khi duyệt hoàn, lập lệnh chi, ký số (mục 8) | Elbardan ch09 — books/elbardan-erp-governance-audit/chapters/ch09-case-study-4-international-bank.md |
| 16 | Process modelling | Actors vs workers; swimlane activity diagram answers "who does what" | Mục 1.7 các bên tham gia; Hình 1, 3, 4 | Parthasarathy ch12 — books/parthasarathy-erp-fundamentals/chapters/ch12-business-modeling-uml.md |
| 17 | Quote-to-cash flow | Describe flows across modules, not functions in isolation | Mục 1.8 và 3.4: booking → NCC → dự toán → lịch thu → hóa đơn → hoàn tiền | Parthasarathy ch08 — books/parthasarathy-erp-fundamentals/chapters/ch08-erp-and-crm.md |
| 18 | Outputs and reports | List standard and ad hoc reports per function; prefer views over custom reports | Mục 3.8 báo cáo BC-01 … BC-06 | O'Leary ch05 — books/oleary-erp-systems-lifecycle/chapters/ch05-erp-output-capabilities.md |
