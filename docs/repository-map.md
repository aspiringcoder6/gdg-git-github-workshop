# Bản đồ repository

## Nên đọc theo thứ tự

1. `README.md`: mục đích, môi trường và cách chạy.
2. Cấu trúc thư mục ở gốc repo.
3. `requirements.txt`: dependency PyYAML.
4. `configs/train.yaml`, `.env.example` và `.gitignore`: cấu hình và file local.
5. `train.py`: entry point, tham số CLI và cách đọc YAML.
6. `src/services/training.py`: tạo chuỗi output.
7. `docs/`: tài liệu giải thích luồng chạy.

## Luồng chương trình

```text
Tham số CLI + file YAML
           |
           v
train.py: đọc, kiểm tra, chọn epochs hiệu lực
           |
           v
src/services/training.py: describe_run(...)
           |
           v
Output trên terminal
```

## Câu hỏi đọc code

- Vì sao `--epochs` có mặc định là `None`?
- Dòng nào chọn CLI thay cho giá trị mặc định từ YAML?
- Nếu YAML ghi 20, chạy với `--epochs 50` có sửa file YAML không?
- Bắt đầu đọc ở đâu nếu muốn đổi cách nhận tham số?
- Bắt đầu đọc ở đâu nếu muốn đổi các dòng output?