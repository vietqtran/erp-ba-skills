# Chương 6: Tái cấu trúc dựa trên công nghệ so với tái cấu trúc từ đầu (Technology Enabled versus Clean Slate Reengineering)

## Ý tưởng cốt lõi (Core Idea)
Vì "triển khai SAP = tái cấu trúc bắt buộc", mọi dự án ERP phải chọn vị trí trên dải liên tục giữa hai cực: **technology enabled (constrained) reengineering** — chọn phần mềm trước rồi thiết kế quy trình trong giới hạn phần mềm; và **clean slate reengineering** — thiết kế quy trình tối ưu trước rồi mới "fit" phần mềm vào. Lựa chọn này quyết định độ tự do và chi phí khi BA đặc tả quy trình.

## Framework được giới thiệu (Frameworks Introduced)
- **Technology Enabled (Constrained) Reengineering** — tái cấu trúc dựa trên/bị ràng buộc bởi công nghệ:
  - Cách làm: (1) chọn ERP trước; (2) chọn MAPs từ những gì phần mềm chấp nhận ⇒ phần mềm dẫn dắt tái cấu trúc. Gemini Consulting gọi là **concurrent transformation**.
  - Khi nào dùng: doanh nghiệp ngân sách hạn chế, bị ép thời gian, quy trình tương đối chuẩn.
- **Clean Slate Reengineering** — tái cấu trúc từ đầu/"starting from scratch":
  - Cách làm: thiết kế quy trình tối ưu không bị ràng buộc bởi artifact/quy trình có sẵn, rồi chọn/tùy biến phần mềm fit theo thiết kế.
  - Khi nào dùng: doanh nghiệp lớn, "deep pockets", có thời gian, dùng quy trình làm lợi thế cạnh tranh, cần giải pháp độc nhất.
- **Reengineering–ERP Sequencing** — trình tự tái cấu trúc so với ERP: BPR trước ERP, đồng thời, hay sau. Khảo sát Gemini cho thấy đa số chọn đồng thời (technology enabled), nhưng sau khi làm, tỉ lệ chọn "BPR trước ERP" tăng mạnh.

## Khái niệm chính (Key Concepts)
- **Feasibility of design**: với technology enabled, thiết kế luôn khả thi vì chọn từ danh mục phần mềm chấp nhận và tương tác được với quy trình khác.
- **Bounds on design**: công nghệ đặt "ranh giới" cho thiết kế, tránh quá tải lựa chọn và ranh giới quy trình mờ nhòe.
- **Evidence it works**: nếu một quy trình là best practice trong ERP thì đã có doanh nghiệp khác chạy thành công.
- **Buy-in to future versions**: dùng ERP nghĩa là "mua" luôn các phiên bản tương lai nếu muốn hệ thống tiến hóa.
- **Unique value-creating processes**: quy trình tạo giá trị độc quyền mà doanh nghiệp *chủ động* không cho vào cơ sở dữ liệu best practices của tư vấn/ERP.

## Mô hình tư duy (Mental Models)
- Coi technology enabled là "đi theo bản đồ có sẵn" (nhanh, rẻ, khả thi, có bằng chứng) và clean slate là "vẽ bản đồ mới" (độc nhất, nhưng tốn kém, có thể không có phần mềm đáp ứng).
- Nếu quy trình là lợi thế cạnh tranh ⇒ nghiêng clean slate để không "chơi catch-up"; nếu chỉ cần theo kịp ngành ⇒ technology enabled.
- Với công nghệ mới (web, barcode) chưa có best practice, clean slate có thể là cách *duy nhất* khả thi.

## Điều cần tránh (Anti-patterns)
- **Obliterate mà không có công cụ/bản đồ**: lý do chính khiến nhiều nỗ lực tái cấu trúc sớm thất bại — thiếu bộ công cụ dẫn dắt.
- **Lẫn lộn tái cấu trúc với triển khai công nghệ**: khi gộp cả hai vào ERP, dễ bị chê "quá đắt, quá lâu" mà không tách được nguyên nhân.
- **Clean slate khi thiếu nguồn lực/thời gian**: dễ cho ra thiết kế suboptimal, không bounds, có thể không khả thi hoặc không có phần mềm đáp ứng.
- **Technology enabled cho quy trình độc quyền**: để lộ/san phẳng lợi thế cạnh tranh vì thiết kế ai cũng tiếp cận được.

## Bảng tham chiếu (Reference Tables)
**Ma trận chọn cách tiếp cận** (tổng hợp phần "Who Should Use"):

