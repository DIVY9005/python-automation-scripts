import pyautogui
import time
import webbrowser

# Delay to let you see it happen
time.sleep(2)

# List of websites to open
sites = [
    "https://www.linkedin.com",
    "https://github.com",
    "https://chat.openai.com",
    "https://instagram.com"
]

for site in sites:
    webbrowser.open(site)
    time.sleep(3)
