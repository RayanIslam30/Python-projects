#My final project for CS50P
#Code that allows the user to play tictactoe against the computer
#Three different modes: easy, normal, hard
#Easy mode just randomly chooses a square to place on
#Normal mode uses weighted random choice to make 'smarter' moves, make sure to win when able
#Hard mode will always pick the best possible move

import random #Import the random module to randomly generate moves for the computer 

#Color codes for terminal output
BLUE = "\033[34m"
RED = "\033[31m"
RESET = "\033[0m"

#Functions to help make code easier, color the X and O for better visibility, and check if a move is valid
def color_square(square):
    if square == "X":
        return f"{BLUE}X{RESET}"
    elif square == "O":
        return f"{RED}O{RESET}"
    else:
        return square

def is_valid_move(board, position):
    return position in board.available_moves()
    
#Initialize a class to handle our board function
class Board:
    def __init__(self): #Initialize the board state
        self.board = ["1", "2", "3",
                      "4", "5", "6",
                      "7", "8", "9"]
        
    def display(self): #Display the board 
        print(f" {color_square(self.board[0])} | {color_square(self.board[1])} | {color_square(self.board[2])}")
        print("---+---+---")
        print(f" {color_square(self.board[3])} | {color_square(self.board[4])} | {color_square(self.board[5])}")
        print("---+---+---")
        print(f" {color_square(self.board[6])} | {color_square(self.board[7])} | {color_square(self.board[8])}")

    def make_move(self, position, player): #Change a blank square to an X for player or O for computer/player 2
            self.board[position] = player

    def available_moves(self): #Available spaces to move
        moves = [] #Create a list of available moves
        for i, square in enumerate(self.board):
            if square.isnumeric():
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
        for a, b, c in winning_conditions:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] in ["X", "O"]: #If any winning combination is either all X or O, then set variable to true
                return True
        return False #If we didn't find a winner, return false
        

    def is_full(self): #Check if the board is full to determine a tie
        return all(square in ["X", "O"] for square in self.board) #If all squares are either X or O, then the board is full

board = Board() 
def main():
    player2 = False #Initialize variable to check if we have two player mode enabled or not
    while True: #Loop until we get a valid difficulty or two player mode is selected
        mode = input("Choose mode (easy, normal, hard, or two-player): ").lower().strip() #User chooses initial difficulty
        if mode == "2p" or mode == "two-player" or mode =="two player": #Check for two player mode
            player2 = True
            break
        elif mode == "easy" or mode == "normal" or mode =="hard": #If valid difficulty entered, break
            break
        else: #Otherwise, ask for valid input
            print("Please choose a valid mode.")
    print(play_game(player2, mode))

#Get where user wants to place their X, check if that placement is legal.
def get_user_move(board):
    while True: #Get user position, keep going until we get valid input
        try:
            position = int(input("Player 1 (X), enter your move: "))
            position-=1 #Our value is actually 0 indexed, so lower number by 1

            if is_valid_move(board, position): #Check that the position is valid
                break
            elif 0<=position<=8: #Check that they inputed a valid square
                print("That square is already occupied.")
            else: #Otherwise, invalid square
                print("Please choose valid square.")
        except(ValueError): #If they inputed a non-integer, catch the error and ask for valid square
            print("Please choose valid square.")
    board.make_move((position), "X") #Make the move
#Only used for a second human player, get where they want to place their O, check if that placement is legal.
def get_user2_move(board):
    while True: #Get user position, keep going until we get valid input
        try:
            position = int(input("Player 2 (O), enter your move: "))
            position-=1 #Our value is actually 0 indexed, so lower number by 1

            if is_valid_move(board, position): #Check that the position is valid
                break
            elif 0<=position<=8: #Check that they inputed a valid square
                print("That square is already occupied.")
            else: #Otherwise, invalid square
                print("Please choose valid square.")
        except(ValueError): #If they inputed a non-integer, catch the error and ask for valid square
            print("Please choose valid square.")
    board.make_move((position), "O") #Make the move

#Logic for our computer moves on all three difficulties
def get_computer_move(board, mode):
    if mode == "easy": #Easy mode, just randomly choose a square to place on
        position = random.choice(board.available_moves())
        board.make_move(position, "O")
    elif mode == "normal": #Normal mode, use weighted random choice and a flowchart design to make 'smarter' moves, make sure to win when able
        ... 
    elif mode == "hard": #Hard mode will always pick the best possible move using minimax algorithm
        ...

#The main gameplay loop. Different logic for player vs computer and player vs player, and checks for win or tie after every move. Gets difficulty 
def play_game(player2, mode): 
    if player2: #If two player mode
        while True: #Loop until we get a winner or tie
            print("\n") #New line for spacing
            board.display() 
            print("\n") #new line for spacing

        # Player 1's turn
            get_user_move(board)
            print("\n") #new line for spacing
            board.display() #Display board with player's move 
            print("\n") #new line for spacing
        # Check if player 1 won
            winner = board.check_winner() #Check for a winner   
            if winner:
                return("Player 1 wins!")
        # Check for tie
            if board.is_full():
                return("It's a tie!")

        # Player 2's turn
            get_user2_move(board)
            board.display() #Display board with player's move
    # Check if player 2 won
            winner = board.check_winner() #Check for a winner   
            if winner:
                return("Player 2 wins!")

    # Check for tie
            if board.is_full():
                return("It's a tie!")

    else: #If player vs computer
        while True: #Loop until we get a winner or tie
            print("\n") #new line for spacing
            board.display()
            print("\n") #new line for spacing

        # Player's turn
            get_user_move(board)
            board.display() #Display board with player's move
        # Check if player won
            winner = board.check_winner()
            if winner:
                return("Player wins!")

        # Check for tie
            if board.is_full():
                return("It's a tie!")

        # Computer's turn
            get_computer_move(board, mode)
            board.display() #Display board with computer's move

        # Check if computer won
            winner = board.check_winner()
            if winner:
                return("Computer wins!")

        # Check for tie
            if board.is_full():
                return("It's a tie!")
        
if __name__ == "__main__": #Only run main if called directly, allows us to test functions
    main()