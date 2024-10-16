from flask import Flask, request, jsonify
from main import start_like
import threading

app = Flask(__name__)

@app.route('/getlike', methods=['GET'])
def get_like():
    uid = request.args.get('uid')
    
    if uid is None:
        return jsonify({"error": "Missing 'uid' parameter"}), 400

    # Call the start_like function in a separate thread
    threading.Thread(target=start_like, args=(uid,)).start()

    return jsonify({"message": f"Started liking for UID: {uid}"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Adjust the port as necessary
