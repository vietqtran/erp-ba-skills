# Chương 3: Nền tảng về hệ thống ERP (ERP Systems Background)

## Ý tưởng cốt lõi (Core Idea)
Cấu hình một hệ thống ERP thực chất là lựa chọn các **MAPs (Models, Artifacts, and Processes)** — mô hình, hiện vật (chứng từ/danh mục) và quy trình — được nhúng sẵn trong phần mềm. Hiểu modules chuẩn, khung MAPs và cách ERP vận hành xuyên module là nền tảng để BA thiết kế chức năng "chuẩn ERP".

## Framework được giới thiệu (Frameworks Introduced)
- **MAPs — Models, Artifacts, and Processes**: khung ba thành phần tạo nên một hệ ERP được cấu hình.
  - Khi nào dùng: khi thiết kế/đặc tả bất kỳ chức năng ERP nào — xác định rõ mô hình, hiện vật, quy trình liên quan.
  - **Models**: biểu diễn thế giới mà hệ thống bao phủ (ví dụ organizational structures model trong R/3, chi tiết tới cấp "bin" kho, tổng hợp lên cấp tập đoàn). Mỗi mô hình có *giả định* bắt buộc phải tuân theo (ví dụ R/3 buộc mỗi phòng ban phải là cost center hoặc profit center).
  - **Artifacts** (hiện vật/chứng từ): "thức ăn" cho các tiến trình thông tin — chứng từ (hóa đơn, đơn hàng) vừa là đầu ra vừa là đầu vào; và các *instantiation của model* (chart of accounts, danh sách nhà cung cấp, danh mục sản phẩm) tạo cấu trúc cho hệ thống.
  - **Processes**: luồng hoạt động và thông tin để hoàn thành một tác vụ; không duy nhất (nhiều cách làm), nên có cái tốt hơn cái khác; trong ERP là các quy trình liên chức năng (cross-functional).
- **Best of Breed** — chiến lược "chọn tinh hoa": phối ghép module từ nhiều nhà cung cấp.
  - Khi nào dùng: khi một ERP chủ đạo thiếu một bộ tính năng then chốt; khi nhiều bộ phận có yêu cầu khác nhau; khi không gói nào đáp ứng hết.
  - Đánh đổi: tăng chi phí tìm kiếm, khác biệt "look and feel", chi phí tích hợp liên module, đội ngũ đa dạng khó đặc tả kỳ vọng, lệch chu kỳ phiên bản, mất tính đồng nhất.

## Khái niệm chính (Key Concepts)
- **BOPSE**: năm vendor ERP chính — **BAAN, Oracle, PeopleSoft, SAP, J.D. Edwards**.
- **ERP partners** (của SAP): bốn loại — alliance (dịch vụ tư vấn), platform (phần cứng), technology (HĐH/CSDL), complementary (công cụ chạy cùng R/3).
- **Module**: thành phần chức năng của ERP; cách đặt tên/phạm vi khác nhau giữa các gói.
- **Add-ons**: phần mềm bên thứ ba tăng năng lực, nối qua ALE, OLE, RFC.
- **Interchangeability**: module ERP *không* thay thế lẫn nhau giữa các vendor — ít động lực để làm tương thích.

## Mô hình tư duy (Mental Models)
- Khi đặc tả một chức năng, hãy tách tư duy theo MAPs: *mô hình* (cấu trúc tổ chức/dữ liệu) + *hiện vật* (chứng từ, danh mục) + *quy trình* (luồng liên chức năng).
- Coi chứng từ (invoice, đơn hàng) là "artifact" đi xuyên nhiều module — nên thiết kế một lần, dùng lại ở nhiều quy trình.
- Mặc định chọn một gói ERP duy nhất; chỉ cân nhắc best of breed khi có lý do rõ và chấp nhận sáu nhóm chi phí phát sinh.

## Điều cần tránh (Anti-patterns)
- **Giả định module các vendor ghép được với nhau**: module không khả tương thích; best of breed luôn kéo theo chi phí giao tiếp/tích hợp.
- **Thiết kế trái giả định của model**: ép dữ liệu/quy trình không khớp giả định mô hình gốc (như Microsoft phải sửa mô hình tổ chức theo R/3) gây xung đột.
- **Bỏ qua chi phí giữ model cập nhật**: nếu mô hình tổ chức biến động mà không cập nhật vào hệ thống thì rất tốn kém.

## Bảng tham chiếu (Reference Tables)
Một số module tiêu biểu của SAP R/3 (BA nên biết tên chuẩn):

