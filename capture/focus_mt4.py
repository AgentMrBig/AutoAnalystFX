import pygetwindow as gw
import pyautogui
import time

def focus_window(title_contains):
    windows = gw.getWindowsWithTitle(title_contains)
    if windows:
        win = windows[0]
        win.activate()
        time.sleep(1)
        print(f"✅ Focused window: {win.title}")
    else:
        print(f"❌ No window found with title containing: {title_contains}")

if __name__ == "__main__":
    focus_window("BoForex")
    time.sleep(2)