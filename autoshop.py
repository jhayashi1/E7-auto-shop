from pyautogui import *
import pyautogui
import random
import keyboard
import time
import win32api, win32con

isChecked = False

# REFRESH_BUTTON_MIN_X = 200
# REFRESH_BUTTON_MAX_X = 525
# REFRESH_BUTTON_MIN_Y = 940
# REFRESH_BUTTON_MAX_Y = 980

# REFRESH_CONFIRM_MIN_X = 975
# REFRESH_CONFIRM_MAX_X = 1200
# REFRESH_CONFIRM_MIN_Y = 625
# REFRESH_CONFIRM_MAX_Y = 675

BUY_BUTTON_MIN_X_OFFSET = 675   #725
BUY_BUTTON_MAX_X_OFFSET = 875   #925
BUY_BUTTON_MIN_Y_OFFSET = 15    #75
BUY_BUTTON_MAX_Y_OFFSET = 55    #115

CONFIRM_BUTTON_MIN_X = 875
CONFIRM_BUTTON_MAX_X = 1225
CONFIRM_BUTTON_MIN_Y = 725
CONFIRM_BUTTON_MAX_Y = 775

REFRESH_BUTTON_MIN_X_OFFSET = 20
REFRESH_BUTTON_MAX_X_OFFSET = 400
REFRESH_BUTTON_MIN_Y_OFFSET = 20
REFRESH_BUTTON_MAX_Y_OFFSET = 75

REFRESH_CONFIRM_BUTTON_MIN_X_OFFSET = 20
REFRESH_CONFIRM_BUTTON_MAX_X_OFFSET = 250
REFRESH_CONFIRM_BUTTON_MIN_Y_OFFSET = 20
REFRESH_CONFIRM_BUTTON_MAX_Y_OFFSET = 75

#Clicks at x and y position on screen
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(random.uniform(0.05, 0.1))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

#Buys item from the shop based on the position of the item
def buy_item(point):
    #Get random offsets and position of buttons to randomize clicks
    buy_x = random.randrange(BUY_BUTTON_MIN_X_OFFSET, BUY_BUTTON_MAX_X_OFFSET)
    buy_y = random.randrange(BUY_BUTTON_MIN_Y_OFFSET, BUY_BUTTON_MAX_Y_OFFSET)
    confirm_x = random.randrange(CONFIRM_BUTTON_MIN_X, CONFIRM_BUTTON_MAX_X)
    confirm_y = random.randrange(CONFIRM_BUTTON_MIN_Y, CONFIRM_BUTTON_MAX_Y)
    buy_pos=None

    #Click on buy button until the confirm button shows up
    while (buy_pos) == None:
        click(point[0]+buy_x, point[1]+buy_y)
        sleep(random.uniform(0.4, 1.0))
        buy_pos=pyautogui.locateOnScreen('buy.png', confidence=0.95)

    #Click on confirm button until it goes away
    while (buy_pos) != None:
        click(confirm_x, confirm_y)
        sleep(random.uniform(0.4, 1.0))
        buy_pos=pyautogui.locateOnScreen('buy.png', confidence=0.95)

#Checks for items on the screen
def check_for_items():
    #Time to let the items to show up after refreshing
    time.sleep(random.uniform(0.5, 1.0))

    #Look for covenant and mystics
    coven_pos=pyautogui.locateOnScreen('covenant.png', confidence=0.95)
    mystic_pos=pyautogui.locateOnScreen('mystic.png', confidence=0.95)

    #Buy covenant bookmarks if they show up
    if (coven_pos) != None:
        coven_point=pyautogui.center(coven_pos)
        print('Buying covenant bookmarks')
        buy_item(coven_point)
    
    #Buy mystic medals if they show up
    if (mystic_pos) != None:
        mystic_point=pyautogui.center(mystic_pos)
        print('Buying mystic medals')
        buy_item(mystic_point)

while keyboard.is_pressed('q') == False:
    #Look for refresh and refresh confirm button on the screen
    confirm_pos=pyautogui.locateOnScreen('confirm.png', confidence=0.95)
    refresh_pos=pyautogui.locateOnScreen('refresh.png', confidence=0.95)

    #Click on the confirm button if it is on the screen
    if (confirm_pos) != None:
            confirm_point=pyautogui.center(confirm_pos)
            click(confirm_pos[0]+random.randrange(REFRESH_CONFIRM_BUTTON_MIN_X_OFFSET, REFRESH_CONFIRM_BUTTON_MAX_X_OFFSET), confirm_pos[1]+random.randrange(REFRESH_CONFIRM_BUTTON_MIN_Y_OFFSET, REFRESH_CONFIRM_BUTTON_MAX_Y_OFFSET))
            isChecked = False
    #Click on the refresh button if the shop has already been checked and the confirm button isn't on the screen
    elif isChecked and (refresh_pos) != None and (confirm_pos) == None:
        refresh_point=pyautogui.center(refresh_pos)
        click(refresh_pos[0]+random.randrange(REFRESH_BUTTON_MIN_X_OFFSET, REFRESH_BUTTON_MAX_X_OFFSET), refresh_pos[1]+random.randrange(REFRESH_BUTTON_MIN_Y_OFFSET, REFRESH_BUTTON_MAX_Y_OFFSET))
    #Check for items in the shop
    else:
        check_for_items()
        keyboard.press_and_release('up arrow')
        time.sleep(0.75)    #Extra time to allow the scroll to complete
        check_for_items()
        isChecked = True

    time.sleep(random.uniform(0.25, 0.75))

