# Bằng chứng vòng 1

Report và journal được sao chép từ runs/, không chỉnh số đo. Hai output adhoc chạy trên snapshot prepared; tests.txt là kết quả18 test; gate-prepared.txt đối chiếu ngưỡng đã ký.

queue-stress.json dùng ops.attach_queue:14ticket cần người tới cùng phút0,1 người/6 ca giờ. Chờ tối đa130 phút,7 ca vượt SLA 60 phút. Không trộn số này vào bộ nền hoặc coi là tải thực.

Lần after 154231 ghi report/journal thành công nhưng console lỗi Unicode; 154241 chạy lại cùng cấu hình. Sau đó chỉ thêm dự toán trần LLM, đo 154345; checkpoint 154346. B0 ghi rõ lần đầu sửa gộp nhiều cổng/config nên không tách đóng góp từng thay đổi.

Chưa kiểm thẻ, test ẩn hay production. CI[1;1] trên mock không bảo đảm100% đúng ngoài thực tế. Kênh ops-gate1 và hạn dừng5 phút chưa được diễn tập thật.
