# 01 — Individual Problem Scan

> Điền theo Phase 1 + Phase 2 trong `01-worksheet.md`. Tự scan trước, dùng AI sau để phản biện. Không copy ví dụ Weekly Report.

## Thông tin cá nhân

- Họ và tên: Đỗ Hoàng Quân
- Mã học viên: 2A202603016
- Vai trò / bối cảnh (VD: sinh viên năm X, intern PM, ...): Sinh viên mới tốt nghiệp KHMT.
- Công việc hằng tuần (3-5 gạch đầu dòng để soi problem):
  - Phát triển và kiểm thử các API, pipeline xử lý dữ liệu và tích hợp mô hình AI/LLM vào các hệ thống phần mềm.
  - Đọc, phân tích và trích xuất lỗi từ nhật ký hệ thống (system logs / telemetry) để hỗ trợ đội ngũ vận hành (Ops) xử lý sự cố.
  - Xây dựng các bản mẫu kỹ thuật (prototyping), benchmark độ trễ/chi phí và kiểm thử ranh giới an toàn (prompt guardrails) của mô hình.
  - Viết tài liệu kỹ thuật, tài liệu API và soạn thảo release notes từ các commit/PR trên GitHub.
  - Phối hợp với đội ngũ nghiệp vụ (Ops/BA) để làm rõ yêu cầu bài toán và chuyển hóa thành logic kỹ thuật/luồng xử lý (workflow).

---

## Phase 1 — Scan 5+ problems (tối thiểu 5, khuyến khích 8-10)

**Cách điền:** mỗi dòng = việc gì + ai chịu + đo bằng gì. Cột `Dấu hiệu thật` bắt buộc có số: mất bao lâu (bấm giờ mấy lần), mấy lần/tuần, bao nhiêu người gặp, log/ticket/quote nào.

