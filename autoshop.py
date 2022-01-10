from pyautogui import *
import pyautogui
import random
import keyboard
import time
import win32api, win32con

REFRESH_BUTTON_MIN_X = 200
REFRESH_BUTTON_MAX_X = 525
REFRESH_BUTTON_MIN_Y = 940
REFRESH_BUTTON_MAX_Y = 980

REFRESH_CONFIRM_MIN_X = 975
REFRESH_CONFIRM_MAX_X = 1200
REFRESH_CONFIRM_MIN_Y = 625
REFRESH_CONFIRM_MAX_Y = 675

BUY_BUTTON_MIN_X_OFFSET = 675   #725
BUY_BUTTON_MAX_X_OFFSET = 875   #925
BUY_BUTTON_MIN_Y_OFFSET = 15    #75
BUY_BUTTON_MAX_Y_OFFSET = 55    #115

CONFIRM_BUTTON_MIN_X = 875
CONFIRM_BUTTON_MAX_X = 1225
CONFIRM_BUTTON_MIN_Y = 725
CONFIRM_BUTTON_MAX_Y = 775

def click(x, y):
    win32api.SetCursorPos((x, y))
    for i in range(1):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(random.uniform(0.05, 0.1))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def buy_item(point):
    buy_x = random.randrange(BUY_BUTTON_MIN_X_OFFSET, BUY_BUTTON_MAX_X_OFFSET)
    buy_y = random.randrange(BUY_BUTTON_MIN_Y_OFFSET, BUY_BUTTON_MAX_Y_OFFSET)
    confirm_x = random.randrange(CONFIRM_BUTTON_MIN_X, CONFIRM_BUTTON_MAX_X)
    confirm_y = random.randrange(CONFIRM_BUTTON_MIN_Y, CONFIRM_BUTTON_MAX_Y)
    
    click(point[0]+buy_x, point[1]+buy_y)
    click(point[0]+buy_x, point[1]+buy_y)
    sleep(random.uniform(0.4, 1.0))
    click(confirm_x, confirm_y)
    click(confirm_x, confirm_y)
    sleep(random.uniform(0.4, 1.0))

def check_for_items():
    time.sleep(random.uniform(0.5, 1.0))

    coven_pos=pyautogui.locateOnScreen('covenant.png', confidence=0.95)
    mystic_pos=pyautogui.locateOnScreen('mystic.png', confidence=0.95)

    if (coven_pos) != None:
        coven_point=pyautogui.center(coven_pos)
        print('Buying covenant bookmarks')
        buy_item(coven_point)
        time.sleep(random.uniform(1.5, 2.0))
    
    if (mystic_pos) != None:
        mystic_point=pyautogui.center(mystic_pos)
        print('Buying mystic medals')
        buy_item(mystic_point)

        time.sleep(random.uniform(1.5, 2.0))
        check_for_items()

while keyboard.is_pressed('q') == False:
    check_for_items()
    keyboard.press_and_release('up arrow')
    check_for_items()

    click(random.randrange(REFRESH_BUTTON_MIN_X, REFRESH_BUTTON_MAX_X), random.randrange(REFRESH_BUTTON_MIN_Y, REFRESH_BUTTON_MAX_Y))
    time.sleep(random.uniform(0.4, 0.75))
    click(random.randrange(REFRESH_CONFIRM_MIN_X, REFRESH_CONFIRM_MAX_X), random.randrange(REFRESH_CONFIRM_MIN_Y, REFRESH_CONFIRM_MAX_Y))

