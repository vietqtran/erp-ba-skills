# bpmn-kit — sinh bộ BPMN chuẩn ERP từ định nghĩa quy trình

Dùng chung cho mọi dự án. Không viết lại script; chỉ viết `defs/` của dự án.

Chạy từ gốc repo:

```bash
bpmn-kit/scripts/build.sh --init projects/<tên>   # tạo projects/<tên>/defs/_common.py từ templates/
bpmn-kit/scripts/build.sh projects/<tên>          # sinh → render → bpmnlint; dừng ở lỗi đầu tiên; "OK" là xong
bpmn-kit/scripts/build.sh projects/<tên> BP-05    # chỉ một quy trình (khi đang sửa)
```

Lần chạy đầu tự cài thư viện (`npm install` trong `bpmn-kit/`). Cần Python 3, Node.js ≥ 18, Chrome hoặc Edge.

Đầu ra trong `<dự-án>/`: `bpmn/` (BPMN 2.0 có toạ độ), `svg/`, `png/`, `docs/` (tài liệu từng quy trình),
`viewer.html` (chạy `python3 -m http.server` ở gốc repo rồi mở `/projects/<tên>/viewer.html`), `CAU-HOI-KHAO-SAT.md` (gom câu hỏi + tham số đề xuất).
Ví dụ đầy đủ: [`examples/tour-operator`](../examples/tour-operator/README.md) (17 quy trình), mẫu một file: `templates/vi_du_bp05.py`.

## Cú pháp

`defs/_common.py`: `register(roles={KHÓA: tên}, pools={KHÓA: tên}, processes={'BP-NN': (slug, tiêu đề)})`. Luôn có vai trò `SYS`.

`defs/bpNN_<slug>.py` khai báo `PROCESS = dict(...)`:

| Khóa | Nội dung |
|---|---|
| `id`, `name`, `objective`, `trigger`, `outcome`, `scope`, `out_of_scope`, `modules`, `erp_standard`, `upstream`, `downstream`, `pool_name` | Thông tin chung (chuỗi hoặc danh sách; dùng `bp('BP-xx', 'ghi chú')` để liên kết) |
| `lanes=[lane(KHÓA, 'trách nhiệm')]`, `lane_rows={KHÓA: số hàng}` | Làn theo thứ tự trên → dưới |
| `pools=[pool(KHÓA, 'top'\|'bottom', cols=(c0, c1))]` | Bên ngoài; `cols` để đặt nhiều pool cạnh nhau |
| `nodes`, `flows`, `messages`, `data`, `annotations` | Sơ đồ (bên dưới) |
| `controls=[(mã, mô tả, loại, nguồn)]` | Mã `C<NN>-xx`; loại: Có sẵn / Cấu hình / Phân quyền / Báo cáo / Phòng ngừa |
| `documents=[(chứng từ, trạng thái, ghi chú)]`, `postings=[(nghiệp vụ, Nợ, Có, ghi chú)]` | |
| `parameters=[(tham số, ý nghĩa, đề xuất)]`, `kpis=[(chỉ số, cách tính, mục tiêu)]` | Tham số đi vào bộ câu hỏi khảo sát |
| `references=[book('P'\|'W'\|'O'\|'E', 'chNN-....md', 'ý')]` hoặc `ref(nhãn, đường dẫn, 'ý')` | Sách trong `books/`: P Parthasarathy · W Wallace · O O'Leary · E Elbardan. `ref` cho tài liệu khách (đường dẫn tương đối thư mục dự án) |
| `questions=['…']`, `extra_md` | Câu hỏi cho khách; markdown thêm (`{sec}` = số mục) |

Phần tử (lưới: làn × cột × hàng trong làn; một ô một phần tử; cột tăng theo chiều luồng):

- `N(id, loại, làn, cột, 'tên', row=0, doc=, docs='trạng thái', ctrl=['C..'])`
  - sự kiện: `start` `end` `catch` `throw` + `ev=` `message|timer|signal|conditional|terminate|error|escalation`;
    `boundary` + `attach=id, edge='top'|'bottom', interrupting=False`
  - việc: `user` (người), `service` (hệ thống — chỉ ở làn SYS), `send`, `receive`, `manual`, `rule`,
    `call` + `called='BP-xx'` (tên: `call_name('BP-xx')`), `sub` + `inner=[(id, loại, tên, mô tả)…]` (bắt đầu…kết thúc), `loop=True`
  - cổng: `xor` (tách: tên là câu hỏi; gộp: tên rỗng), `and`, `evt`
- `F(nguồn, đích, 'nhãn', default=True, route='vh'|'hv'|'hv_in', loop='top'|'bottom', via=[(cột, làn, hàng)])` — mọi nhánh ra của cổng tách có nhãn, đúng một nhánh `default`
- `M(nguồn, đích, 'nhãn', dx=±30, side='left'|'right')` — một đầu là KHÓA pool; ô giữa phần tử và pool phải trống
- `A(id, đích, 'chú thích kiểm soát (C..)', làn, cột, row=, dx=, w=)` — đặt vào ô trống
- `D(id, 'store'|'obj', 'tên', làn, cột, row=, links=[(id, 'in'|'out')])`

## Sửa cảnh báo khi build

| Cảnh báo | Sửa |
|---|---|
| `Luồng X→Y cắt qua Z` | Dời Z hoặc đích sang ô khác; hoặc đặt `route` / `via` |
| `Luồng … chồng lên luồng …` | Đổi `route` (`hv` ↔ `hv_in`) hoặc dời cổng gộp sang cột khác |
| `Trùng ô lưới`, `Chồng lấn` | Mỗi ô một phần tử; chú thích cũng chiếm ô |
| `bước tự động nhưng không nằm ở làn SYS` | Đưa `service`/`script` về làn SYS (hoặc đổi thành `user`) |
| bpmnlint: thiếu nhãn, nhánh không điều kiện, cổng vừa gộp vừa tách | Đặt tên cổng tách, `default=True` cho một nhánh, tách cổng gộp riêng |
| Vòng lặp quay lại | Thêm cổng gộp `xor` không tên trước bước nhận vòng; `loop='top'|'bottom'` |
