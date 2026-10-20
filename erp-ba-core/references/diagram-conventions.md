# Quy ước & mẫu sơ đồ (Mermaid)

## Mục lục
1. Quy tắc chung (để sơ đồ luôn render được)
2. Sơ đồ luồng nghiệp vụ swimlane
3. Sơ đồ quyết định (if-else, hình thoi)
4. Sơ đồ tuần tự (sequence)
5. Sơ đồ trạng thái (state)
6. Sơ đồ dữ liệu (ER)
7. Luồng chứng từ liên module & sơ đồ tổ chức
8. Lỗi cú pháp hay gặp
9. Kiểm tra sơ đồ

---

## 1. Quy tắc chung

- Viết trong khối ```` ```mermaid ````. Mỗi sơ đồ ≤ ~25 nút; lớn hơn thì tách theo giai đoạn.
- **ID nút**: chữ ASCII không dấu, không khoảng trắng (`A1`, `KT_DUYET`). **Nhãn** đặt trong ngoặc kép: `A1["Tạo đơn mua hàng (PO)"]`.
- Trong nhãn **không** dùng dấu ngoặc kép `"`, dấu `;`, ký tự `#`. Cần nhấn mạnh thì dùng chữ, không dùng ký hiệu.
- Nhãn cạnh: `-->|"Có"|`. Nhánh của hình thoi luôn có nhãn.
- Không dùng `end` (chữ thường) làm ID nút; không đặt ID nút bắt đầu bằng `o` hoặc `x` ngay sau mũi tên (Mermaid hiểu thành kiểu mũi tên tròn/chéo) — viết hoa hoặc thêm khoảng trắng.
- Hình dạng: `(["Bắt đầu"])` bắt đầu/kết thúc · `["Hành động"]` bước xử lý · `{"Điều kiện?"}` quyết định · `[("Dữ liệu")]` lưu trữ · `[["Chức năng khác"]]` chức năng con/được gọi.
- Ngôn ngữ nhãn: tiếng Việt, ngắn (≤ 8 từ), dùng đúng thuật ngữ trong glossary và ID (BR-…, MSG-…, trạng thái chuẩn).

## 2. Sơ đồ luồng nghiệp vụ swimlane

Mỗi vai trò (và "Hệ thống") là một `subgraph`. Khai báo nút bên trong subgraph; cạnh nối giữa các làn khai báo bên ngoài, sau các subgraph.

```mermaid
flowchart LR
    subgraph NV["Nhân viên mua hàng"]
        S(["Bắt đầu"]) --> A1["Tạo đơn mua hàng từ đề nghị đã duyệt"]
        A2["Sửa theo ý kiến người duyệt"]
    end
    subgraph HT["Hệ thống"]
        H1["Kiểm tra dữ liệu và hạn mức"]
        H2["Gửi đơn cho nhà cung cấp"]
    end
    subgraph TP["Trưởng phòng mua hàng"]
        D1{"Duyệt đơn?"}
    end
    A1 --> H1 --> D1
    D1 -->|"Đồng ý"| H2 --> E(["Kết thúc"])
    D1 -->|"Trả lại"| A2 --> H1
```

Ở mức quy trình đầu-cuối (BP), mỗi nút là một chức năng/chứng từ; ở mức chức năng (FN), mỗi nút là một bước thao tác. Bảng luồng chính (mục 4.2) và sơ đồ phải mô tả cùng một luồng.

## 3. Sơ đồ quyết định (if-else)

Mỗi quy tắc nghiệp vụ có điều kiện là một hình thoi; mọi nhánh có nhãn; mỗi lá là một kết quả cụ thể (thông báo MSG, trạng thái, hành động). Đặt mã BR trong nhãn để dev đối chiếu.

