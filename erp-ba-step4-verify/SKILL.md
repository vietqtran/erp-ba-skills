---
name: erp-ba-step4-verify
description: "Bước 4 của bộ skill BA ERP — tự kiểm tài liệu BA (research, yêu cầu, SRS, đặc tả chức năng/báo cáo) trước khi review độc lập: chạy công cụ lint và ma trận truy vết, điền checklist Yes/No có bằng chứng, trả lời 4 câu hỏi bắt buộc (còn gì chưa rõ? cần xác nhận gì? đối chiếu yêu cầu ban đầu có lệch/thiếu/thừa? checklist và template đã đủ chưa?), săn mâu thuẫn và từ mơ hồ, sửa và lặp tới khi đạt (tối đa 3 vòng), rồi chuyển sang review độc lập. Nghiệm thu bằng checklist C4 và PASS/FAIL tự động. Dùng khi người dùng hỏi “kiểm tra lại tài liệu”, “còn thiếu gì không”, “có lệch yêu cầu không”, “bạn có thắc mắc gì không”, “có chỗ nào cần xác nhận không”, “checklist done chưa”, “template điền đủ chưa”, hoặc khi vừa viết xong tài liệu ở bước 1–3. English — self-verification of ERP BA documents against sources and checklists."
---

# Bước 4 — Tự kiểm tài liệu

Thuộc bộ skill BA ERP: `erp-ba-core` → `erp-ba-step1-research` → `erp-ba-step2-requirements` → `erp-ba-step3-specification` → **bước 4 (skill này)** → `erp-ba-step5-review`.

Đường dẫn: `<skill-dir>` = thư mục chứa file SKILL.md này; `<core>` = thư mục `erp-ba-core` nằm cạnh (`<skill-dir>/../erp-ba-core`). Không thấy `<core>` → báo người dùng cài đủ bộ skill.

## Mục tiêu & đầu ra

Tìm và sửa lệch, thiếu, thừa, mâu thuẫn, mơ hồ **trước khi** người khác review. Bước này chỉ có giá trị khi trung thực: một câu "Yes" không có bằng chứng tệ hơn một câu "No", vì nó che lỗi khỏi vòng sau.

| Đầu ra | Template | Nghiệm thu |
|---|---|---|
| `04-verification/verify-report-r<N>.md` (N = số vòng) | `<skill-dir>/assets/templates/04-verification/verify-report.md` (lệnh `checklist --out` tự tạo từ template) | `<skill-dir>/references/checklists/C4-verification.md` + chạy lại checklist của các bước đã làm (C1 ở skill bước 1, C2 ở bước 2, C3/C3F/C3R ở bước 3) |

## Quy trình một vòng

1. **Đọc lại nguồn gốc** của phạm vi kiểm: biên bản (mục 3 nguyên văn), file khách hàng, issue-log (câu trả lời mới). Không chỉ đọc requirement-register — chính register cũng có thể đã lệch.

2. **Chạy công cụ:**
   ```bash
   python3 <core>/scripts/ba.py lint <root>
   python3 <core>/scripts/ba.py trace <root>
   python3 <core>/scripts/ba.py checklist <root> --step all --round <N> --out <root>/04-verification/verify-report-r<N>.md
   ```
   `--step all` sinh checklist của mọi bước đã có tài liệu + C4. Ghi số lỗi/cảnh báo vào mục 2 của báo cáo. Mỗi cảnh báo VAGUE (từ mơ hồ) phải được xem: sửa, hoặc giữ nếu từ đó có định nghĩa/số đo ngay trong câu.

3. **Trả lời 4 câu hỏi bắt buộc (mục 3 của báo cáo) bằng nội dung cụ thể:**
   1. *Bạn có thắc mắc hay chưa rõ chỗ nào không?* — liệt kê từng chỗ (file §), vì sao chưa rõ, Q đã tạo. "Không có" chỉ hợp lệ khi lint không còn marker mở và bạn đã thử vai dev/QA (C3F-30/31).
   2. *Có chỗ nào cần xác nhận lại không?* — mọi `[ĐỀ XUẤT]`, `[GIẢ ĐỊNH]`, CFL chưa có DEC, con số mặc định do BA đặt.
   3. *Đối chiếu yêu cầu ban đầu: lệch / thiếu / thừa?* — kỹ thuật ở dưới; điền ba bảng.
   4. *Checklist đã xong? Template đã điền đủ?* — số Yes/No/N/A và lỗi lint.

4. **Điền checklist mục 4:** mỗi câu Yes (kèm bằng chứng: file + mục/ID), No (kèm hành động sửa), N/A (kèm lý do). Với C3F/C3R, trả lời cho **từng** chức năng.

5. **Ghi phát hiện** (VF-R<N>-NN): Critical (sai nghiệp vụ/luật, thiếu chức năng được yêu cầu, không code được) / Major (mơ hồ, mâu thuẫn, thiếu quy tắc/trường/luồng quan trọng) / Minor (trình bày, thuật ngữ).

6. **Sửa** mọi "No" và phát hiện sửa được ngay (theo hướng dẫn của skill bước tương ứng, ví dụ `erp-ba-step3-specification` cho đặc tả). Thông tin chỉ khách hàng biết → Q (không tự trả lời). Chạy lại lint, trace, cập nhật kết quả checklist.

