---
name: erp-ba-step2-requirements
description: "Bước 2 của bộ skill BA ERP — thu thập yêu cầu khách hàng từ biên bản/ghi âm/ghi chú buổi họp, email và file khách hàng gửi, kết hợp kết quả research, để lập sổ yêu cầu (mỗi yêu cầu có trích nguyên văn và nguồn), tài liệu tổng quan và quy trình tổng quan TO-BE chuẩn ERP (sơ đồ swimlane), nhật ký câu hỏi – mâu thuẫn – quyết định, và danh sách câu hỏi gửi lại khách hàng. Điền theo template, nghiệm thu bằng checklist C2. Dùng khi người dùng có biên bản họp/khảo sát, transcript, ghi chú, file Excel/biểu mẫu của khách hàng và muốn tổng hợp yêu cầu, viết BRD/URD/tài liệu tổng quan, vẽ quy trình nghiệp vụ tổng thể, hoặc chuẩn bị câu hỏi cho buổi họp tiếp theo — kể cả khi chỉ nói “tổng hợp biên bản”, “lấy yêu cầu từ cuộc họp”. English — ERP requirements elicitation and BRD/process overview from meeting notes."
---

# Bước 2 — Thu thập yêu cầu → tài liệu tổng quan & quy trình tổng quan

Thuộc bộ skill BA ERP: `erp-ba-core` → `erp-ba-step1-research` → **bước 2 (skill này)** → `erp-ba-step3-specification` → `erp-ba-step4-verify` → `erp-ba-step5-review`.

Đường dẫn: `<skill-dir>` = thư mục chứa file SKILL.md này; `<core>` = thư mục `erp-ba-core` nằm cạnh (`<skill-dir>/../erp-ba-core`). Không thấy `<core>` → báo người dùng cài đủ bộ skill.

## Mục tiêu & đầu ra

Biến những gì khách hàng nói và đưa (buổi họp, file, email) thành: một **sổ yêu cầu gốc** truy được về từng câu của khách hàng, một **tài liệu tổng quan** (phạm vi, tổ chức, quy trình TO-BE chuẩn ERP), và một **nhật ký câu hỏi/mâu thuẫn** để quay lại hỏi. Bước này quyết định tài liệu về sau có "lệch" hay không — ưu tiên trung thực với nguồn hơn là trôi chảy.

| Đầu ra (trong workspace) | Template (trong `<skill-dir>/assets/templates/`) |
|---|---|
| `00-inputs/source-register.md` — sổ đăng ký nguồn | `00-inputs/source-register.md` |
| `00-inputs/meetings/MTG-*.md` — biên bản họp | `00-inputs/meeting-notes.md` |
| `02-requirements/requirement-register.md` — sổ yêu cầu (REQ) | `02-requirements/requirement-register.md` |
| `02-requirements/requirements-overview.md` — tổng quan & quy trình TO-BE | `02-requirements/requirements-overview.md` |
| `02-requirements/issue-log.md` — câu hỏi, giả định, quyết định, mâu thuẫn, thay đổi | `02-requirements/issue-log.md` |
| `03-specification/catalogs/glossary.md` (bản đầu) — thuật ngữ | (template của bước 3) |

Nghiệm thu: `<skill-dir>/references/checklists/C2-requirements.md`.

Workspace chưa có → hỏi tên dự án và nơi lưu (mặc định `docs/ba/<mã-dự-án>/`), rồi `python3 <core>/scripts/ba.py init <root> --project "<Tên dự án>"`. Quy ước ID (SRC, MTG, REQ, BP, BO, Q, ASM, DEC, CFL, CHG), marker và nơi định nghĩa: `<core>/references/conventions.md` — đọc trước khi bắt đầu.

## Nguyên tắc bắt buộc

1. **Không có nguồn thì không có yêu cầu.** Mỗi REQ có trích nguyên văn và nguồn (`MTG-001 L14`, `SRC-003 sheet "PO" dòng 5`). Lý do: chỉ có trích dẫn mới cho thấy tài liệu có lệch khỏi ý khách hàng hay không.
2. **Hỏi thay vì đoán.** Ngưỡng, số cấp duyệt, người duyệt, ưu tiên, định nghĩa của từ mơ hồ ("nhanh", "đẹp", "dễ dùng") — khách hàng chưa nói thì ghi Q trong issue-log, không tự quyết.
3. **Mâu thuẫn ghi lại, không tự chọn bên.** Hai người/hai tài liệu nói khác nhau → CFL + Q.
4. **Chuẩn ERP để tìm câu hỏi, không để thêm yêu cầu.** Phần chuẩn mà khách hàng chưa nhắc → Q (hoặc nội dung đề xuất gắn `[ĐỀ XUẤT → Q-…]`), không ghi thành REQ.
5. **Không xóa mục template**; `N/A – <lý do>` cho mục không áp dụng.

