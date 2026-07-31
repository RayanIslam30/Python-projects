#My final project for CS50P
#Code that allows the user to play tictactoe against the computer
#Three different modes: easy, normal, hard
#Easy mode just randomly chooses a square to place on
#Normal mode uses weighted random choice to make 'smarter' moves, make sure to win when able
#Hard mode will always pick the best possible move

import random #Import the random module to randomly generate moves for the computer

#Initialize a class to handle our board function
class Board:
    def __init__(self): #Initialize the board state
        self.board = ["1", "2", "3",
                      "4", "5", "6",
                      "7", "8", "9"]
    
    def display(self): #Display the board 
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")

    def make_move(self, position, player): #Change a blank square to an X for player or O for computer/player 2
            self.board[position] = player

    def available_moves(self): #Available spaces to move
        moves = [] #Create a list of available moves
        for i, square in enumerate(self.board):
            if square.isnumeric:
                moves.append(i)
        return moves

    def check_winner(self): #Check if a player has won
        winning_conditions = [ #All possible combinations of squares that can result in a win
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]
        

    def is_full(self): #Check if the board is full
        ...

board = Board() 
def main():
    player2 = False #Initialize variable to check if we have two player mode enabled or not
    print("How to play: ") #Instructions on how it works
    while True: #Loop until we get a valid difficulty or two player mode is selected
        mode = input("Choose difficulty (easy, normal, hard): ").lower().strip() #User chooses initial difficulty
        if mode == "2p" or mode == "two-player" or mode =="two player": #Check for two player mode
            player2 = True
            break
        elif mode == "easy" or mode == "normal" or mode =="hard": #If valid difficulty entered, break
            break
    play_game(player2, mode)

#Get where user wants to place their X, check if that placement is legal.
def get_user_move(board):
    while True: #Get user position, keep going until we get valid input
        try:
            position = int(input("Player 1 (X), enter your move: "))
            position-=1 #Our value is actually 0 indexed, so lower number by 1
            if position in board.available_moves(): #Check that the position is unoccupied
                break
            else:
                print("That square is already occupied.")
        except(ValueError):
            print("Please choose valid square.")
    board.make_move((position), "X") 
#Only used for a second human player, get where they want to place their O, check if that placement is legal.
def get_user2_move(board):
    ...

#Logic for our computer moves on all three difficulties
def get_computer_move(board, mode):
    ...

#The main gameplay loop. Different logic for player vs computer and player vs player, and checks for win or tie after every move. Gets difficulty 
def play_game(player2, mode):
    if player2: #If two player mode
        while True:
            print("\n") #New line for spacing
            board.display() 
            print("\n") #new line for spacing

        # Player 1's turn
            get_user_move(board)
            board.display() #Display board with player's move
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

            break #temporary break to prevent infinite loop
    else: #If player vs computer
        while True:
            print("\n") #new line for spacing
            board.display()
            print("\n") #new line for spacing

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
        
            break #temporary break to prevent infinite loop
if __name__ == "__main__": #Only run main if called directly, allows us to test functions
    main()