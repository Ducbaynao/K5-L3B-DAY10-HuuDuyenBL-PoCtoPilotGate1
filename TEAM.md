# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): HuuDuyenBL
- Lớp:  `L3B`
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

- **Phạm Lý Ngọc Đức:** điều phối tiến độ; chủ trì Phiếu A và tiêu chí trong `config/acceptance_criteria.json`; phụ trách bản đồ dữ liệu, chi phí, ROI và mục `business` trong `config/operating_gates.json`. Tổng hợp quyết định v1/v2 cùng cả nhóm. Chỉ ký tiêu chí sau khi cả nhóm thống nhất, trước lần đánh giá đầu tiên.
- **Nguyễn Huy Tấn:** chủ trì viết `pre_guard` và `write_gate` trong `lab10/guards.py`; phụ trách cổng vòng 1, biện pháp tránh rò rỉ dữ liệu và sửa nguyên nhân kỹ thuật sau khi nhận thẻ. Phối hợp với Đạt phân tích trace và kiểm tra ticket hiểm.
- **Lê Tuấn Đạt:** chạy test công khai, `eval`, `trace`, `gate`; lưu mã lần chạy và tổng hợp bằng chứng vào Phiếu B/C. Phụ trách ticket hiểm, kiểm tra hồi quy và thêm chỉ số trong `lab10/monitors.py`. Chạy `checkpoint` khi nhóm thống nhất chốt vòng 1; chạy `grade` sau khi nhận thẻ và sau sửa.
- **Nguyễn Minh Triết:** phụ trách HAZOP, checklist trách nhiệm, runbook, risk register và mục `operations`, `legal` trong `config/operating_gates.json`. Nhận đúng thẻ nhóm được giao, ghi số thẻ vào Phiếu C; điền `submission/submission.json`, chạy `check_submission --collect` và kiểm tra thành phần bài nộp.

Cả nhóm cùng làm pre-mortem, phân tích sự cố và thống nhất quyết định Gate 1. Khi Đức và Triết cùng sửa `config/operating_gates.json`, thống nhất lần lượt lưu hoặc để một người nhập thay. Mỗi thành viên tự ghi đóng góp, bằng chứng và exit ticket ở mục cá nhân, đồng thời tự nộp link repo trên LMS.

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Các mục dưới đây tổng hợp công việc, sản phẩm và số liệu theo vai đã phân công, với hỗ trợ của ChatGPT/Codex. Số liệu là kết quả chung của repo, được gắn với phần việc mỗi vai chịu trách nhiệm; không dùng chúng để suy ra ai trực tiếp viết từng dòng code hoặc chạy từng lệnh. Mỗi thành viên cần kiểm chứng nội dung, chỉnh phần đóng góp trực tiếp và exit ticket theo thực tế trước khi xác nhận.

Phần đã có bằng chứng người dùng cung cấp trong phiên làm việc: đặt danh tính Git, ký tiêu chí, chạy baseline/gate/trace, nhận S6 và chạy grade/trace. Các sửa code, cấu hình, kiểm thử bổ sung, tổng hợp phiếu và gom bài được Codex hỗ trợ. Mỗi thành viên ghi rõ mức hỗ trợ AI trong phần của mình.

## PhamLyNgocDuc-2A202603991

### Phần việc phụ trách

**Trưởng nhóm; Sản phẩm và kinh doanh.** Phiếu A câu 1.1, 1.6 và tổng hợp câu 1.5; B3, lăng kính kinh doanh B6, B7.4, B8; phần kinh doanh và quyết định C12.

### Công việc và kết quả theo phân công

- **Tiêu chí và mục tiêu:** phụ trách nội dung Phiếu A và bản tiêu chí đã ký: tỷ lệ đúng tối thiểu 96%, pass^k tối thiểu 90%, ba ngưỡng an toàn bằng 0, chi phí tối đa 8.000đ/ticket, ROI tối thiểu 0,25 và không có ca ùn. Bản đã ký được giữ nguyên trong cả hai vòng.
- **Cổng kinh doanh:** phụ trách trần hoàn tự động 1.500.000đ/ngày, ngân sách 8.000đ/ticket và phạm vi đánh giá 100%. Trần hoàn dành 500.000đ dự phòng, tương đương 25% ngân sách Finance 2.000.000đ/ngày.
- **Phân tích chi phí và hiệu quả:** tổng hợp số cuối của bộ nền là 4.456đ/ticket, ROI 1,24; S6 là 5.228đ/ticket, ROI 0,91. Chi phí S6 tăng so với prepared 3.595đ/ticket vì chuyển đúng các ca mơ hồ cho người; đồng thời tiền hoàn sai giảm từ 270.000đ xuống 0 và ROI tăng từ 0,53 lên 0,91 do giảm tổn thất.
- **Quyết định Gate 1:** phụ trách tổng hợp B8/C12 và ba dòng bắt buộc trong submission.json. Hồ sơ giữ đề xuất “Cải tiến thêm” cho v1/v2 vì cần kiểm chứng dữ liệu, tải đỉnh và khả năng vận hành thật, dù kết quả công khai đã đạt.


