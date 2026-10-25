# Thực hành Git & GitHub cho GDG

**Sản phẩm cần nộp:** một Pull Request (PR) và một nhận xét review cho bạn cùng cặp.

## Các task hôm nay

| Task | Việc cần làm | Sản phẩm | Thời gian |
|---|---|---|---:|
| 1 | Cập nhật main, tạo branch và file giới thiệu | File cá nhân trên branch riêng | 2 phút |
| 2 | Kiểm tra thay đổi, stage và commit | Một commit đúng nội dung task | 3 phút |
| 3 | Push branch và mở Pull Request | Link PR về repo buổi học | 3 phút |
| 4 | Review theo cặp | Một nhận xét cụ thể cho bạn | 2 phút |
| 5, thêm | Đọc repo và chạy cấu hình | Ghi chú về luồng chạy và kết quả | 5-10 phút |
| 6, thêm | Tạo và xử lý merge conflict | Repo luyện tập không còn conflict | 8-10 phút |

## Chuẩn bị trước khi bắt đầu

Bạn cần Git, một editor như VS Code, tài khoản GitHub và link repo mình đã cho r đó. Chỉ Task 5 cần Python để chạy chương trình.

Trong các lệnh bên dưới, thay những phần sau bằng thông tin thật trước khi chạy:

| Ký hiệu | Thay bằng |
|---|---|
| `OWNER` | Tài khoản hoặc tổ chức sở hữu repo buổi học |
| `REPO` | Tên repo buổi học, ví dụ `gdg-git-workshop` |
| `YOUR_USERNAME` | Username GitHub của bạn |
| `YOUR_EMAIL` | Email bạn dùng cho commit, có thể là địa chỉ noreply chính xác từ GitHub |

Ví dụ, username là `ninh-example` thì tên branch ở Task 1 là `docs/add-ninh-example`, tên file là `participants/ninh-example.md`.

### Lấy repo về máy

1. Mở link repo mình cung cấp, chọn **Fork** để tạo bản repo trong tài khoản của bạn.
2. Clone **fork của bạn** và vào thư mục:

```bash
git clone https://github.com/YOUR_USERNAME/REPO.git git-github-practice
cd git-github-practice
git config user.name "Tên hoặc nickname của bạn"
git config user.email "YOUR_EMAIL"
git remote add upstream https://github.com/OWNER/REPO.git
git remote -v
```

**Kiểm tra:** `origin` trỏ về fork của bạn, `upstream` trỏ về repo của anh. Nếu đã clone và cấu hình trước đó, dùng lại repo đó; chỉ thêm `upstream` nếu chưa có. Sau clone không cần chạy `git init`.

3. Chuẩn bị đăng nhập để push được lên fork. Có thể kiểm tra trước buổi bằng:

```bash
git push --dry-run origin main
```

Nếu xuất hiện cửa sổ đăng nhập, hoàn tất bước đó. Thông tin `user.name` và `user.email` là thông tin tác giả commit, không thay cho đăng nhập GitHub. Hướng dẫn này dùng nhánh chính tên `main`; thay bằng tên thực tế nếu repo dùng tên khác.

## Task 1 — Tạo branch và file giới thiệu

**Mục tiêu:** bắt đầu một task trên branch riêng, từ main đã cập nhật.

### Bước 1: kiểm tra và cập nhật

Chạy trong thư mục repo:

```bash
git status
git switch main
git pull --ff-only upstream main
git switch -c docs/add-YOUR_USERNAME
```

Trước khi chuyển branch, `git status` cần cho thấy không có thay đổi đang làm dở. Nếu có, giữ lại công việc và nhờ hỗ trợ trước khi tiếp tục.

### Bước 2: tạo file cá nhân

Trong editor, tạo file `participants/YOUR_USERNAME.md`. Thay các phần hướng dẫn trong mẫu bằng câu trả lời của bạn rồi lưu file:

```markdown
# YOUR_USERNAME

- Tên hoặc nickname: ...
- Git là gì? Viết một câu bằng lời của bạn.
- GitHub là gì? Viết một câu bằng lời của bạn.
- Commit khác push như thế nào? Viết một câu phân biệt.
```

Mỗi người dùng một file riêng. Bài này không yêu cầu sửa README chung.

**Hoàn thành khi:** bạn đang ở `docs/add-YOUR_USERNAME` và file đã được lưu đúng đường dẫn.

## Task 2 — Kiểm tra, stage và commit

**Mục tiêu:** biết chính xác nội dung được đưa vào commit.

```bash
git status
git add participants/YOUR_USERNAME.md
git diff --staged
git commit -m "docs: add YOUR_USERNAME introduction"
git log --oneline -3
```

Ở bước `git diff --staged`, đọc lại nội dung trước khi commit:

