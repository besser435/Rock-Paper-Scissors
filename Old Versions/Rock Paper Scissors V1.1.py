#Code that doesnt do something related is seperated by two blank lines
#Related code is seperated by one blank lines


from colorama import init
init()
from colorama import Fore, Back, Style
init(autoreset=True)

import random
import time


#bad-ish way of doing it, but the first way i tried broke the win/loose/draw statement
rolla = Fore.GREEN + 'rock'
rollb = Fore.BLUE + 'paper'
rollc = Fore.RED + 'scissors'


playerScore = 0
compScore = 0


print(Fore.BLUE + Back.YELLOW + 'Rock Paper Scissors by Brandon (V1.1, Updated August 2021)')
print('first to 5 points wins!')

    
while True:  #part of the check if the player want to keep playing
    print(Fore.CYAN + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
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
        print(Fore.RED + 'Not a valid answer dummy! Restart the program.')    #im too lazy to figure out how to restart it without closing the program
        time.sleep(90000)
        break


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
        print('I win!')                             #probably a better way of checking who wins but this works and is easy to read
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
    print()
    print("The player has: " + str(playerScore) + " points")

    print("The computer has: " + str(compScore) + " points")


    #game end display
    if playerScore>=5:                                  
        print('The player wins the game! (Restart program)')
        print()
        print('Thanks for playing!')
        time.sleep(120)
        break

        

    if compScore>=5:                  
        print('The computer wins wins the game!')  
        print() 
        print('Thanks for playing! (Restart program)')
        time.sleep(120)
        break