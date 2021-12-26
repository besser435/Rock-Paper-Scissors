def notes(): # This is so long stuff like this can be collapsed in the IDE
    '''
    RPS Game by Brandon Esser | Updated December 2021
    It looks bad, I know.


    This will probably be the final version. It doesn't really
    make sense to keep the Arcade version and this stand-alone
    version updated. The Arcade is more advanced and has a better
    framework, so I'll be sticking with that. 
    '''

version = "v1.8"

from colorama import init   # pip install colorama
init()
from colorama import Fore, Back, Style
init(autoreset=True)
import winsound         # broken, needs to be updated to PyGame. Thats done:tm: in the IFT101 Arcade Project, just impliment it
import random           # update it so it grabs music file from cwd. also in IFT project
import time
import sys
import os

# the plays but with colors
rolla = Fore.GREEN + "rock"
rollb = Fore.BLUE + "paper"
rollc = Fore.RED + "scissors"


# options
enable_debug_flags = 0  # its sad that this is even a thing
skip_rig_ask = 0        # disables rigging if this is enabled
cls_after_turn = 0      # clears the terminal after each turn
enable_music = 1        
rickroll_professor = 0
enable_asteroid = 1
match_point = 3


# storage
player_score = 0
comp_score = 0
enable_rig = 0
enable_super_rig = 0    # this is reduntant since you can just read the input,
player_history = []     # but this way you can do certain things with it
comp_history = []


print(Fore.BLUE + Back.YELLOW + "Rock Paper Scissors by Brandon | " + version + " | December 2021")
print("First to " + str(match_point) + " points wins!")


def cc():   # shortens long command to just cc()
    os.system("cls" if os.name == "nt" else "clear")


# Operation Astroid 2 is just a stupid easter egg. serves no purpose execpt to fuel my "creativity"
def Operation_Astroid2():
    if enable_debug_flags == True:
        pass
    else:
        random_astroid = random.randint(0, 12)                  # 1 in 13 chance (if the player rigs the game)
        if enable_asteroid == True and random_astroid == 0:
            print("Game is rigged: " + str(enable_rig))         # I was diagnosed with autism and this has
            time.sleep(0.5)                                     # more of it than I do somehow lmao
            print("is 12-25-27: True")                          # I know its inconsistant and innacurate, 
            time.sleep(1)                                       # but it just has to look interes- I mean this is real code
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
            print("{issue master.cmd Neuralink.killall}")       # issues the hidden command for all Nueralink devices
            time.sleep(0.03)
            print('{//success.B7D1-Nueralink// ["est. 8.3 bill eleminated"]}')   #    :) 
            print('{//global-calc.processing_power{issue "ON" for IoT}')    # I like obscene amounts of processing power
            time.sleep(0.1)
            print('//launch.rockets [count=all arg- s- lightspeed] galactic-payload[astroid 3(goal=spread)]')   #asteroid 3
            time.sleep(0.1)
            print("Operation Astroid2 Complete.")               # "I mean, can you really disagree?" -Thanos, probably
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")    # You saw nothing. You saw nothing. You saw nothing. You saw nothing. You s
            # teaching sand to think was a mistake


# change to pygame code, maybe axe it

"""if enable_music == True:                # add to arcade game instead of just this
    song_choice = random.randint(0, 2)  # Music by Epic Mountain, it doesnt fit the theme, but it works
    os.chdir(r'C:\arcadeMusic')           # no idea how else to play sounds. place rpsSounds folder here
    if song_choice == 0:
        winsound.PlaySound("TheEgg.wav", winsound.SND_ASYNC)            # compress files, they are dummy thicc right now
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

"""

class match_fixing:    
    # added this feature just to practice. in reality its useless and a waste of time
    # enable_rig = computer leans towards rock
    # enable_super_rig = computer always wins
    global enable_rig
    global enable_super_rig

    if skip_rig_ask == True:
        if enable_debug_flags == 1: print(Fore.YELLOW + "                          skip_rig_ask = " + str(skip_rig_ask))
    else:        
        ask_for_rig = input("Would you like to rig the game? y/n ")

        if ask_for_rig == "y":
            ask_for_super_rig = input("Would you like to super rig the game? y/n ")

            if "y" in ask_for_super_rig:
                enable_super_rig = 1
                print()
                print("Game is rigged: " + str(enable_rig))
                print("Game is super rigged: " + str(enable_super_rig))
                Operation_Astroid2()
            else: 
                enable_rig = 1
                print()
                print("Game is rigged: " + str(enable_rig))
                print("Game is super rigged: " + str(enable_super_rig))
                Operation_Astroid2()


