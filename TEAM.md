# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): HuuDuyenBL
- Lớp:  `L3B`
- Repo của bàn: `https://github.com/Ducbaynao/K5-L3B-DAY10-HuuDuyenBL-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Phạm Lý Ngoc Đức | 2A202603991 | Sản phẩm và kinh doanh | Có |
|   2 | Nguyễn Huy Tấn | 2A202603925 | Kỹ sư cổng — lập trình cổng phòng ngừa | |
|   3 | Lê Tuấn Đạt | 2A202603949 | Kỹ sư cổng — đánh giá, kiểm thử và chỉ số theo dõi | |
|   4 | Nguyễn Minh Triết | 2A202603995 | Vận hành và pháp lý | |

### Phân công cho nhóm 4 người

- **Phạm Lý Ngoc Đức:** điều phối tiến độ; chủ trì Phiếu A và tiêu chí trong `config/acceptance_criteria.json`; phụ trách bản đồ dữ liệu, chi phí, ROI và mục `business` trong `config/operating_gates.json`. Tổng hợp quyết định v1/v2 cùng cả nhóm. Chỉ ký tiêu chí sau khi cả nhóm thống nhất, trước lần đánh giá đầu tiên.
- **Nguyễn Huy Tấn:** chủ trì viết `pre_guard` và `write_gate` trong `lab10/guards.py`; phụ trách cổng vòng 1, biện pháp tránh rò rỉ dữ liệu và sửa nguyên nhân kỹ thuật sau khi nhận thẻ. Phối hợp với Đạt phân tích trace và kiểm tra ticket hiểm.
- **Lê Tuấn Đạt:** chạy test công khai, `eval`, `trace`, `gate`; lưu mã lần chạy và tổng hợp bằng chứng vào Phiếu B/C. Phụ trách ticket hiểm, kiểm tra hồi quy và thêm chỉ số trong `lab10/monitors.py`. Chạy `checkpoint` khi nhóm thống nhất chốt vòng 1; chạy `grade` sau khi nhận thẻ và sau sửa.
- **Nguyễn Minh Triết:** phụ trách HAZOP, checklist trách nhiệm, runbook, risk register và mục `operations`, `legal` trong `config/operating_gates.json`. Nhận đúng thẻ nhóm được giao, ghi số thẻ vào Phiếu C; điền `submission/submission.json`, chạy `check_submission --collect` và kiểm tra thành phần bài nộp.

Cả nhóm cùng làm pre-mortem, phân tích sự cố và thống nhất quyết định Gate 1. Khi Đức và Triết cùng sửa `config/operating_gates.json`, thống nhất lần lượt lưu hoặc để một người nhập thay. Mỗi thành viên tự ghi đóng góp, bằng chứng và exit ticket ở mục cá nhân, đồng thời tự nộp link repo trên LMS.

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Ghi nhận hỗ trợ công cụ: Đức dùng ChatGPT/Codex hỗ trợ soạn tiêu chí, phần Sản phẩm và kinh doanh trong Phiếu A/B và cấu hình business. Các bản nháp từng điền hộ phần kỹ thuật/vận hành đã được trả về biểu mẫu để Tấn, Đạt, Triết tự thực hiện. Mỗi thành viên tự ghi phần đã dùng AI, kiểm chứng nội dung và đóng góp thực tế; không coi phần chờ là công việc đã hoàn thành.

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## PhamLyNgocDuc-2A202603991

### Phần việc phụ trách

Sản phẩm và kinh doanh, trưởng nhóm: câu1.1 và1.6, tổng hợp câu1.5 cùng nhóm; Phiếu A mục A4–A5; câu2.3/Phiếu B mục B3; lăng kính kinh doanh ở B6; câu2.9/B7.4; mục business của config/operating_gates.json. Tổng hợp quyết định v1 ở B8 và v2 ở C12 sau khi nhận đủ bằng chứng từ các thành viên.

### Đóng góp cụ thể

- Đã lập và ký tiêu chí, gồm chất lượng96%, pass^k90%, ba ngưỡng an toàn0, ngân sách8000đ/ticket, ROI0.25 và không có ca ùn; lưu trong commit cc18f49. Phần diễn giải Phiếu A được bổ sung sau baseline, không ghi nhận là hoàn tất trước baseline.
- Đã lập bản đồ nguồn dữ liệu và rủi ro đổi REFUND-v3 sang v4 từ2026-12-01; điền rủi ro kinh doanh trong pre-mortem.
- Đã cấu hình business: trần hoàn1500000đ/ngày, ngân sách8000đ/ticket, ROI tối thiểu0.25, phạm vi đánh giá all/100%; ghi lý do ở B7.4. Cần kỹ sư triển khai guard để thực thi và đo lại.
- Đã tổng hợp bằng chứng baseline cho cuộc họp quyết định: chi phí4203đ/ticket, ROI1.34 đạt nhưng hoàn sai20000đ và1 lỗi hãng oan không đạt. Chưa ký v1, chưa có thẻ để viết kết luận v2.
- Có sử dụng ChatGPT/Codex hỗ trợ đọc repo, soạn thảo và kiểm tra cấu trúc; chưa có PRD/eval card Lab9 trong repo để đối chiếu.

### Bằng chứng

- Commit ký tiêu chí: cc18f49; hash tiêu chí: 216e4226d5ba6eb9c0dfb837ca5c7d6c9b8ff25b68d06e857bd27b7e68b067c4.
- Baseline: runs/R-base-before-20261119-145954-bde05c/report.json; đây là số của cấu hình baseline, không phải kết quả xác minh business mới.
- Hồ sơ: templates/form-a-criteria.md mục A1/A3/A4/A5; templates/form-b-evaluation-gates.md mục B3/B6/B7.4/B8; config/operating_gates.json mục business.
- Commit phần bàn giao này: bổ sung mã sau khi commit thực tế; không tự ghi mã chưa tồn tại. Hướng dẫn tiếp việc: HANDOFF.md.

### Exit ticket

Chưa nộp; Đức tự viết sau khi hoàn thành buổi lab một điều học được và một điều còn chưa chắc.

### Việc chờ bằng chứng hoặc quyết định chung

- Đối chiếu PRD v1.1/eval card Lab9 khi có nguồn.
- Nhận kết quả after/prepared và hash checkpoint từ Đạt, sau đó cùng cả nhóm chốt B8/v1.
- Khi có thẻ, đọc chi phí/ROI/độ phủ và số xấu nhất theo kho/hãng, đề xuất phạm vi rồi cùng nhóm chốt C12/v2; không đổi tiêu chí đã ký.

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
