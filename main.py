import pyautogui
import time

time.sleep(10)

print("Hit CTRL + C to cancel at anytime")

def moveAround():
    pyautogui.press("w")
    pyautogui.press("a")
    pyautogui.press("s")
    pyautogui.press("d")

while True:
    moveAround()