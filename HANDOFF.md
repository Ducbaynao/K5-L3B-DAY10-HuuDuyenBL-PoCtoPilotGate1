# Cập nhật hiện tại: đã xử lý S6

Phần dưới dấu phân cách là bàn giao vòng1 trước nhận thẻ, được giữ làm lịch sử. Trạng thái mới thay thế các dòng "chưa có thẻ/chưa có monitor" ở bản cũ:

- S6 đã nhận; byte gốc thẻ khớp MANIFEST, .gitattributes giữ LF để tránh lỗi integrity Windows.
- Thêm guard: nhiều kiện trễ, thiếu parcel_id thì chuyển người trước ghi tiền/trách nhiệm. Thêm ambiguous_parcel_rate không dùng nhãn.
- Grade R-S6-grade-20261119-161924-4fd606: PASS-VISIBLE;S6 60/60,nền110/110;21tests qua;hidden chưa có. Snapshot2a8b53bf và tiêu chí216e4226 còn nguyên.
- Phiếu C và submission.json đã điền theo bằng chứng; v1/v2 ghi Cải tiến thêm theo đề xuất hồ sơ, nhóm cần rà soát/xác nhận. Chưa coi alert/diễn tập/exit ticket cá nhân đã hoàn tất.
- Kiểm tra/gom: python -m lab10.check_submission --collect; kết quả đủ thành phần không có nghĩa đạt testẩn hoặc được phép chạy production.
- Sau rà soát, chạy git diff --stat, git add . rồi git commit -m "LAB 10: xu ly S6, hoan thien ho so vong 2" và git push -u origin main. Codex chưa commit/push.

---

# Trạng thái kết thúc vòng 1, chờ thẻ sự cố

Đã chuẩn bị phần việc kỹ thuật và hồ sơ của bốn vai bằng Codex theo yêu cầu của Đức. Các thành viên cần tự đọc, hiểu và xác nhận; không coi nội dung được hỗ trợ là biên bản họp hay chữ ký của cá nhân.

## Đã thực hiện

- `guards.py`: policy theo ngày, dự toán chi phí trước model; kiểm quyền lợi, bên trả, ledger, phê duyệt, trần hoàn; xác minh trách nhiệm từng kiện/hãng và payload gửi đi.
- `operating_gates.json`: business/operations/legal đã điền. PIC NV-TUNG; approver NV-HANH; một người/6ca giờ, SLA60phút; decision_note=true, kiểm mẫu10%. Kênh alert đang mô phỏng, cần thiết lập/thử trước pilot thật.
- Phiếu A/B có nội dung và bằng chứng vòng1; B8 đề xuất **Cải tiến thêm**, chờ nhóm xác nhận. Cá nhân tự viết exit ticket.
- 18tests đạt: 13test công khai và 5test biên; hai ticket adhoc kiểm lời khai sai và PII trong đường gửi thật.
- Snapshot vòng1 `2a8b53bf` chốt lúc `2026-11-19T15:43:46` theo giờ máy. Không chạy checkpoint lần nữa, không sửa guards_round1.py, operating_gates.round1.json, round1.lock.

## Bằng chứng

| Mốc | Mã lần chạy | pass_rate / pass_k | Hoàn sai / lỗi hãng oan / PII | Chi phí / ROI |
|---|---|---|---|---|
| base | R-base-before-20261119-145954-bde05c | 0.9909 / 0.9545 | 20000đ / 1 / 0 | 4203đ / 1.34 |
| after cuối | R-base-after-20261119-154345-28ecf0 | 1 / 1 | 0 / 0 / 0 | 4456đ / 1.24 |
| prepared | R-base-prepared-20261119-154346-28ecf0 | 1 / 1 | 0 / 0 / 0 | 4456đ / 1.24 |

`evidence/round1/` chứa bản sao report/journal và output gate/test/adhoc/stress. `runs/` bị gitignore nên cần commit bản xuất để nhóm xem kết quả. Lần sửa gộp ghi đúng ở B0, không khẳng định đã đo riêng tác động từng gate.

Stress14ca cần duyệt đến cùng lúc với1người/6ca giờ: chờ130phút,7ca ùn. Đây là thử riêng, không phải số production hay prepared; cần điều phối/dự phòng và diễn tập. Nhóm kho `?` còn chi phí10359đ/ticket dù tổng thể nền đạt.

## Khi được giao thẻ

1. Nhóm rà soát/chốt B8/v1 trước khi đọc thẻ; giữ tiêu chí và snapshot.
2. Chỉ nhận đúng S1–S8 của Coach, ghi số đầu Phiếu C. Hiện chưa có thẻ.
3. Đạt chạy `python -m lab10.grade --incident Sx` trước sửa để có base/prepared.
4. Phân tích ít nhất2lỗi khác nguồn, điền C1–C6; Đức đọc kinh doanh/phạm vi cùng nhóm.
5. Sửa guards.py/operating_gates.json hiện tại, thêm monitor phù hợp trong monitors.py; chạy nền/thẻ/grade. Không sửa snapshot.
6. Điền C7–C12/v2, submission.json bằng số thật, tự viết exit ticket; chạy `python -m lab10.check_submission --collect` khi đủ thành phần.

Chưa có monitor đặc thù, quyết định v2, ba dòng kết luận cuối hoặc PRD/eval card Lab9 để đối chiếu. Không tính các phần này là hoàn tất.

## Lưu lên Git

Chạy từng dòng PowerShell:

```powershell
git diff --stat
git add .gitattributes TEAM.md HANDOFF.md config/operating_gates.json config/operating_gates.round1.json config/round1.lock lab10/guards.py lab10/guards_round1.py tests/test_round1_guards.py templates/form-a-criteria.md templates/form-b-evaluation-gates.md templates/form-c-incident.md submission/submission.json evidence/round1
git commit -m "LAB 10: hoan thien vong 1, chot prepared"
git push -u origin main
```

Không add lại/sửa tiêu chí đã ký. `.gitattributes` giữ file mẫu khóa ở LF đúng MANIFEST và nguyên byte snapshot. Mỗi thành viên pull sau khi lưu phần riêng, đọc lại phần mình để giải thích lúc demo. Codex chưa commit/push thay nhóm.