```mermaid
flowchart TD
    S(["Bấm Gửi duyệt"]) --> C1{"Đủ trường bắt buộc - BR-PUR-02-01?"}
    C1 -->|"Không"| M1["Báo MSG-PUR-02-01, giữ DRAFT"]
    C1 -->|"Có"| C2{"Nhà cung cấp đang hoạt động - BR-PUR-02-03?"}
    C2 -->|"Không"| M2["Báo MSG-PUR-02-03, giữ DRAFT"]
    C2 -->|"Có"| C3{"Tổng tiền lớn hơn PRM-PUR-001?"}
    C3 -->|"Có"| P2["Tạo luồng duyệt 2 cấp"]
    C3 -->|"Không"| P1["Tạo luồng duyệt 1 cấp"]
    P1 --> R(["Chuyển PENDING, gửi NTF-PUR-01"])
    P2 --> R
```

Thứ tự hình thoi = thứ tự kiểm tra trong code. Nếu các kiểm tra độc lập và phải báo tất cả lỗi một lần, ghi rõ trong BR ("kiểm tra tất cả, hiển thị danh sách lỗi") thay vì vẽ chuỗi.

## 4. Sơ đồ tuần tự (sequence)

Thành phần chuẩn: người dùng (actor), Giao diện, Dịch vụ của module, CSDL, dịch vụ module khác/duyệt/thông báo, hệ thống ngoài. Luôn có nhánh lỗi bằng `alt`. Dùng `rect` để thể hiện phạm vi một giao dịch CSDL khi quan trọng.

```mermaid
sequenceDiagram
    actor U as Nhân viên mua hàng
    participant UI as Giao diện
    participant PUR as Dịch vụ mua hàng
    participant DB as CSDL
    participant WF as Dịch vụ duyệt
    participant NT as Dịch vụ thông báo
    U->>UI: Bấm Gửi duyệt
    UI->>PUR: Gửi yêu cầu submit kèm số phiên bản
    PUR->>DB: Đọc đơn và kiểm tra phiên bản
    alt Phiên bản đã thay đổi
        PUR-->>UI: Lỗi MSG-PUR-02-09, yêu cầu tải lại
    else Vi phạm quy tắc
        PUR-->>UI: Danh sách lỗi MSG-PUR-02-01..03
    else Hợp lệ
        rect rgb(235, 245, 255)
            PUR->>DB: Cập nhật trạng thái PENDING, ghi lịch sử
            PUR->>WF: Khởi tạo luồng duyệt theo hạn mức
        end
        PUR-)NT: Phát sự kiện gửi NTF-PUR-01
        PUR-->>UI: Thành công
    end
```

Ký hiệu: `->>` gọi đồng bộ, `-->>` phản hồi, `-)` gửi bất đồng bộ (sự kiện). Không dùng `;` hay `#` trong nội dung thông điệp.

## 5. Sơ đồ trạng thái

ID trạng thái là **mã chuẩn** (conventions §6), nhãn tiếng Việt khai báo bằng `state "Nhãn" as MÃ`. Nhãn chuyển trạng thái là **hành động** (tên hành động chuẩn).

```mermaid
stateDiagram-v2
    state "Nháp" as DRAFT
    state "Chờ duyệt" as PENDING
    state "Trả lại để sửa" as RETURNED
    state "Đã duyệt" as APPROVED
    state "Hoàn thành một phần" as PARTIAL
    state "Hoàn thành" as COMPLETED
    state "Đã đóng" as CLOSED
    state "Đã hủy" as CANCELLED
    [*] --> DRAFT
    DRAFT --> PENDING : Gửi duyệt
    PENDING --> APPROVED : Duyệt cấp cuối
    PENDING --> RETURNED : Trả lại
    PENDING --> DRAFT : Thu hồi
    RETURNED --> PENDING : Gửi duyệt lại
    DRAFT --> CANCELLED : Hủy
    APPROVED --> PARTIAL : Nhận hàng một phần
    APPROVED --> COMPLETED : Nhận đủ hàng
    PARTIAL --> COMPLETED : Nhận đủ hàng
    PARTIAL --> CLOSED : Đóng phần còn lại
    APPROVED --> CANCELLED : Hủy khi chưa nhận hàng
    COMPLETED --> [*]
    CLOSED --> [*]
    CANCELLED --> [*]
```

Kiểm tra: mọi trạng thái có đường vào và (trừ trạng thái kết thúc) đường ra; trạng thái kết thúc nối `[*]`; mọi mã có trong bộ trạng thái của chứng từ ở `document-types.md`.

