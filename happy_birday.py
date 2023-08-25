import time
import pyautogui

my_time = time.ctime().split()
date = int(input('Enter date...'))
while True:
    if int(my_time[2]) == date:
        word = 'Happy Birthday!!!'
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        exit(0)
    else:
        hour, mins, seks = my_time[3].split(':')
        if int(mins) < 59:
            time.sleep(50)
        else:
            time.sleep(1)
        print(my_time)
        my_time = time.ctime().split()
        continue