## Quy trình

1. **Đăng ký nguồn.** Mỗi file khách hàng gửi (đặt vào `00-inputs/files/`) có một SRC; mỗi buổi họp một MTG trong `source-register.md`.

2. **Ghi biên bản họp** bằng `python3 <core>/scripts/ba.py new-meeting <root> --date <yyyy-mm-dd>`:
   - Mục 3 chứa nội dung **nguyên văn** (transcript, ghi chú gõ lại, tin nhắn), đánh số dòng L01, L02… Chỉ có bản tóm tắt của người khác → ghi nguyên bản tóm tắt đó, độ tin cậy "Trung bình".
   - Không diễn giải hay "làm đẹp" ở mục 3 — đó là bằng chứng.
   - Mục 4–6: mỗi dòng của mục 3 đi vào đúng một nơi — yêu cầu sơ bộ, quyết định/câu hỏi, hoặc "không phải yêu cầu" (kèm lý do, ví dụ chuyện ngoài lề). `ba.py trace` báo dòng chưa xử lý.

3. **Lập sổ yêu cầu (REQ)**:
   - **Nguyên tử:** "Đơn mua trên 50 triệu phải được giám đốc duyệt và gửi email cho kế toán" → 2 REQ.
   - **Trích nguyên văn** + nguồn.
   - **Diễn đạt lại không thêm ý.** Gốc "duyệt nhanh trong ngày" → đúng: "Đơn mua cần được duyệt trong ngày làm việc tạo đơn [CẦN XÁC NHẬN: Q-007 — 'trong ngày' tính đến mấy giờ, quá hạn xử lý thế nào]"; sai: "Hệ thống tự động duyệt sau 8 giờ" (bịa cơ chế).
   - Phân loại BUS/STK/FR/NFR/DATA/RPT/INT/CON/MIG, gán module và BP. Ưu tiên do khách hàng nói; chưa nói → "Chưa xác định" + Q.

4. **Tìm khoảng trống và mâu thuẫn** — nơi kiến thức ERP phát huy:
   - Với mỗi quy trình liên quan, mở `<core>/references/processes/<quy-trình>.md` (và `<core>/references/industries/<ngành>.md`): so bước chuẩn, chứng từ chuẩn, quy tắc, tham số, báo cáo với điều khách hàng đã nói. Phần chuẩn chưa được nhắc → **câu hỏi** (dùng mục 14 của file quy trình, mục 10 của file ngành, `<core>/references/question-bank.md`).
   - Hai nguồn nói khác nhau → **CFL** (trích cả hai phía, đề xuất cách xử lý, tạo Q).
   - Yêu cầu trái chuẩn ERP hoặc trái luật (ví dụ "cho xóa phiếu chi đã ghi sổ") → CFL + giải thích rủi ro + phương án chuẩn (đảo bút toán) để khách hàng quyết.

5. **Viết tài liệu tổng quan** `requirements-overview.md`:
   - Bối cảnh, mục tiêu đo được (BO), phạm vi trong/ngoài, cơ cấu tổ chức & cấp duyệt, hiện trạng.
   - **Danh sách luồng tổng quan (§5)**: các quy trình đầu-cuối BP-NN (ví dụ "Cung ứng vật tư công trường"), mỗi BP ghi module, file chuẩn tham chiếu, các luồng chi tiết của nó và REQ được phủ.
   - **Luồng chi tiết trong từng BP (§6)**: dựng khung từ mục 5 của file quy trình chuẩn rồi điều chỉnh theo REQ; sơ đồ swimlane Mermaid của BP (cú pháp: `<core>/references/diagram-conventions.md`); bảng **luồng chi tiết** FL-<BP>-NN — mỗi luồng là một chuỗi việc có điểm bắt đầu và kết thúc, vai trò thực hiện, chứng từ, module, REQ (ví dụ FL-01-01 "Lập và duyệt đề xuất vật tư", FL-01-02 "Nhận hàng giao thẳng công trường", FL-01-03 "Nhận hàng kho tổng và điều chuyển ra công trường"). Mỗi nhánh nghiệp vụ khách hàng mô tả phải là một luồng chi tiết hoặc nằm trong một luồng chi tiết; mỗi REQ chức năng thuộc ít nhất một luồng chi tiết; khác chuẩn ERP ghi nguồn (REQ/DEC). Bước 3 phân rã mỗi luồng chi tiết thành chức năng — `ba.py trace` báo luồng chưa được phân rã.
   - Bảng 5 thành phần ERP theo module (§8: hệ thống, danh mục, nghiệp vụ, phân quyền & tham số, báo cáo): mỗi ô là REQ hoặc Q — không để trống. Đây là nơi phát hiện sớm việc "thiếu".
   - NFR tổng quan, tích hợp, chuyển đổi dữ liệu, ràng buộc/giả định/rủi ro. Điều khách hàng nói "chưa cần" → ghi ngoài phạm vi kèm nguồn.

