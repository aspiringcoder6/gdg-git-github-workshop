# Git & GitHub Workshop

Demo repo để luyện tập các câu lệnh github và cách đọc repo.
Chỉ là demo thôi, không có dataset hay gì để chạy đâu

## Yêu cầu

- Git và editor để làm bài Git.
- Python 3.10 trở lên cho demo cấu hình; khuyến nghị Python 3.10-3.13.
- Kết nối mạng để cài dependency lần đầu và thao tác với GitHub.

## Quickstart trên Windows PowerShell

Chạy từ thư mục gốc của repo:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe train.py --config configs/train.yaml
```

## Quickstart trên macOS/Linux

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python train.py --config configs/train.yaml
```

Không cần activate môi trường nếu gọi trực tiếp Python trong `.venv`.

Kết quả mặc định:

```text
DEMO ONLY: no model is trained.
model=resnet18
epochs=20
batch_size=32
dataset=data/train
```

## Đọc repo

Đọc `docs/repository-map.md` để thấy entry point và luồng dữ liệu.

`configs/train.yaml` giữ giá trị mặc định. `.env.example` chỉ là ví dụ
về tên biến môi trường; chương trình này không dùng và không tự đọc `.env`.

## Thực hành Git

Tạo branch riêng, thêm file `participants/<github-username>.md`, commit,
push và mở Pull Request theo hướng dẫn của giảng viên. File chỉ cần chứa
nickname và câu trả lời về Git/GitHub; không cần thông tin cá nhân khác.

Không commit `.env`, môi trường `.venv`, cache hoặc output sinh ra khi chạy.
