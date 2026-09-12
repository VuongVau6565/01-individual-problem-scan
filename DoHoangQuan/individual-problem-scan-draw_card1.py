import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_card1_workflow():
    # Khởi tạo canvas kích thước lớn, độ phân giải cao
    fig, ax = plt.subplots(figsize=(16, 9.5), dpi=300)
    ax.set_facecolor("#F8FAFC")
    fig.patch.set_facecolor("#F8FAFC")

    # ==========================================
    # TIÊU ĐỀ CHÍNH
    # ==========================================
    plt.text(0.5, 0.96, "PROBLEM CARD #1: ĐIỀU PHỐI CỨU HỘ PIN & TRẠM SẠC (XANH SM)", 
             ha="center", va="center", fontsize=15, fontweight="bold", color="#0F172A")
    plt.text(0.5, 0.925, "So sánh Quy trình Hiện tại (Current State) vs Quy trình Tương lai với AI (Future State)", 
             ha="center", va="center", fontsize=11, color="#475569", style="italic")

    # ==========================================
    # PHẦN 1: CURRENT STATE (THỦ CÔNG — 15 PHÚT)
    # ==========================================
    # Khung bao bọc Current State
    current_bg = patches.FancyBboxPatch(
        (0.02, 0.50), 0.96, 0.39,
        boxstyle="round,pad=0.015,rounding_size=0.015",
        edgecolor="#CBD5E1", facecolor="#FFFFFF", linewidth=1.2
    )
    ax.add_patch(current_bg)
    ax.text(0.04, 0.86, "🔴 CURRENT STATE — Quy trình thủ công hoàn toàn (⏱ Tổng: 15 phút/lượt)", 
            fontsize=12, fontweight="bold", color="#DC2626")

    current_steps = [
        {"num": "Bước 1", "title": "Nhận cuộc gọi\nbáo hết pin", "time": "⏱ 2 phút", "actor": "Dispatcher", "is_bn": False, "sub": "In: SĐT / Biển số\nOut: Tạo ticket"},
        {"num": "Bước 2", "title": "Tra cứu GPS xe\n& % pin hiện tại", "time": "⏱ 2 phút", "actor": "Dispatcher", "is_bn": False, "sub": "In: Biển số xe\nOut: Tọa độ, % Pin"},
        {"num": "Bước 3", "title": "Tra trụ sạc trống\n& cổng tương thích", "time": "⏱ 5 phút", "actor": "Dispatcher", "is_bn": True, "bn_label": "🔴 BOTTLENECK 1", "sub": "Mở đa màn hình\nLọc cổng sạc VF5/VF8"},
        {"num": "Bước 4", "title": "Soạn tin nhắn SMS\nhoặc Lệnh cứu hộ", "time": "⏱ 5 phút", "actor": "Dispatcher", "is_bn": True, "bn_label": "🔴 BOTTLENECK 2", "sub": "Gõ tay tin nhắn\nTính toán khoảng cách"},
        {"num": "Bước 5", "title": "Duyệt & Gửi tin\nhoặc điều xe", "time": "⏱ 1 phút", "actor": "Dispatcher", "is_bn": False, "sub": "In: SMS / Lệnh\nOut: Gửi tài xế"}
    ]

    c_box_w, c_box_h, c_y = 0.165, 0.24, 0.54
    c_x_coords = [0.04 + i * 0.192 for i in range(5)]

    for i, s in enumerate(current_steps):
        x = c_x_coords[i]
        edge_col = "#EF4444" if s["is_bn"] else "#3B82F6"
        fill_col = "#FEF2F2" if s["is_bn"] else "#EFF6FF"
        
        # Step Box
        rect = patches.FancyBboxPatch((x, c_y), c_box_w, c_box_h,
                                     boxstyle="round,pad=0.01,rounding_size=0.015",
                                     edgecolor=edge_col, facecolor=fill_col, linewidth=1.5)
        ax.add_patch(rect)

        # Header tag
        tag_bg = "#EF4444" if s["is_bn"] else "#3B82F6"
        t_rect = patches.FancyBboxPatch((x + 0.01, c_y + c_box_h - 0.035), c_box_w - 0.02, 0.028,
                                       boxstyle="round,pad=0.003,rounding_size=0.008",
                                       edgecolor="none", facecolor=tag_bg)
        ax.add_patch(t_rect)
        ax.text(x + c_box_w/2, c_y + c_box_h - 0.021, s["num"], ha="center", va="center", fontsize=8.5, fontweight="bold", color="white")

        # Step Title
        ax.text(x + c_box_w/2, c_y + c_box_h - 0.08, s["title"], ha="center", va="center", fontsize=9, fontweight="bold", color="#1E293B")
        
        # Time & Actor
        ax.text(x + c_box_w/2, c_y + c_box_h - 0.14, f"{s['time']} | {s['actor']}", ha="center", va="center", fontsize=8, color="#475569", fontweight="semibold")
        
        # Sub detail
        ax.text(x + c_box_w/2, c_y + c_box_h - 0.19, s["sub"], ha="center", va="center", fontsize=7.5, color="#64748B", style="italic")

        # Bottleneck badge
        if s.get("is_bn"):
            bn_rect = patches.FancyBboxPatch((x + 0.01, c_y + 0.01), c_box_w - 0.02, 0.025,
                                             boxstyle="round,pad=0.003,rounding_size=0.006",
                                             edgecolor="none", facecolor="#DC2626")
            ax.add_patch(bn_rect)
            ax.text(x + c_box_w/2, c_y + 0.022, s["bn_label"], ha="center", va="center", fontsize=7.5, fontweight="bold", color="white")

        # Arrow
        if i < 4:
            ax.annotate("", xy=(c_x_coords[i+1] - 0.005, c_y + c_box_h/2), 
                        xytext=(x + c_box_w + 0.005, c_y + c_box_h/2),
                        arrowprops=dict(arrowstyle="-|>", color="#94A3B8", lw=1.8, mutation_scale=12))

    # ==========================================
    # PHẦN 2: FUTURE STATE (CÓ AI & HITL — 2.2 PHÚT)
    # ==========================================
    future_bg = patches.FancyBboxPatch(
        (0.02, 0.08), 0.96, 0.38,
        boxstyle="round,pad=0.015,rounding_size=0.015",
        edgecolor="#CBD5E1", facecolor="#FFFFFF", linewidth=1.2
    )
    ax.add_patch(future_bg)
    ax.text(0.04, 0.43, "🟢 FUTURE STATE — Tối ưu hóa bằng AI Feature + Human-in-the-loop (⏱ Tổng: 2.2 phút/lượt)", 
            fontsize=12, fontweight="bold", color="#15803D")

    # Step 1 Future: Nhận ticket
    f1_rect = patches.FancyBboxPatch((0.05, 0.17), 0.22, 0.21, boxstyle="round,pad=0.01,rounding_size=0.015",
                                    edgecolor="#64748B", facecolor="#F1F5F9", linewidth=1.5)
    ax.add_patch(f1_rect)
    ax.text(0.16, 0.35, "Bước 1: Tiếp nhận tự động", ha="center", va="center", fontsize=9.5, fontweight="bold", color="#0F172A")
    ax.text(0.16, 0.30, "⏱ 10 giây (0.2')\nHệ thống bắt tín hiệu GPS &\ntelemetry pin xe tức thì", ha="center", va="center", fontsize=8.5, color="#475569")
    ax.text(0.16, 0.21, "Actor: Hệ thống Xanh SM", ha="center", va="center", fontsize=8, color="#059669", fontweight="bold")

    # Arrow 1 -> 2
    ax.annotate("", xy=(0.33, 0.275), xytext=(0.275, 0.275),
                arrowprops=dict(arrowstyle="-|>", color="#10B981", lw=2, mutation_scale=15))

    # Step 2 Future: AI Step (LLM Feature)
    f2_rect = patches.FancyBboxPatch((0.34, 0.17), 0.27, 0.21, boxstyle="round,pad=0.01,rounding_size=0.015",
                                    edgecolor="#2563EB", facecolor="#EFF6FF", linewidth=2.0)
    ax.add_patch(f2_rect)
    ax.text(0.475, 0.35, "Bước 2: 🔵 AI LLM Engine (Gemini 2.5)", ha="center", va="center", fontsize=9.5, fontweight="bold", color="#1D4ED8")
    ax.text(0.475, 0.28, "⏱ 30 giây (0.5')\n- Đọc pin, vị trí & gọi API trạm trống\n- Pin < 5%: Draft JSON điều xe cứu hộ\n- Pin >= 5%: Draft SMS [DRAFT_ONLY]", ha="center", va="center", fontsize=8, color="#1E293B")
    ax.text(0.475, 0.195, "🛡️ Enforce Prompt Boundary Rules", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#2563EB")

    # Arrow 2 -> 3
    ax.annotate("", xy=(0.675, 0.275), xytext=(0.615, 0.275),
                arrowprops=dict(arrowstyle="-|>", color="#10B981", lw=2, mutation_scale=15))

    # Step 3 Future: Human in the loop
    f3_rect = patches.FancyBboxPatch((0.685, 0.17), 0.27, 0.21, boxstyle="round,pad=0.01,rounding_size=0.015",
                                    edgecolor="#16A34A", facecolor="#F0FDF4", linewidth=2.0)
    ax.add_patch(f3_rect)
    ax.text(0.82, 0.35, "Bước 3: 🟢 Dispatcher Phê duyệt (HITL)", ha="center", va="center", fontsize=9.5, fontweight="bold", color="#15803D")
    ax.text(0.82, 0.28, "⏱ 1.5 phút\n- Kiểm tra nội dung nháp [DRAFT_ONLY]\n- Bấm 1-Click Approve gửi tài xế\nhoặc xác nhận điều xe cứu hộ", ha="center", va="center", fontsize=8, color="#1E293B")
    ax.text(0.82, 0.195, "Actor: Dispatcher (Human-in-the-loop)", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#16A34A")

    # Fallback Branching Arrow & Box
    ax.annotate("", xy=(0.475, 0.11), xytext=(0.475, 0.17),
                arrowprops=dict(arrowstyle="-|>", color="#D97706", lw=1.5, mutation_scale=10))
    fb_rect = patches.FancyBboxPatch((0.30, 0.09), 0.35, 0.055, boxstyle="round,pad=0.005,rounding_size=0.008",
                                    edgecolor="#D97706", facecolor="#FFFBEB", linewidth=1.2)
    ax.add_patch(fb_rect)
    ax.text(0.475, 0.117, "↩️ FALLBACK: Nếu AI timeout (>5s) hoặc lỗi\n➔ Dispatcher tự động xử lý thủ công theo quy trình cũ", 
            ha="center", va="center", fontsize=7.5, fontweight="semibold", color="#B45309")

    # ==========================================
    # PHẦN 3: SUMMARY BANNER (DƯỚI CÙNG)
    # ==========================================
    summary_text = (
        "📊 HIỆU QUẢ: Giảm thời gian xử lý từ 15 phút ➔ 2.2 phút (Tiết kiệm >85% thời gian)  |  "
        "Bảo vệ an toàn 100% tài xế qua ranh giới pin < 5% & thẻ [DRAFT_ONLY]"
    )
    ax.text(0.5, 0.035, summary_text, ha="center", va="center", fontsize=9.5, fontweight="bold", color="#0F172A",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#E2E8F0", edgecolor="#CBD5E1", lw=1))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    output_file = "01-individual-problem-scan-workflow-card-1.png"
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    print(f"🎉 Đã xuất thành công sơ đồ: {output_file}")

if __name__ == "__main__":
    generate_card1_workflow()