Thư mục ADD - Hướng dẫn sử dụng

📁 Mục đích:
Tất cả file và thư mục trong đây sẽ được copy vào mỗi thư mục c_user trong output.

📋 Cách sử dụng:
1. Đặt các file/thư mục cần thiết vào đây
2. Chạy Export Nhanh hoặc Chuyển đổi Cookie
3. Mỗi thư mục c_user sẽ chứa:
   - Cookie_Headerstring.txt
   - Password.txt
   - Tất cả nội dung từ thư mục add/

💡 Ví dụ:
input/add/
├── tool.exe
├── config.txt
└── scripts/
    └── run.bat

Kết quả output:
output/timestamp_(count)/
├── 100019763392942/
│   ├── Cookie_Headerstring.txt
│   ├── Password.txt
│   ├── tool.exe
│   ├── config.txt
│   └── scripts/
│       └── run.bat
└── 100041749641794/
    ├── Cookie_Headerstring.txt
    ├── Password.txt
    ├── tool.exe
    ├── config.txt
    └── scripts/
        └── run.bat
