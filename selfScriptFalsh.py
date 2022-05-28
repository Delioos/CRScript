import sys
import pyautogui
import time
import random
import keyboard 
import sys


def checkUserInput():
    if keyboard.is_pressed("esc"):
        sys.exit("esc pressed -> exit the script")
  
  
def findGame():
    checkUserInput()
    time.sleep(2)
    pyautogui.click(1247, 665) # fiesta 
    time.sleep(3)    
    #pyautogui.click(1284, 699) # normal game genant le tirage un peu
    pyautogui.click(1284, 483) # special mode
    time.sleep(2)


keys = ['&','fuck victor','"',"'"]
def selectCard():
    checkUserInput()
    index = random.randint(0,3)
    if index == 1:
        pyautogui.click(1143, 888)
    else:
        pyautogui.hotkey(keys[index])
    time.sleep(0.2)


def playCard():
    checkUserInput()
    x = random.randint(999,1341)
    y = random.randint(300, 700)
    time.sleep(0.1)
    pyautogui.click(x,y) 


def emot():
    checkUserInput()
    time.sleep(0.1)
    pyautogui.click(989, 794) # emot menu
    time.sleep(0.1)
    pyautogui.click(1233, 742) # emot
    pyautogui.click(1233, 642) # quit emot menu


def chooseDeck(i):
    checkUserInput()
    time.sleep(4)
    # switch to the deck window
    pyautogui.click(1075, 890)
    time.sleep(0.5)
    # pick deck num i
    rawStr = pick(i) #string in "x|y" format 
    sepStr = rawStr.split("|") #list : [x,y] /!\ type = string -> cast is necessary
    x = int(sepStr[0])      
    y = int(sepStr[1])
    # click on the deck
    pyautogui.click(x,y)
    time.sleep(0.5)
    
    # get back on main window
    pyautogui.click(1199, 886)
    # sleep a sec to avoid bug
    time.sleep(1)
    

def pick(i):
    checkUserInput()
    switch={
        0:"1085|320",
        1:"1137|319",
        2:"1169|319",
        3:"1228|324",
        4:"1277|323"
    }
    return switch.get(i, "a number between 0 and 4 is required")    
    
    
def endOfGame():
    checkUserInput()
    time.sleep(1)
    pyautogui.click(1183, 842)
    
    
play = True    

# variable to handle deck switching
deckIndex = 0
while(play):
    # search for a game 
    findGame()
    # variable to handle the end of the game     
    inGame = True
    igClock = 0
    # in game
    while(inGame):
        selectCard()
        playCard()
        time.sleep(2)
        emot()
        time.sleep(2)
        igClock += 4.4
        if igClock >= 42:
            inGame = False
    endOfGame() 
    time.sleep(2) 
    checkUserInput()
    time.sleep(4)
    # switch deck every game min
    if deckIndex == 5:
        deckIndex = 0
    chooseDeck(deckIndex)
    deckIndex += 1
    
