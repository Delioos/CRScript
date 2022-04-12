# Code to find the coord of the mouse when a click is detected 
# we used it here to find the coordinates of every button / dimension of the field etc  
import pyautogui
import time
import win32api
import keyboard 

def getKeypress():
    #if keyboard.read_key() == 'f': # this method stop the action before having a key pressed 
    #    print("press")
    if keyboard.is_pressed("esc"): # seems to be the gud solution 
        print("ca sort vite vite ")
        exit()
    time.sleep(0.05)
    if keyboard.is_pressed("a"): 
        print("zob")
    if keyboard.is_pressed("space"): 
        print("space")

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
    # keypress test 
    getKeypress()
    time.sleep(0.001)