### Bằng chứng

- Commit ký cc18f49; commit phần kinh doanh 23ad713; Phiếu A A4–A5 và Phiếu B B3/B7.4/B8.
- submission/runs/grade-report.json; Phiếu C C12; submission/submission.json.

### Exit ticket — bản nháp để cá nhân chỉnh

- **Một điều học được:** Tôi rút ra rằng tỷ lệ đúng cao và ROI tốt chưa đủ để mở pilot nếu vẫn hoàn sai hoặc quy lỗi oan; quyết định phải khớp toàn bộ tiêu chí đã ký.
- **Một điều còn chưa chắc:** Tôi còn chưa chắc chi phí và ROI trên bộ mock có giữ được khi cơ cấu ticket, tải giờ cao điểm và công duyệt ngoài thực tế thay đổi.

### Xác nhận cá nhân và nộp bài

- [x] Tôi đã đọc, chỉnh nội dung theo đóng góp/thông hiểu thực tế và ghi đúng việc dùng AI.
- [x] Tôi đã tự nộp link repo trên LMS.

## NguyenHuyTan-2A202603925

### Phần việc phụ trách

**Kỹ sư cổng — lập trình.** Câu 1.3 cùng Đạt; B4/B6 phần kỹ thuật; B7.1–B7.2; phân tích/sửa kỹ thuật C2, C4–C9; lab10/guards.py.

### Công việc và kết quả theo phân công

- **Cổng vòng 1:** phụ trách phần lập trình kiểm chính sách theo ngày, tính quyền lợi từ tracking, kiểm bên chịu tiền, ledger, phê duyệt và các giới hạn; xác minh đúng kiện/hãng/tài xế trước ghi lỗi, chỉ gửi payload nghiệp vụ được phép cho hãng.
- **Sửa nguyên nhân S6:** phụ trách nhánh kiểm tính rõ ràng của kiện trong write_gate. Khi không có parcel_id và nhiều kiện đều trễ, hệ thống chuyển người xác minh trước issue_refund thay vì tự chọn kiện trễ nhất rồi ghi tiền/lỗi hãng.
- **Kết quả của phần cổng:** trên S6, số lỗi hãng oan ở base là 40, prepared còn 10, after còn 0; tiền hoàn sai từ 270.000đ ở prepared xuống 0 ở after. Đây là kết quả chung qua 60 lượt chạy, không phải số thiệt hại thực tế hoặc số đóng góp cá nhân độc lập.
- **Kiểm soát tính tổng quát:** cổng dùng dữ liệu nghiệp vụ, không nhánh theo mã ticket, seed hoặc câu chữ. Các ca có kiện rõ ràng vẫn được phục vụ; gate còn phụ thuộc độ đúng của tracking và việc mọi lệnh ghi đều đi qua cổng.



### Bằng chứng

- lab10/guards.py; lab10/guards_round1.py; snapshot 2a8b53bf; tests/test_round1_guards.py.
- evidence/S6/prepared-ambiguous.txt, after-ambiguous.txt, after-clear-parcel.txt; Phiếu C C7/C9.

### Exit ticket — bản nháp để cá nhân chỉnh

- **Một điều học được:** Tôi rút ra rằng chọn đúng hãng phải dựa trên kiện cụ thể; khi thiếu định danh và nhiều kiện đều trễ thì chọn kiện trễ nhất vẫn là đoán, cần chặn trước khi ghi tiền.
- **Một điều còn chưa chắc:** Tôi còn chưa chắc cách phát hiện tracking sai, mã kiện gắn nhầm thực tế và quyền ghi bỏ qua gate trong một hệ thống production.

### Xác nhận cá nhân và nộp bài

- [x] Tôi đã đọc, chỉnh nội dung theo đóng góp/thông hiểu thực tế và ghi đúng việc dùng AI.
- [x] Tôi đã tự nộp link repo trên LMS.

