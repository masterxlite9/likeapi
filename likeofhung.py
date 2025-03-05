from flask import Flask, request, jsonify
from main import start_like
import threading

app = Flask(__name__)

@app.route('/getlike', methods=['GET'])
def get_like():
    uid = request.args.get('uid')
    
    # التحقق من عدم توفير معرف المستخدم
    if uid is None:
        return jsonify({"error": "لم تقم بتقديم المعرف"}), 400

    # التحقق من صحة المعرف (يجب أن يكون بين 8 و12 رقمًا)
    if not uid.isdigit() or not (8 <= len(uid) <= 12):
        return jsonify({"error": "معرف المستخدم غير صالح. يجب أن يكون بين 8 و12 رقمًا."}), 400

    try:
        # تشغيل `start_like` في خيط منفصل
        threading.Thread(target=start_like, args=(uid,)).start()
        return jsonify({
            "dev": "HVH VZ",
            "status": "تم تعزيز الإعجابات بنجاح",
            "id": uid,
            "game": "فري فاير"
        }), 200
    except Exception as e:
        # في حالة حدوث خطأ تقني
        return jsonify({"error": "حدثت مشكلة تقنية."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # تعديل المنفذ إذا لزم الأمر
