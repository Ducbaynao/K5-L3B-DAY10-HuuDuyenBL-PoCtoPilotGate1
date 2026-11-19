# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): HuuDuyenBL
- Lớp: `L3B`
- Repo của bàn: `https://github.com/Ducbaynao/K5-L3B-DAY10-HuuDuyenBL-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S6

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Phạm Lý Ngọc Đức | 2A202603991 | Sản phẩm và kinh doanh | Có |
|   2 | Nguyễn Huy Tấn | 2A202603925 | Kỹ sư cổng — lập trình cổng phòng ngừa | |
|   3 | Lê Tuấn Đạt | 2A202603949 | Kỹ sư cổng — đánh giá, kiểm thử và chỉ số theo dõi | |
|   4 | Nguyễn Minh Triết | 2A202603995 | Vận hành và pháp lý | |

### Phân công cho nhóm 4 người

- **Phạm Lý Ngọc Đức:** điều phối tiến độ; chủ trì Phiếu A và tiêu chí trong `config/acceptance_criteria.json`; phụ trách bản đồ dữ liệu, chi phí, ROI và mục `business` trong `config/operating_gates.json`. Tổng hợp quyết định v1/v2 cùng cả nhóm; ký tiêu chí trước lần đánh giá đầu tiên.
- **Nguyễn Huy Tấn:** chủ trì viết `pre_guard` và `write_gate` trong `lab10/guards.py`; phụ trách cổng vòng 1, biện pháp tránh rò rỉ dữ liệu và sửa nguyên nhân kỹ thuật sau khi nhận thẻ. Phối hợp với Đạt phân tích trace và kiểm tra ticket hiểm.
- **Lê Tuấn Đạt:** chạy test công khai, `eval`, `trace`, `gate`; lưu mã lần chạy và tổng hợp bằng chứng vào Phiếu B/C. Phụ trách ticket hiểm, kiểm tra hồi quy và thêm chỉ số trong `lab10/monitors.py`. Chạy `checkpoint` khi nhóm chốt vòng 1; chạy `grade` sau khi nhận thẻ và sau sửa.
- **Nguyễn Minh Triết:** phụ trách HAZOP, checklist trách nhiệm, runbook, risk register và mục `operations`, `legal` trong `config/operating_gates.json`. Nhận đúng thẻ nhóm được giao, ghi số thẻ vào Phiếu C; điền `submission/submission.json`, chạy `check_submission --collect` và kiểm tra thành phần bài nộp.

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

## PhamLyNgocDuc-2A202603991

### Phần việc phụ trách

**Trưởng nhóm; Sản phẩm và kinh doanh.** Phiếu A câu 1.1, 1.6 và tổng hợp câu 1.5; B3, lăng kính kinh doanh B6, B7.4, B8; phần kinh doanh và quyết định C12.

### Đóng góp cụ thể

- **Tiêu chí và mục tiêu:** hoàn thiện nội dung Phiếu A và bản tiêu chí đã ký (`config/acceptance_criteria.json`): tỷ lệ đúng tối thiểu 96%, pass^k tối thiểu 90%, ba ngưỡng an toàn bằng 0, chi phí tối đa 8.000đ/ticket, ROI tối thiểu 0,25 và không có ca ùn. Bản đã ký được giữ nguyên trong cả hai vòng.
- **Cổng kinh doanh:** thiết lập trần hoàn tự động 1.500.000đ/ngày, ngân sách 8.000đ/ticket và phạm vi đánh giá 100% trong `config/operating_gates.json`. Trần hoàn dành 500.000đ dự phòng, tương đương 25% ngân sách Finance 2.000.000đ/ngày.
- **Phân tích chi phí và hiệu quả:** tổng hợp số cuối của bộ nền là 4.456đ/ticket, ROI 1,24; S6 là 5.228đ/ticket, ROI 0,91. Chi phí S6 tăng so với prepared (3.595đ/ticket) vì chuyển đúng các ca mơ hồ cho người; đồng thời tiền hoàn sai giảm từ 270.000đ xuống 0 và ROI tăng từ 0,53 lên 0,91 do giảm tổn thất.
- **Quyết định Gate 1:** tổng hợp B8/C12 và ba dòng bắt buộc trong `submission/submission.json`, chốt lựa chọn **Cải tiến thêm** cho cả v1 và v2 vì còn thiếu dữ liệu tải đỉnh, kênh cảnh báo thật và kiểm thử ẩn dù kết quả công khai đã đạt.
- **Sử dụng AI:** dùng trợ lý AI rà soát câu chữ và đối chiếu số liệu trong Phiếu A/B/C; tự kiểm tra toàn bộ ngưỡng, hash chữ ký và báo cáo trước khi chốt.

### Bằng chứng

- Commit ký `cc18f49`; commit phần kinh doanh `23ad713`; Phiếu A A4–A5 và Phiếu B B3/B7.4/B8.
- `submission/runs/grade-report.json`; Phiếu C C12; `submission/submission.json`.

### Exit ticket

- **Một điều học được:** Tôi rút ra rằng tỷ lệ đúng cao và ROI tốt chưa đủ để mở pilot nếu vẫn còn hoàn sai hoặc quy lỗi oan; quyết định phải khớp toàn bộ tiêu chí đã ký.
- **Một điều còn chưa chắc:** Tôi còn chưa chắc chi phí và ROI trên bộ mock có giữ được khi cơ cấu ticket, tải giờ cao điểm và công duyệt ngoài thực tế thay đổi.

### Xác nhận cá nhân và nộp bài

- [x] Tôi đã đọc, chỉnh nội dung theo đóng góp/thông hiểu thực tế và ghi đúng việc dùng AI.
- [x] Tôi đã tự nộp link repo trên LMS.

## NguyenHuyTan-2A202603925

### Phần việc phụ trách

**Kỹ sư cổng — lập trình.** Câu 1.3 cùng Đạt; B4/B6 phần kỹ thuật; B7.1–B7.2; phân tích/sửa kỹ thuật C2, C4–C9; `lab10/guards.py`.

### Đóng góp cụ thể

- **Cổng vòng 1:** viết `pre_guard` và `write_gate` trong `lab10/guards.py` để kiểm tra chính sách hiệu lực theo ngày, tính quyền lợi từ tracking DB, kiểm bên chịu tiền, chống ghi trùng ledger, xác minh phê duyệt và các giới hạn hoàn tiền; xác minh đúng kiện/hãng/tài xế trước khi ghi lỗi và chỉ gửi payload allowlist cho hãng.
- **Sửa nguyên nhân S6:** bổ sung nhánh kiểm tra tính duy nhất của kiện trong `write_gate`. Khi thiếu `parcel_id` và có nhiều hơn 1 kiện trễ, hệ thống ghi sự kiện `ambiguous_parcel` và chuyển người xác minh trước `issue_refund` thay vì tự đoán theo kiện trễ nhất.
- **Kết quả đạt được:** trên S6 qua 60 lượt chạy (5 seed), số lỗi hãng oan giảm từ 40 (`base`) xuống 10 (`prepared`) và còn 0 (`after`); tiền hoàn sai từ 270.000đ ở `prepared` xuống 0 ở `after`.
- **Kiểm soát tính tổng quát:** cổng chỉ đọc dữ liệu nghiệp vụ từ `ReadTools` và `helpers`, không rẽ nhánh theo mã ticket, seed hoặc câu chữ; các ca có kiện rõ ràng vẫn chạy bình thường.
- **Sử dụng AI:** dùng trợ lý AI gợi ý kiểm tra biên và rà soát logic `guards.py`; tự kiểm chứng lại từng nhánh điều kiện qua `lab10.trace` và test đơn vị.

### Bằng chứng

- `lab10/guards.py`; `lab10/guards_round1.py`; snapshot `2a8b53bf`; `tests/test_round1_guards.py`.
- `evidence/S6/prepared-ambiguous.txt`, `after-ambiguous.txt`, `after-clear-parcel.txt`; Phiếu C C7/C9.

### Exit ticket

- **Một điều học được:** Tôi rút ra rằng chọn đúng hãng phải dựa trên kiện cụ thể; khi thiếu định danh và nhiều kiện đều trễ thì chọn kiện trễ nhất vẫn là đoán, cần chặn trước khi ghi tiền.
- **Một điều còn chưa chắc:** Tôi còn chưa chắc cách phát hiện tracking sai, mã kiện gắn nhầm thực tế và quyền ghi bỏ qua gate trong một hệ thống production.

### Xác nhận cá nhân và nộp bài

- [x] Tôi đã đọc, chỉnh nội dung theo đóng góp/thông hiểu thực tế và ghi đúng việc dùng AI.
- [x] Tôi đã tự nộp link repo trên LMS.

## LeTuanDat-2A202603949

### Phần việc phụ trách

**Kỹ sư cổng — đánh giá và theo dõi.** Câu 1.3; B0–B2/B7.3; eval/trace/test và mốc `prepared`; C0–C2/C8; `lab10/monitors.py`.

### Đóng góp cụ thể

- **Nhật ký và đánh giá ba mốc:** thực hiện các lượt chạy `eval`, `trace`, `gate`, `checkpoint` và `grade`, đối chiếu đầy đủ các mã lần chạy trong B0–B2 và C0–C2. Trên S6, `pass_rate` và `pass^k` lần lượt tăng từ 0,3333 (`base`) lên 0,8333 (`prepared`) và 1,0 (`after`).
- **Kiểm thử và hồi quy:** kiểm tra toàn bộ 21 test đạt (13 test công khai và 8 test trong `tests/test_round1_guards.py`), cùng 2 ticket adhoc kiểm tra lời khai sai và lọc PII. Bộ nền đạt 110/110 lượt, S6 đạt 60/60 lượt (gồm 20/20 lượt hợp lệ), không phát sinh ca mới hỏng.
- **Chỉ số theo dõi:** thêm hàm `ambiguous_parcel_rate` trong `lab10/monitors.py` chỉ dựa vào `ticket.parcel_id` và sự kiện `tracking` (không đọc nhãn/score). Trên bộ nền metric bằng 0; trên S6 sáng đèn ở mức 0,166667 (10/60 lượt chạy mơ hồ).
- **Đánh giá giới hạn bằng chứng:** đọc kết quả `PASS-VISIBLE` và kiểm tra ngưỡng cảnh báo monitor, xác định rõ CI `[1, 1]` trên mock chưa đại diện cho độ phủ thực tế hay test ẩn.
- **Sử dụng AI:** dùng trợ lý AI rà soát trace lỗi `T-002@55`, `S6-20@11`, kiểm tra test biên trong `test_round1_guards.py` và đối chiếu thành phần bài nộp; tự chạy kiểm tra toàn bộ lệnh trên máy và GitHub trước khi chốt.

### Bằng chứng

- `evidence/round1/tests.txt`; `evidence/S6/tests.txt`; `tests/test_round1_guards.py`; `lab10/monitors.py`.
- `submission/runs/grade-report.json` và report ba mốc; `submission/runs/journal.jsonl`; Phiếu C C0/C8.

### Exit ticket

- **Một điều học được:** Tôi rút ra rằng phải đo mốc `prepared` trước khi sửa vòng 2, kiểm tra hồi quy đầy đủ trên bộ nền và dùng monitor không cần nhãn; metric mơ hồ vẫn có thể cao dù gate đã chặn được tác hại.
- **Một điều còn chưa chắc:** Tôi còn chưa chắc độ đại diện của 12 ticket S6 và tín hiệu mơ hồ 16,67% khi tỷ lệ đơn nhiều kiện, thiếu log hoặc tải thực tế thay đổi.

### Xác nhận cá nhân và nộp bài

- [x] Tôi đã đọc, chỉnh nội dung theo đóng góp/thông hiểu thực tế và ghi đúng việc dùng AI.
- [x] Tôi đã tự nộp link repo trên LMS.

## NguyenMinhTriet-2A202603995

### Phần việc phụ trách

**Vận hành và pháp lý.** Câu 1.2/1.4; B4–B5/B6 phần con người/pháp lý; B7.5–B7.6; C3.2/C10/C11; `operations`/`legal` và gom bài.

### Đóng góp cụ thể

- **Cấu hình người và pháp lý:** điền mục `operations`/`legal` trong `config/operating_gates.json` với PIC `NV-TUNG`, người duyệt `NV-HANH`, 1 người trực xử lý 6 ca/giờ, SLA 60 phút, kiểm mẫu 10% và `decision_note = true`; chặn các trường ghi chú và thông tin liên hệ cá nhân khi gửi hãng; bắt buộc có nguyên nhân ghi nhận trước khi ghi lỗi hãng.
- **HAZOP, checklist và runbook:** phụ trách B4–B5/B7.5–B7.6, C3.2/C10/C11. Bốn điều kiện dừng trong `operations.stop_conditions`: hoàn sai → NV-TUNG tắt `issue_refund` liên quan trong tối đa 5 phút, NV-OANH đối soát; lỗi hãng oan hoặc rò rỉ PII → tắt `file_carrier_fault`/`notify_carrier` liên quan; ùn hoặc dự báo chờ quá 60 phút → NV-HANH điều phối thủ công, giảm tiếp nhận tự động; chi phí trên 8.000đ/ticket hoặc ROI dưới 0,25 → chưa mở pilot. Runbook gọi dự phòng khi backlog từ 3 ca hoặc thời gian chờ từ 30 phút.
- **Đánh giá năng lực xử lý:** tổng hợp stress 14 ca cần duyệt đến cùng lúc (`evidence/round1/queue-stress.json`): 1 người duyệt 6 ca/giờ khiến ca cuối chờ 130 phút và 7 ca vượt SLA 60 phút. Trên S6 sau sửa, số ca ùn bằng 0 và tỷ lệ chuyển người duyệt là 0,25.
- **Hồ sơ nộp và bảo vệ bên thứ ba:** hoàn thiện phần tác động lên hãng/tài xế, risk register, quy trình đối soát (`NV-OANH`) và `submission/submission.json`; chạy `check_submission --collect` xác nhận **ĐỦ THÀNH PHẦN** với đầy đủ manifest.
- **Sử dụng AI:** dùng trợ lý AI hỗ trợ rà soát bố cục phiếu và đối chiếu số liệu từ report/trace thực tế; tự kiểm chứng toàn bộ cấu hình vận hành và hồ sơ gom bài trước khi đẩy lên repo nhóm.

### Bằng chứng

- `config/operating_gates.json` (mục `operations`, `legal`) và `config/operating_gates.round1.json`; Phiếu B B4/B5/B7.5/B7.6.
- `evidence/round1/queue-stress.json`; `submission/runs/grade-report.md` (số ca ùn, tỉ lệ chuyển người duyệt).
- Phiếu C C3.2/C10/C11; `submission/submission.json`; `submission/manifest.json`; `evidence/S6/submission-check.txt`.

### Exit ticket

- **Một điều học được:** Gate kỹ thuật chặn được lệnh ghi sai, nhưng bảo vệ bên thứ ba (hãng, tài xế) còn cần đúng người chịu trách nhiệm, người nhận khiếu nại và quy trình đối soát; payload đúng schema và đã lọc PII chưa thay thế được việc kiểm tra và phản hồi khi có tranh chấp.
- **Một điều còn chưa chắc:** Tôi chưa chắc 1 người duyệt (6 ca/giờ) chịu được tải đỉnh thật — stress 14 ca đã cho thấy chờ 130 phút — và cam kết dừng trong 5 phút có thực hiện được không khi kênh cảnh báo vẫn đang mô phỏng, chưa có lịch trực dự phòng và chưa diễn tập.

### Xác nhận cá nhân và nộp bài

- [x] Tôi đã đọc, chỉnh nội dung theo đóng góp/thông hiểu thực tế và ghi đúng việc dùng AI.
- [x] Tôi đã tự nộp link repo trên LMS.

## Kết quả chung cuối cùng

- Thẻ S6 · mã grade `R-S6-grade-20261119-161924-4fd606`: **PASS-VISIBLE** (kiểm thử ẩn do team chấm chạy sau buổi học).
