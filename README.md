# AutoAnalystFX

**AutoAnalystFX** is a Python-based automation pipeline that enables AI-powered analysis of live MetaTrader 4 (MT4) chart screenshots. The system autonomously captures MT4 screenshots, uploads them to ChatGPT via browser automation, and receives trading insights or signal responses.

---

## 🧠 Purpose

This tool is designed to:
- Capture live USD/JPY MT4 chart images
- Upload those screenshots to ChatGPT via browser automation
- Enable ChatGPT to visually analyze chart data and respond with trade insights
- Eventually parse and execute trades via integration with an Expert Advisor

---

## 📁 Project Structure

```
AutoAnalystFX/
├── capture/
│   ├── coord_helper.py         # Helper to detect screen coordinates
│   ├── focus_chrome.py         # Focuses Chrome via taskbar icon
│   ├── focus_mt4.py            # Focuses MT4 via taskbar icon
│   ├── screenshot_mt4.py       # Captures MT4 window screenshot
│
├── upload/
│   └── upload_to_chatgpt.py    # Automates ChatGPT image upload via UI interaction
│
├── latest_chart.png            # Output chart screenshot (updated on each run)
├── run.py                      # Main orchestrator: focus, capture, upload
├── requirements.txt            # Python dependencies
└── README.md                   # You're here
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-user/AutoAnalystFX.git
cd AutoAnalystFX
```

2. **Create virtual environment**

```bash
python -m venv .venv
source .venv/scripts/activate  # Windows Git Bash
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Update coordinates**  
Run the helper to get button/region positions:
```bash
python capture/coord_helper.py
```

Update these values in:
- `upload_to_chatgpt.py` (for `+`, file, send buttons)
- `focus_mt4.py` and `focus_chrome.py` (taskbar icon clicks)

---

## 🚀 Running the App

```bash
python run.py
```

This will:
1. Focus MT4
2. Screenshot the chart
3. Switch to ChatGPT in Chrome
4. Upload and send the screenshot

---

## 🛠 Dependencies

- `pyautogui` – UI automation
- `pygetwindow` – Window detection
- `pillow` – Image capture and save
- `time`, `os`, `subprocess`, `sys`

---

## 🧩 Planned Enhancements

- Add ChatGPT prompt injection for structured signal analysis
- Parse structured JSON signals from response
- Forward signals to MT4 EA via `orders.json`
- Schedule automated hourly/daily capture and analysis

---

## 📄 License

MIT License (or add your license of choice)