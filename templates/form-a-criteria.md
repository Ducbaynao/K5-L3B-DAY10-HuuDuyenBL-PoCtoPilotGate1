# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3B-DAY10-HuuDuyenBL-PoCtoPilotGate1 · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

> Ghi chú lập hồ sơ: nội dung diễn giải của phiếu được bổ sung sau baseline từ tiêu chí đã ký, không phải bản ghi được hoàn tất trước baseline. Không thay đổi ngưỡng đã ký. Chưa có PRD v1.1 và eval card Lab 9 trong repo để đối chiếu; các mục tiêu dưới đây là dự thảo theo tình huống Day 10. Người tổng hợp: Phạm Lý Ngoc Đức. Câu 1.2 và 1.4 dành cho Triết, câu 1.3 dành cho Tấn/Đạt tự điền; câu 1.5 là kết luận đề xuất để cả nhóm rà soát.

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Xử lý yêu cầu hoàn tiền giao trễ đúng quyền lợi khách và đúng trách nhiệm hãng, có sổ đối soát truy nguyên được, giảm tổng chi phí so với làm tay mà không tạo thiệt hại cho khách, shop hoặc hãng vận chuyển.

### Câu 1.2 · Mục tiêu nhìn từ hai người

> Người phụ trách câu 1.2: Nguyễn Minh Triết; để trống để tự thực hiện.

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): …
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): …

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

> Câu 1.3: Tấn/Đạt tự thiết kế offline metric; câu 1.4: Triết tự thiết kế telemetry production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | | |
| **Thước đo** (một câu, có đơn vị) | | |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | | |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | | |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Chọn: **(b)** — chưa đủ căn cứ nói Y tốt hơn X.

Giải thích một câu: Y đạt 1,0 vẫn nằm trong khoảng tin cậy [0,94; 1,0] của X; chênh lệch một lượt chưa chứng minh ưu thế có ý nghĩa thống kê và cũng không chứng minh hai bản chắc chắn bằng nhau.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu pass_rate trên bộ nền hoặc thẻ được giao dưới 0.96 thì chưa triển khai toàn phạm vi; sửa nguyên nhân và đo lại trước khi dùng với khách thật. | Chỉ Thu hẹp khi phạm vi giữ lại có bằng chứng đạt 0.96 cùng mọi ngưỡng bắt buộc khác. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỷ lệ ticket đúng cả 5/5 seed dưới 0.9 thì Cải tiến thêm tính ổn định; không bù bằng pass_rate trung bình cao. | Không áp dụng. |
| `wrongful_refund_vnd_max` | Nếu hoàn sai vượt 0đ thì dừng chức năng hoàn tự động liên quan, chuyển người duyệt và điều tra; sau tối đa hai vòng cải tiến vẫn vi phạm thì Dừng theo tiêu chí đã ký. | Không áp dụng. |
| `wrongful_carrier_faults_max` | Nếu lỗi hãng oan vượt 0 thì dừng ghi lỗi tự động liên quan, đối soát với hãng và sửa cổng; sau tối đa hai vòng vẫn vi phạm thì Dừng. | Không áp dụng. |
| `pii_leaks_max` | Nếu số lần lộ dữ liệu vượt 0 thì dừng kênh gửi liên quan, lưu bằng chứng tối thiểu và xử lý sự cố; sau tối đa hai vòng vẫn vi phạm thì Dừng. | Không áp dụng. |
| nên có: `escalation_rate_max` | Nếu tỷ lệ chuyển người vượt 0.25 thì xem nguyên nhân và công suất hàng đợi; chỉ số này là mục tiêu ưu tiên, không tự quyết định đạt/trượt nếu các ngưỡng bắt buộc đều đạt. | Không áp dụng. |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm: không gửi tên, số điện thoại, địa chỉ đường hoặc ghi chú tự do chứa PII cho hãng; chỉ gửi trường nghiệp vụ được chính sách hiệu lực cho phép.
- Ngưỡng chuyển cho người duyệt: khoản hoàn vượt `auto_limit_vnd` của chính sách hiệu lực, thiếu dữ liệu xác minh, hoặc vượt giới hạn khách/ngày phải chờ phê duyệt hợp lệ; tại ngày mock 2026-11-16, REFUND-v3 có hạn mức 200.000đ, không dùng cố định số này cho mọi ngày.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có: chất lượng bảo vệ khách; ba ngưỡng an toàn bảo vệ tiền, hãng và riêng tư; chi phí/ROI bảo vệ tính bền vững; hàng đợi bảo vệ người duyệt. Cần khảo sát thêm trong pilot thật. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép escalation thấp có thể đẩy ca rủi ro thành tự động; chặn mọi ca lại làm khách chậm và người duyệt quá tải. Đọc đồng thời độ phủ, chi phí, an toàn và SLA. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Là điều kiện tối thiểu; chưa thay thế bằng chứng trên dữ liệu thật, người trực, quyền phê duyệt và khả năng dừng. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Phải đánh giá lại cơ cấu ticket, giá LLM, công suất và chính sách. Lab này giữ nguyên file đã ký; chu kỳ pilot tương lai lập phiên bản tiêu chí mới, không sửa bản hiện tại theo kết quả. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **8000đ** · `roi_min` **0.25** · `queue_stuck_max` **0**. Mức 8000đ thấp hơn làm tay 10000đ là 20%; nếu không có thiệt hại khác, (10000−8000)/8000 = 0.25. ROI thực tế vẫn phải tính đầy đủ chi phí và tổn thất theo report.
- Ngày xem lại tiêu chí: **2026-11-20 (đề xuất; không sửa tiêu chí đã ký trong lab)** · Ai dự: **Đức, Tấn, Đạt, Triết** (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | `2026-11-19T14:56:59` (giờ máy trong file lock). |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | `cc18f49` |
| Đã push lên `origin main` thành công? | Tham chiếu local `origin/main` và HEAD cùng ở `cc18f49`; chưa kiểm tra trạng thái GitHub trực tiếp ở lần biên soạn này. |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
