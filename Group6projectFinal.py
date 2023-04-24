# This is the Three Game Group Project Reynol Garcia, Sherlly Paz, Vanji Moise

import random

choice = None

while choice != "":

    print(
        """
        Welcome to the Triple Game Simulator, You will be given the choice to play one of three different games which include Rock, Paper, Scissor, Tic-Tac-Toe, and Text Adventure. 
        If you do want to play then you may exit the program at any time. 
    
        0 - Exit program
        1 - Battleship
        2 - Text Adventure
        3 - Rock, Paper, Scissors
    
        """
    )

    choice = input("Choice: ")
    print()

    if choice == "0":
        print("You didn't have it in you!")
        break

    elif choice == "1":
        from random import randint

        # ship location unchanged
        HiddenBoard = [[" "] * 8 for x in range(8)]
        # loaction of player hits and misses
        GuessBoard = [[" "] * 8 for i in range(8)]
        # how the locations pair on board
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

        print(
            """
            Welcome to the Best War Game of our time: Battleship.  
            This will be a showdown between you solider and our AI mapping.  

            You will make your move known by entering a number and letter, 0 - 8 and A - H.  The number and letter
            will correspond to the board position as illustrated:
                             A B C D E F G H
                            1| | | | | | | | |
                            2| | | | | | | | |
                            3| | | | | | | | |
                            4| | | | | | | | |
                            5| | | | | | | | |
                            6| | | | | | | | |
                            7| | | | | | | | |
                            8| | | | | | | | |

            Prepare yourself, solider. The ultimate battle is about to begin.\n
            """)


        def print_board(board):
            print("  A B C D E F G H")

            row_number = 1
            for row in board:
                # each row created need to be seprated
                print("%d|%s|" % (row_number, "|".join(row)))
                row_number += 1


        # computers random ship location
        def create_ship(board):
            for ship in range(6):
                ship_row, ship_column = randint(0, 7), randint(0, 7)
                while board[ship_row][ship_column] == "X":
                    ship_row, ship_column = get_ship_location()
                board[ship_row][ship_column] = "X"


        # hit and miss board
        def get_ship_location():
            row = input("Select a ship location 1 to 8: ")
            while row not in "12345678":
                print("Please select a correct row between 1 and 8")
                row = input("Select a ship location 1 to 8: ")
            column = input("Select a ship location A to H: ").upper()
            while column not in "ABCDEFGH":
                print("Please select correct row between A to H")
                column = input("Select a ship location A to H: ").upper()
            # -1 bc of indexs didnt print right before
            return int(row) - 1, letters_to_numbers[column]


        # tracking the hit ships
        def count_hits(board):
            count = 0
            for row in board:
                for column in row:
                    if column == "X":
                        count += 1
            return count


        create_ship(HiddenBoard)
        turns = 10
        while turns > 0:
            print("\nWelcome to Battleships!!!")
            print_board(GuessBoard)
            row, column = get_ship_location()
            if GuessBoard[row][column] == "-":
                print("You already hit that solider try a different spot")
            elif HiddenBoard[row][column] == "X":
                print("Great shot solider you got a battleship")
                GuessBoard[row][column] = "X"
                turns -= 1
            else:
                print("Solide you just missed, next time aim")
                GuessBoard[row][column] = "-"
                turns -= 1
            if count_hits(GuessBoard) == 5:
                print("Great shooting solider you sunk all the battleships")
                break
            print("You only have", turns, "shots remaining.")
            if turns == 0:
                print("Sorry solider you used up all your ammo, better luck next time")
                break

    elif choice == "2":
        print("""WELCOME TO THE ADVENTURE GAME! let's start the action

               Ivett spends the night at friend's house for a sleepover at the middle of the night. She wake up
               by herself in the room,let's find out what's going on""")


        def playGame():
            print("""WELCOME TO THE ADVENTURE GAME! let's start the action

               Ivett spends the night at her friend's house for a sleepover. at the middle of the night. She wake up
               by herself in the room, let's find out what's going on""")


        stillplaying = True
        while stillplaying:
            choice = input(" Ivett leaves the room, and checks the room of her parents friend , "
                           "you want to knock the door? (y/n) ")
            if choice == "y":
                print(
                    "when she knocks on the door, the door opens slowly as she is so scared! There is no one there when"
                    "she looks through the door.")
                choice = input("1: Go down stairs to the kitchen to find out was going on? \n2: "
                               "Just go back to sleep hopping tomorrow everything would be okay.. ")
                if choice == "1":
                    print(
                        "she spotted an elderly woman racing from the kitchen to the living room as she descended the stairs \n")
                    print(
                        "When she realized she was still trying to make a decision, she began hurrying back to the room and lock the door. ")
                    choice = input("1: go back to sleep, 2: come back to find out more about what happened. ")
                    if choice == "1":
                        print("She decide to go back to sleep.")
                    elif choice == "2":
                        print("Her friend and her parents were tie up in the kitchen, so she ran to the living room"
                              "and threw something at the elderly women there ")
                        choice = input(
                            "1 : you fling the flower-filed vase at the elderly women head or"
                            "  2: run out of the house without the elderly women find out and call the police  ")
                        if choice == "1":
                            print(" you hit her in the head, she passes out and assist a friend of yours to leave "
                                  "and call the police ")
                        if choice == "2":
                            print(" you attempt to flee, but she finds you and kills you.")
                            print("GAME-OVER")
            else:
                print("She decided go back to sleep")

            playAgain = input("you want  play again ? (y/n) ")
            if playAgain == "n":
                print("Thanks for playing")
                stillplaying = False
        playGame()

    elif choice == "3":
        
        # I am using a while that only runs for three rounds like a traditional rock, paper, scissor game
        while True:

            # This list needs to come before the computer option
            possibleChoices = ["rock", "paper", "scissors"]
            # The computer needs to pull a random value to play with the user
            computerOption = random.choice(possibleChoices)
            # This will show the user the options that they can input for the game
            userOption = input("Enter a choice (rock, paper, scissors): ")
            
            print(f"You chose {userOption}, the computer chose {computerOption}.")
            # this line should be first because in the case of a tie you dont need to worry about other lines of code trying to run.
            if userOption == computerOption:
                print("Both players selected the same option, what a waste of time!")

            elif userOption == "rock":
                if computerOption == "scissors":
                    print("Rock destroys your flimsy scissors! VICTORY!")
                else:
                    print("Paper envelopes your rock! who would choose a pebble,instead of the mighty paper HA!.")
                
            elif userOption == "paper":
                if computerOption == "rock":
                    print("Paper envelopes your rock! who would choose a pebble,instead of the mighty paper HA!")
                else:
                    print("Scissors slices your wimpy paper, who even chooses paper? LOSER!")
                    
            elif userOption == "scissors":
                if computerOption == "paper":
                    print("Scissors slices your wimpy paper, who even chooses paper? LOSER!")
                else:
                    print("Rock destroys your flimsy scissors!  VICTORY!")
            #This else statement will run if you do not put one of the options from the userOption string        
            else:
                print("That is not a valid choice. Pick again. CHEATER!")
            #With the playAgain option you can play as many times as you want after pressing "y" after each game if you press anything else it should take you back to the game selection menu
            playAgain = input("Do you want to play again? (y/n) ")
            if playAgain != "y":               
                    break
