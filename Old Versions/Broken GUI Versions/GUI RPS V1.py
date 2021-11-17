'''
Brandon's RPS game modified for a gooey (GUI for you dummies)
I may or may not have "borrowed" snippets of some code I found online

Code that is part of a different system is seperated by two blank lines
Related code is seperated by one blank line


Changelog:
First version
'''


# resources needed
from tkinter import *
root = Tk()
from tkinter import messagebox
import tkinter.font as font

import random
import time
import sys

player_score = 0
comp_score = 0



while True:
    # window setup
    root.title("Rock Paper Scissors Game")
    root.geometry("650x600")
    root["bg"] = "gray15"
    lbl = Label(root, text = "Rock, paper, or scissors? ")
    lbl.grid(padx=20)

    # score display
    if player_score == 1:
        print("The player has: 1 point")    # this is so plural isnt a thing when the player or coputer has 1 point. tHe CoMpUtEr hAs 1 PoInT"s"
    else:
        print("The player has: " + str(player_score) + " points")

    if comp_score == 1:
        print("The computer has: 1 point")
    else:
        print("The computer has: " + str(comp_score) + " points")
 

    p_comp_play = ["rock", "paper", "scissors"]
    comp_choice = random.choice(p_comp_play)


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


    # game settings and menus
    def reset_game():
        print()

    def how_to_play():
        print("seriously?!?!")
        how_toPlay_msgbox = messagebox.askquestion("askyesno", "Are you serious?!?!")
        if how_toPlay_msgbox == "yes":
            sys.exit()
        elif how_toPlay_msgbox == "no":
            print("Good.")

    def about_me():
        print('Im a bad software "dev" who only knows print commands and if statements in python lol')

    def flashbang():
        print('helo')
        win= Tk()
        new= Toplevel(win)
        new.geometry("7680x4320") # 8K because why not. but by doing this the whole screen is flled with white
        new.title("I did warn you")
        #Create a Label in New window
        Label(new, text="Get flashbanged lol", font=('Tahoma 17 bold')).pack(pady=30)


    # buttons
    buttonFont = font.Font(family='Comic Sans MS', size=15,) # button text properties
        
    def dark_mode():  #regular buttons. will fall to light_mode if light mode is enabled in the options menu
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
        
    if __name__ == "__main__": # this makes it so dark_mode is ran my default when the code starts.
        dark_mode()

    def light_mode():   # if user selects light mode this will change window and buttons to light
        light_mode_other()
        root["bg"] = "#F0F0F0"
        btn_r = Button(root, text = "Rock",
            fg = "green2", command=entry_rock, bg="white", height=1, width=10, font=buttonFont)
        btn_r.grid(column=1, row=0)

        btn_p = Button(root, text = "Paper",
            fg = "black", command=entry_paper, bg="white", height=1, width=10, font=buttonFont)
        btn_p.grid(column=2, row=0)

        btn_s = Button(root, text = "Scissors",
            fg = "firebrick1", command=entry_scissors, bg="white",height=1, width=10, font=buttonFont)      
        btn_s.grid(column=3, row=0)


    def light_mode_other(): # other stuff to be exectued when light mode is enabled
        print("light_mode_enabled")
        darksavemenu = Menu(menu)
        darksavemenu = Menu(menu, tearoff = 0)
        menu.add_cascade(label="GO BACK TO DARK MODE", menu=darksavemenu)
        darksavemenu.add_command(label="MY EYES OH GOD", command=dark_mode)


    # menu options
    menu = Menu(root)
    root.config(menu=menu)

    optionmenu = Menu(menu)
    optionmenu = Menu(menu, tearoff = 0)
    menu.add_cascade(label="Options", menu=optionmenu)
    optionmenu.add_command(label="Light Mode (Seriously don't click this)", command=flashbang)
    optionmenu.add_command(label="Reset Game", command=reset_game)
    optionmenu.add_command(label="Other Light Mode", command=light_mode)


    helpmenu = Menu(menu)
    helpmenu = Menu(menu, tearoff = 0)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="How to Play", command=how_to_play)
    helpmenu.add_command(label="About Me (why are you interested?)", command=about_me)

    

    btn_rp = Button(root, text = "Reset",
            fg = "cyan", command=reset_game, bg="gray60",height=1, width=10, font=buttonFont)
    btn_rp.grid(column=2, row=1)




    again = input("run again? y/n ")
    if 'y' in again:
        continue   
    else:
        print("Goodbye")
        time.sleep(1)
        break


      
    root.mainloop() # Ends everything pretty much. code can run after window is closed, but it looses certain data