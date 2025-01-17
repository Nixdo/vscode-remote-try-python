#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import os
import time
import random

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

os.system('clear')
def menu():
    print("Welcome to Rock, Paper, Scissors!\n")
    print("1. Play Game")
    print("0. Exit")

def GM_menu():
    print("SELECT GAME MODE:")
    print("1. Best of 3")
    print("2. Best of 5")
    print("3. Best of 7")
    print("4. Best of 9")
    print("5. Back to Main Menu")

def game_info():
    
    for n in range(3, 0, -1):
        print("NEXT ROUND STARTS IN: " + str(n))
        time.sleep(1)
        os.system('clear')

def game_actions():

    print("Please enter your move: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit\n")

def RPS_Game(g_mode):
    
    p1_marker = 0
    p2_marker = 0

    for n in range(g_mode):
        
        os.system('clear')

        print("Best of " + str(g_mode))
        print("\n" + player_1 + " V.S. " + player_2)
        print("\nRound " + str(n))
        game_actions()
        choice_p1 = int(input(player_1 + "! Enter your choice: "))
        os.system('clear')

        print("Best of " + str(g_mode))
        print("\n" + player_1 + " V.S. " + player_2)
        print("\nRound " + str(n))
        game_actions()
        ## Enable this line to play against the computer
        choice_p2 = random.randint(1, 3)
        ## Enable this line to play against another 'human' player
        #choice_p2 = int(input(player_2 + "! Enter your choice: "))
        os.system('clear')

        if choice_p1 == 1 and choice_p2 == 1:
            print("It's a draw!")
            time.sleep(2)
            game_info()
            p1_marker = p1_marker + 1
            p2_marker = p2_marker + 1
        elif choice_p1 == 1 and choice_p2 == 2:
            print(player_2 + " wins!")
            time.sleep(2)
            game_info()
            p2_marker = p2_marker + 1
        elif choice_p1 == 1 and choice_p2 == 3:
            print(player_1 + " wins!")
            time.sleep(2)
            game_info()
            p1_marker = p1_marker + 1
        elif choice_p1 == 2 and choice_p2 == 1:
            print(player_1 + " wins!")
            time.sleep(2)
            game_info()
            p1_marker = p1_marker + 1
        elif choice_p1 == 2 and choice_p2 == 2:
            print("It's a draw!")
            time.sleep(2)
            game_info()
            p1_marker = p1_marker + 1
            p2_marker = p2_marker + 1
        elif choice_p1 == 2 and choice_p2 == 3:
            print(player_2 + " wins!")
            time.sleep(2)
            game_info()
            p2_marker = p2_marker + 1
        elif choice_p1 == 3 and choice_p2 == 1:
            print(player_2 + " wins!")
            time.sleep(2)
            game_info()
            p2_marker = p2_marker + 1
        elif choice_p1 == 3 and choice_p2 == 2:
            print(player_1 + " wins!")
            time.sleep(2)
            game_info()
        elif choice_p1 == 3 and choice_p2 == 3:
            print("It's a draw!")
            time.sleep(2)
            game_info()
            p1_marker = p1_marker + 1
            p2_marker = p2_marker + 1
        elif choice_p1 == 4 and choice_p2 == 4:
            print("Bye Bye!")
        else:
            print("Invalid option")

    os.system('clear')
    print("Final Score:")
    print(player_1 + ": " + str(p1_marker), end="\n")
    print(player_2 + ": " + str(p2_marker))
    print()
    if p1_marker > p2_marker:
        print(player_1 + " WINS THE GAME!")
    elif p1_marker < p2_marker:
        print(player_2 + " WINS THE GAME!")
    elif p1_marker == p2_marker:
        print("It's a draw!\nNO ONE WINS THE GAME!")
    input("\nPress Enter to continue...")
    os.system('clear')

menu()
option = int(input("Enter option: "))

while option != 0:

    if option == 1:
        os.system('clear')
        player_1 = input("Player 1, please enter your name: ")
        player_2 = input("Player 2, please enter your name: ")
        os.system('clear')
        GM_menu()
        GM_option = int(input("Enter Game Mode: "))
        os.system('clear')

        while GM_option != 5:
            if GM_option == 1:
                RPS_Game(3)
            elif GM_option == 2:
                RPS_Game(5)
            elif GM_option == 3:
                RPS_Game(7)
            elif GM_option == 4:
                RPS_Game(9)
            elif GM_option == 5:
                os.system('clear')
                print("Back to Main Menu")
            else:
                os.system('clear')
                print("Invalid option")
            print()
            GM_menu()
            GM_option = int(input("Enter Game Mode: "))

    else:
        print("Invalid option")

    os.system('clear')
    print()
    menu()
    option = int(input("Enter option: "))

os.system('clear')
print("Bye Bye!")