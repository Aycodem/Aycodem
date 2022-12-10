import pyautogui
import time
time.sleep(3)
count=1

while count <= 100:
    pyautogui.typewrite("i love you " + str(count) + " time")
    pyautogui.press("enter")
    count+=1

