import sys
import pyautogui
import time
import random
import keyboard 
import sys

screen_width, screen_height = pyautogui.size()
print("x : ",screen_width)
print("y : ",screen_height)
ratioX = screen_width / 1920
ratioY = screen_height / 1080
hardcoded_field_coords = [705,1211,100,700]
hardcoded_deck_coords = []

def checkUserInput():
    if keyboard.is_pressed("esc"):
        sys.exit("esc pressed -> exit the script")
  
  
def findGame():
    checkUserInput()
    time.sleep(2)
    pyautogui.click(878*ratioX, 681*ratioY) 
    time.sleep(2)

cards = [[835,918],]
def selectCard():
    checkUserInput()
    car = random.randint(0, len(cards)-1)
    pyautogui.click(cards[car][0]*ratioX, cards[car][1]*ratioY) 
    time.sleep(0.2)


def playCard():
    checkUserInput()
    x = random.randint(hardcoded_field_coords[0],hardcoded_field_coords[1])*ratioX
    y = random.randint(hardcoded_field_coords[2],hardcoded_field_coords[3])*ratioY
    time.sleep(0.1)
    pyautogui.click(x,y) 


def emot():
    checkUserInput()
    time.sleep(0.1)
    pyautogui.click(719*ratioX, 904*ratioY) # emot menu
    time.sleep(0.1)
    pyautogui.click(833*ratioX, 732*ratioY)  # emot
    pyautogui.click(833*ratioX, 642) # quit emot menu


def chooseDeck(i):
    checkUserInput()
    time.sleep(4)
    # switch to the deck window
    pyautogui.click(804*ratioX, 1011*ratioY)
    time.sleep(0.5)
    # pick deck num i
    ## lignes un peu useless mais c est technique et on aime bien les trucs technique et j ai la flemme de mettre a jour mon code meme si ce serai plus opti 
    rawStr = pick(i) #string in "x|y" format 
    sepStr = rawStr.split("|") #list : [x,y] /!\ type = string -> cast is necessary
    x = int(sepStr[0])*ratioX
    y = int(sepStr[1])*ratioY
    # click on the deck
    pyautogui.click(x,y)
    time.sleep(0.5)
    
    # get back on main window
    pyautogui.click(1006*ratioX, 1018*ratioY)
    # sleep a sec to avoid bug
    time.sleep(1)
    

def pick(i):
    checkUserInput()
    switch={
        0:"830|255",
        1:"899|255",
        2:"962|255",
        3:"1026|255",
        4:"1086|255"
    }
    return switch.get(i, "a number between 0 and 4 is required")    
    
    
def endOfGame():
    checkUserInput()
    time.sleep(1)
    pyautogui.click(968*ratioX, 922*ratioY)
    
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