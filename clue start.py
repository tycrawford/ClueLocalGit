import random
import turtle
#Making some test changes for Git
human_player = 7
player_select_string = "Which player do you want to be? \n 1.) Miss Scarlet \n 2.) Col. Mustard \n 3.) Mrs. White \n 4.) Mr. Green \n 5.) Mrs. Peacock \n 6.) Professor Plum \n"  

num_rooms = 9
num_suspects = 6
num_weapons = 6

rooms = ["Conservatory", 'Lounge', 'Kitchen', 'Library', 'Hall', 'Study', 'Ballroom', 'Dining Room', 'Billiard Room']
suspects = ['Miss Scarlet', 'Col. Mustard', 'Mrs. White', 'Mr. Green', 'Mrs. Peacock', 'Professor Plum']
weapons = ['Candlestick', 'Knife', 'Lead Pipe', 'Revolver', 'Rope', 'Wrench']
characters = ['Miss Scarlet', 'Col. Mustard', 'Mrs. White', 'Mr. Green', 'Mrs. Peacock', 'Professor Plum']
num_players = 0
while num_players == 0:
    try:
        num_players = int(input("How many players? \n"))
    except:
        print("Must choose a number!")
    if num_players < 7 and num_players > 2:
        print("A " + str(num_players) + "-player game")
    elif num_players <= 2:
        print("Clue requires 3 - 6 players")
        num_players = 0
    else:
        print("Clue has a maximum of 6 players")
        num_players = 0
while human_player == 7:
    try:
        human_player = (int(input(player_select_string)) - 1)
    except:
        print("Must choose a number!")
    if human_player < 6:
        print("Player has selected " + suspects[human_player])
    else:
        print("Please select a value 1-6")
        human_player = 7
remaining_cards = []
def solution(remaining_cards):
    #randomly select solution cards
    sol_suspect = suspects[random.randrange(6)]
    sol_weapons = weapons[random.randrange(6)]
    sol_rooms = rooms[random.randrange(9)]

    #use reveal to test or check the solution
    reveal = input("Reveal the solution?")
    if reveal == "yes":
        print("It was " + sol_suspect + " with the " + sol_weapons + " in the " + sol_rooms)
    
    rem_sus = suspects
    rem_room = rooms
    rem_weap = weapons
    #with the solution removed, use the rest of the cards to make one deck
    rem_sus.remove(sol_suspect)
    rem_weap.remove(sol_weapons)
    rem_room.remove(sol_rooms)

    inde = 0
    for i in range(len(rooms)):
        remaining_cards.append(rem_room[inde])
        inde += 1
    inde = 0
    for i in range(len(weapons)):
        remaining_cards.append(rem_weap[inde])
        inde += 1
    inde = 0
    for i in range(len(suspects)):
        remaining_cards.append(rem_sus[inde])
        inde += 1

def deal(num_players, human_player, rem_cards):
    player_list = []
    player_index = human_player
    hands = []
    for i in range(num_players):
        player_list.append(characters[player_index])
        player_index = ((player_index + 2)%6) - 1
    cards_per_player = (len(rem_cards) // len(player_list))
    for i in range(num_players):
        new_hand = []
        for j in range(cards_per_player):
            new_card_number = random.randrange(len(rem_cards))
            new_hand.append(rem_cards[new_card_number])
            rem_cards.remove(rem_cards[new_card_number])       
        hands.append(new_hand)


def turn(player, end_turn_room, start_room):
    #Consider Options
    #Roll Dice
    #Move
    #Secret Passage
    #check if they've moved rooms
    #if different room, allow suggestion
    #check once at beginning of turn
    #check again at end of turn
    #pass the roll
    pass

class Char:
    #Character has control (Human/AI)
    #Character has name (See Suspects)
    #Character has cards
    #Character has a location at the end of the turn
    #Character has a current location
    def __init__(self):
        pass

    
def dice_roll():
    return random.randrange(2, 13)
def playersetup(num_players, human_player):
    for i in range(len(num_players)):
        new_guy = characters[human_player]
        new_guy.Char()
    
    human

#while mystery == "unsolved":
#    mystery = "solved"
solutiontest = solution(remaining_cards)
deal(num_players, human_player, remaining_cards)
playersetup(num_players, human_player)
