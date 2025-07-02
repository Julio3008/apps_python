import pyautogui as botMouse
import webbrowser
import time

webbrowser.open("https://www.youtube.com/@HablandoHuevadasOficial")
while True:
    x = 1726
    y = 460

    botMouse.moveTo(x,y,0.5)
    time.sleep(4)
    botMouse.click()