| # | Lăng kính | Problem quan sát được | Ai chịu ảnh hưởng? | Dấu hiệu thật (số + bằng chứng) |
|---|---|---|---|---|
| 1 | **Tốn thời gian** | Điều phối viên xử lý thủ công sự cố xe điện cạn pin (<5%) và tra cứu trạm sạc/điều xe cứu hộ pin lưu động. | Điều phối viên Xanh SM, Tài xế | Trung bình 80-100 vụ/ngày; mất 15 phút/lượt xử lý thủ công; tài xế chờ lâu gây rò rỉ ~15% doanh thu giờ cao điểm. |
| 2 | **Lặp lại** | Phân loại và định tuyến tự động phản ánh sự cố hạ tầng (mất nước, hỏng đèn, ồn ào) trên App Resident về đúng BQL tòa nhà. | CSKH Vinhomes, Cư dân | ~200 ticket/ngày tại mỗi đại đô thị; mất 8 phút/ticket để đọc, phân loại thủ công; phản hồi chậm trễ sau 12-24h. |
| 3 | **AI có thể tốt hơn** | Chẩn đoán sơ bộ mã lỗi hỏng hóc xe điện VinFast từ mô tả bằng tiếng Việt tự nhiên của chủ xe qua Hotline/App. | Kỹ thuật viên tiếp nhận xưởng dịch vụ, Khách hàng | Mất 12-15 phút/lượt tiếp nhận; khách không biết thuật ngữ kỹ thuật nên tổng đài viên phải hỏi đi hỏi lại 3-4 lần. |
| 4 | **Pain từ người khác** | Bác sĩ mất quá nhiều thời gian viết tóm tắt hồ sơ xuất viện (Discharge Summary) từ kết quả xét nghiệm và bệnh án điện tử. | Bác sĩ điều trị Vinmec, Bệnh nhân | 20-25 phút/bệnh nhân; 15-20 ca xuất viện/ngày/khoa; bác sĩ phàn nàn quá tải công việc giấy tờ hành chính. |
| 5 | **AI có thể tốt hơn** | Quét và tổng hợp đánh giá của khách hàng từ nhiều kênh (Google Maps, Agoda, Booking) để cảnh báo khẩn cấp phàn nàn phòng ốc. | Quản lý vận hành khách sạn Vinpearl | ~300 review/tuần; mất 4 tiếng quét thủ công mỗi tuần; thường bỏ sót các phàn nàn nghiêm trọng về vệ sinh trong 24h đầu. |
| 6 | **Lặp lại** | So khớp và đối chiếu số liệu sạc điện hằng tuần giữa dữ liệu trụ sạc VinFast và hóa đơn đối tác bên thứ ba. | Kế toán vận hành VinFast | 1.000+ giao dịch sạc liên kết/tuần; mất 6 tiếng/tuần dò bảng tính Excel; tỉ lệ sai lệch số liệu ban đầu ~4%. |
| 7 | **Pain từ người khác** | Tài xế Xanh SM phàn nàn việc hệ thống gợi ý điểm đón tại các sảnh chung cư/TTTM không đúng cổng ra thực tế của khách. | Tài xế Xanh SM, Khách đặt xe | 15% cuốc xe tại TTTM lớn tài xế phải gọi 2-3 cuộc để tìm khách; tăng thời gian chờ trung bình thêm 4-6 phút/cuốc. |
| 8 | **Tốn thời gian** | Trợ lý cư dân ảo hỗ trợ tra cứu và điền biểu mẫu đăng ký thi công nội thất / đăng ký gửi xe định kỳ. | Cư dân Vinhomes, Ban quản lý | Mất 30 phút xếp hàng tại sảnh BQL; 40% hồ sơ giấy bị trả lại vì thiếu thông tin hoặc sai biểu mẫu. |
| 9 | **Tốn thời gian** | Tổng hợp lý do khách hàng hủy cuốc xe Xanh SM từ file ghi âm cuộc gọi và ghi chú của tài xế để tìm pattern lỗi. | Đội ngũ Phân tích nghiệp vụ (BA/Ops) | 500+ cuốc hủy/ngày; mất 10 giờ làm việc/tuần nghe mẫu ghi âm; báo cáo phân tích trễ 1 tuần so với thực tế. |
| 10 | **Lặp lại** | Trích xuất và soạn thảo thông báo Release Notes kỹ thuật từ 20-30 commit messages / PR merges mỗi đợt triển khai. | Kỹ sư phần mềm, Đội Ops/QA | 30 phút/bản release; diễn ra 2 lần/tuần; commit message thường viết tắt khiến QA khó nắm bắt tính năng cần test. |

**AI đã dùng ở Phase 1:**
- **Prompt đã hỏi:** *"Tôi là AI Engineer tại Vin Smart Future. Hãy gợi ý 5 vấn đề vận hành thủ công, tốn thời gian kèm số liệu đo lường cụ thể cho các mảng VinFast, Xanh SM, Vinhomes, Vinmec."*
- **Ý dùng được:** Gợi ý các bottleneck về sự cố pin Xanh SM, phân loại ticket Vinhomes và tóm tắt bệnh án Vinmec với các số liệu thời gian ước tính sát thực tế.
- **Ý bỏ vì không phải pain thật:** Bỏ ý tưởng *"AI tự động định giá lại giá vé VinWonders theo thời tiết"* vì đây là quyết định thương mại chiến lược của ban giám đốc, không phải bottleneck vận hành hằng ngày.

**Self-check Phase 1:**
- [x] Đủ 5+ dòng, mỗi dòng có actor + số đo cụ thể (Đạt 10/10 dòng).
- [x] Dùng ít nhất 3/4 lăng kính (Đã dùng đủ 4 lăng kính).
- [x] Không có dòng chung chung kiểu "mất nhiều thời gian".

> Gợi ý tự soi: tuần trước mất nhiều thời gian nhất vào việc gì? Việc gì hay trì hoãn? Người khác hay hỏi lại câu gì? Workflow nào ai cũng biết là chậm?

**AI đã dùng ở Phase 1 (nếu có):**
- Prompt đã hỏi:
- Ý dùng được:
- Ý bỏ vì không phải pain thật:

