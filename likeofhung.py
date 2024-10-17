from flask import Flask, request, jsonify
from main import start_like
import threading

app = Flask(__name__)

@app.route('/getlike', methods=['GET'])
def get_like():
    uid = request.args.get('uid')
    
    # Kiểm tra nếu không có giá trị `uid`
    if uid is None:
        return jsonify({"error": "Bạn chưa cung cấp api"}), 400

    # Kiểm tra nếu `uid` không hợp lệ (không phải từ 8 đến 12 số)
    if not uid.isdigit() or not (8 <= len(uid) <= 12):
        return jsonify({"error": "UID không hợp lệ. UID phải là từ 8 đến 12 số."}), 400

    try:
        # Gọi hàm `start_like` trong một luồng riêng biệt
        threading.Thread(target=start_like, args=(uid,)).start()
        return jsonify({
            "Dev": "HVH VZ",
            "status": "Đã buff like thành công",
            "id": uid,
            "game": "Free Fire"
        }), 200
    except Exception as e:
        # Trường hợp lỗi kỹ thuật
        return jsonify({"error": "Đang trục chặc kỹ thuật."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Điều chỉnh cổng nếu cần
