#My final project for CS50P
#Code that allows the user to play tictactoe against the computer
#Three different modes: easy, normal, hard
#Easy mode just randomly chooses a square to place on
#Normal mode uses weighted random choice to make 'smarter' moves, make sure to win when able
#Hard mode will always pick the best possible move

import random #Import the random module to randomly generate moves for the computer

#Initialize a class to handle our board function
class Board:
    def __init__(self): #Initialize the board
        self.board = [" "] * 9
    
    def display(self): #Display the board
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")

    def make_move(self, position, player): #Change a blank square to an X for player or O for computer/player 2
        ...

    def available_moves(self): #Available spaces to move
        ...

    def check_winner(self): #Check if a player has won
        ...

    def is_full(self): #Check if the board is full
        ...

board = Board() 

def main():
    print("How to play: ") #Instructions on how it works
    while True: #Loop until we get a valid difficulty or two-player mode is selected
        mode = input("Choose difficulty: ").lower().strip() #User chooses initial difficulty
        if mode == "2p" or mode == "two-player":
            player = True
            break
        elif mode == "easy" or mode == "normal" or mode =="hard":
            break
    print("\n") #New line for spacing
    board.display() #Display the initial board




#Get where user wants to place their X, check if that placement is legal.
def get_user_move(board):
    ...

#Only used for a second human player, get where they want to place their O, check if that placement is legal.
def get_user2_move():
    ...

#Logic for our computer moves on all three difficulties
def get_computer_move(board, mode):
    ...


#The main gameplay loop. Different logic for player vs computer and player vs player, and checks for win or tie after every move. Gets difficulty 
def play_game(player, mode):
    if player: #If two player mode
        while True:
            board.display()

        # Player 1's turn
            get_user_move(board)

        # Check if player 1 won
            ...

        # Check for tie
            ...

        # Player 2's turn
            get_user2_move(board)

    # Check if player 2 won
            ...

    # Check for tie
            ...
    else: #If player vs computer
        while True:
            board.display()

        # Player's turn
            get_user_move(board)

        # Check if player won
            ...

        # Check for tie
            ...

        # Computer's turn
            get_computer_move(board, mode)

        # Check if computer won
            ...

        # Check for tie
            ...
        

if __name__ == "__main__": #Only run main if called directly, allows us to test functions
    main()