**Self-check Phase 1:**
- [ ] Đủ 5+ dòng, mỗi dòng có actor + số đo cụ thể
- [ ] Dùng ít nhất 3/4 lăng kính
- [ ] Không có dòng chung chung kiểu "mất nhiều thời gian"

---

## Phase 2 — Top 3 Problem Cards

### 2.1. Chọn top 3

Giữ bài nào: actor cụ thể, workflow vẽ được 3-7 bước, bottleneck ở 1 bước, impact đo được. Loại bài quá rộng.

| Rank | Problem (copy từ bảng scan) | Vì sao chọn (2-3 ý) | Điều còn chưa chắc |
|---|---|---|---|
| 1 | Xử lý sự cố pin nguy cấp (<5%) & điều phối xe sạc di động cho tài xế Xanh SM | 1. Ảnh hưởng trực tiếp đến an toàn và doanh thu xe.<br>2. Bottleneck rõ ràng (15' $\rightarrow$ <2.5').<br>3. Có thể kiểm soát ranh giới an toàn nghiêm ngặt bằng Prompt Prototype. | Cách thức tích hợp realtime giữa API vị trí xe và API tình trạng trụ sạc VinFast. |
| 2 | Phân loại & định tuyến tự động phản ánh sự cố cư dân trên App Vinhomes Resident | 1. Tần suất lặp lại cực cao (200 ticket/ngày).<br>2. Dữ liệu văn bản tiếng Việt rõ ràng, dễ đo lường.<br>3. Giảm tải tức thì 80% công việc đọc phân loại cho CSKH. | Xử lý các phản ánh chứa nhiều vấn đề hỗn hợp (multi-intent) trong 1 ticket. |
| 3 | Trợ lý chẩn đoán sơ bộ mã lỗi hỏng hóc xe điện VinFast từ mô tả ngôn ngữ tự nhiên | 1. Cải thiện trực tiếp trải nghiệm khách hàng tại xưởng dịch vụ.<br>2. AI phát huy thế mạnh hiểu tiếng Việt đời thường để ánh xạ mã OBD.<br>3. Giảm thời gian tiếp nhận từ 15' xuống 4'. | Độ bao phủ của bảng mã lỗi kỹ thuật đối với các dòng xe mới (VF3, VF7). |

### 2.2. Problem Cards chi tiết (lặp lại cho cả 3 cards)

---

#### Problem Card #1 — [Tên problem]

```text
Problem 1 câu:
Điều phối viên Xanh SM mất 15 phút xử lý thủ công mỗi khi tài xế báo sự cố cạn kiệt pin thực địa do phải tra cứu đa màn hình và soạn tin nhắn hướng dẫn/lệnh cứu hộ.

Actor:
Điều phối viên Trung tâm Điều vận Xanh SM (Dispatcher).

Thời điểm / bối cảnh:
Xảy ra liên tục hằng ngày trong giờ cao điểm khi tài xế chạy liên tục dẫn đến pin báo động nguy cấp (<5%).

Current workflow 3-7 bước:
1. Nhận cuộc gọi khẩn cấp từ tài xế báo sắp hết pin.
2. Mở dashboard định vị tra cứu tọa độ GPS và % pin xe hiện tại.
3. Mở bản đồ trạm sạc VinFast tra cứu trụ sạc trống còn hoạt động và tương thích cổng sạc.
4. Tự gõ tin nhắn SMS hướng dẫn đường đi hoặc soạn lệnh điều xe cứu hộ pin lưu động (nếu pin <5%).
5. Bấm gửi tin nhắn SMS cho tài xế hoặc kích hoạt điều xe cứu hộ.

Bottleneck:
Bước 3 & Bước 4 (mất ~10 phút) — Phải đối chiếu thủ công nhiều hệ thống và gõ nội dung văn bản thủ công.

Impact:
~80-100 vụ/ngày; tiêu tốn 20-25 giờ lao động/ngày của đội điều vận; xe nằm chờ lâu làm tăng tỉ lệ hủy cuốc và rò rỉ 15-18% doanh thu giờ cao điểm.

Success metric:
- Giảm thời gian xử lý sự cố từ 15 phút xuống dưới 2.5 phút/lượt (giảm >80%).
- 100% các ca pin <5% không bị hướng dẫn đến trạm sạc xa >5km mà kích hoạt cứu hộ sạc di động.
- 95% tin nhắn nháp được điều phối viên duyệt mà không cần sửa lại.

Non-AI alternative:
Xây dựng bảng tra cứu Excel / Hard-coded Rule kết hợp Google Maps API. Tuy nhiên, rule cứng không thể sinh tin nhắn hướng dẫn tiếng Việt ngữ cảnh linh hoạt và khó xử lý các tình huống phức tạp (tắc đường, tài xế hoảng loạn).

AI hypothesis:
Sử dụng LLM Feature kết hợp System Prompt nghiêm ngặt (Prompt Boundary) để đọc thông tin xe/trạm sạc, tự động draft tin nhắn SMS gắn tag [DRAFT_ONLY] hoặc xuất JSON kích hoạt cứu hộ để Dispatcher bấm duyệt 1-click.

Quick gut:
[ ] No AI / process fix
[ ] Rule
[x] Workflow (LLM Feature with Guardrails)
[ ] Agent
[ ] Chưa biết
```

