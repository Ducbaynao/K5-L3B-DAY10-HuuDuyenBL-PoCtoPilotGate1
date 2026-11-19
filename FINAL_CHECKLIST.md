# Kiểm tra bài nộp LAB 10 — S6

Nguồn yêu cầu: [SUBMISSION.md](SUBMISSION.md), [submission/README.md](submission/README.md), [RUBRIC.md](RUBRIC.md), [RULES.md](RULES.md). Đây là bảng kiểm bổ sung, không thay đổi yêu cầu của lớp.

## Bài cần nộp

**Nộp link repo Public của nhóm trên GitHub, chứa toàn bộ `submission/` và `TEAM.md`.** Không cần tạo file ZIP riêng theo hướng dẫn hiện có. Mỗi thành viên phải tự nộp cùng link repo bằng tài khoản LMS cá nhân.

Link của nhóm: https://github.com/Ducbaynao/K5-L3B-DAY10-HuuDuyenBL-PoCtoPilotGate1

| Thành phần | Đường dẫn | Kết quả kiểm tra local |
|---|---|---|
| Thông tin bài, bốn thành viên, S6, v1/v2, ba dòng bắt buộc | submission/submission.json | Đủ trường; khớp tên nhóm, mục cá nhân và Phiếu C |
| Code vòng1 đã chốt | submission/code/guards_round1.py | Khớp snapshot2a8b53bf |
| Code vòng2 và monitor | submission/code/guards.py; monitors.py | Khớp source cuối và code_hash của grade |
| Config vòng1/vòng2 | submission/config/operating_gates.round1.json; operating_gates.json | Đủ và khớp bản gom |
| Tiêu chí đã ký | submission/config/acceptance_criteria.json; acceptance_criteria.lock | Hash216e4226 còn nguyên |
| Dấu chốt và công tắc | submission/config/round1.lock; switches.json | Đủ, snapshot không đổi |
| Báo cáo tự kiểm tra | submission/runs/grade-report.json; grade-report.md | PASS-VISIBLE; hidden chưa có |
| Report ba mốc | submission/runs/R-S6-before-20261119-161925-4fd606/report.json; R-S6-prepared-20261119-161925-4fd606/report.json; R-S6-after-20261119-161925-4fd606/report.json | Đủ base/prepared/after |
| Nhật ký mọi lần chạy | submission/runs/journal.jsonl | Có lịch sử ký trước đo; không xoá lần chạy thất bại |
| Ba phiếu | submission/docs/form-a-criteria.md; form-b-evaluation-gates.md; form-c-incident.md | Khớp templates; mọi mục áp dụng đã điền; C3.2 dành S6 |
| Manifest | submission/manifest.json | 19hash file khớp; 20đường dẫn bắt buộc có mặt tính cả manifest |
| Thành viên và mục cá nhân | TEAM.md ở gốc repo | Đủ4mục; đã chuẩn bị đóng góp/exit ticket nháp, cần từng người xác nhận |

Giữ cả source `lab10/`, `config/`, `templates/`, thẻ `incidents/S6/`, `.gitattributes` và test bổ sung trên repo để truy nguyên/chạy lại. Thư mục `evidence/` là bằng chứng bổ sung. `runs/` ở gốc bị gitignore; các report cần nộp đã nằm trong `submission/runs/`.

## Kiểm tra đã đạt

- Repo đã kiểm qua GitHub connector: Public, đúng tên; origin local trỏ đúng repo.
- Grade `R-S6-grade-20261119-161924-4fd606`: integrity, criteria, visible, regression, monitor đạt; chưa có kiểm thử ẩn.
- S6:60/60; bộ nền:110/110;21tests đạt. Hoàn sai/lỗi hãng oan/PII đều0 trên dữ liệu đã đo.
- S6 chi phí5228đ/ticket,ROI0.91,queue_stuck0,coverage1; monitor mơ hồ0.166667 so nền0.
- Tiêu chí ký14:56:59, commit ký14:59:04, lần eval đầu14:59:54 ngày19/11/2026 theo hồ sơ. Không ghi lại thứ tự khác.
- Bản v1 đã commit trước nhận thẻ; không sửa Phiếu B để viết lại lịch sử. Phiếu A vẫn ghi rõ phần diễn giải được bổ sung sau baseline.
- Chi tiết kiểm tra máy: evidence/S6/final-audit.json và final-submission-check.txt.

