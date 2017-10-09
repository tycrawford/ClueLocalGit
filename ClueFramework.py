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
        if optionsDict.get(choice) == "Roll the Dice":
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
    sugSusp = "Mrs. White"
    sugWeap = "Revolver"
    sugRoom = player.currentRoom
    print(player.character + " suggested " + sugSusp + " in the " + sugRoom + " with the " + sugWeap + "\n")

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

mystery = "Unsolved"

plum = Player("Professor Plum")
white = Player("Mrs. White")
scarlet = Player("Ms. Scarlet")
plum.human = True
players = [
    plum, scarlet, white
]


rounds_played = 0
play_turn(plum)
# while mystery == "Unsolved":
#     for player in players:
#         play_turn(player)
#     rounds_played += 1
#     if rounds_played == 5:
#         mystery = "Solved"

# print("The game is over")