## LeTuanDat-2A202603949

### Phần việc phụ trách

**Kỹ sư cổng — đánh giá và theo dõi.** Câu 1.3; B0–B2/B7.3; eval/trace/test và mốc prepared; C0–C2/C8; lab10/monitors.py.

### Công việc và kết quả theo phân công

- **Nhật ký và đánh giá ba mốc:** phụ trách tổng hợp B0–B2/C0–C2, trace và báo cáo base/prepared/after. Trên S6, pass_rate và pass^k lần lượt tăng từ 0,3333 lên 0,8333 rồi 1,0; giữ đủ mã lần chạy để truy nguyên từng kết luận.
- **Kiểm thử và hồi quy:** phần việc kiểm tra có 21 test đạt, gồm 13 test công khai và 8 test bổ sung; hai ticket adhoc vòng 1 kiểm lời khai sai và dữ liệu gửi hãng. Bộ nền cuối đạt 110/110 lượt, S6 đạt 60/60 lượt, trong đó 20/20 lượt hợp lệ đạt; không có ca mới hỏng.
- **Chỉ số theo dõi:** phụ trách ambiguous_parcel_rate trong monitors.py, chỉ dùng parcel_id và tracking, không dùng nhãn/score. Kết quả nền bằng 0; S6 bằng 0,166667, tương ứng 10/60 lượt chạy có yêu cầu mơ hồ.
- **Đọc giới hạn bằng chứng:** tổng hợp kết quả PASS-VISIBLE và kiểm monitor sáng đèn, không diễn giải CI [1;1] trên mock thành bảo đảm 100% ngoài thực tế; kiểm thử ẩn chưa có trên máy.



### Bằng chứng

- evidence/round1/tests.txt; evidence/S6/tests.txt; tests/test_round1_guards.py.
- submission/runs/grade-report.json và report ba mốc; runs/journal.jsonl; Phiếu C C0/C8.

### Exit ticket — bản nháp để cá nhân chỉnh

- **Một điều học được:** Tôi rút ra rằng phải đo prepared trước khi sửa, kiểm cả regression và dùng monitor không cần nhãn; metric mơ hồ có thể vẫn cao dù gate đã ngăn tác hại.
- **Một điều còn chưa chắc:** Tôi còn chưa chắc độ đại diện của 12 ticket S6 và tín hiệu mơ hồ 16,67% khi tỷ lệ đơn nhiều kiện, thiếu log hoặc tải thực thay đổi.

### Xác nhận cá nhân và nộp bài

- [x] Tôi đã đọc, chỉnh nội dung theo đóng góp/thông hiểu thực tế và ghi đúng việc dùng AI.
- [x] Tôi đã tự nộp link repo trên LMS.

## NguyenMinhTriet-2A202603995

### Phần việc phụ trách

**Vận hành và pháp lý.** Câu 1.2/1.4; B4–B5/B6 phần con người/pháp lý; B7.5–B7.6; C3.2/C10/C11; operations/legal và gom bài.

### Công việc và kết quả theo phân công

- **Cấu hình người và pháp lý:** phụ trách operations/legal với PIC NV-TUNG, người duyệt NV-HANH, một người trực xử lý 6 ca/giờ, SLA 60 phút, kiểm mẫu 10% và ghi chú quyết định. Các trường ghi chú/thông tin liên hệ cá nhân bị chặn khi gửi hãng; ghi lỗi phải có nguyên nhân được ghi nhận.
- **HAZOP, checklist và runbook:** phụ trách B4–B5/B7.5–B7.6, C3.2/C10/C11. Bốn điều kiện dừng trong `operations.stop_conditions`: hoàn sai → NV-TUNG tắt `issue_refund` liên quan trong tối đa 5 phút, NV-OANH đối soát; lỗi hãng oan hoặc rò rỉ PII → tắt `file_carrier_fault`/`notify_carrier` liên quan; ùn hoặc dự báo chờ quá 60 phút → NV-HANH điều phối thủ công, giảm tiếp nhận tự động; chi phí trên 8.000đ/ticket hoặc ROI dưới 0,25 → chưa mở pilot. Runbook gọi dự phòng khi backlog từ 3 ca hoặc thời gian chờ từ 30 phút. Kênh cảnh báo `ops-gate1` hiện chỉ là kênh mô phỏng; đây là kế hoạch, chưa diễn tập thật.
- **Đánh giá năng lực xử lý:** tổng hợp stress 14 ca cần duyệt đến cùng lúc (evidence/round1/queue-stress.json): một người duyệt 6 ca/giờ thì ca cuối chờ 130 phút và 7 ca vượt SLA 60 phút. Trên bộ S6 sau sửa, số ca ùn bằng 0, tỷ lệ chuyển người duyệt là 0,25 (base 0, prepared 0,0833); không lấy kết quả mock này thay bằng chứng chịu tải đỉnh thực tế.
- **Hồ sơ nộp và bảo vệ bên thứ ba:** phụ trách phần tác động lên hãng/tài xế, risk register, quy trình đối soát (người nhận khiếu nại bên thứ ba: NV-OANH) và submission.json (`members` khớp bảng thành viên, thẻ S6, v1/v2, ba dòng). Bộ nộp có đủ code/config hai vòng, ba phiếu, report ba mốc và journal; `check_submission` in **ĐỦ THÀNH PHẦN**, kiểm tra 20 đường dẫn bắt buộc cùng 19 hash manifest đều đạt. S6 sau sửa không còn lỗi hãng oan hoặc rò rỉ PII trong dữ liệu đã đo.