| Yếu tố doanh nghiệp | Clean slate | Technology enabled |
|---|---|---|
| Quy mô | lớn | nhỏ/vừa |
| Ngân sách | deep pockets | hạn chế |
| Thời gian | dư dả | bị ép |
| Vai trò quy trình | lợi thế cạnh tranh, độc nhất | tương đối chuẩn |
| Chi phí triển khai | cao hơn | thấp hơn |
| Rủi ro khả thi | thiết kế có thể bất khả thi | luôn khả thi |

**Chiến lược BPR và SAP R/3** (Table 6.2, khảo sát Gemini Consulting 1996):

| Chiến lược | Ban đầu dùng | Nếu làm lại sẽ chọn |
|---|---|---|
| BPR và SAP đồng thời | 48% | 51% |
| BPR trước SAP | 16% | 35% |
| BPR sau SAP | 3% | 3% |
| Trước và sau | 1% | 1% |
| Không cần BPR | 33% | 10% |

Công cụ chọn *cái gì cần tái cấu trúc* (Table 6.1, CSC Index 1994): None 41%/36% (Mỹ/Âu), process value analysis 36/27, benchmarking 34/36, competitive analysis 25/28, ABC 20/17.

## Ví dụ minh họa (Worked Example)
**Geneva Steel — clean slate; Quantum — technology enabled.** Delta Project của Geneva (Phụ lục 3-1) là ví dụ clean slate: khi khởi động *chưa có* công cụ nào dẫn dắt, nên không mang thiên kiến của bất kỳ tool nào và có thể dùng một *portfolio* công cụ. Ngược lại, Geneva sau đó dùng SAP như technology enabled để đổi dòng thông tin — minh họa rằng một doanh nghiệp có thể nằm *giữa* dải liên tục.

Quantum chọn technology enabled vì bị ép thời gian: ổ đĩa đã thành hàng hóa phổ thông, Quantum cạnh tranh bằng *customer service*, khách không thể chờ, nên không có thời gian cho clean slate ⇒ chọn ERP enabled để tích hợp nhà máy và nhà cung cấp toàn cầu nhanh. Procter & Gamble minh họa "deep pockets": dùng nhiều thiết kế ở nhiều công ty khách để phát triển hệ quản trị chuỗi cung ứng (rồi trao cho IBM) — chỉ khả thi với nguồn lực lớn. **Bài học cho BA**: xác định vị trí dự án trên dải liên tục *trước khi* viết spec quy trình, vì nó quyết định bạn được tự do thiết kế hay phải chọn trong danh mục phần mềm.

## Điểm cần nhớ (Key Takeaways)
1. Technology enabled vs clean slate là một *dải liên tục*, hầu hết dự án nằm ở giữa.
2. Technology enabled: nhanh, rẻ, khả thi, có bằng chứng, nhưng bị ràng buộc và ai cũng tiếp cận được.
3. Clean slate: độc nhất, không bị ràng buộc công cụ, nhưng tốn kém, rủi ro bất khả thi, có thể không có phần mềm.
4. Quy mô + ngân sách + thời gian + tính độc quyền của quy trình quyết định hướng đi.
5. Đa số doanh nghiệp làm BPR *đồng thời* với ERP; sau trải nghiệm, nhiều doanh nghiệp muốn BPR *trước* — và hầu như luôn cần *một ít* tái cấu trúc.

## Ứng dụng cho BA ERP (BA Application)
- Mở đầu tài liệu quy trình bằng việc ghi rõ dự án nghiêng technology enabled hay clean slate — điều này định ra: được thiết kế tự do hay phải chọn trong danh mục best practices của gói ERP.
- Nếu technology enabled, đặc tả quy trình bằng cách *chọn từ MAPs khả thi* của phần mềm và nêu rõ ranh giới (bounds) để tránh thiết kế ngoài khả năng gói ERP (chống "thừa chức năng").
- Nếu clean slate, cảnh báo rủi ro "không có phần mềm đáp ứng" và đề xuất kiểm tra tính khả thi trước khi chốt thiết kế.
- Với quy trình là lợi thế cạnh tranh, khuyến nghị giữ nó ngoài best practices dùng chung và thiết kế riêng.
- Tách bạch trong tài liệu phần "tái cấu trúc quy trình" và phần "triển khai công nghệ" để nghiệm thu rõ ràng, tránh đổ lỗi lẫn lộn.

## Liên hệ (Connects To)
- **Chương 2**: best practices vs obliteration là gốc của hai cách tiếp cận này.
- **Chương 3**: Geneva Delta Project và khung MAPs.
- **Chương 7**: rationale clean slate/technology enabled ảnh hưởng tới đo lường business case.
- **Chương 9**: đổi quy trình hay đổi phần mềm — quyết định cốt lõi của thiết kế.
