import random

def play_turn(player): #series of events that take place during a turn
    turnOver = False #initial conditions of a fresh turn
    dice = 0
    suggestionMade = False
    moved = False
    while turnOver == False: #a turn can have many different phases or pieces, and so long as the player can continue to act, the turn is still ongoing
        optionsList = check_options(player, dice, suggestionMade, moved) #calls function to assess current game situation
        optionsDict = {}  #starts a dictionary for options. only really useful for having a numbereed list that is mutable
        optionsString = player.character + ', your options are:\n' #the repeated prompt to ask the player what they can do
        for lineItem in optionsList:
            optionsString += str(lineItem[0]) + '.' + lineItem[1] + '\n'
            optionsDict[lineItem[0]] = lineItem[1] #the idea of whats happening here is to take a list of options and number them in consecutive order. overall just looks neater this way
        validChoice = False #this is a check to make sure that the choice the player makes exists within the dictionary of chocies available
        while validChoice == False:
            print(optionsString)
            choice = input(player.character + ", make your selection \n") #gets a prompt from player, must be number, must be in list
            if choice.isnumeric() == False:
                print("Please type a number from the choices!")
            else:
                choice = int(choice)
                if optionsDict.get(choice) == None:
                    print("Not a valid choice!\n")
                else:
                    print(player.character + " has chosen to " + optionsDict.get(choice))
                    validChoice = True
        if optionsDict.get(choice) == "Roll the Dice": #compares numerical value of player choice to the actual function listed in the dictionary to decide what the player wants to do
            dice = rollDice()
            print(player.character + " rolled " + str(dice))
        if optionsDict.get(choice) == "Make a Suggestion":
            makeSuggestion(player)
            suggestionMade = True
        if optionsDict.get(choice) == "End Your Turn":
            print(player.character + " has ended their turn")
            turnOver = True
        if optionsDict.get(choice) == "Move " + str(dice) + " Spaces":
            print(player.character + " has chosen to move")
            move(dice)
            moved = True

def rollDice(): #basic roll dice function
    roll = random.randrange(2,13)
    return roll

def move(dice):
    validMove = False
    while validMove == False:
        moveString = input("Please enter a move command consisting of U, D, L, and R.") 
        if len(moveString) > dice:
            print("This is not a valid move string: it is too long")
            continue
        if len(moveString) < dice:
            print("This is not a valid move stirng: it is too short")
            continue
        else:
            for command in moveString:
                if command not in "UDLR":
                    print("this is not a valid move string")
                    print(command)
                    break
                else:
                    validMove = True
    
    print("Move string accepted")

def makeSuggestion(player):
    list_suspects = ['Miss Scarlet', 'Col. Mustard', 'Mrs. White', 'Mr. Green', 'Mrs Peacock', 'Professor Plum']
    validSusp = False
    suspStr = ''
    for i in range(6):
        suspStr = suspStr + str(i) + ") " + list_suspects[i] + "\n"
    while validSusp == False:
        print("Please select a suspect \n")
        sugSusp = input(suspStr)
        if sugSusp.isnumeric() == False:
            print("Please type a number ranging from 0-5")
        else:
            if int(sugSusp) < 6:
                validSusp = True
            else:
                print(sugSusp + " is not in range!")
    sugSusp = list_suspects[int(sugSusp)]
    list_weapons = ['Revolver', 'Lead Pipe', 'Candlestick', 'Rope', 'Knife', 'Wrench']
    validWeap = False
    weapStr = ''
    for i in range(6):
        weapStr = weapStr + str(i) + ") " + list_weapons[i] + "\n"
    while validWeap == False:
        print("Please select a weapon \n")
        sugWeap = input(weapStr)
        if sugWeap.isnumeric() == False:
            print("Please type a number ranging from 0-5")
        else:
            if int(sugWeap) < 6:
                validWeap = True
            else:
                print(sugWeap + " is not in range!")

    sugWeap = list_weapons[int(sugWeap)]
    sugRoom = player.currentRoom
    sugList = [sugSusp, sugWeap, sugRoom]
    print(player.character + " suggested " + sugSusp + " in the " + sugRoom + " with the " + sugWeap + "\n")
    otherPlayers = []
    questioning = True
    otherPlayers = [white, scarlet]
    while questioning == True:
        possibleCards = []
        for players in otherPlayers:
            for card in sugList:
                if card in players.hand:
                    possibleCards.append(card)
            if len(possibleCards) > 0:
                provingCharacter = players
                print(players.character + " can disprove the suggestion")
                break
            else:
                print(players.character + " cannot disprove the suggestion")
        if players.human == True:
            playerCardChoices = {}
            selectCardString = ''
            startIndex = 0
            for card in possibleCards:
                playerCardChoices[startIndex] = card
                startIndex += 1
            startIndex = 0
            for values in playerCardChoices:
                selectCardString = selectCardString + startIndex + ". " + playerCardChoices.get(startIndex) + "\n"
                startIndex += 1
            validChoice = False
            while validChoice == False:
                choice = input("Please choose a card to show the opponent: \n" + selectCardString)
                if choice.isnumeric() == False:
                    print("Please type a number from the choices!")
                else:
                    choice = int(choice)
                    if playerCardChoices.get(choice) == None:
                        print("Not a valid choice! \n")
                    else:
                        print(provingCharacter + " has " + choice)
        else:
            shownCard = possibleCards[random.randrange(0, len(possibleCards))]
            print(players.character + " has " + shownCard)
        questioning = False
def makeAccusation(player):
    accSusp = ''
    accWeap = ''
    accRoom = ''
    print(player.character + " has accused " + accSusp + " in the " + accRoom + " with the " + accWeap + '\n')

