#Rock Paper Scissors by Brandon Esser
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


print(Fore.BLUE + 'Rock Paper Scissors by Brandon (V1, Updated August 2021)')

    
while True:  #precursor to check if the player wants to play again
    print(Fore.CYAN + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print()
    


    #User imputs their play here
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
        print(Fore.RED + 'Not a valid answer dummy! Restart this program.')
        time.sleep(90000)
        break

    #roll message
    print()
    print(rolla)
    time.sleep(0.5)
    print(rollb)
    time.sleep(0.5)
    print(rollc)
    time.sleep(0.5)
    print('shoot!')
    print()

    #RNG to come up with the computer's play
    #pcompPlay means possible plays the computer can make
    #compvs is the choice the computer goes with
    pcompPlay = [rolla, rollb, rollc]
    compChoice = random.choice(pcompPlay) 
    print('I choose ' + compChoice)

    #outcome logic for player chooing rock
    
    
    if playerInput == 'rock' and compChoice == rolla:
        print("It's a draw!")
    elif playerInput == 'rock' and compChoice == rollb:
        print('I win!')
    elif playerInput == 'rock' and compChoice == rollc:
        print('I loose :(')
    

    #outcome logic for player choosing paper
    elif playerInput == 'paper' and compChoice == rolla:
        print('I loose :(')
    elif playerInput == 'paper' and compChoice == rollb:
        print("It's a draw!")
    elif playerInput == 'paper' and compChoice == rollc:
        print('I win!')

    #outcome logic for player choosing scissors
    elif playerInput == 'scissors' and compChoice == rolla:
        print('I win!')
    elif playerInput == 'scissors' and compChoice == rollb:
        print('I loose :(')
    elif playerInput == 'scissors' and compChoice == rollc:
        print("It's a draw!")
        

    #checks if the player wants to re run the program
    print()
    again = input("play again? y/n ")
    if 'y' in again:
        continue 
    else:
        print(Fore.RED + 'Goodbye world!')
        time.sleep(1)
        break