| Mã | Module | Thành phần con tiêu biểu |
|---|---|---|
| FI | Financial accounting | GL, AR, AP, legal consolidations |
| CO | Controlling | cost center accounting, product cost, ABC |
| AM | Asset management | khấu hao, bảo hiểm, giá trị tài sản |
| MM | Materials management | inventory mgmt, invoice verification, warehouse |
| PP | Production planning | **SOP**, **MRP**, **CRP** |
| SD | Sales and distribution | bán hàng và phân phối |
| HR | Human resources | personnel admin, planning & development |
| PM | Plant maintenance | thiết bị, bảo trì phòng ngừa, service |
| QM | Quality management | chứng chỉ, inspection, quality notifications |
| PS | Project system | theo dõi dự án, quản lý ngân sách |

Oracle Applications nhóm theo ba cụm: **Demand** (order entry, AR, inventory), **Supply** (engineering, BOM, MRP, WIP, purchasing), **Finance** (GL, AP, cost management).

## Ví dụ minh họa (Worked Example)
**Geneva Steel (Phụ lục 3-1)** — nhà máy thép tích hợp duy nhất phía tây sông Mississippi, văn hóa truyền thống thứ bậc, "đứng chót" về mức hài lòng khách hàng. CEO Joseph Cannon mô tả hệ thống cũ là "road map from hell": một mainframe, hệ kế toán "nguyên thủy", rất nhiều máy mini khác loại khó nói chuyện với nhau, sinh "hàng triệu điểm dữ liệu" nhưng không tích hợp và không truy cập được; mỗi phòng cần một kế toán giá thành riêng, việc tích hợp "nằm trong đầu người quản lý".

Dự án **Delta Project** (1997) đặt mục tiêu giảm 20% chi phí so với 1996 và đổi cách làm việc. Geneva định nghĩa một bộ **balanced metrics**: giao hàng đúng hạn, độ chính xác hoàn thành đơn, chi phí sản xuất/tấn, chi phí quản lý/tấn, khiếu nại khách, hiệu suất sản xuất theo hoạt động, mức tồn kho. Nhưng hệ cũ không bắt đủ dữ liệu để đo các chỉ số này, nên Geneva chọn SAP R/3.

Kỳ vọng từ SAP (có thể dùng làm checklist "lợi ích kỳ vọng" khi viết business case): ít hệ thống phần cứng/phần mềm hơn (giảm legacy 50–90%); năng lực báo cáo tích hợp (gộp DOR/DRO/sales thành một); thông tin sẵn có và "actionable"; hỏi "what if"; tích hợp dựa trên hệ thống thay vì dựa vào con người; giảm nhân sự IT (80→12) và kế toán (60→10). Chi phí dự kiến 8–10 triệu USD, hoàn tất 1999. **Bài học cho BA**: Geneva dùng ERP để *đổi văn hóa* bằng cách đổi dòng chảy thông tin; và chống đối người dùng là có thật ("just a big hassle", "buying a new toy") nhưng đạt được "critical mass" ủng hộ khi đào tạo bắt đầu.

## Điểm cần nhớ (Key Takeaways)
1. Cấu hình ERP = chọn MAPs; mọi spec chức năng nên nêu rõ Models + Artifacts + Processes.
2. Mỗi model có giả định bắt buộc — thiết kế phải tuân theo, nếu không sẽ xung đột.
3. Module giữa các vendor không thay thế lẫn nhau; best of breed có sáu nhóm chi phí ẩn.
4. Biết tên module chuẩn (FI, CO, MM, PP/SOP/MRP/CRP, SD, HR...) để đặt tên chức năng theo chuẩn ERP.
5. Business case ERP nên gắn với bộ chỉ số đo được (như balanced metrics của Geneva).

## Ứng dụng cho BA ERP (BA Application)
- Cấu trúc mỗi đặc tả chức năng theo MAPs: nêu mô hình dữ liệu/tổ chức, chứng từ & danh mục (artifacts), và luồng quy trình liên chức năng.
- Khi đặt tên module/chức năng, dùng thuật ngữ chuẩn (GL, AR, AP, MRP, SOP, SD, MM...) để tài liệu nhất quán và dễ map sang gói ERP.
- Ghi rõ *giả định của model* (ví dụ mỗi đơn vị phải là cost center hay profit center) như một ràng buộc thiết kế, tránh conflict khi code.
- Khi viết business case, kèm bộ chỉ số đo được (on-time delivery, cost/ton, tồn kho...) để sau golive nghiệm thu thành công — tránh tài liệu chỉ nêu lợi ích chung chung.
- Nếu đề xuất best of breed, bắt buộc liệt kê chi phí tích hợp liên module và rủi ро lệch phiên bản.

## Liên hệ (Connects To)
- **Chương 4–5**: nhập liệu và đầu ra là cách artifacts đi vào/ra khỏi hệ thống.
- **Chương 6**: Geneva Delta Project là ví dụ clean slate reengineering.
- **Chương 9–10**: thiết kế ERP — chọn standard models, artifacts và processes.
- **Simon (Sciences of the Artificial)**: định nghĩa "artifact" là giao diện giữa môi trường trong (chương trình) và ngoài (thế giới vận hành).
