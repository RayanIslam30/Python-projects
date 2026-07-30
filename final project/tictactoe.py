#My final project for CS50P
#Code that allows the user to play tictactoe against the computer
#Three different modes: easy, normal, hard
#Easy mode just randomly chooses a square to place on
#Normal mode uses weighted random choice to make 'smarter' moves, make sure to win when able
#Hard mode will always pick the best possible move

import random #Import the random module to randomly generate moves for the computer


def main():
    draw_board

#Used to draw the board with X and O in proper spots
def draw_board():
    ...

#
def get_user_move():
    ...

#Only used for a second human player
def get_user2_move():
    ...

#Logic for our computer moves on all three difficulties
def get_com_move(mode):
    ...


if __name__ == "__main__": #Only run main if called directly, allows us to test functions
    main()