
# Code that doesnt do something related is seperated by two blank lines
# Related code is seperated by one blank line


"""
This is just verion V1.4.1 but modified to be rigged.
Im calling it 1.4.2


"""


from colorama import init   # pip install colorama
init()
from colorama import Fore, Back, Style
init(autoreset=True)

import random
import time
import sys

# the plays but colored
rolla = Fore.GREEN + "rock"
rollb = Fore.BLUE + "paper"
rollc = Fore.RED + "scissors"

# storage
player_score = 0
comp_score = 0
player_history = []
comp_history = []
enable_rig = False


# options
match_point = 3
p_comp_play_rigged = ["rock", "rock", "paper", "scissors"]
# if you want to add something other than r, p, or s, you need to edit the logic code


print(Fore.BLUE + Back.YELLOW + "Rock Paper Scissors by Brandon (V1.4.1, Updated October 2021)")
print("First to " + str(match_point) + " points wins!")


# asks player if they would like the game to be rigged in the computer's favor
# added this feature just to practice. in reality its useless
ask_for_rig = input("would you like to rig the game (50% chance of rock vs 33%)? y/n ")

if ask_for_rig == "y":
    enable_rig = True
    print("Rigging enabled")
else:
    enable_rig = False
    print("Rigging disabled")


# main game
while True:
    print()
    print(Fore.CYAN + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    class player_entry():
        # User inputs their play here
        print("Enter " + rolla + ", " + rollb + ", " + Fore.RESET + "or " + rollc)
        global player_input
        player_input = input()
        print()
        
        if player_input == "rock":
            print("You chose " + rolla)
            player_history.append(rolla)

        elif player_input == "paper":
            print("You chose " + rollb)
            player_history.append(rollb)

        elif player_input == "scissors":
            print("You chose " + rollc)
            player_history.append(rollc)

        else:
            print(Fore.RED + "Not a valid answer dummy! Restart the program")    # im too lazy to figure out how to ask again properly
            time.sleep(5)
            sys.exit()


    class roll_msg():
        print()
        print(rolla)
        time.sleep(0.2)
        print(rollb)
        time.sleep(0.2)
        print(rollc)
        time.sleep(0.2)
        print("shoot!")
        time.sleep(0.4)
        print()


    # RNG to come up with the computer's play
    # p_comp_play are the possible plays the computer can make
    # comp_choice is the choice the computer goes with
    p_comp_play = ["rock", "paper", "scissors"]
    comp_choice = random.choice(p_comp_play) 

    if comp_choice == "rock":
        print("I chose " + rolla)
    elif comp_choice == "paper":
        print("I choose " + rollb)
    else:
        print("I choose " + rollc)
    

    def normal_logic():
        print("def normal_logic")
        # outcome logic for player chooing rock
        if player_input == "rock" and comp_choice == "paper":
            print("I win!")
            global comp_score   # need the globals because this stuff is in a class
            global player_score
            comp_score += 1
        elif player_input == "rock" and comp_choice == "scissors":
            print("I loose :(")
            player_score += 1

        # outcome logic for player choosing paper
        elif player_input == "paper" and comp_choice == "scissors":
            print("I win!")                             
            comp_score += 1
        elif player_input == "paper" and comp_choice == "rock":
            print("I loose :(")
            player_score += 1

        # outcome logic for player choosing scissors and tie
        elif player_input == "scissors" and comp_choice == "rock":
            print("I win!")
            comp_score += 1
        elif player_input == "scissors" and comp_choice == "paper":
            print("I loose :(")
            player_score += 1
            
        elif player_input == comp_choice:
            print(Fore.YELLOW + "It's a draw!")
            print("No points given")
    

    def rigged_logic():
        print("def rigged_logic")
        # p_comp_play_rigged is defined at the top of the code by the other options
        global comp_choice_rigged
        comp_choice_rigged = random.choice(p_comp_play_rigged) 


        # outcome logic for player chooing rock
        if player_input == "rock" and comp_choice_rigged == "paper":
            print("I win!")
            global comp_score   # need the globals because this stuff is in a class
            global player_score
            comp_score += 1
        elif player_input == "rock" and comp_choice_rigged == "scissors":
            print("I loose :(")
            player_score += 1

        # outcome logic for player choosing paper
        elif player_input == "paper" and comp_choice_rigged == "scissors":
            print("I win!")                             
            comp_score += 1
        elif player_input == "paper" and comp_choice_rigged == "rock":
            print("I loose :(")
            player_score += 1

        # outcome logic for player choosing scissors and tie
        elif player_input == "scissors" and comp_choice_rigged == "rock":
            print("I win!")
            comp_score += 1
        elif player_input == "scissors" and comp_choice_rigged == "paper":
            print("I loose :(")
            player_score += 1
            
        elif player_input == comp_choice_rigged:
            print(Fore.YELLOW + "It's a draw!")
            print("No points given")


    if enable_rig == False:
        normal_logic()
        print("norm logic")
    else:
        rigged_logic()
        print("rigged logic")


    # round end points display
    if player_score == 1:
        print()
        print("The player has: 1 point")    # this is so plural isnt a thing when the player or coputer has 1 point. tHe CoMpUtEr hAs 1 PoInT"s" 
    else:
        print()
        print("The player has: " + str(player_score) + " points")

    if comp_score == 1:
        print("The computer has: 1 point")
        print()
    else:
        print("The computer has: " + str(comp_score) + " points")
        print()


    def hist_comp_rigged():
        print("comp rigged hist")

        print("Player play history: ", end="")
        print(*player_history, sep = ", ")
        print("Computer play history: ", end="")    # this wont tell you much, its 100% random
        
        if comp_choice_rigged == "rock":
            comp_history.append(rolla)
            
        elif comp_choice_rigged == "paper":
            comp_history.append(rollb)

        else:
            comp_history.append(rollc)
        print(*comp_history, sep = ", ")

    def hist_comp():
        print("comp hist")

        print("Player play history: ", end="")
        print(*player_history, sep = ", ")
        print("Computer play history: ", end="")    # this wont tell you much, its 100% random

        if comp_choice == "rock":
            comp_history.append(rolla)

        elif comp_choice == "paper":
            comp_history.append(rollb)

        else:
            comp_history.append(rollc)
        print(*comp_history, sep = ", ")

    # determines what history to log
    if enable_rig == True:
        hist_comp_rigged()
    else:
        hist_comp()


    # game end display
    if player_score >= match_point:     
        print()                             
        print("You win :(")
        print("GG!")
        time.sleep(30)
        sys.exit()

    if comp_score >= match_point:   
        print()               
        print("I win the game :D")  
        print("GG!")
        time.sleep(30)
        sys.exit()