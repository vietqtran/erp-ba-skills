# Chương 19: Phụ lục C — Kế hoạch triển khai mẫu (Appendix C — Sample Implementation Plan)

## Ý tưởng cốt lõi (Core Idea)
Một mẫu *vài bước đầu* của kế hoạch triển khai chi tiết, cho phần xử lý **inventory record accuracy** (độ chính xác bản ghi tồn kho). Mục đích: cho người đọc cảm nhận một kế hoạch triển khai chi tiết trông như thế nào — mỗi task có *người chịu trách nhiệm* và *ngày bắt đầu/hoàn thành* (cả lịch dự kiến "Sched" lẫn thực tế "Act"). (Đây là chương mỏng theo bản chất — chỉ là một artifact mẫu, không có khung lý thuyết mới.)

## Framework được giới thiệu (Frameworks Introduced)
- **Detailed implementation plan format** — định dạng kế hoạch triển khai chi tiết: bảng task với các cột **Task · Responsible · Start (Sched/Act) · Complete (Sched/Act)**. Nguyên tắc ngầm: "naming names and dates" — nêu tên người và ngày cụ thể cho mỗi task (so với checklist nghiệm thu chỉ trả lời yes/no ở cuối mỗi chương).

## Khái niệm chính (Key Concepts)
- **Cycle counting** — đếm chu kỳ: quy trình đếm tồn kho định kỳ (liên tục/"ongoing") thay cho kiểm kê toàn bộ một lần, để đạt và duy trì độ chính xác bản ghi.
- **Limited access** — giới hạn truy cập: điều kiện tiên quyết để có độ chính xác tồn kho (vạch khu kho/stockroom có kiểm soát ra/vào — xem "chicken wire stockroom" ở Ch14).
- **Sched vs Act**: mỗi mốc có ngày dự kiến và ngày thực tế để theo dõi tiến độ.

## Bảng tham chiếu (Reference Tables)
Kế hoạch triển khai mẫu — phần Inventory Record Accuracy (tái dựng từ bảng gốc; cột "Act" để trống vì là mẫu lập kế hoạch):

| # | Task | Người chịu trách nhiệm | Start (Sched) | Complete (Sched) |
|---|---|---|---|---|
| 1 | Đo 100 item làm điểm khởi đầu | Nancy Hodgkins | 11/1 | 11/8 |
| 2 | Vạch giới hạn truy cập kho & khu stockroom | Nancy Hodgkins; Tom Brennan | 11/1 | 11/10 |
| 3 | Thiết lập quy trình cycle counting | John Grier; Nancy Hodgkins; Maureen Boylan | 11/3 | 11/10 |
| 4 | Bắt đầu cycle counting | Nancy Hodgkins | 11/13 | (ongoing) |
| 5 | Giáo dục ERP cho nhân viên kho & stockroom | David Ball | 11/5 | 11/20 |
| 6 | Đào tạo phần mềm cho nhân viên kho & stockroom | Helen Weiss | 11/8 | 11/23 |

Quan sát: các task chạy *song song* (đo lường, giới hạn truy cập, thiết lập cycle counting cùng khởi động đầu tháng), giáo dục ERP đi trước đào tạo phần mềm, và cycle counting là hoạt động liên tục sau khi bắt đầu.

## Ví dụ minh họa (Worked Example)
Chính bảng trên là artifact mẫu. Trình tự logic của nó cho một mục tiêu dữ liệu (inventory accuracy): (1) *đo* hiện trạng trên một mẫu 100 item để biết điểm xuất phát → (2) *bảo vệ* dữ liệu bằng giới hạn truy cập kho → (3) *thiết lập* quy trình cycle counting (nhiều người cùng chịu trách nhiệm) → (4) *bắt đầu* đếm (ongoing) → song song (5)(6) *giáo dục + đào tạo* nhân viên vận hành kho. Mỗi dòng gắn tên người thật và ngày cụ thể — đó là điểm phân biệt "kế hoạch triển khai" với "checklist nghiệm thu".

## Điểm cần nhớ (Key Takeaways)
1. Kế hoạch triển khai chi tiết = bảng task với Responsible + ngày Sched/Act, "naming names and dates".
2. Đạt inventory accuracy theo trình tự: đo mẫu → giới hạn truy cập → lập cycle counting → đếm (ongoing) → giáo dục/đào tạo nhân sự kho.
3. Task có thể song song; giáo dục đi trước đào tạo phần mềm.

## Ứng dụng cho BA ERP (BA Application)
- Dùng định dạng bảng này (Task · Responsible · Start Sched/Act · Complete Sched/Act) làm template cho phần kế hoạch/lộ trình trong tài liệu triển khai — tách bạch với checklist acceptance (yes/no) đặt ở cuối mỗi chức năng.
- Khi viết chức năng quản lý tồn kho, đặc tả **cycle counting** và **limited access** như hai điều kiện/tiêu chí để đạt mục tiêu độ chính xác (ví dụ ngưỡng 95-98% đã nêu ở các chương trước) — không để "làm cho tồn kho chính xác" ở dạng mơ hồ.
- Nhấn mạnh trình tự "đo trước, cải thiện sau": mọi mục tiêu dữ liệu nên bắt đầu bằng một phép đo baseline trên mẫu.

## Liên hệ (Connects To)
- **Ch 14**: "chicken wire stockroom", limited access, và thách thức on-hand inventory accuracy trong Quick-Slice.
- **Ch 15**: đo lường độ chính xác inventory/BOM/routing hằng tuần khi vận hành.
- **Appendix A**: inventory data là đầu vào bắt buộc của MRP — nên accuracy của nó là nền móng.
