import os
from flask import Flask, request, jsonify
from ocr import extract_chart_data
from strategy import generate_signal

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
EQUITY = 400
RISK_PERCENT = 5

@app.route('/')
def home():
    return jsonify({
        'message': 'Trading Screenshot Bot is running',
        'upload_endpoint': '/upload'
    })

@app.route('/upload', methods=['POST'])
def upload_screenshot():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    market_data = extract_chart_data(file_path)
    signal = generate_signal(market_data, EQUITY, RISK_PERCENT)

    return jsonify(signal)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
