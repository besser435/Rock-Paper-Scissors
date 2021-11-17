#Code that doesnt do something related is seperated by two blank lines
#Related code is seperated by one blank line

'''
V2 beta Changelog:
Abandoned V1. This is because there was too many flaws with how it was written. This time I will
gradually take the terminal based features and add a GUI to them. This code started off as RPS V1.3 no GUI.
Removed Colorama stuff from no GUI v1.3 to make adding a GUI more simple.
'''

from tkinter import *
root = Tk()
from tkinter import messagebox
import tkinter.font as font

import random   
import time
import sys


#bad-ish way of doing it?, but the first way i tried broke the win/loose/draw statement
rolla = 'rock'
rollb = 'paper'
rollc = 'scissors'


print('Rock Paper Scissors with GUI by Brandon (V2 beta, Updated September 2021)')
print('First to 3 points wins!')


player_score = 0
comp_score = 0 


while True:  #part of the check if the player want to keep playing
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print()
    # window setup
    root.title("Rock Paper Scissors Game")
    root.geometry("650x600")
    root["bg"] = "gray15"
    lbl = Label(root, text = "Rock, paper, or scissors? ")
    lbl.grid(padx=20)

    # references
    buttonFont = font.Font(family='Comic Sans MS', size=15,) # button text properties

                                 # ORDER: BUTTONS > ENTRY_THING > ROUND_WIN_THING
    def entry_rock():
        if comp_choice == "rock":
            round_win_tie()
            
        elif comp_choice == "paper":
            round_win_comp()
            
        elif comp_choice == "scissors":
            round_win_player()
            

    def entry_paper():
        if comp_choice == "rock":
            round_win_player()
        elif comp_choice == "paper":
            round_win_tie()
        elif comp_choice == "scissors":
            round_win_comp()

    def entry_scissors():
        if comp_choice == "rock":
            round_win_comp()
        elif comp_choice == "paper":
            round_win_player()
        elif comp_choice == "scissors":
            round_win_tie()
       
    pcompPlay = ['rock', 'paper', 'scissors']
    comp_choice = random.choice(pcompPlay) 
    print('I choose ' + comp_choice)
    re_roll = print("debug")
    class dark_mode_buttons():  #regular buttons. will fall to light_mode if light mode is enabled in the options menu
        root["bg"] = "gray15"
        btn_r = Button(root, text = "Rock",
            fg = "lawn green", command=entry_rock, bg="gray60", height=1, width=10, font=buttonFont)
        btn_r.grid(column=1, row=0)

        btn_p = Button(root, text = "Paper",
            fg = "ghost white", command=entry_paper, bg="gray60", height=1, width=10, font=buttonFont)
        btn_p.grid(column=2, row=0)

        btn_s = Button(root, text = "Scissors",
            fg = "firebrick1", command=entry_scissors, bg="gray60",height=1, width=10, font=buttonFont)
        btn_s.grid(column=3, row=0)

        btn_p = Button(root, text = "Re Roll",
            fg = "blue", command=re_roll, bg="gray60", height=1, width=10, font=buttonFont)
        btn_p.grid(column=1, row=1)    
    if __name__ == "__main__": # this makes it so dark_mode is ran my default when the code starts.
        dark_mode_buttons()   

        # round win logic
    def round_win_comp():  # good excersize for using def and class. update old code with it?
        print("I win :D")
        global comp_score
        comp_score += 1
        lbl = Label(root, text = "I win!")
        lbl.grid()
        lbl = Label(root, text = "I chose " + comp_choice)
        lbl.grid()

    def round_win_player():
        print("You win :(")
        global player_score
        player_score += 1
        lbl = Label(root, text = "You win :(")
        lbl.grid()
        lbl = Label(root, text = "I chose " + comp_choice)
        lbl.grid()
        
    def round_win_tie():
        print("It's a tie!")
        lbl = Label(root, text = "It's a tie!")
        lbl.grid()
        lbl = Label(root, text = "I chose " + comp_choice)
        lbl.grid()
    
    # User inputs their play here
    print("Enter rock, paper, or scissors")
    playerInput = input()
    print()

    # old player input
    if playerInput == 'rock':
        print('You chose ' + rolla)
    elif playerInput == 'paper':
        print('You chose ' + rollb)
    elif playerInput == 'scissors':
        print('You chose ' + rollc)
    else:
        print("Not a valid answer dummy! Restarting the program...")    #im too lazy to figure out how to restart it without closing the program
        time.sleep(4)
        sys.exit()


    #RNG to come up with the computer's play
    #pcompPlay means possible plays the computer can make
    #compvs is the choice the computer goes with


    #outcome logic for player chooing rock
    if playerInput == 'rock' and comp_choice == 'paper':
        print('I win!')
        comp_score+=1
    elif playerInput == 'rock' and comp_choice == 'scissors':
        print('I loose :(')
        player_score+=1

    #outcome logic for player choosing paper
    elif playerInput == 'paper' and comp_choice == 'scissors':
        print('I win!')                             
        comp_score+=1
    elif playerInput == 'paper' and comp_choice == 'rock':
        print('I loose :(')
        player_score+=1

    #outcome logic for player choosing scissors
    elif playerInput == 'scissors' and comp_choice == 'rock':
        print('I win!')
        comp_score+=1
    elif playerInput == 'scissors' and comp_choice == 'paper':
        print('I loose :(')
        player_score+=1

    elif playerInput == comp_choice:
        print("It's a draw!")
        print('No points given')

   
    #round end points display
    if player_score == 1:
        print()
        print("The player has: 1 point")    # this is so plural isnt a thing when the player or coputer has 1 point. tHe CoMpUtEr hAs 1 PoInT"s"
    else:
        print()
        print("The player has: " + str(player_score) + " points")

    if comp_score == 1:
        print()
        print("The computer has: 1 point")
    else:
        print()
        print("The computer has: " + str(comp_score) + " points")


    # old game end display
    if player_score>=3:                                  
        print("You win :(")
        print()
        print("Thanks for playing! (Closing in 30 seconds)")
        time.sleep(30)
        sys.exit()

    if comp_score>=3:                  
        print("I win the game :D")  
        print() 
        print("Thanks for playing! (Closing in 30 seconds)")
        time.sleep(30)
        sys.exit()

    root.mainloop()
    # new game end display
    again = input("run again? y/n ")
    if 'y' in again:
        continue   
    else:
        print("Goodbye")
        time.sleep(1)
        break


      
