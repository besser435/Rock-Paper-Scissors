
# Code that doesnt do something related is seperated by two blank lines
# Related code is seperated by one blank line


"""
V1.4.1 (1.4 but re-written to fix bugs) Changelog:
Added history. it displays past player and computer plays
Added classes to the longer things for organization
Made match point a single variable so it just has to be changed once rather than everywhere its used
Cleaned up formatting to how it should be in Python
"I choose:" for the computer is now in color


V1.5 (IFT101 Version) should:

merge rigged version to main
add ability to enter a letter instead of the full word
Upload project to GitHub with past versions
add proper way of asking again for input if its invalid
add sounds and background music, add option to enable/disable it

make it create a useless log file because why not
"""


from colorama import init   # pip install colorama
init()
from colorama import Fore, Back, Style
init(autoreset=True)

import random
import time
import sys


rolla = Fore.GREEN + "rock"     # need to referance a variable. some things
rollb = Fore.BLUE + "paper"     # dont allow adding the color part
rollc = Fore.RED + "scissors"


player_score = 0
comp_score = 0
match_point = 3
player_history = []
comp_history = []


print(Fore.BLUE + Back.YELLOW + "Rock Paper Scissors by Brandon (V1.4.1, Updated October 2021)")
print("First to " + str(match_point) + " points wins!")

    
while True:  # game logic
    print()
    print(Fore.CYAN + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    

    class player_entry():
        # User inputs their play here
        global player_input

        print("Enter " + rolla + ", " + rollb + ", " + Fore.RESET + "or " + rollc)
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
    

    class logic():
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


    # prints game history
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