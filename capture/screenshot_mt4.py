import pygetwindow as gw
import pyautogui
import time
import os

save_path = os.path.join(os.path.dirname(__file__), '..', 'latest_chart.png')

print("🖱 [SCREENSHOT] Clicking MT4 taskbar icon...")
pyautogui.click(504, 1060)
time.sleep(1)

print("⏳ [SCREENSHOT] Waiting 5 seconds for MT4 to render...")
time.sleep(5)

windows = gw.getWindowsWithTitle("BoForex")
if windows:
    win = windows[0]
    print(f"📐 [SCREENSHOT] MT4 bounds: left={win.left}, top={win.top}, width={win.width}, height={win.height}")
    bbox = (win.left, win.top, win.width, win.height)

    print("📸 [SCREENSHOT] Taking screenshot...")
    screenshot = pyautogui.screenshot(region=bbox)
    screenshot.save(save_path)
    print(f"✅ [SCREENSHOT] Saved to {save_path}")
else:
    print("❌ [SCREENSHOT] MT4 window not found.")