def game():
    while True:
        print()
        print(Fore.CYAN + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if enable_debug_flags == True: print(Fore.YELLOW + "Current directory: " + os.getcwd())   # music thing

        # had issues with scopes earlier
        if enable_debug_flags == 1: print(Fore.YELLOW + "Game is rigged in def game(): " + str(enable_rig))
        if enable_debug_flags == 1: print(Fore.YELLOW + "Game is super rigged in def game(): " + str(enable_super_rig))
        

        class player_entry:
            # User inputs their play here
            print("Enter " + rolla + ", " + rollb + ", " + Fore.RESET + "or " + rollc)

            global player_input
            player_input = input()
            print()


        class rng():
            global comp_choice
            if enable_rig == True:
                p_comp_play_rigged = ["rock", "rock", "rock", "paper", "scissors"]
                comp_choice = random.choice(p_comp_play_rigged)
                if enable_debug_flags == 1: print(Fore.YELLOW + "                      rng rigged")

            elif enable_super_rig == True:
                if player_input == "rock":
                    comp_choice = "paper"

                elif player_input == "paper":
                    comp_choice = "scissors"
                
                elif player_input == "scissors":
                    comp_choice = "rock"
                if enable_debug_flags == 1: print(Fore.YELLOW + "                      rng super rigged")

            else:
                p_comp_play = ["rock", "paper", "scissors"]
                comp_choice = random.choice(p_comp_play)
                if enable_debug_flags == 1: print(Fore.YELLOW + "                      rng normal")


            # adds to player history
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
                print(Fore.RED + "Not a valid answer dummy!")
                game()

    
            # roll message thing
            if enable_debug_flags == False: # skips this while debugging crap
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


            if comp_choice == "rock":
                print("I chose " + rolla)
            elif comp_choice == "paper":
                print("I choose " + rollb)
            elif comp_choice == "scissors":
                print("I choose " + rollc)


        class normal_logic():
            if enable_debug_flags == 1: print(Fore.YELLOW + "                      def normal_logic")
            global comp_score   
            global player_score

            # outcome logic for player chooing rock
            if player_input == "rock" and comp_choice == "paper":
                print("I win!")
                comp_score += 1
            elif player_input == "rock" and comp_choice == "scissors":
                print("I loose :(")
                player_score += 1

            # paper
            elif player_input == "paper" and comp_choice == "scissors":
                print("I win!")                             
                comp_score += 1
            elif player_input == "paper" and comp_choice == "rock":
                print("I loose :(")
                player_score += 1

            # scissors and tie
            elif player_input == "scissors" and comp_choice == "rock":
                print("I win!")
                comp_score += 1
            elif player_input == "scissors" and comp_choice == "paper":
                print("I loose :(")
                player_score += 1
            elif player_input == comp_choice:
                print(Fore.YELLOW + "It's a draw!")
                print("No points given")


        class points():
            if player_score == 1:       # round end points display
                print()
                print("The player has: 1 point")    # tHe CoMpUtEr hAs 1 PoInT"s" 
            else:
                print()
                print("The player has: " + str(player_score) + " points")

            if comp_score == 1:
                print("The computer has: 1 point")
            else:
                print("The computer has: " + str(comp_score) + " points")
        

        class history:
            print("Player play history: ", end="")
            print(*player_history, sep = ", ")

            print("Computer play history: ", end="")    # this wont tell you much, its 100% random (until its not)

            if comp_choice == "rock":
                comp_history.append(rolla)
            elif comp_choice == "paper":
                comp_history.append(rollb)
            elif comp_choice == "scissors":
                comp_history.append(rollc)

            print(*comp_history, sep = ", ")


        def game_reset():   
            global player_score
            global comp_score
            global player_history
            global comp_history
            # could probably be done better
            player_score = 0
            comp_score = 0
            comp_history.clear()
            player_history.clear()  


        def menu():
            print()
            print("Would you like to:")
            print("1: Play again")
            print("2: Quit the program")


        class scores():
            if player_score >= match_point:     
                print()                             
                print("You win :(")
                print("GG!")
                menu()
                ask_menu = input()
                if "1" in ask_menu:
                    game_reset()                                               
                else:
                    print("Goodbye")
                    time.sleep(1)
                    sys.exit()


            if comp_score >= match_point:   
                print()               
                print("I win the game :D")  
                print("GG!")
                menu()
                ask_menu = input()
                if "1" in ask_menu:
                    game_reset()                                                 
                else:
                    print("Goodbye")
                    time.sleep(1)
                    sys.exit()
    

        if cls_after_turn == True:
            print()
            input("Press enter to continue ")
            cc()


game()