**Draft workflow Card #1** (ASCII / Mermaid / ảnh đính kèm):

```text
[1 Nhận cuộc gọi: 2'] → [2 Tra GPS xe: 2'] → [3 Tra trụ sạc trống: 5'] 🔴 → [4 Gõ SMS/Cứu hộ: 5'] 🔴 → [5 Gửi: 1']

FUTURE STATE — 2.2 phút

[1 Tiếp nhận ticket: 0.2'] → [2 🔵 AI tra cứu & draft SMS/JSON cứu hộ: 0.5'] → [3 🟢 Dispatcher review [DRAFT_ONLY] & bấm gửi: 1.5']

Fallback: Nếu AI timeout (>5s) hoặc trả kết quả lỗi, hệ thống tự động fallback về quy trình tra cứu thủ công cũ của Dispatcher.
```

File đính kèm: `01-individual-problem-scan-workflow-card-1.png`

---

#### Problem Card #2 — [Tên problem]

```text
Problem 1 câu:
Nhân viên CSKH Vinhomes mất trung bình 8 phút để đọc, phân loại thủ công và chuyển tiếp từng phản ánh của cư dân từ App Resident về đúng BQL tòa nhà.

Actor:
Nhân viên Chăm sóc khách hàng (CSKH) Ban Quản lý Vinhomes.

Thời điểm / bối cảnh:
Diễn ra liên tục khi cư dân gửi phản ánh về sự cố căn hộ, điện nước, an ninh, tiện ích công cộng.

Current workflow 3-7 bước:
1. Tiếp nhận ticket phản ánh của cư dân trên hệ thống CRM.
2. Đọc nội dung mô tả, xem hình ảnh và xác định phân loại sự cố (kỹ thuật, an ninh, vệ sinh...).
3. Tra cứu danh bạ ban quản lý tòa nhà và phân bổ người phụ trách.
4. Gõ nội dung xác nhận và chuyển tiếp ticket đến kỹ thuật viên tòa nhà.

Bottleneck:
Bước 2 & Bước 3 (mất 6 phút) — Đọc hiểu nội dung mô tả dài, không có cấu trúc và chọn thủ công đúng bộ phận xử lý.

Impact:
~200 ticket/ngày/khu đô thị; mất ~26 giờ làm việc/ngày; thời gian phản hồi cư dân bị chậm trễ từ 12-24 giờ gây bức xúc.

Success metric:
- Giảm thời gian phân loại ticket từ 8 phút xuống dưới 20 giây.
- Độ chính xác phân loại danh mục và định tuyến đúng tòa nhà đạt trên 92%.

Non-AI alternative:
Bắt cư dân tự chọn menu thả xuống (Dropdown menu 4 cấp) khi gửi phản ánh. Nhược điểm: Trải nghiệm cư dân kém, cư dân hay chọn bừa "Khác" dẫn đến vẫn phải phân loại tay.

AI hypothesis:
Sử dụng LLM trích xuất thực thể (tòa nhà, số phòng, loại sự cố, mức độ khẩn cấp) và phân loại văn bản tự động sang định dạng JSON để định tuyến tự động qua API.

Quick gut:
[ ] No AI / process fix
[ ] Rule
[x] Workflow (LLM Feature)
[ ] Agent
[ ] Chưa biết
```