7. **Kết luận:** `python3 <core>/scripts/ba.py status <root>/04-verification/verify-report-r<N>.md` → PASS hoặc FAIL.

## Kỹ thuật tìm "Thiếu – Thừa – Lệch"

- **Thiếu:** `traceability.md` liệt kê REQ chưa phủ; `trace` liệt kê dòng biên bản chưa xử lý; bảng 5 thành phần (srs-overview §3.1) còn ô trống; so mục 4–5 của file quy trình chuẩn (`<core>/references/processes/`) với chuỗi chức năng (có nhập hàng mà không có trả hàng NCC → hỏi khách hàng có cần không).
- **Thừa:** chức năng/FR/BR/trường/màn hình không trỏ về REQ/DEC; FEAT dùng làm nguồn mà chưa có DEC; chi tiết khách hàng không yêu cầu. Xử lý: gắn `[ĐỀ XUẤT → Q-…]` hoặc xóa.
- **Lệch:** chọn ≥ 10 REQ (hoặc tất cả nếu < 30), đặt trích nguyên văn cạnh nội dung đặc tả tương ứng: ý nghĩa có bị mở rộng, thu hẹp, đổi điều kiện không? Chú ý số liệu, phạm vi áp dụng, ai làm, khi nào.

## Kỹ thuật săn mâu thuẫn

- Cùng một chứng từ: bộ trạng thái ở `document-types.md` với mục 7 của mọi FN đụng tới chứng từ đó (lint kiểm một phần).
- Cùng một vai trò: ma trận tổng hợp với mục 2 từng FN (lint kiểm).
- Cùng một trường (ví dụ "đơn giá"): `grep -rn "đơn giá" <root>/03-specification` — kiểu, số chữ số thập phân, làm tròn có giống nhau?
- Cùng một con số (ngưỡng, hạn mức): phải là một PRM duy nhất.
- Thuật ngữ: một khái niệm hai tên → thống nhất theo glossary.
- Hạch toán: cùng nghiệp vụ ở hai FN có dùng cùng tài khoản không.

## Vòng lặp & điều kiện dừng (điều phối bước 3 → 4 → 5)

- **FAIL** → sửa (bước 3 hoặc bước tương ứng) → vòng N+1 của skill này.
- **PASS** → chuyển `erp-ba-step5-review` (review độc lập bằng agent khác). Phát hiện Critical/Major của review → sửa → quay lại skill này (vòng mới) → review vòng mới.
- Tài liệu chỉ được đặt `status: Ready` khi đạt đủ: lint 0 Error; trace 0 lỗi (không REQ chưa phủ, không FN không nguồn, không FR thiếu AC); `status` = PASS; review độc lập 0 Critical/Major còn mở; 0 marker `[CẦN XÁC NHẬN]`/`[ĐỀ XUẤT]` còn mở.
- **Tối đa 3 vòng.** Sau 3 vòng vẫn còn mục chưa đạt → dừng và báo người dùng: đã đạt gì, còn gì, vì sao (thường là câu hỏi chỉ khách hàng trả lời được). Tài liệu giữ `In Review`, kèm danh sách câu hỏi gửi khách hàng (gom từ issue-log, nhóm theo người cần hỏi, phương án A/B). Lặp thêm không giải quyết được câu hỏi của khách hàng — chỉ tốn công và dễ dẫn tới "làm cho đạt".

## Quy tắc trung thực

- Không trả lời Yes cho câu chưa thực sự kiểm. Không kiểm được (thiếu nguồn) → No và ghi lý do.
- Không dùng N/A để né việc: N/A chỉ khi câu hỏi thật sự không áp dụng (ví dụ hạch toán cho chức năng danh mục).
- Không tự trả lời câu hỏi của khách hàng để checklist đạt. Không hạ tiêu chuẩn (sửa checklist, xóa mục template) để đạt.

## Khi người dùng hỏi trực tiếp một trong 4 câu

Không trả lời bằng cảm nhận. "Bạn có thắc mắc gì không?" → chạy lint (đếm marker), đọc Q đang mở, thử vai dev/QA, trả lời bằng danh sách Q cụ thể. "Có chỗ nào cần xác nhận?" → đề xuất chưa có DEC, giả định, mâu thuẫn, con số do BA đặt. "Có lệch/thiếu không?" → đọc lại nguồn, chạy trace, trả lời bằng ba bảng Thiếu/Thừa/Lệch. "Checklist done chưa?" → `checklist` (nếu chưa có) + `status` + `lint`, trả lời bằng con số.

## Tài liệu không theo cấu trúc workspace của skill

Với tài liệu cũ hoặc của đội khác: dùng các câu hỏi C3F/C4 làm bộ câu hỏi kiểm thủ công, đối chiếu với yêu cầu gốc được cung cấp; `ba.py` chỉ chạy được trên workspace của skill — nếu cần chạy công cụ, dựng workspace bằng `ba.py init` và chuyển nội dung vào đúng template trước. Ghi rõ trong báo cáo phần nào đã kiểm bằng công cụ, phần nào kiểm thủ công.
