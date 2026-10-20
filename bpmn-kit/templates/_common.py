"""Danh mục dùng chung của DỰ ÁN: vai trò (làn), bên ngoài (pool), mã quy trình.

Một vai trò = một tên ở mọi sơ đồ. Mã quy trình chốt trước khi vẽ, không đánh số lại.
Sửa ba danh sách dưới đây cho ngành của dự án; giữ khóa 'SYS'.
"""
from bpmn_gen import register

register(
    roles={
        'DIR': 'Ban Giám đốc',
        'SALES': 'Kinh doanh',
        'SALES_MGR': 'Trưởng phòng Kinh doanh',
        'PUR': 'Mua hàng',
        'PUR_MGR': 'Trưởng phòng Mua hàng',
        'OPS': 'Vận hành',
        'OPS_MGR': 'Trưởng Vận hành',
        'WH': 'Kho',
        'ACC': 'Kế toán công nợ',
        'CASH': 'Kế toán thanh toán / Thủ quỹ',
        'CHIEF_ACC': 'Kế toán trưởng',
        'CS': 'Chăm sóc khách hàng',
        'HR': 'Hành chính – Nhân sự',
        'REQ': 'Bộ phận đề nghị',
        'MDM': 'Quản trị dữ liệu gốc',
        'SYS': 'Hệ thống ERP',
    },
    pools={
        'KH': 'Khách hàng',
        'NCC': 'Nhà cung cấp',
        'NH': 'Ngân hàng / Cổng thanh toán',
        'CQT': 'Cơ quan thuế (hệ thống HĐĐT)',
    },
    # mã: (slug tên file — ASCII không dấu, tiêu đề ngắn)
    processes={
        'BP-00': ('BP-00-tong-quan-chuoi-gia-tri', 'Tổng quan chuỗi giá trị'),
        'BP-01': ('BP-01-quan-ly-du-lieu-goc', 'Quản lý dữ liệu gốc'),
    },
)
