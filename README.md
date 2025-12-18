ConvertCookie Tool - Desktop Version FINAL

🚀 TÍNH NĂNG MỚI:
- Tự động copy thư mục input/add/ vào mỗi thư mục c_user
- Tạo file Password.txt cho mỗi account
- Cấu trúc output có tổ chức theo ID

📁 CẤU TRÚC THƯ MỤC:
ConvertCookie_Package_v2/
├── ConvertCookie_New.exe    # File chính (Linux) / ConvertCookie_New.exe (Windows)
├── input/
│   ├── input.txt           # Đặt cookie ở đây
│   └── add/                # Đặt file/thư mục cần copy ở đây
│       ├── example_tool.txt
│       └── scripts/
│           └── run.bat
├── output/                 # Kết quả xuất ra
└── README.txt             # File này

🎯 CÁCH SỬ DỤNG:

1. CHUẨN BỊ:
   - Đặt cookie vào input/input.txt
   - Đặt các file/tool cần thiết vào input/add/

2. EXPORT NHANH (Khuyến nghị):
   - Chạy ConvertCookie_New.exe
   - Nhấn nút "Export Nhanh"
   - Kết quả tự động xuất ra output/

3. CÁCH THỦ CÔNG:
   - Chạy ConvertCookie_New.exe
   - Nhấn "Chọn file input.txt" hoặc nhập trực tiếp
   - Nhấn "Chuyển đổi Cookie"

📋 FORMAT COOKIE:
cookie_data|password

Ví dụ:
datr=UXtVa...; sb=UXtVa...; c_user=100019763392942; xs=39%3A...|kiler87*
datr=XnxVa...; sb=XnxVa...; c_user=100041749641794; xs=13%3A...|Dominic1978

📦 KẾT QUẢ OUTPUT:
output/HH-MM-SS_DD-MM-YYYY_(số_cookie)/
├── 100019763392942/
│   ├── Cookie_Headerstring.txt    # Cookie Netscape format
│   ├── Password.txt               # Password của account
│   ├── example_tool.txt           # Copy từ input/add/
│   └── scripts/                   # Copy từ input/add/
│       └── run.bat
└── 100041749641794/
    ├── Cookie_Headerstring.txt
    ├── Password.txt
    ├── example_tool.txt
    └── scripts/
        └── run.bat

💡 TÍNH NĂNG THƯ MỤC ADD:
- Tất cả file/thư mục trong input/add/ sẽ được copy vào mỗi thư mục c_user
- Có thể đặt: .exe, .bat, config files, thư mục con, v.v.
- Mỗi account sẽ có bản copy riêng của tất cả file trong add/

⚠️ LƯU Ý:
- Cookie phải có c_user để tạo thư mục
- Password (phần sau dấu |) sẽ được lưu vào Password.txt
- Nếu không có password, file Password.txt sẽ rỗng
- Tool hoạt động hoàn toàn offline

🛡️ BẢO MẬT:
- Không gửi dữ liệu lên internet
- Chỉ xử lý trên máy tính của bạn
- Tất cả file được lưu local

📞 HỖ TRỢ:
Nếu gặp vấn đề:
1. Kiểm tra format cookie trong input.txt
2. Đảm bảo cookie có c_user
3. Kiểm tra quyền ghi vào thư mục output
4. Xem file README.txt trong input/add/ để hiểu cách sử dụng thư mục add

🔄 WORKFLOW KHUYẾN NGHỊ:
1. Đặt cookie vào input/input.txt
2. Đặt tool/script cần thiết vào input/add/
3. Chạy exe và nhấn "Export Nhanh"
4. Mỗi account sẽ có thư mục riêng với đầy đủ file cần thiết
5. Có thể chạy script trong mỗi thư mục account độc lập
