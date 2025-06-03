import pyautogui
import time
import os

coords = {
    "plus_button": (736, 977),
    "file_option": (736, 920),
    "send_button": (1443, 976)
}

image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'latest_chart.png'))

print("📤 [UPLOAD] Starting upload sequence in 3 seconds...")
time.sleep(3)

print("🖱 [UPLOAD] Clicking '+' button...")
pyautogui.click(coords["plus_button"])
time.sleep(1)

print("🖱 [UPLOAD] Selecting 'Add photos and files'...")
pyautogui.click(coords["file_option"])
time.sleep(1.5)

print(f"⌨️ [UPLOAD] Typing path: {image_path}")
pyautogui.write(image_path)
time.sleep(0.5)
pyautogui.press("enter")

print("⏳ [UPLOAD] Waiting 3 seconds for file to load...")
time.sleep(3)

print("🖱 [UPLOAD] Clicking Send button...")
pyautogui.click(coords["send_button"])

print("✅ [UPLOAD] Screenshot sent successfully.")