## 6. Sơ đồ dữ liệu (ER)

Tên thực thể ASCII viết hoa (tên bảng nghiệp vụ), thuộc tính dạng `kiểu tên_cột [PK|FK|UK] "mô tả"`; nhãn quan hệ trong ngoặc kép.

```mermaid
erDiagram
    VENDOR ||--o{ PURCHASE_ORDER : "nhận"
    PURCHASE_ORDER ||--|{ PURCHASE_ORDER_LINE : "gồm"
    ITEM ||--o{ PURCHASE_ORDER_LINE : "được đặt"
    PURCHASE_ORDER {
        bigint id PK
        string doc_no UK "Số đơn"
        date doc_date "Ngày đơn"
        bigint vendor_id FK "Nhà cung cấp"
        string status "Mã trạng thái chuẩn"
        int version "Khóa lạc quan"
    }
    PURCHASE_ORDER_LINE {
        bigint id PK
        bigint po_id FK
        bigint item_id FK
        decimal quantity "Số lượng đặt"
        decimal received_qty "Đã nhận"
    }
```

Ký hiệu quan hệ: `||--||` một-một, `||--o{` một-không hoặc nhiều, `||--|{` một-một hoặc nhiều, `}o--o{` nhiều-nhiều.

## 7. Luồng chứng từ liên module & sơ đồ tổ chức

```mermaid
flowchart LR
    PR["Đề nghị mua hàng"] --> PO["Đơn mua hàng"]
    PO --> GRN["Phiếu nhập kho"]
    PO --> INV["Hóa đơn mua hàng"]
    GRN --> INV
    INV --> PAY["Phiếu chi hoặc Ủy nhiệm chi"]
    GRN -.->|"Bút toán kho"| GL[("Sổ cái")]
    INV -.->|"Bút toán công nợ"| GL
    PAY -.->|"Bút toán thanh toán"| GL
```

```mermaid
flowchart TD
    GD["Giám đốc"] --> KTT["Kế toán trưởng"]
    GD --> TPMH["Trưởng phòng mua hàng"]
    KTT --> KTCN["Kế toán công nợ"]
    TPMH --> NVMH["Nhân viên mua hàng"]
```

## 8. Lỗi cú pháp hay gặp

| Sai | Đúng | Vì sao |
|---|---|---|
| `A[Tạo đơn (PO)]` | `A["Tạo đơn (PO)"]` | Ngoặc đơn trong nhãn không trích dẫn làm vỡ cú pháp |
| `B{Tổng > 50tr?}` | `B{"Tổng lớn hơn PRM-PUR-001?"}` | Ký tự `>` và không trích dẫn |
| `end[Kết thúc]` | `E(["Kết thúc"])` | `end` là từ khóa |
| `U->>UI: Lưu; gửi duyệt` | `U->>UI: Lưu và gửi duyệt` | `;` trong sequence bị hiểu là xuống dòng |
| `Nháp --> Chờ duyệt` | `DRAFT --> PENDING : Gửi duyệt` | ID trạng thái phải ASCII; dùng `state "Nhãn" as ID` |
| `A ||--o{ B : gồm nhiều` | `A ||--o{ B : "gồm nhiều"` | Nhãn quan hệ có khoảng trắng phải trích dẫn |
| Thiếu `end` của `subgraph` / `alt` | Đếm cặp mở-đóng | Lỗi phổ biến nhất khi sửa sơ đồ |
| Nhãn có `"` bên trong | Bỏ dấu ngoặc kép bên trong | Không thoát được an toàn |

## 9. Kiểm tra sơ đồ

- `python3 erp-ba-core/scripts/ba.py lint <root>` kiểm cú pháp cơ bản (loại sơ đồ, cặp subgraph/end và alt/end, nhãn chưa trích dẫn, ID trạng thái, nhãn quan hệ ER) và sự có mặt của 5 sơ đồ bắt buộc trong mỗi đặc tả chức năng.
- Nếu môi trường có mermaid-cli (`mmdc`), render thử từng khối để chắc chắn: tách khối ra file `.mmd` và chạy `mmdc -i x.mmd -o x.svg`.