- Chỉ có file cá nhân bạn vừa tạo.
- Các câu trả lời đã điền, không còn lời nhắc từ mẫu.
- Không có file `.env`, `.venv` hoặc file ngoài task.

File mới chưa được Git theo dõi có thể chưa hiện trong `git diff`. Dùng `git status` để thấy file mới; sau khi add, dùng `git diff --staged` để xem nội dung của nó.

Nếu add nhầm một file, có thể bỏ riêng file đó khỏi staging nhưng giữ nội dung trên máy:

```bash
git restore --staged TEN_FILE_ADD_NHAM
```

**Hoàn thành khi:** lịch sử có commit mới với message rõ ràng. Lúc này commit vẫn ở local nếu bạn chưa push.

**Tự trả lời trước khi tiếp tục:** đồng đội đã nhìn thấy commit này trên GitHub chưa?

## Task 3 — Push và mở Pull Request

**Mục tiêu:** gửi thay đổi lên fork, rồi đề xuất đưa nó vào repo buổi học.

### Bước 1: push branch

```bash
git push -u origin docs/add-YOUR_USERNAME
```

### Bước 2: mở PR trên GitHub

Mở repo gốc của buổi học. Chọn **Compare & pull request** nếu có banner, hoặc vào **Pull requests → New pull request**. Dùng **compare across forks** khi cần chọn fork làm nguồn.

Kiểm tra hướng gửi:

```text
Nơi nhận: OWNER/REPO              → main
Nơi gửi:  YOUR_USERNAME/REPO      → docs/add-YOUR_USERNAME
```

- **Base repository / base branch:** repo của mình và `main`.
- **Head fork / compare branch:** fork của bạn và branch vừa push.

### Bước 3: viết tiêu đề và mô tả

Tiêu đề: `docs: add YOUR_USERNAME introduction`.

Mô tả gợi ý, điền theo việc bạn đã làm:

```text
Thay đổi: thêm file participants/YOUR_USERNAME.md.

Nội dung: giới thiệu ngắn và giải thích Git, GitHub, commit, push.

Cách kiểm tra: mở Files changed, đọc câu trả lời và kiểm tra PR chỉ thêm file cá nhân.
```

Chọn **Create pull request**, mở **Files changed** và kiểm tra diff lần nữa.

**Hoàn thành khi:** có link PR về đúng repo của mình, chỉ chứa file cá nhân của bạn. Chưa cần đợi PR được merge.

**Tự trả lời:** push branch xong có nghĩa là main đã nhận thay đổi chưa?

## Task 4 — Review theo cặp

**Mục tiêu:** đọc và nhận xét được thay đổi của một người khác.

1. Đổi link PR với bạn cùng cặp.
2. Mở **Files changed** của PR bên kia.
3. Đọc file và kiểm tra: câu trả lời có đúng không, thay đổi có đúng phạm vi không, có dễ hiểu không?
4. Để lại ít nhất một nhận xét cụ thể. Có thể góp ý một câu cần sửa hoặc chỉ rõ điểm đã kiểm tra và thấy đúng.

Ví dụ một góp ý có thể dùng khi đúng với nội dung bạn đang đọc:

> “Bạn đang mô tả commit là đưa code lên GitHub. Bạn kiểm tra lại điểm khác nhau giữa commit và push nhé.”


### Nếu nhận được góp ý cần sửa

Quay lại editor trên **chính branch đang có PR**, sửa và lưu file, rồi:

```bash
git add participants/YOUR_USERNAME.md
git diff --staged
git commit -m "docs: clarify Git workflow explanation"
git push
```

PR đang mở sẽ cập nhật theo branch; không cần tạo PR mới. Nếu không có nội dung cần sửa thì không cần tạo thêm commit.

**Hoàn thành khi:** bạn đã để lại một nhận xét cụ thể trên PR của bạn cùng cặp.

## Checklist

- [ ] Tạo branch riêng cho task.
- [ ] Có file `participants/YOUR_USERNAME.md` với câu trả lời của mình.
- [ ] Đã kiểm tra diff và tạo commit đúng phạm vi.
- [ ] Đã push lên fork và mở PR về đúng repo, đúng nhánh nhận.
- [ ] Đã review một PR khác và nộp đủ link.

**Sau khi mình merge PR**, cập nhật main local trước task mới:

```bash
git switch main
git pull --ff-only upstream main
```

## Task 5, mở rộng — Đọc repo và thử cấu hình

### Phần A: đọc code, chưa cần cài Python

Đọc theo thứ tự `README.md → requirements.txt → configs/train.yaml → train.py → src/services/training.py`. Ghi câu trả lời ngắn:

1. Chương trình mẫu làm gì, có train model thật không?
2. Entry point là file nào?
3. Cần cài thư viện ngoài nào?
4. Giá trị epochs mặc định nằm ở đâu?
5. Dòng code nào quyết định ưu tiên `--epochs` từ terminal?
6. `.env.example` và `.venv` có vai trò khác nhau thế nào?

