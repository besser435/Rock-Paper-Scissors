
#Code that doesnt do something related is seperated by two blank lines
#Related code is seperated by one blank line


'''
V1.3 Changelog:
Added a changelog
Figured out how to to kill the program automagically, so I added that in some places
Now if the player has 1 point it is not displayed in plural
'''


from colorama import init
init()
from colorama import Fore, Back, Style
init(autoreset=True)

import random
import time
import sys


#bad-ish way of doing it?, but the first way i tried broke everything
rolla = Fore.GREEN + 'rock'
rollb = Fore.BLUE + 'paper'
rollc = Fore.RED + 'scissors'


playerScore = 0
compScore = 0


print(Fore.BLUE + Back.YELLOW + 'Rock Paper Scissors by Brandon (V1.3, Updated September 2021)')
print('First to 3 points wins!')

    
while True:  # game logic
    print(Fore.CYAN + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print()


    #User inputs their play here
    print('Enter ' + rolla + ', ' + rollb + ', ' + Fore.RESET + 'or ' + rollc)
    playerInput = input()
    print()

    if playerInput == 'rock':
        print('You chose ' + rolla)
    elif playerInput == 'paper':
        print('You chose ' + rollb)
    elif playerInput == 'scissors':
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
    pcompPlay = ['rock', 'paper', 'scissors']
    compChoice = random.choice(pcompPlay) 
    print('I choose ' + compChoice)


    #outcome logic for player chooing rock
    if playerInput == 'rock' and compChoice == 'paper':
        print('I win!')
        compScore+=1
    elif playerInput == 'rock' and compChoice == 'scissors':
        print('I loose :(')
        playerScore+=1

    #outcome logic for player choosing paper
    elif playerInput == 'paper' and compChoice == 'scissors':
        print('I win!')                             
        compScore+=1
    elif playerInput == 'paper' and compChoice == 'rock':
        print('I loose :(')
        playerScore+=1

    #outcome logic for player choosing scissors
    elif playerInput == 'scissors' and compChoice == 'rock':
        print('I win!')
        compScore+=1
    elif playerInput == 'scissors' and compChoice == 'paper':
        print('I loose :(')
        playerScore+=1

    elif playerInput == compChoice:
        print(Fore.YELLOW + "It's a draw!")
        print('No points given')

   
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


    #game end display
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