## Các việc nhóm còn phải tự xác nhận

- [ ] Mỗi người đọc mục cá nhân trong TEAM.md, sửa bản nháp theo đóng góp và hiểu biết thực tế; ghi đúng phần dùng AI.
- [ ] Nhóm xác nhận v1/v2 “Cải tiến thêm”, lý do và người phụ trách; hồ sơ hiện ghi là đề xuất, chưa có bằng chứng họp/chữ ký.
- [ ] Thực hiện demo/phản biện nếu lớp chưa làm; nếu demo đổi code/config thì chạy lại grade, cập nhật phiếu và gom lại.
- [ ] Commit/push bản cuối và kiểm tra trên GitHub có đủ thư mục submission/runs/ cùng TEAM.md.
- [ ] Cả4thành viên tự nộp link repo trên LMS; không đánh dấu đã nộp khi chưa thực hiện.

PRD/eval card Lab9, dữ liệu/hạ tầng production và lịch trực/kênh cảnh báo thật chưa có trong repo để kiểm chứng. Những hạn chế này đã được nêu trong phiếu/risk register và lý do đề xuất Cải tiến thêm; không tự tạo kết quả hoặc xác nhận giả.

## Kịch bản demo5phút đã chuẩn bị

1. **Đức — 45giây:** bài toán hoàn tiền/trách nhiệm hãng, tiêu chí ký trước đo; chất lượng cao vẫn cần ba ngưỡng an toàn bằng0.
2. **Đạt — 60giây:** chiếu grade-report.md. S6 base:pass0.3333,270000đ hoàn sai,40lỗi oan; prepared:pass0.8333,270000đ,10lỗi oan; after:pass1,0đ,0lỗi oan. Nêu rõ số tiền/lỗi cộng qua5seed, không phải thiệt hại thật.
3. **Tấn — 90giây:** S6-01 base dùng hãng kiện đầu; prepared sửa đúng kiện. S6-20 prepared vẫn đoán khi nhiều kiện trễ/thiếuparcel_id; after chuyển người trước ghi. Monitor không dùng nhãn, khác với số lỗi có nhãn trong đánh giá.
4. **Triết — 45giây:** PIC/approver, SLA60phút, kiểm mẫu10%, ngưỡng gọi dự phòng; chưa diễn tập tải/cảnh báo thật. Gate chỉ bảo đảm nhánh đã kiểm trong điều kiện dữ liệu đúng.
5. **Đức — 60giây:** đề xuất giữ Cải tiến thêm dù visible đạt; cần kiểm chứng dữ liệu/điều phối thật, testẩn do team chấm. Nhóm trả lời “giảm hay ngăn” theo C12 và ba dòng bắt buộc.

Lệnh demo chỉ đọc/chạy trace, không sửa snapshot:

```powershell
python -m lab10.trace --suite S6 --stage prepared --ticket S6-20 --seed 11
python -m lab10.trace --suite S6 --stage after --ticket S6-20 --seed 11
python -m lab10.trace --suite S6 --stage after --ticket S6-01 --seed 11
```

## Gom và đẩy bản cuối

Sau khi chỉnh phiếu hoặc submission.json, chạy từ thư mục gốc:

```powershell
python -m lab10.check_submission --collect
git diff --stat
git add .
git commit -m "LAB 10: bai nop cuoi S6"
git push -u origin main
```

Nếu sửa code/config sau grade cuối, phải chạy `python -m lab10.grade --incident S6` trước lệnh gom và cập nhật số trong phiếu. Không ký lại tiêu chí, không chạy lại checkpoint. Sau push, mở GitHub kiểm bản cuối; không push lên repo đề.

Hạn nộp theo SUBMISSION.md: lab sáng trước23h59 cùng ngày; lab chiều/tối trước11h59 hôm sau (GMT+7), trừ khi Coach gia hạn. Chưa có dữ kiện xác nhận ca học cụ thể nên không tự đánh dấu thời hạn của nhóm.
