---
name: erp-ba-step5-review
description: "Bước 5 của bộ skill BA ERP — review độc lập, khách quan tài liệu BA (tài liệu tổng quan, SRS, đặc tả chức năng/báo cáo) bằng một agent khác không mang ngữ cảnh của người viết: đối chiếu với yêu cầu gốc, soi theo 6 góc nhìn (khách hàng/PO, dev, QA, chuyên gia ERP, kiểm toán/bảo mật, nhất quán) để tìm chỗ lệch, thiếu, thừa, mâu thuẫn, mơ hồ, sai chuẩn ERP/luật, chưa đủ để code; ghi báo cáo phát hiện có mức độ và bằng chứng; điều phối vòng sửa → tự kiểm → review lại tới khi 0 lỗi Critical/Major (tối đa 3 vòng). Nghiệm thu bằng checklist C5. Dùng khi người dùng nói “review khách quan”, “nhờ agent khác review”, “soát lại tài liệu”, “tìm lỗi trong spec/SRS/BRD”, “tài liệu này đã đủ để dev code chưa”, kể cả với tài liệu không do bộ skill này tạo. English — independent adversarial review of ERP requirement/spec documents."
---

# Bước 5 — Review độc lập bằng agent khác

Thuộc bộ skill BA ERP: `erp-ba-core` → `erp-ba-step1-research` → `erp-ba-step2-requirements` → `erp-ba-step3-specification` → `erp-ba-step4-verify` → **bước 5 (skill này)**.

Đường dẫn: `<skill-dir>` = thư mục chứa file SKILL.md này; `<core>` = thư mục `erp-ba-core` nằm cạnh (`<skill-dir>/../erp-ba-core`); `<suite>` = thư mục cha chứa cả bộ skill.

## Vì sao cần agent khác

Người viết đọc lại tài liệu của mình sẽ "thấy" điều mình định viết chứ không phải điều đã viết, và có xu hướng bảo vệ lựa chọn của mình. Một agent khởi động mới, không có ngữ cảnh hội thoại của người viết, chỉ có nguồn gốc + tài liệu, sẽ đọc giống dev, QA và khách hàng sẽ đọc. Vì vậy reviewer phải: (1) là phiên/agent riêng, (2) không nhận lời giải thích của người viết, (3) không sửa tài liệu — chỉ ghi phát hiện.

| Đầu ra | Template | Nghiệm thu |
|---|---|---|
| `05-review/review-report-r<N>.md` (hoặc file người dùng chỉ định) | `<skill-dir>/assets/templates/05-review/review-report.md` | `<skill-dir>/references/checklists/C5-review.md`; qua khi 0 phát hiện Critical/Major còn mở |

Hướng dẫn chi tiết cho reviewer: `<skill-dir>/agents/independent-reviewer.md`.

## Cách khởi chạy

**Có công cụ Agent/subagent (Claude Code):** người viết (hoặc phiên điều phối) khởi chạy một subagent với prompt:

```
Bạn là reviewer độc lập. Đọc và làm đúng hướng dẫn trong <skill-dir>/agents/independent-reviewer.md.
Workspace tài liệu: <root>   (hoặc: file cần review <đường dẫn>, yêu cầu gốc <đường dẫn>)
Phạm vi review: <toàn bộ | danh sách FN | module>
Vòng review: <N>
Báo cáo review vòng trước (nếu có): <root>/05-review/review-report-r<N-1>.md
Ghi kết quả vào: <root>/05-review/review-report-r<N>.md
```

Không gửi kèm: tóm tắt của người viết, lý do thiết kế, hay báo cáo tự kiểm như "kết luận sẵn" — reviewer chỉ đọc báo cáo tự kiểm ở cuối để kiểm tra tính trung thực (C5-CON-02).

**Phạm vi lớn:** chạy nhiều reviewer song song, mỗi reviewer một góc nhìn (Dev, QA, Khách hàng, ERP, Kiểm toán/Bảo mật, Nhất quán) hoặc một module, rồi gộp phát hiện vào một báo cáo (bỏ trùng).

