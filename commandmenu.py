import time, random, math, cmd, textwrap, sys, os, time, gamemap1

WIDTH = 800 # window size
HEIGHT = 800

# title screen
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()
            
def title_screen():
    os.system('clear')
    print("############################")
    print("#######Space Adventure######")
    print("############################")
    print("           -Play-           ")
    print("           -Help-           ")
    print("           -Quit-           ")
    title_screen_selections()
    
def help_menu():
    print("############################")
    print("#######Space Adventure######")
    print("############################")
    print("   Use up, down, left, right to move ")
    print("  avoid dangers such as oil splats and energy balls  ")
    print("        Good luck   ")
    title_screen_selections()
    
def start_game():
    print('gamemap1')


    