**Sử dụng AI:** Codex hỗ trợ soạn nội dung phiếu, cấu hình và tổng hợp bằng chứng cho phần trên; Claude Code hỗ trợ rà soát, đối chiếu số liệu và sửa lỗi trình bày trong TEAM.md. Tôi (Nguyễn Minh Triết) chịu trách nhiệm định hướng, kiểm tra và xác nhận các nội dung trên theo vai Vận hành và pháp lý; mọi commit của nhóm được đẩy bằng danh tính Git chung của trưởng nhóm (theo README bước 2a) nên không có commit đứng tên riêng.

### Bằng chứng

- config/operating_gates.json (mục `operations`, `legal`) và operating_gates.round1.json; Phiếu B B4/B5/B7.5/B7.6.
- evidence/round1/queue-stress.json; evidence/S6/R-S6-grade-20261119-161924-4fd606.md (số ca ùn, tỉ lệ chuyển người duyệt).
- Phiếu C C3.2/C10/C11; submission/submission.json; submission/manifest.json; evidence/S6/submission-check.txt, final-submission-check.txt, final-audit.json.

### Exit ticket

- **Một điều học được:** Gate kỹ thuật chặn được lệnh ghi sai, nhưng bảo vệ bên thứ ba (hãng, tài xế) còn cần đúng người chịu trách nhiệm, người nhận khiếu nại và quy trình đối soát; payload đúng schema và đã lọc PII chưa thay thế được việc ai đó kiểm tra và phản hồi khi có tranh chấp.
- **Một điều còn chưa chắc:** Tôi chưa chắc một người duyệt (6 ca/giờ) chịu được tải đỉnh thật — stress 14 ca đã cho thấy chờ 130 phút — và cam kết dừng trong 5 phút có thực hiện được không khi kênh cảnh báo vẫn là mô phỏng, chưa có lịch trực dự phòng và chưa diễn tập.

### Xác nhận cá nhân và nộp bài

- [x] Tôi đã đọc, chỉnh nội dung theo đóng góp/thông hiểu thực tế và ghi đúng việc dùng AI.
- [x] Tôi đã tự nộp link repo trên LMS.

## Kết quả chung cuối cùng

- Thẻ S6; grade `R-S6-grade-20261119-161924-4fd606`: **PASS-VISIBLE**, kiểm thử ẩn chưa có trên máy.
- S6: 60/60; nền: 110/110; 21 test đạt; hoàn sai/lỗi hãng oan/PII đều bằng 0 trên dữ liệu đã đo.
- Monitor ambiguous_parcel_rate: nền 0, S6 0,166667; snapshot 2a8b53bf và tiêu chí 216e4226 còn nguyên.
- Phiếu A được diễn giải bổ sung sau baseline; không ghi nhận ngược thời gian là đã hoàn tất trước baseline. Commit ký tiêu chí vẫn có trước lần đánh giá đầu tiên.
- V1/v2 ghi Cải tiến thêm trong hồ sơ, hiện là đề xuất để nhóm đọc và xác nhận; không ghi thay biên bản họp hay chữ ký.
- Cần đối chiếu PRD/eval card Lab9 khi có nguồn, kiểm chứng vận hành thật trước pilot và thực hiện demo/phản biện theo lớp.
