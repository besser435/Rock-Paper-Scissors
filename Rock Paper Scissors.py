def notes(): # This is so long stuff like this can be collapsed in the IDE
    '''
    RPS Game by Brandon Esser | Updated November 2021
    It looks bad, we know.

    Changes over 1.6:
    If debug flags are enabled, there is a message that
    tells the player what to roll in order to win. This means
    comp_choice is moved above player input, but its not like
    there is code to cheat off of that. (yet)

    Operation Astroid 2 doesnt display if debug flags
    are enabled true


    V1.8 should:
    add ability to enter a letter instead of the full word 

    add a way of replaying or going to menu when game ends

    Make an even more rigged version. Comp will always win
    '''




from colorama import init   # pip install colorama
init()
from colorama import Fore, Back, Style
init(autoreset=True)
import winsound         # broken, needs to be updated to PyGame. Thats done in IFT101 Project, just impliment it
import random           # update it so it grabs music file from cwd. also in IFT project
import time
import sys
import os

# the plays but with colors
rolla = Fore.GREEN + "rock"
rollb = Fore.BLUE + "paper"
rollc = Fore.RED + "scissors"



# change all the colors to the betters ones
print(Fore.LIGHTMAGENTA_EX + "Hello")   



# options
enable_debug_flags = 1  # its sad that this is even a thing
skip_rig_ask = 0        # disables rigging if this is enabled
cls_after_turn = 0      # clears the terminal after each turn
enable_music = 1        # no idea how to make it more quiet
rickroll_professor = 0
enable_asteroid = 1
match_point = 3


# storage
player_score = 0
comp_score = 0
enable_rig = 0          # this is reduntant since you can just read the input,
player_history = []     # but this way you can do certain things with it
comp_history = []


print(Fore.BLUE + Back.YELLOW + "Rock Paper Scissors by Brandon | V1.7 | November 2021")
print("First to " + str(match_point) + " points wins!")


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


if enable_music == True:                # add to arcade game instead of just this
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


class match_fixing():
    # added this feature just to practice. in reality its useless and a waste of time
    if skip_rig_ask == True:
        if enable_debug_flags == True: print("                          skip_rig_ask = " + str(skip_rig_ask))

    else:
        global enable_rig   # took me 20 minutes to figure out where this needed to go haha :sad:
        ask_for_rig = input("would you like to rig the game? y/n ")
        # Yes, I know the player can just guess paper and win if enabled
        if ask_for_rig == "y":       
            enable_rig = True
            Operation_Astroid2()
        else:
            enable_rig = False


def game():
    if enable_debug_flags == True: print("Game is rigged: " + str(enable_rig))
    while True:
        print()
        print(Fore.CYAN + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if enable_debug_flags == True: print("Current directory: " + os.getcwd())   # music thing

        class rng():
            if enable_rig == False: 
                global comp_choice
                p_comp_play = ["rock", "paper", "scissors"] 
                comp_choice = random.choice(p_comp_play)
                if enable_debug_flags == True: print("                      rng normal")
                
            elif enable_rig == True:
                p_comp_play_rigged = ["rock", "rock", "rock", "paper", "scissors"] 
                comp_choice = random.choice(p_comp_play_rigged)
                if enable_debug_flags == True: print("                      rng rigged")


            if enable_debug_flags == True:
                print("                      comp_choice = " + comp_choice)
                if comp_choice == "rock": print("                      Roll Paper")
                if comp_choice == "paper": print("                      Roll Scissors")
                if comp_choice == "scissors": print("                      Roll Rock")


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
                print(Fore.RED + "Not a valid answer dummy!")
                game()

    
        class normal_logic():
            if enable_debug_flags == True: print("                      def main_logic")
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
        

        class hist_comp():
            if enable_debug_flags == True: print("                      def hist_comp")
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
    

        def menu():
            print()
            print("Would you like to:")
            print("1: Play again")
            print("2: Return to menu")
            print("3: Quit the program")


        def game_reset():   
            global player_score
            global comp_score
            global player_history
            global comp_history

            player_score = 0
            comp_score = 0
            comp_history.clear()
            player_history.clear()
            game()


        class scores():
            if player_score >= match_point:     
                print()                             
                print("You win :(")
                print("GG!")
                menu()
                ask_menu = input()
                if "1" in ask_menu:
                    game_reset()                                               
                elif "2" in ask_menu:
                    os.system("cls" if os.name == "nt" else "clear")     # IFT Project specific code. Returns to main menu in arcade game
                    #main_menu()                                          # comment this out if needed. 
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
                elif "2" in ask_menu:
                    os.system("cls" if os.name == "nt" else "clear")     # IFT Project specific code. Returns to main menu in arcade game
                    #main_menu()                                          # comment this out if needed. 
                else:
                    print("Goodbye")
                    time.sleep(1)
                    sys.exit()
    

        if cls_after_turn == True:
            print()
            input("Press enter to continue ")
            os.system("cls" if os.name == "nt" else "clear")


game()