6. **Thuật ngữ:** ghi tên khách hàng dùng và ánh xạ sang tên chuẩn ERP (`<core>/references/glossary.md`) vào `catalogs/glossary.md`; dùng tên của khách hàng trong tài liệu.

7. **Nghiệm thu** (mục cuối).

8. **Đầu ra cho người dùng:** tóm tắt (số REQ theo module/loại, số CFL, số Q chặn) + **danh sách câu hỏi gửi khách hàng** nhóm theo người cần hỏi, mỗi câu có phương án gợi ý A/B khi được — đây là agenda buổi họp tiếp theo.

## Ví dụ tách & diễn đạt yêu cầu

| Trích nguyên văn | REQ đúng | Vì sao |
|---|---|---|
| "Kho muốn biết hàng nào sắp hết để báo mua" | REQ-021: Hệ thống cảnh báo mặt hàng có tồn kho dưới mức tối thiểu cho thủ kho. REQ-022: Từ cảnh báo, thủ kho tạo được đề nghị mua hàng. | Hai hành vi; "mức tối thiểu" là cách hiểu chuẩn ERP → cần Q xác nhận có quản lý tồn tối thiểu theo mặt hàng/kho không |
| "Báo cáo công nợ như bên MISA đang dùng" | REQ-030: Báo cáo công nợ phải trả theo mẫu khách hàng đang dùng (SRC-005 — ảnh chụp báo cáo hiện tại) | Không tự suy ra mẫu; xin mẫu (SRC) hoặc ghi Q |
| "Giám đốc duyệt hết các đơn" | REQ-011: Mọi đơn mua phải được giám đốc duyệt trước khi gửi nhà cung cấp | Không thêm ngưỡng/cấp duyệt khách hàng chưa nói; có thể ghi Q hỏi có cần phân cấp không |

Workspace mẫu hoàn chỉnh (biên bản → REQ → Q/DEC): `<core>/assets/examples/sample-workspace/`.

## Lỗi thường gặp

| Lỗi | Hậu quả | Cách tránh |
|---|---|---|
| Tóm tắt biên bản thay vì ghi nguyên văn | Mất bằng chứng, bước sau lệch ý | Mục 3 nguyên văn, có số dòng |
| Gộp nhiều ý vào một REQ | Truy vết sai, dễ sót | Tách nguyên tử |
| Viết giải pháp ở bước này (màn hình, trường) | Khóa thiết kế khi chưa đủ thông tin | Chỉ ghi nhu cầu; giải pháp để bước 3 |
| Tự gán ưu tiên/ngưỡng/số cấp duyệt | Bịa yêu cầu | Q |
| Bỏ qua dòng "không quan trọng" | Thiếu yêu cầu ngầm | Mọi dòng được xử lý hoặc ghi lý do loại |
| Lấy quy trình chuẩn ERP làm yêu cầu khách hàng | Thừa chức năng | Chuẩn dùng để tìm câu hỏi; đề xuất mang marker |

## Nghiệm thu & chuyển bước

```bash
python3 <core>/scripts/ba.py lint <root>
python3 <core>/scripts/ba.py trace <root>
python3 <core>/scripts/ba.py checklist <root> --step 2 --round <N> --out <root>/04-verification/verify-report-r<N>.md
python3 <core>/scripts/ba.py status <root>/04-verification/verify-report-r<N>.md
```

Trả lời từng câu C2: Yes (kèm bằng chứng) / No (kèm việc phải sửa) / N/A (kèm lý do); sửa mọi No, chạy lại tới khi PASS. Câu hỏi mở được phép tồn tại nếu đã ghi đầy đủ trong issue-log (người cần hỏi, mức ảnh hưởng, hạn). Trước khi báo xong, tự trả lời 4 câu: còn chỗ nào chưa rõ? chỗ nào cần xác nhận? đối chiếu biên bản gốc có lệch/thiếu/thừa không? checklist và template đã đủ chưa?

Bước tiếp theo: `erp-ba-step3-specification` (khi các Q mức "Chặn" của phạm vi cần đặc tả đã có câu trả lời, hoặc đặc tả phần không bị chặn trước).