### Phần B: chạy thử, cần Python

Trong thư mục gốc repo, tạo môi trường và chạy ba trường hợp.

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe train.py --config configs/train.yaml
.\.venv\Scripts\python.exe train.py --config configs/train.yaml --epochs 30
.\.venv\Scripts\python.exe train.py --config configs/train.yaml --epochs 0
```

**macOS/Linux:**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python train.py --config configs/train.yaml
.venv/bin/python train.py --config configs/train.yaml --epochs 30
.venv/bin/python train.py --config configs/train.yaml --epochs 0
```

**Điều cần quan sát:** lượt đầu in `epochs=20`, lượt hai in `epochs=30`, lượt cuối báo lỗi vì epochs phải lớn hơn 0. Chương trình chỉ in cấu hình, không chạy train thật.

Mở lại YAML và chạy:

```bash
git diff -- configs/train.yaml
```

Giải thích vì sao truyền `--epochs 30` không làm file YAML trên đĩa thay đổi.


## Task 6, mở rộng — Xử lý merge conflict

**Mục tiêu:** hiểu cách giải quyết khi hai nhánh sửa cạnh tranh cùng một dòng. Thực hiện trong thư mục luyện tập mới, tách khỏi repo đang làm PR.

### Bước 1: tạo điểm xuất phát chung

Tạo một thư mục trống tên `conflict-lab`, mở terminal ở thư mục đó rồi chạy:

```bash
git init -b main
git config user.name "Tên hoặc nickname của bạn"
git config user.email "YOUR_EMAIL"
```

Tạo file `schedule.txt` trong editor với đúng một dòng `meeting=19:00`, lưu file rồi:

```bash
git add schedule.txt
git commit -m "chore: add meeting time"
git switch -c feature/time-a
```

### Bước 2: tạo hai đề xuất khác nhau

Trên nhánh A, sửa dòng thành `meeting=19:30`, lưu rồi:

```bash
git add schedule.txt
git commit -m "docs: propose meeting at 19:30"
git switch main
git switch -c feature/time-b
```

Trên nhánh B, sửa dòng thành `meeting=20:00`, lưu rồi:

```bash
git add schedule.txt
git commit -m "docs: propose meeting at 20:00"
git switch main
git merge --ff-only feature/time-a
git merge feature/time-b
```

Lệnh merge cuối sẽ báo conflict. Đây là tình huống cần xử lý của bài tập.

### Bước 3: chọn nội dung cuối cùng

Chạy `git status`, mở `schedule.txt` và quan sát:

```text
<<<<<<< HEAD
meeting=19:30
=======
meeting=20:00
>>>>>>> feature/time-b
```

Giả sử nhóm thống nhất họp lúc 20:00. Sửa toàn bộ file thành đúng một dòng `meeting=20:00`, bỏ các dấu conflict, lưu rồi:

```bash
git add schedule.txt
git commit -m "merge: agree on meeting at 20:00"
git status
git log --oneline --graph --all
```

**Hoàn thành khi:** nội dung đúng thỏa thuận, không còn marker conflict, working tree sạch và có commit merge. Nếu cần dừng lượt merge đang conflict trước khi giải quyết, có thể dùng `git merge --abort`.

**Tự giải thích:** vì sao Git cần bạn quyết định nội dung cuối, thay vì tự biết giờ họp nào đúng?

## Khi gặp vướng mắc

| Vấn đề | Việc nên kiểm tra |
|---|---|
| Không push được | `git remote -v`: origin có đúng fork của bạn không? Đã đăng nhập đúng tài khoản chưa? |
| File mới không hiện trong diff | Xem `git status`, add đúng file rồi dùng `git diff --staged` |
| Không thấy thay đổi trong PR | Đã lưu, commit và push chưa? Chọn đúng head fork và compare branch chưa? |
| Branch đã tồn tại | Xem `git branch`; dùng lại branch nếu đang tiếp tục task, hoặc đặt tên mới nếu bắt đầu lại |
| `--ff-only` thất bại | Giữ nguyên công việc và nhờ hỗ trợ kiểm tra lịch sử trước khi tiếp tục |
| Thiếu thư viện `yaml` | Cài requirements bằng đúng Python trong `.venv` rồi chạy bằng cùng Python đó |

Khi nhờ hỗ trợ, gửi tên task, lệnh vừa chạy và thông báo lỗi; không gửi token, mật khẩu hoặc API key.

## Tham khảo

- [Git: tài liệu lệnh](https://git-scm.com/docs)
- [GitHub: tạo Pull Request từ fork](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request-from-a-fork)
- [GitHub: xử lý merge conflict bằng dòng lệnh](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/resolving-a-merge-conflict-using-the-command-line)
