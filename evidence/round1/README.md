# Bằng chứng vòng 1

Report và journal được sao chép từ runs/, không chỉnh số đo. Hai output adhoc chạy trên snapshot prepared; tests.txt là kết quả18test; gate-prepared.txt đối chiếu ngưỡng đã ký.

queue-stress.json dùng ops.attach_queue:14ticket cần người tới cùng phút0,1người/6ca giờ. Chờ tối đa130phút,7ca vượt SLA60phút. Không trộn số này vào bộ nền hoặc coi là tải thực.

Lần after154231 ghi report/journal thành công nhưng console lỗi Unicode;154241 chạy lại cùng cấu hình. Sau đó chỉ thêm dự toán trầnLLM, đo154345; checkpoint154346. B0 ghi rõ lần đầu sửa gộp nhiều cổng/config nên không tách đóng góp từng thay đổi.

Chưa kiểm thẻ, testẩn hay production. CI[1;1] trên mock không bảo đảm100% đúng ngoài thực tế. Kênh ops-gate1 và hạn dừng5phút chưa được diễn tập thật.