def check_options(player, dice, suggestionMade, moved): #uses conditions to check to see if a player can make certain moves on their turns
    optionsList = []
    currentOption = 1
    if player.lter != player.currentRoom and suggestionMade == False: #uses current room vs previous turn end room as well as wether a suggestion has been made already
        optionsList.append([currentOption, "Make a Suggestion"])
        currentOption += 1 #iterates through a sequential list of options
    if dice == 0: #unrolled dice = 0, any rolled dice is between 2 and 12
        optionsList.append([currentOption, "Roll the Dice"])
        currentOption += 1
    if dice > 0 and moved == False: # a player can roll and opt to not move, this is the case for this if statement
        moveString = "Move " + str(dice) + " Spaces"
        optionsList.append([currentOption, moveString])
        currentOption += 1
    optionsList.append([currentOption, "Make an Accusation"]) #an accusation can be made at any time
    optionsList.append([0, "End Your Turn"]) #a player can end their turn at any time
    return optionsList

class Player: 
    def __init__(self, character):
        self.character = character
        self.human = False
        self.turns_played = 0
        self.lter = "Corridor"
        self.currentRoom = "Hall"
        self.hand = []
class Room:
    def __init__(self,name):
        self.name = name
        self.players = []
        self.secretPassage = None
        self.boardTiles = []
        self.walls = []
        self.doors =[]



mystery = "Unsolved"
plum = Player("Professor Plum") 
white = Player("Mrs. White")
scarlet = Player("Ms. Scarlet")
white.hand = ['Knife', 'Library']
scarlet.hand = ['Revolver', 'Hall']
plum.human = True
players = [
    plum, scarlet, white
]
def playerSelect(suspects):
    validChoice = False
    while validChoice == False:
        numPlayers = input("How many players? 3-6")
        if numPlayers.isnumeric() == False:
            print("Please select a number from 3 to 6")
        else:
            if int(numPlayers) < 3 or int(numPlayers) > 6:
                print("Please select a number from 3 to 6")
            else:
                print("A " + numPlayers + "-player game")
                validChoice = True
    remainingPlayers = []
    for char in suspects:
        remainingPlayers.append(char)
    suspectString = []
    startIndex = 1
    for char in remainingPlayers:
        suspectString = suspectString + str(startIndex) + ") " + remainingPlayers[startIndex - 1] + "\n"
        startIndex +=1
    validPlayer = False
    while validPlayer == False:
        print("Available characters")
        print(suspectString)
        player = input("Make a selection \n")
        if player.isnumeric() == False or int(player) < 1 or int(player) > len(suspects):
            print("Please make a valid selection")
        else:
            print("The player has chosen to play as " + suspects[int(player - 1)])
            playerOne = Player(suspects[int(player - 1)])
            remainingNumPlayers = numPlayers - 1
            listOfPlayers = [playerOne]
            validPlayer = True
            remainingPlayers.remove()
    while remainingNumPlayers > 0:
        validAIChoice = False:
        while validAIChoice == False:
            suspectString = []
            startIndex = 1
            for char in remainingPlayers:
                suspectString = suspectString + str(startIndex) + ") " + remainingPlayers[startIndex - 1] + "\n"
                startIndex +=1

def buildBoard(rooms):
    rooms = ['Hall', 'Billiard Room', 'Ballroom', 'Lounge', 'Conservatory', 'Kitchen', 'Study', 'Library', 'Dining Room']
    for room in rooms:
        newroom = Room(room)
    Conservatory.secretPassage = Lounge
    Lounge.secretPassage = Conservatory
    Kitchen.secretPassage = Study
    Study.secretPassage = Kitchen

def dealSolution(rooms, suspects, weapons):
    solSusp = suspects[random.randrange(0, len(suspects))]
    solWeap = weapons[random.randrange(0, len(weapons))]
    solRoom = rooms[random.randrange(0, len(rooms))]
    remainingCards = []
    for card in rooms:
        if card == solRoom:
            continue
        else:
            remainingCards.append(card)
    for card in suspects:
        if card == solSusp:
            continue
        else:
            remainingCards.append(card)
    for card in weapons:
        if card == solWeap:
            continue
        else:
            remainingCards.append(card)
    return [remainingCards, solSusp, solWeap, solRoom]

def playGame():
    gameType = input("What type of game would you like to play? \n 1) Classic \n 2) Master Detective (NOT OPERATIONAL) \n")
    if gameType == "1":
        rooms = ['Hall', 'Billiard Room', 'Ballroom', 'Lounge', 'Conservatory', 'Kitchen', 'Study', 'Library', 'Dining Room']
        suspects = ['Miss Scarlet', 'Col. Mustard', 'Mrs. White', 'Mr. Green', 'Mrs. Peacock', 'Professor Plum']
        weapons = ['Knife', 'Revolver', 'Candlestick', 'Rope', 'Lead Pipe', 'Wrench']
    #if gameType == "2":
    #TODO insert rooms, suspects, and weapons from master detective
    remainingCardsPlusSolution = dealSolution(rooms, suspects, weapons)
    solSusp = remainingCardsPlusSolution[1]
    solWeap = remainingCardsPlusSolution[2]
    solRoom = remainingCardsPlusSolution[3]
    
    buildBoard(rooms)
    mysterySolved = False
    while mysterySolved == False:

rounds_played = 0
play_turn(plum)
# while mystery == "Unsolved":
#     for player in players:
#         play_turn(player)
#     rounds_played += 1
#     if rounds_played == 5:
#         mystery = "Solved"

# print("The game is over")
