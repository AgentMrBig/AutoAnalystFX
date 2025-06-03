import pygetwindow as gw

for win in gw.getAllTitles():
    if win.strip():
        print(f"🪟 {win}")
