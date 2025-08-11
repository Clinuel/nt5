from paddleocr import PaddleOCR
import cv2

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def extract_chart_data(image_path):
    result = ocr.ocr(image_path, cls=True)
    prices = []

    for line in result[0]:
        text = line[1][0]
        try:
            prices.append(float(text.replace(",", "")))
        except ValueError:
            continue

    current_price = max(prices) if prices else None

    return {
        'symbol': 'XAUUSD',
        'timeframe': '15m',
        'current_price': current_price
    }
