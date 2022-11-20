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
    # click on the main page button
    pyautogui.click(995*ratioX, 1014*ratioY)
    
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

    # sleep a sec to avoid bug
    time.sleep(1)
    

def pick(i):
    # funny function to pick the right deck
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
    
    
def collectRewards():
    # deck menu 
    pyautogui.click(811*ratioX, 1011*ratioY)
    time.sleep(0.5)
    # card rewards menu 
    pyautogui.click(1040*ratioX, 794*ratioY)
    time.sleep(0.5)
    # pour 10 cartes
    for i in range(10):
        # top left card
        pyautogui.click(785*ratioX, 317*ratioY)
        time.sleep(0.5)
        # challenge 1
        for j in range(10):
            pyautogui.click(941*ratioX, 544*ratioY)
            time.sleep(0.5)
        # challenge 2
        for j in range(10):
            pyautogui.click(941*ratioX, 680*ratioY)
            time.sleep(0.5)
        # challenge 3
        for j in range(10): 
            pyautogui.click(941*ratioX, 827*ratioY)
            time.sleep(0.5) 
        # exit the card 
        pyautogui.click(1200*ratioX, 151*ratioY)
        time.sleep(1) 
        # exit the challend reward menu
        pyautogui.click(1195*ratioX, 180*ratioY)
        time.sleep(1)
        
def main():         
    play = True    
    chronoStart = time.time()
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
        # switch deck every game 
        if deckIndex == 5:
            deckIndex = 0
        chooseDeck(deckIndex)
        deckIndex += 1
        # if the script has been running for more than 1h30
        if time.time() - chronoStart > 5400:
            # collect rewards
            collectRewards()
            # reset the chrono
            chronoStart = time.time()
        