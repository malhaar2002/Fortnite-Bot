import pyautogui
from time import sleep



pyautogui.click(627, 818)
pyautogui.press('f')

x, y = pyautogui.position()

def run():
    pyautogui.keyDown('w')
    sleep(30)
    pyautogui.keyUp('w')

def double_ramp():
    pyautogui.keyDown('w')
    pyautogui.keyDown('q')
    sleep(15)
    pyautogui.keyUp('w')
    pyautogui.keyUp('q')

def box_up(x, y):
    time = 0
    pyautogui.keyDown('tab')
    pyautogui.mouseDown()
    while time < 10:
        pyautogui.moveTo(x+300, y)
        x, y = pyautogui.position()
        time += 1
    pyautogui.keyUp('tab')
    pyautogui.keyDown('alt')
    pyautogui.moveTo(x, y-300)
    pyautogui.moveTo(x, y+200)
    pyautogui.keyUp('alt')
    pyautogui.mouseUp()

def spam_90s(x, y):
    pyautogui.press('q')
    pyautogui.click()
    sleep(1)
    pyautogui.keyDown('w')
    sleep(0.9)
    pyautogui.keyUp('w')

    pyautogui.press('tab')
    pyautogui.click()
    pyautogui.moveTo(x+2000, y)
    pyautogui,press('tab')
    pyautogui.click()


    x, y = pyautogui.position()

while True:
    spam_90s(x, y)
    x, y = pyautogui.position()
