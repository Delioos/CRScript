import pyautogui
import time
import win32api


def getMousePos():
    pos = pyautogui.position()
    print(pos.x, pos.y)  
    


# Get mouse position

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
loop = True
while (loop):
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)

    if a != state_left:  # Button state changed
        state_left = a
        if a < 0:
            print('Left Button Pressed')
            getMousePos()

    if b != state_right:  # Button state changed
        state_right = b
        if b < 0:
            print('Right Button Pressed')
            getMousePos()
    time.sleep(0.001)