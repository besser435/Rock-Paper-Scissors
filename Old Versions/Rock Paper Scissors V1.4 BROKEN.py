# RPS by besser, v1.4 - 10-13-2021
# Code that doesnt do something related is seperated by two blank lines
# Related code is seperated by one blank line


'''
V1.4 Changelog:
Added history. it displays past player and computer plays
Added classes to the longer things for organization
Can enter just r instead of rock, same for others ~~~~~~~~~~~THIS HAS BUGS FIX IT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Made match point a single variable so it just has to be changed once rather than everywhere its used
Cleaned up formatting to how it should be in Python
Uploaded project to GitHub (past versions available, but I'm just adding it now)
'''




'''Many bugs, version abandoned. next version is v1.4.1'''




from colorama import init
init()
from colorama import Fore, Back, Style
init(autoreset=True)

import random
import time
import sys


rolla = Fore.GREEN + "rock"
rollb = Fore.BLUE + "paper"
rollc = Fore.RED + "scissors"

player_score = 0
comp_score = 0
match_point = 3
current_pp = 0
player_history = []
comp_history = []


print(Fore.BLUE + Back.YELLOW + "Rock Paper Scissors by Brandon (V1.4, Updated October 2021)")
print("First to " + str(match_point) +  " points wins!")

 
while True:  # game logic
    print(Fore.CYAN + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()


    # User inputs their play here
    print("Enter " + rolla + ", " + rollb + ", " + Fore.RESET + "or " + rollc)
    player_input = input()
    print()


    if player_input == "rock" or "r":
        print("You chose " + rolla)

    elif player_input == "paper":
        print("You chose " + rollb)

    elif player_input == "scissors":
        print("You chose " + rollc)

    else:
        print(Fore.RED + "Not a valid answer dummy! Restart the program")  # im too lazy to figure out how to restart it without closing the program
        time.sleep(4)
        sys.exit()
    

    class roll_msg():
        print()
        print(rolla)
        time.sleep(0.3)
        print(rollb)
        time.sleep(0.3)
        print(rollc)
        time.sleep(0.3)
        print("shoot!")
        time.sleep(0.5)
        print()


    # RNG to come up with the computer's play
    # p_comp_Play means possible plays the computer can make
    # comp_choice is the choice the computer goes with
    p_comp_play = ["rock", "paper", "scissors"]
    comp_choice = random.choice(p_comp_play) 
    print("I choose " + comp_choice)


    class logc():
        # outcome logic for player chooing rock
        if player_input == "rock" and comp_choice == "paper":
            print("I win!")
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
        print("The player has: 1 point")  # this is so plural isnt a thing when the player or coputer has 1 point. tHe CoMpUtEr hAs 1 PoInT"s"
    else:
        print()
        print("The player has: " + str(player_score) + " points")

    if comp_score == 1:
        print()
        print("The computer has: 1 point")
    else:
        print("The computer has: " + str(comp_score) + " points")
        print()


    # prints game history
    class history_logic():
        print("Player play history:  ", end="")
        player_history.append(player_input)
        print(*player_history, sep = ", ")

        print("Computer play history (this wont tell you much, its 100% random): ", end="")
        comp_history.append(comp_choice)
        print(*comp_history, sep = ", ")

    # game end display
    if player_score >= match_point:                                  
        print("You win the game :(")
        print("GG! (Closing in 30 seconds)")
        time.sleep(30)
        sys.exit()

    if comp_score >= match_point:                  
        print("I win the game :D") 
        print("Thanks for playing! (Closing in 30 seconds)")
        time.sleep(30)
        sys.exit()