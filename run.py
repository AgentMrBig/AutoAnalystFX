import subprocess
import time
import os
import sys

venv_python = sys.executable
base_dir = os.path.dirname(__file__)

focus_mt4 = os.path.join(base_dir, 'capture', 'focus_mt4.py')
screenshot = os.path.join(base_dir, 'capture', 'screenshot_mt4.py')
focus_chrome = os.path.join(base_dir, 'capture', 'focus_chrome.py')
upload = os.path.join(base_dir, 'upload', 'upload_to_chatgpt.py')

print("🪟 [FOCUS_MT4] Starting...")
subprocess.run([venv_python, focus_mt4])

print("📸 [SCREENSHOT] Capturing chart...")
subprocess.run([venv_python, screenshot])

print("🌐 [FOCUS_CHROME] Switching to ChatGPT...")
subprocess.run([venv_python, focus_chrome])

print("📤 [UPLOAD] Uploading screenshot to ChatGPT...")
subprocess.run([venv_python, upload])

print("✅ [COMPLETE] Full automation cycle finished.")