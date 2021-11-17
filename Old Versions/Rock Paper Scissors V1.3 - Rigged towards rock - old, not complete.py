
#Code that doesnt do something related is seperated by two blank lines
#Related code is seperated by one blank line


'''
This is a modified version of RPS V1.3 with 1.4 history
This game is rigged towards rock
You can enter a weight as a float and that will determine how often it rolls rock



rigged merged to main in V1.5



'''


from colorama import init
init()
from colorama import Fore, Back, Style
init(autoreset=True)

import random
import time
import sys


# bad-ish way of doing it?, but the first way i tried broke everything
rolla = Fore.GREEN + 'rock'
rollb = Fore.BLUE + 'paper'
rollc = Fore.RED + 'scissors'


playerScore = 0
compScore = 0
enable_rig = True   # not yet a thing rigged_weight = 0.5 # enter a value between 0 and 1
player_history = []
comp_history = []



print(Fore.BLUE + Back.YELLOW + 'Rock Paper Scissors by Brandon (V1.3, Updated September 2021)')
print('First to 3 points wins!')

    
while True:  # game logic
    print(Fore.CYAN + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print()


    #User inputs their play here
    print('Enter ' + rolla + ', ' + rollb + ', ' + Fore.RESET + 'or ' + rollc)
    player_input = input()
    print()

    if player_input == 'rock':
        print('You chose ' + rolla)
    elif player_input == 'paper':
        print('You chose ' + rollb)
    elif player_input == 'scissors':
        print('You chose ' + rollc)
    else:
        print(Fore.RED + "Not a valid answer dummy! Restarting the program...")    #im too lazy to figure out how to restart it without closing the program
        time.sleep(4)
        sys.exit()


    #roll message
    print()
    print(rolla)
    time.sleep(0.3)
    print(rollb)
    time.sleep(0.3)
    print(rollc)
    time.sleep(0.3)
    print('shoot!')
    print()


    #RNG to come up with the computer's play
    #pcompPlay means possible plays the computer can make
    #compvs is the choice the computer goes with
    if enable_rig == True:
        p_comp_play_r = ["rock", "rock", "paper", "scissors"]
        comp_choice_r = random.choice(p_comp_play_r)
        print("I choose " + comp_choice_r + " rig true")

    else:
        p_comp_play = ['rock', 'paper', 'scissors']
        comp_choice = random.choice(p_comp_play) 
        print('I choose ' + comp_choice)


    def rigged_logic():
        #outcome logic for player chooing rock
        if player_input == 'rock' and comp_choice_r == 'paper':
            print('I win!')
            global compScore
            compScore+=1
        elif player_input == 'rock' and comp_choice_r == 'scissors':
            print('I loose :(')
            global playerScore
            playerScore+=1

        #outcome logic for player choosing paper
        elif player_input == 'paper' and comp_choice_r == 'scissors':
            print('I win!')                             
            compScore+=1
        elif player_input == 'paper' and comp_choice_r == 'rock':
            print('I loose :(')
            playerScore+=1

        #outcome logic for player choosing scissors
        elif player_input == 'scissors' and comp_choice_r == 'rock':
            print('I win!')
            compScore+=1
        elif player_input == 'scissors' and comp_choice_r == 'paper':
            print('I loose :(')
            playerScore+=1

        elif player_input == comp_choice_r:
            print(Fore.YELLOW + "It's a draw!")
            print('No points given')
    
    def norm_logic():
        #outcome logic for player chooing rock
        if player_input == 'rock' and comp_choice == 'paper':
            print('I win!')
            global compScore
            compScore+=1
        elif player_input == 'rock' and comp_choice == 'scissors':
            print('I loose :(')
            global playerScore
            playerScore+=1

        #outcome logic for player choosing paper
        elif player_input == 'paper' and comp_choice == 'scissors':
            print('I win!')                             
            compScore+=1
        elif player_input == 'paper' and comp_choice == 'rock':
            print('I loose :(')
            playerScore+=1

        #outcome logic for player choosing scissors
        elif player_input == 'scissors' and comp_choice == 'rock':
            print('I win!')
            compScore+=1
        elif player_input == 'scissors' and comp_choice == 'paper':
            print('I loose :(')
            playerScore+=1

        elif player_input == comp_choice:
            print(Fore.YELLOW + "It's a draw!")
            print('No points given')


    if enable_rig == False:
        norm_logic()
    else:
        rigged_logic()

   
    #round end points display
    if playerScore == 1:
        print()
        print("The player has: 1 point")    # this is so plural isnt a thing when the player or coputer has 1 point. tHe CoMpUtEr hAs 1 PoInT"s"
    else:
        print()
        print("The player has: " + str(playerScore) + " points")

    if compScore == 1:
        print()
        print("The computer has: 1 point")
    else:
        print()
        print("The computer has: " + str(compScore) + " points")

    # prints game history
    class history_logic():
        print("Player play history:  ", end="")
        player_history.append(player_input)
        print(*player_history, sep = ", ")

        print("Computer play history (this wont tell you much, its 100% random): ", end="")
        comp_history.append(comp_choice)
        print(*comp_history, sep = ", ")

    # game end display
    if playerScore>=3:                                  
        print("You win :(")
        print()
        print("GG! (Closing in 30 seconds)")
        time.sleep(30)
        sys.exit()

    if compScore>=3:                  
        print("I win the game :D")  
        print() 
        print("Thanks for playing! (Closing in 30 seconds)")
        time.sleep(30)
        sys.exit()