**Không có subagent** (chat thường): đề nghị người dùng mở phiên mới (có thể bằng model khác), dán nội dung `agents/independent-reviewer.md` và cho quyền đọc workspace. Nếu buộc phải tự review trong cùng phiên, ghi rõ "review không độc lập" trong báo cáo và áp dụng nghiêm các góc nhìn của C5 — phương án kém hơn.

**Người dùng gọi thẳng skill này để review một tài liệu** (không phải tài liệu mình vừa viết trong phiên): bạn chính là reviewer — đọc `agents/independent-reviewer.md` và làm theo, không cần khởi chạy thêm agent.

**Tài liệu không theo cấu trúc của bộ skill** (tài liệu cũ, đội khác viết): vẫn review theo 6 góc nhìn với câu hỏi C5 và C3F (`<suite>/erp-ba-step3-specification/references/checklists/C3F-function.md`) làm bộ câu hỏi, đối chiếu yêu cầu gốc được cung cấp. `ba.py lint/trace` chỉ chạy trên workspace của bộ skill — khi không áp dụng được, kiểm thủ công nội dung tương ứng (nguồn từng yêu cầu, AC, thông báo lỗi, nhất quán trạng thái/vai trò, cú pháp sơ đồ) và ghi rõ trong báo cáo.

## Mức độ phát hiện

| Mức | Định nghĩa | Ví dụ |
|---|---|---|
| Critical | Sai nghiệp vụ/luật; thiếu chức năng/quy tắc khách hàng đã yêu cầu; nội dung trái yêu cầu gốc; dev không thể code phần đó | Hạch toán doanh thu sai thời điểm; REQ duyệt 2 cấp nhưng đặc tả 1 cấp |
| Major | Mơ hồ hoặc mâu thuẫn ảnh hưởng hành vi; thiếu trường/luồng/ngoại lệ/phân quyền quan trọng; chức năng thừa không đánh dấu đề xuất | Hai bộ trạng thái khác nhau cho cùng chứng từ |
| Minor | Trình bày, thuật ngữ, thiếu sót nhỏ không đổi hành vi | Thông báo lỗi thiếu tham số hiển thị |
| Info | Gợi ý cải thiện | Đề xuất thêm bộ lọc |

## Xử lý phát hiện (người viết) & vòng lặp

Với mỗi RV, người viết điền cột "Xử lý":
- **Đã sửa** (ghi phiên bản file) — sửa theo `erp-ba-step3-specification` (hoặc skill bước tương ứng), ghi mục 20 của FN.
- **Từ chối – lý do** — chỉ khi reviewer hiểu sai và có bằng chứng (trích nguồn). Reviewer vòng sau xem lại lý do.
- **Chuyển Q-…** — khi cần khách hàng quyết; phát hiện vẫn tính là mở với mức độ cũ cho tới khi Q được trả lời, trừ khi tài liệu ghi rõ phần đó chưa `Ready`.

Sau khi xử lý: chạy lại `erp-ba-step4-verify` cho phạm vi bị sửa, rồi review vòng N+1 (reviewer mới hoặc reviewer cũ nhận báo cáo vòng trước). Reviewer vòng sau kiểm: phát hiện cũ đã đóng đúng chưa, và có lỗi mới do sửa sinh ra không.

**Điều kiện dừng:** PASS khi 0 Critical/Major còn mở, checklist C5 không còn "No", và bước 4 vòng mới nhất PASS → tài liệu được đặt `status: Ready`. Tối đa 3 vòng review; sau đó báo người dùng các mục còn mở và lý do (thường là câu hỏi chỉ khách hàng trả lời được), kèm danh sách câu hỏi gửi khách hàng.

## Báo cáo cho người dùng

Đường dẫn báo cáo, số phát hiện theo mức độ, kết luận PASS/FAIL, 3–5 phát hiện quan trọng nhất (một dòng mỗi cái), và các câu hỏi cần khách hàng trả lời.
