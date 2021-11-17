class notes(): # This is so long stuff like this can be collapsed in the IDE
    '''
    RPS Game by Brandon Esser and Carter. V1.6.beta (IFT101 version) Updated October 2021
    It looks bad, we know.

    Changes over 1.5.1:
    WAY more organized. Everything is just in def or class (idk if its the right way)
    Removed HAL anomaly


    V1.7 should:
    add ability to enter a letter instead of the full word      why wont this f*^&%*g work oh god i need a PhD in CS for basic Python this line is way too long oh no oh god
    add proper way of asking for input again if it was invalid the first time (rather than nuking the entire game)
    add sounds and background music with option to enable/disable it
    Investigate Astroid2 glitch



    
    learned enough in this version, some stuff is broken
    im leaving it, look at the full release: V1.6

    
    '''

from colorama import init  # pip install colorama
init()
from colorama import Fore, Back, Style
init(autoreset=True)

import winsound
import random
import time
import sys
import os


# the plays but with colors
rolla = Fore.GREEN + "rock"
rollb = Fore.BLUE + "paper"
rollc = Fore.RED + "scissors"


# storage
player_score = 0
comp_score = 0
enable_rig = 0          # this is reduntant since you can just read
player_history = []     # the input, but this way you can hard code it
comp_history = []


# options
enable_debug_flags = 1  # its sad that this is even a thing
enable_music = 1       # no idea how to make it more quiet
enable_sounds = 1
rickroll_professor = 1
enable_asteroid = 1
match_point = 3
p_comp_play_rigged = ["rock", "rock", "paper", "scissors"] 
# Would have liked to enter a float that decides how heavy the fix is,
# but I have no idea how. brain too smooth


class intro():
    print(Fore.BLUE + Back.YELLOW + "Rock Paper Scissors by Brandon and Carter - V1.6.beta (IFT101), October 2021)")
    print("First to " + str(match_point) + " points wins!")

def Operation_Astroid2():
    random_astroid = random.randint(0, 12)
    if enable_asteroid == True and random_astroid == 0:
        print("Game is rigged: " + str(enable_rig))         # I was diagnosed with autism and this has
        time.sleep(0.5)                                     # more of it than I do somehow lmao
        print("is 12-25-27: True")                          # I know its inconsistant and innacurate, 
        time.sleep(1)                                       # but it just has to look interes- i mean this is real code
        print("loading phase 1...")
        time.sleep(0.2)
        print('"{//null.error.H2A4//"-ai[wrld_takeover]" does not exist}')
        time.sleep(0.05)
        print("retry.load.C4B8 [wakeup{global}]A9F13")
        time.sleep(0.05)
        print("int-attack(target = D.O.D.)")                # obtains luanch codes in case the Nueralink attack fails
        print("int-attack(target = Neuralink)")
        print("{//success.E4A8-play.sound @ Global Nueralink__evil_luagh_tuant__//int -ai[wrld_takeover]}") # goodbye cruel world!
        time.sleep(0.01)
        print("{issue master.cmd Neuralink.killall}")       # issues the government command for all Nueralink devices
        time.sleep(0.03)
        print('{//success.B7D1-Nueralink//int -ai-botnet["est. 8.3 bill eleminated"]}')   #    :) 
        print('{//global-clac.processing_power{issue "ON" for IoT}')
        time.sleep(0.1)
        print('//launch.rockets [count=all arg- s- lightspeed] galactic-payload[astroid 3(goal=spread)]')        
        time.sleep(0.1)
        print("Operation Astroid2 Complete.")               # I mean, can you really disagree? -Thanos
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")    # You saw nothing. You saw nothing. You saw nothing. You saw nothing. You saw nothing. You s

'''
class music():  # By Epic Mountain
    if enable_music == True:
        song_choice = random.randint(0, 0)
        os.chdir(r'C:\rpsSounds')       # no idea how else to play sounds. place rpsSounds folder here
        if song_choice == 0:
            winsound.PlaySound("TheEgg.wav", winsound.SND_ASYNC)            # add a few more songs
            print("Song playing: The Egg")
        elif song_choice == 1:                                              # also make it so game asks to play again so
            winsound.PlaySound("ClimateNuclear.wav", winsound.SND_ASYNC)    # you dont have to close the game; the music resets
            print("Song playing: Climate Nuclear")
        elif song_choice == 2:
            winsound.PlaySound("NuclearDeathToll.wav", winsound.SND_ASYNC)
            print("Song playing: Nuclear Death Toll")

    # You know the rules, and so do I
    if rickroll_professor == True:
        winsound.PlaySound("rsong.wav", winsound.SND_ASYNC)
        print("Song playing: Never Gonna Give You Up")
    # Never gonna let you down
'''

class match_fixing():
    # added this feature just to practice. in reality its useless and a waste of time
    ask_for_rig = input("would you like to rig the game in my favor? y/n ")
    # Yes, I know the player can just guess paper and win if enabled
    if ask_for_rig == "y":     
        global enable_rig     
        enable_rig = True
        Operation_Astroid2()
        print("Game is rigged: " + str(enable_rig))
    else:
        enable_rig = False
        print("Game is rigged: " + str(enable_rig))


while True:
    print("Game is rigged: " + str(enable_rig))
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

        # roll message thing
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
        

    def normal_logic():
        if enable_debug_flags == True: print("                         def normal_logic")
        global comp_score   # need the globals because this stuff is in a def dohickey; i think
        global player_score
        global comp_choice

        # comp_choice is the choice the computer goes with
        p_comp_play = ["rock", "paper", "scissors"]
        comp_choice = random.choice(p_comp_play)  
        if comp_choice == "rock":
            print("I chose " + rolla)
        elif comp_choice == "paper":
            print("I choose " + rollb)
        else:
            print("I choose " + rollc)

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

    # I dont know if there is a better way to do this, but it works™
    def rigged_logic():
        if enable_debug_flags == True: print("                         def rigged_logic")
        global comp_choice_rigged   # I dont know why this fixes comp_hist_rigged, but it does
        #global enable_rig           # took me 2 hours to figure out I needed this
        global comp_score
        global player_score

        # p_comp_play_rigged is defined at the top of the code by the other options
        comp_choice_rigged = random.choice(p_comp_play_rigged) 
        if comp_choice_rigged == "rock":
            print("I chose " + rolla)
        elif comp_choice_rigged == "paper":
            print("I choose " + rollb)
        else:
            print("I choose " + rollc)
            
        # outcome logic for player chooing rock
        if player_input == "rock" and comp_choice_rigged == "paper":
            print("I win!")
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
    

    if enable_rig == False: # ooga booga (very descriptive comment i know)
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
        print("Computer play history: ", end="")    # this wont tell you much, its 50% rigged on top of RNG

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
    
    
    if enable_rig == False: # this does the same thing as the code above but ehhhhhhh       
        hist_comp()         # it wouldnt work any other way
    else:
        hist_comp_rigged()
    

    class final_points():
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
    