**Draft workflow Card #2:**

```text
CURRENT STATE — 8 phút

[1 Nhận ticket: 1'] → [2 Đọc & phân loại danh mục: 4'] 🔴 → [3 Chọn BQL & chuyển tiếp: 2'] 🔴 → [4 Gửi xác nhận: 1']

FUTURE STATE — 25 giây

[1 Nhận ticket: 2s] → [2 🔵 AI trích xuất JSON & gắn tag phân loại: 3s] → [3 🟢 Hệ thống tự route / CSKH kiểm tra nhanh: 20s]

Fallback: Nếu confidence score của AI < 0.85, ticket được gắn cờ đẩy về hàng đợi xử lý thủ công của CSKH.
```

File đính kèm: `01-individual-problem-scan-workflow-card-2.png`

---

#### Problem Card #3 — [Tên problem]

```text
Problem 1 câu:
Kỹ thuật viên tiếp nhận xưởng dịch vụ mất 15 phút hỏi đáp và tra cứu sổ tay để xác định cụm chi tiết lỗi khi khách hàng chỉ mô tả hiện tượng bằng ngôn ngữ đời thường.

Actor:
Cố vấn dịch vụ / Kỹ thuật viên tiếp nhận xưởng dịch vụ VinFast.

Thời điểm / bối cảnh:
Khách hàng gọi điện hoặc mang xe đến xưởng và mô tả triệu chứng bất thường (ví dụ: "xe đi qua gờ giảm tốc kêu lộc cộc phía trước").

Current workflow 3-7 bước:
1. Lắng nghe khách hàng mô tả triệu chứng bất thường bằng lời nói.
2. Đặt câu hỏi gặng hỏi thêm về điều kiện xảy ra (tốc độ bao nhiêu, khi phanh hay khi đánh lái).
3. Tra cứu tài liệu kỹ thuật/sổ tay OBD của dòng xe (VF5, VF8, VF9).
4. Nhập mã chẩn đoán sơ bộ và danh sách phụ tùng cần kiểm tra vào phiếu tiếp nhận.

Bottleneck:
Bước 2 & Bước 3 (mất 10-12 phút) — Khách hàng không rõ thuật ngữ kỹ thuật, kỹ thuật viên phải tra cứu tài liệu hướng dẫn dày hàng trăm trang.

Impact:
40-50 lượt tiếp nhận/ngày/xưởng; mất 10-12 giờ công; thời gian chờ đợi tiếp nhận lâu khiến khách hàng không hài lòng.

Success metric:
- Giảm thời gian tiếp nhận chẩn đoán từ 15 phút xuống dưới 4 phút.
- Gợi ý chính xác cụm chi tiết lỗi và mã OBD tiềm năng đạt >85%.

Non-AI alternative:
Tạo bảng câu hỏi trắc nghiệm triệu chứng cố định dạng form. Nhược điểm: Không linh hoạt, không bắt được sắc thái mô tả âm thanh, cảm giác lái phong phú bằng tiếng Việt của khách.

AI hypothesis:
LLM đóng vai trò Chuyên gia kỹ thuật tiếp nhận, nhận chuỗi mô tả tiếng Việt đời thường $\rightarrow$ phân tích triệu chứng $\rightarrow$ đề xuất top 3 mã lỗi OBD và danh sách linh kiện nghi vấn kèm câu hỏi cần hỏi thêm.

Quick gut:
[ ] No AI / process fix
[ ] Rule
[x] Workflow (LLM Feature)
[ ] Agent
[ ] Chưa biết
```

