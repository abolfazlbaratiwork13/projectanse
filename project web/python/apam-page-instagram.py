import pyautogui
import time

while True:
    w = input("w: ")
    if w =="end":
        break
    time.sleep(4)
    for i in range(300):
        pyautogui.typewrite(w)
        pyautogui.press("enter")