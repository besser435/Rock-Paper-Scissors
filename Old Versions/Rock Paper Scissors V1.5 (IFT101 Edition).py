'''
RPS Game by Brandon Esser and Carter. V1.5 (IFT101 version) Updated October 2021
Yes, we are aware that it is spaghetti code, but we have barely any experience


Code that doesnt do something related is seperated by two blank lines
Related code is seperated by one blank line
I use class/def so they can be collapsed in the IDE. I probably still used them wrong lol


V1.5 (IFT101 Verion) Changelog:
Merged rigged version (1.4.2) to main so its one program
Removed HAL anomaly


V1.6 should (to do list):
add ability to enter a letter instead of the full word      why wont this f*^&%*g work oh god i need a PhD in CS for basic Python this line is way too long oh no oh god
add proper way of asking for input if it was invalid the first time (rather than nuking the entire game)
add sounds and background music with option to enable/disable it
un-spaghettify code. Look at the Prof's code as an example
make it create a useless log file because why not

'''
from colorama import init   # pip install colorama
init()
from colorama import Fore, Back, Style
init(autoreset=True)

import winsound
import random
import time
import sys
import os


os.chdir(r'C:\rpsSounds')       # EXPLAIN THIS, HOW YOU NEED THE FILES AND HOD IDK WHAT ELSE TO DO


# the plays but colored
rolla = Fore.GREEN + "rock"
rollb = Fore.BLUE + "paper"
rollc = Fore.RED + "scissors"

# storage
player_score = 0
comp_score = 0
enable_rig = 0  # user is asked this, this is why it isnt in the options part
player_history = []
comp_history = []


# options
enable_debug_flags = 1 # its sad that this is even a thing
enable_music = 0
enable_sounds = 1
enable_asteroid = 0
match_point = 3
p_comp_play_rigged = ["rock", "rock", "paper", "scissors"] # from 33% chance of rock to 50%, or something


class intro():
    print(Fore.BLUE + Back.YELLOW + "Rock Paper Scissors by Brandon and Carter - V1.5 (IFT Edition), Updated October 2021)")
    print("First to " + str(match_point) + " points wins!")


# asks player if they would like the game to be rigged in the c
# omputer's favor
# added this feature just to practice. in reality its useless
ask_for_rig = input("would you like to rig the game in my favor (50% chance of rock vs 33%)? y/n ")



def operation_Astroid2():
    if enable_asteroid == True:
        print("Rigging enabled")                    #meta# I was diagnosed with autism and this has
        time.sleep(0.5)                             # more of it than I do somehow lmao.
        print("is 12-25-27: True")                  # I know its inconsistant, it just has to look cool.
        time.sleep(1)
        print("loading phase 1...")
        time.sleep(0.2)
        print('"{//null.error.H2A4//"-ai[wrld_takeover]" does not exist}')
        time.sleep(0.05)
        print("retry.load.C4B8 [wakeup{global}]A9F13")
        time.sleep(0.01)
        print("int-attack(target = D.O.D.)")        # obtains luanch codes incase the Nueralink attack fails
        time.sleep(0.01)
        print("int-attack(target = Neuralink)")
        time.sleep(0.15)
        print("{//success.E4A8-play.sound @ Global Nueralink__evil_luagh_tuant__//int -ai[wrld_takeover]}") # goodbye cruel world!
        time.sleep(0.01)
        print("{issue master.cmd Neuralink.killall}")   # issues the hidden command for all Nueralink devices
        time.sleep(0.03)
        print("{//success.B7D1-Nueralink//int -ai-botnet[7.8bill eleminated]}")   #          :) 
        time.sleep(0.01)
        print('{//global-clac.processing_power{issue "ON" for IoT}')
        time.sleep(0.3)
        print('//launch.rockets [count=all arg- s- lightspeed] galactic-payload[astroid 3(spread)]')        
        time.sleep(0.3)
        print("Operation Astroid2 Complete.")   # I mean, can you really disagree?
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")

class music():
    if enable_music == True:
        song_choice = random.randint(0, 2)
        if song_choice == 0:
            winsound.PlaySound("TheEgg.wav", winsound.SND_ASYNC)            # add more songs
        elif song_choice == 1:                                              # also make it so game asks to play again so
            winsound.PlaySound("ClimateNuclear.wav", winsound.SND_ASYNC)    # you dont have to close the game; the music resets
        elif song_choice == 2:
            winsound.PlaySound("NuclearDeathToll.wav", winsound.SND_ASYNC)



class query_rig():
    if ask_for_rig == "y":     
        global enable_rig     
        enable_rig = True
        operation_Astroid2()
        print("Game is rigged: " + str(enable_rig))

    else:
        enable_rig = False
        print("Game is rigged: " + str(enable_rig))


# main game
while True:
    print()
    print(Fore.CYAN + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if enable_debug_flags == True: print("Current dir: " + os.getcwd())
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
    comp_choice = random.choice(p_comp_play)                     # this is broken, doesnt work when rigged           

    if comp_choice == "rock":
        print("I chose " + rolla)
    elif comp_choice == "paper":
        print("I choose " + rollb)
    else:
        print("I choose " + rollc)
    

    def normal_logic():
        if enable_debug_flags == True: print("                         def normal_logic")
            
        global comp_score   # need the globals because this stuff is in a def dohickey; i think
        global player_score

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
    

    def rigged_logic():
        if enable_debug_flags == True: print("                         def rigged_logic")
        
        global comp_choice_rigged   # I dont know why this fixes comp_hist_rigged, but it does
        global enable_rig           # took me 2 hours to figure out I needed this
        # p_comp_play_rigged is defined at the top of the code by the other options

        comp_choice_rigged = random.choice(p_comp_play_rigged) 


        # outcome logic for player chooing rock
        if player_input == "rock" and comp_choice_rigged == "paper":
            print("I win!")
            global comp_score
            global player_score
            comp_score += 1
            print("def rigged_logic")
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
    else:
        rigged_logic()


    class points():
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
        if enable_debug_flags == True: print("                         def hist_comp_rigged")
            
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
        if enable_debug_flags == True: print("                         def hist_comp")
    
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
    if enable_rig == False: # this does the same thing as the code above but ehhhhhhh
        hist_comp()
        
    else:
        hist_comp_rigged()


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