**Draft workflow Card #3:**

```text
CURRENT STATE — 15 phút

[1 Nghe khách tả: 3'] → [2 Hỏi gặng triệu chứng: 4'] 🔴 → [3 Tra sổ tay OBD: 6'] 🔴 → [4 Tạo phiếu tiếp nhận: 2']

FUTURE STATE — 3.5 phút

[1 Nhập mô tả khách: 1'] → [2 🔵 AI phân tích triệu chứng & gợi ý mã lỗi: 30s] → [3 🟢 Kỹ thuật viên xác nhận & tạo phiếu: 2']

Fallback: Nếu AI không đủ dữ liệu chẩn đoán, hiển thị form câu hỏi chuyên sâu theo checklist tiêu chuẩn để kỹ thuật viên hỏi trực tiếp khách.
```

File đính kèm: `01-individual-problem-scan-workflow-card-3.png`

---

### 2.3. Card muốn pitch nhất (chuẩn bị 2 phút)

**Card tôi muốn pitch nhất:**

```text
Problem Card #1: Trợ lý AI Điều phối Cứu hộ Pin & Chỉ dẫn Trạm sạc Thông minh cho Xanh SM.
```

**Vì sao (2-3 câu: workflow gì, số đo gì, impact gì):**

```text
Bài toán này giải quyết nút thắt cổ chai trực tiếp tại Trung tâm Điều vận Xanh SM, nơi dispatchers mất 15 phút xử lý thủ công cho mỗi ca xe hết pin giữa đường. Bằng cách áp dụng LLM Feature có cài đặt ranh giới an toàn ([DRAFT_ONLY], tự động gọi cứu hộ khi pin <5%), chúng ta cắt giảm thời gian xử lý xuống dưới 2.5 phút (>80% thời gian), cứu được ~20 giờ công/ngày và ngăn chặn hoàn toàn nguy cơ xe chết máy trên đường làm tổn hại doanh thu và hình ảnh thương hiệu.
```

**Câu hỏi tôi muốn nhóm challenge (1-2 câu hỏi đúng chỗ yếu):**

```text
1. "Nếu tín hiệu GPS xe gửi về bị trôi hoặc tài xế khai báo sai % pin, rủi ro AI draft sai lệnh điều xe cứu hộ có gây lãng phí chi phí vận hành không và ai sẽ chịu trách nhiệm?"
2. "Tại sao không dùng thuật toán định tuyến cổ điển (như Dijkstra/Google Maps API) tìm trạm gần nhất mà lại cần đến LLM?"
```

**AI phản biện Card (nếu có):**
- Điểm yếu AI chỉ ra: AI đã phản biện sắc bén rằng việc tìm trạm sạc gần nhất hoàn toàn có thể giải quyết bằng Rule/Maps API đơn giản, không nên lạm dụng LLM để tính toán khoảng cách. Ngoài ra, việc tự động điều xe cứu hộ (Mobile Charger) phát sinh chi phí thực tế rất lớn, nếu AI tự ý quyết định sẽ gây rủi ro thất thoát tài chính.
- Tôi sửa gì: Tôi đã điều chỉnh lại kiến trúc bài toán: Thuật toán Rule/API làm nhiệm vụ lọc tọa độ và khoảng cách số học, còn LLM chỉ đóng vai trò phân tích ngữ cảnh, draft tin nhắn hướng dẫn tiếng Việt và format lệnh cứu hộ dạng nháp [DRAFT_ONLY]. Con người (Dispatcher) bắt buộc phải là người click nút cuối cùng (Human-in-the-loop) để kích hoạt lệnh.

### Self-check nộp phần 01
- [x] Có 5+ problems + top 3 Cards đủ field
- [x] Mỗi Card có workflow trước/sau + bottleneck + metric + fallback
- [x] Đã chọn 1 card pitch + câu hỏi challenge
