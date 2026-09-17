from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

b@app.route('/')
def index():
    """Màn 1: Chọn ngữ cảnh & Hoạt động"""
    return render_template('select.html')

@app.route('/style', methods=['GET', 'POST'])
def style_select():
    """Màn 2: Chọn tiêu chí phong cách & Trọng số DSS"""
    if request.method == 'POST':
        return redirect(url_for('loading'))
    activity = request.args.get('activity', 'Studio làm đồ án')
    return render_template('style.html', activity=activity)

@app.route('/loading')
def loading():
    """Màn 3: Màn hình chờ tính toán Ma trận DSS"""
    return render_template('loading.html')

@app.route('/results')
def results():
    """Màn 4: Hiển thị kết quả xếp hạng Top-3"""
    return render_template('results.html', outfits=MOCK_OUTFITS)

@app.route('/detail')
@app.route('/detail/<int:outfit_id>')
def detail(outfit_id=1):
    """Màn 5: Chi tiết Outfit & Ma trận phân tích điểm DSS"""
    outfit = next((item for item in MOCK_OUTFITS if item["id"] == outfit_id), MOCK_OUTFITS[0])
    return render_template('detail.html', outfit=outfit)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# Cấu trúc dữ liệu mẫu (Mock Data) sẵn sàng để kết nối với thuật toán DSS của bạn sau này
MOCK_OUTFITS = [
    {
        "id": 1,
        "name": "Thu Đông Nhẹ Nhàng (Studio & Lý Thuyết)",
        "items": "Áo khoác len oversize · Áo sơ mi trắng · Jeans xanh navy · Boots da chunky",
        "match_score": 95,
        "temp_score": 98,
        "style_score": 92,
        "activity_score": 95,
        "desc": "Lựa chọn hoàn hảo cho ngày se lạnh làm đồ án tại Studio. Giữ ấm vừa đủ, thoải mái vận động khi cắt dựng mô hình.",
        "tags": ["18-22°C", "Campus", "Casual", "Studio Kiến Trúc"],
        "breakdown": [
            {"category": "ÁO KHOÁC", "name": "Áo khoác len xám nhạt oversize"},
            {"category": "ÁO TRONG", "name": "Áo sơ mi trắng Oxford basic"},
            {"category": "QUẦN", "name": "Quần jeans xanh navy ống suông"},
            {"category": "GIÀY", "name": "Boots da nâu cổ thấp chunky"}
        ]
    },
    {
        "id": 2,
        "name": "Minimalist Layering (Bảo vệ Đồ án)",
        "items": "Blazer ghi xám · Áo thun cổ trụ đen · Quần tây suông · Sneaker tối giản",
        "match_score": 88,
        "temp_score": 85,
        "style_score": 94,
        "activity_score": 85,
        "desc": "Tạo vẻ ngoài chỉn chu, thanh lịch cho các buổi thuyết trình và bảo vệ đồ án trước hội đồng.",
        "tags": ["Smart Casual", "Trang trọng", "Tối giản"],
        "breakdown": [
            {"category": "ÁO KHOÁC", "name": "Blazer màu ghi xám phom rộng"},
            {"category": "ÁO TRONG", "name": "Áo thun cổ trụ màu đen"},
            {"category": "QUẦN", "name": "Quần tây đen dáng suông"},
            {"category": "GIÀY", "name": "Sneaker da trắng tối giản"}
        ]
    },
    {
        "id": 3,
        "name": "Năng Động Xưởng Mô Hình (Thực địa / Xưởng)",
        "items": "Áo Hoodie Be · Quần Cargo Túi Hộp · Sneaker Thể Thao · Túi Tote Canvas",
        "match_score": 82,
        "temp_score": 90,
        "style_score": 80,
        "activity_score": 76,
        "desc": "Tối ưu sự thoải mái và chất liệu bền bỉ cho những ngày làm việc liên tục tại xưởng kiến trúc.",
        "tags": ["Streetwear", "Thoải mái", "Bền bỉ"],
        "breakdown": [
            {"category": "ÁO KHOÁC", "name": "Áo Hoodie Be unisex nỉ bông"},
            {"category": "ÁO TRONG", "name": "Áo thun cotton thoáng khí"},
            {"category": "QUẦN", "name": "Quần Cargo túi hộp màu xanh olive"},
            {"category": "GIÀY", "name": "Sneaker đế thô êm chân"}
        ]
    }
]
