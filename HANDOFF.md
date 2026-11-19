# Bàn giao phần Sản phẩm và kinh doanh

Người phụ trách: Phạm Lý Ngoc Đức — 2A202603991.

## Đã chuẩn bị để commit

- Phiếu A: câu 1.1, kết luận đề xuất câu 1.5 để nhóm rà soát, tiêu chí/hành động câu 1.6 và bằng chứng ký. Các ngưỡng đã ký giữ nguyên.
- Phiếu B: bản đồ dữ liệu và drift (B3), lăng kính kinh doanh trong pre-mortem (B6), cổng kinh doanh và lý do (B7.4), tổng hợp baseline chờ kết quả prepared để chốt B8.
- `config/operating_gates.json`: chỉ thay mục `business`; trần hoàn 1.500.000đ/ngày, ngân sách 8.000đ/ticket, ROI tối thiểu 0.25, phạm vi đánh giá all/100%.
- `TEAM.md`: phân công và đóng góp thực tế của Đức; exit ticket để Đức tự viết cuối buổi.

Các giá trị business đã được nhập; hiệu lực bảo vệ của guard chưa được kiểm chứng. Baseline có trước thay đổi này và không thay thế report after/prepared.

## Các bạn tự thực hiện tiếp

| Người | Phần phiếu cần tự điền | Code/config và bằng chứng cần làm |
|---|---|---|
| Tấn | Câu 1.3 phối hợp Đạt; B7.1–B7.2, phần kỹ thuật của B6; phân tích/sửa kỹ thuật Phiếu C khi có thẻ | Viết guard theo nguồn sự thật, không theo mã ticket; kiểm quyền lợi hoàn tiền, trách nhiệm hãng, dữ liệu gửi hãng và trần kinh doanh; cùng Đạt kiểm hồi quy |
| Đạt | B0–B2, B7.3; nhật ký/bằng chứng và chỉ số theo dõi Phiếu C | Dùng baseline hiện có, chạy after/test/ticket hiểm; chốt checkpoint khi nhóm thống nhất, chạy prepared; sau khi nhận thẻ chạy grade trước sửa và sau sửa; thêm monitor cùng Tấn |
| Triết | Câu 1.2/1.4; B4–B5, phần con người/pháp lý của B6, B7.5–B7.6; runbook/risk register Phiếu C | Tự điền operations/legal; nhận đúng thẻ được giao; điền submission.json và gom bài khi đủ thành phần |
| Đức và cả nhóm | B8/v1 sau prepared; C12/v2 sau thẻ | Quyết định khớp tiêu chí, có bằng chứng thực; chưa đủ dữ liệu thì chưa chốt, không sửa tiêu chí để đạt |

Phiếu C giữ nguyên phần trả lời để các thành viên tự làm vì nhóm chưa được giao thẻ. Không lấy thẻ khác hay dùng baseline thay bằng chứng sự cố.

## Các điều kiện bàn giao cho kỹ sư

- Trần hoàn 1.500.000đ/ngày phải được kiểm trước lệnh ghi theo tổng hoàn tự động, không chỉ nhìn báo cáo sau chạy.
- Giữ giới hạn Ops/Finance: 300.000đ/khách/ngày, ngân sách Finance 2.000.000đ/ngày và tiền LLM tối đa 1.500đ/ticket. Ngân sách 8.000đ của nhóm không cho phép vượt trần LLM 1.500đ.
- Ngưỡng chi phí trong tiêu chí đã ký là tổng chi phí mỗi ticket theo report, gồm máy/người/giữ chỗ; đọc thêm ROI và từng kho. Không suy ROI sau đổi cấu hình từ baseline.
- Chỉ điền cấu hình không bảo đảm guard đã thực thi. Tấn triển khai, Đạt kiểm thử, Triết xác nhận người/quy trình; cả nhóm kiểm tra trước checkpoint.
- Không chạy checkpoint khi guards/operations/legal chưa hoàn tất; đây là mốc chốt một lần.
- Không sửa `config/acceptance_criteria.json` hoặc `.lock`, không sửa snapshot vòng 1 sau khi tạo.

## Lưu phần bàn giao lên Git

Chạy từng dòng trong PowerShell, kiểm tra diff trước khi commit:

```powershell
git diff --stat
git diff -- config/operating_gates.json
git add TEAM.md HANDOFF.md config/operating_gates.json templates/form-a-criteria.md templates/form-b-evaluation-gates.md templates/form-c-incident.md
git commit -m "LAB 10: phan san pham va kinh doanh, ban giao nhom"
git push -u origin main
```

Các thành viên chạy `git pull` khi cây làm việc của họ sạch; nếu đang có thay đổi riêng thì lưu/commit trước và xử lý xung đột theo nội dung, không ghi đè phần của nhau. Không chạy lại lệnh ký tiêu chí. Sau khi nhóm có kết quả prepared/thẻ, Đức còn phải quay lại tổng hợp và cùng nhóm chốt v1/v2.
