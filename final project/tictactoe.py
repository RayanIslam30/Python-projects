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
    play_game(player2, mode)

#Get where user wants to place their X, check if that placement is legal.
def get_user_move(board):
    while True: #Get user position, keep going until we get valid input
        try:
            position = int(input("Player 1 (X), enter your move: "))
            position-=1 #Our value is actually 0 indexed, so lower number by 1

            if position in board.available_moves(): #Check that the position is unoccupied
                break
            elif 0<=position<=8:
                print("That square is already occupied.")
            else:
                print("Please choose valid square.")
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
        while True: #Loop until we get a winner or tie
            print("\n") #New line for spacing
            board.display() 
            print("\n") #new line for spacing

        # Player 1's turn
            get_user_move(board)
            print("\n") #new line for spacing
            board.display() #Display board with player's move 
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