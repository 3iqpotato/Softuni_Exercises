import pyautogui
import time
word = input("Enter a word...")
times = int(input("How many times to clone?..."))
time.sleep(5)
count = 1
while count < times + 1:
    pyautogui.typewrite(str(count) + " " + word)
    pyautogui.press("enter")
    count += 1
time.sleep(3)
enter_times = int(input())
count = 1
while count < enter_times + 1:
    pyautogui.press("left Click")
    count += 1