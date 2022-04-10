import pyautogui
import time
import win32api
import random


def getMousePos():
    pos = pyautogui.position()
    print(pos.x, pos.y)  
    


# Get mouse position

# state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
# state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

# while (loop):
#     a = win32api.GetKeyState(0x01)
#     b = win32api.GetKeyState(0x02)

#     if a != state_left:  # Button state changed
#         state_left = a
#         if a < 0:
#             print('Left Button Pressed')
#             getMousePos()

#     if b != state_right:  # Button state changed
#         state_right = b
#         if b < 0:
#             print('Right Button Pressed')
#             getMousePos()
#     time.sleep(0.001)


def findGame():
    time.sleep(2)
    pyautogui.click(1247, 665)
    time.sleep(3)    
    pyautogui.click(1275, 493)
    time.sleep(2)

keys = ['&','é','"',"'"]
def selectCard():
    index = random.randint(0,3)
    pyautogui.hotkey(keys[index])
    if index == 1:
        pyautogui.click(1143, 888)
    time.sleep(0.2)


def playCard():
    x = random.randint(999,1361)
    y = random.randint(300, 700)
    pyautogui.click(x,y) 

def emot():
    time.sleep(0.1)
    pyautogui.click(989, 794)
    time.sleep(0.1)
    pyautogui.click(1233, 742)
    
    
def endOfGame():
    pyautogui.click(1183, 842)
    
play = True    

while(play):
    # search for a game 
    findGame()
        
    inGame = True
    chrono = 0
    # in game
    while(inGame):
        selectCard()
        playCard()
        emot()
        time.sleep(2)
        chrono += 4.4
        if chrono >= 30:
            inGame = False
    endOfGame()       