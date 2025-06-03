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
│   ├── focus_chrome.py
│   ├── focus_mt4.py
│   ├── screenshot_mt4.py
│
├── config/
│   ├── coord_helper.py
│   ├── window_title.py
│
├── upload/
│   └── upload_to_chatgpt.py
│
├── latest_chart.png            # Output screenshot
├── run.py                      # Orchestrator script
├── requirements.txt            # Python deps
├── .gitignore
└── README.md
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
```bash
python config/coord_helper.py
```

Then update hardcoded coordinates in:
- `upload_to_chatgpt.py` (plus button, file dialog, send button)
- `focus_mt4.py` and `focus_chrome.py` (taskbar icon clicks)

---

## 🚀 Running the App

```bash
python run.py
```

---

## 🛠 Dependencies

- `pyautogui`
- `pygetwindow`
- `pillow`

---

## 🧩 Future Enhancements

- Inject chart prompts for structured analysis
- Parse trade setups from ChatGPT response
- Write to `orders.json` for EA execution

---

## 📄 License

MIT License