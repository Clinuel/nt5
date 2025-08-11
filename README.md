# Trading Screenshot Bot

This bot extracts trade information from a chart screenshot and generates a signal.

## How to Run
1. Clone the repo
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the app:
```bash
python app.py
```
4. Upload screenshot via API:
```bash
curl -F "file=@chart.jpg" http://localhost:5000/upload
```
