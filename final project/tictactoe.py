# My final project for CS50P
# Code that allows the user to play tictactoe against the computer, or against another player
# Three different difficulty modes for the computer: easy, normal, hard
# Easy mode just randomly chooses a square to place on
# Normal mode uses weighted random choice to make 'smarter' moves, making it move more like a real player would
# Hard mode will always pick the best possible move, using a minimax algorithm to find the best move
# Two player mode allows two human players to play against each other, taking turns placing X's and O's on the board

import random  # Import the random module to randomly generate moves for the computer
import time  # Import the time module to add a delay for the computer's move to make it feel more natural

# Escape codes for terminal output, colors and bolding
BLUE = "\033[34m"
RED = "\033[31m"
YELLOW = "\033[33m"
BOLD = "\033[1m"
RESET = "\033[0m"


# Functions to help make code easier, color the X and O for better visibility, and check if a move is valid
def color_square(square):
    if square == "X":
        return f"{BLUE}X{RESET}"
    elif square == "O":
        return f"{RED}O{RESET}"
    else:
        return square


# A simple function to check if a move is valid, returns True if the move is valid, False if not
# Simplifies having to check if a move is valid in multiple places in the code
def is_valid_move(board, position):
    return position in board.available_moves()


# Minimax algorithm to determine the best possible move for the computer in hard mode
# A recursive algorithm that simulates all possible moves and their outcomes
# Chooses the move that maximizes the computer's chances of winning while minimizing the player's chances of winning
def minimax(board, depth, is_maximizing):
    winner = board.check_winner()  # Check if the simulated board has a winner
    if winner:
        if (is_maximizing):  # If it's the computer's turn next, return a score of -1, bad outcome for the computer, they lost
            return -1
        elif (not is_maximizing):  # If it's the player's turn next, return a score of 1, good outcome for the computer, they won
            return 1
    elif (board.is_full()):  # Check if the board is full and return a score of 0 for a tie, neutral outcome for the computer
        return 0

    if is_maximizing:  # If it's the computer's turn, try to maximize the score
        best_score = -float("inf")  # Initialize best score to negative infinity, so any score will be better than it
        for move in board.available_moves():  # Iterate through all available moves
            board.make_move(move, "O")
            score = minimax(board, depth + 1, False)  # Recursively call minimax to simulate the player's turn, and get the score for that move
            board.make_move(move, str(move + 1))  # Reset the square back to its original value
            if (score > best_score):  # If the score is better than the best score, update best score
                best_score = score
        return best_score
    else:  # Simulate the player's turn, assume they try to minimize the score for the computer, so we minimize the score
        best_score = float("inf")
        for move in board.available_moves():  # Iterate through all available moves
            board.make_move(move, "X")
            score = minimax(board, depth + 1, True)  # Recursively call minimax to simulate the computer's turn, and get the score for that move
            board.make_move(move, str(move + 1))  # Reset the square back to its original value
            if (score < best_score):  # If the score is better than the best score, update best score
                best_score = score
        return best_score


# Initialize a class to handle our board function
class Board:
    def __init__(self):  # Initialize the board state
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def display(self):  # Display the board
        print( # First row
            f" {color_square(self.board[0])} | {color_square(self.board[1])} | {color_square(self.board[2])}"
        )
        print("---+---+---") # Separator
        print( # Second row
            f" {color_square(self.board[3])} | {color_square(self.board[4])} | {color_square(self.board[5])}"
        )
        print("---+---+---") # Separator
        print( # Third row
            f" {color_square(self.board[6])} | {color_square(self.board[7])} | {color_square(self.board[8])}"
        )

    def make_move(self, position, player):  # Change a blank square to an X for player or O for computer/player 2
        self.board[position] = player

    def available_moves(self):  # Available spaces to move
        moves = []  # Create a list of available moves
        for i, square in enumerate(self.board):
            if square.isnumeric():
                moves.append(i)
        return moves

    def check_winner(self):  # Check if a player has won
        winning_conditions = [  # All possible combinations of squares that can result in a win
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        for a, b, c in winning_conditions:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] in ["X","O"]:  # If any winning combination is either all X or O, then set variable to true
                return True
        return False  # If we didn't find a winner, return false

    def is_full(self):  # Check if the board is full to determine a tie
        return all(square in ["X", "O"] for square in self.board)  # If all squares are either X or O, then the board is full

board = Board() # Initialize the board class, we will use this to call board methods

def main():
    player2 = False  # Initialize variable to check if we have two player mode enabled or not
    while True:  # Loop until we get a valid difficulty or two player mode is selected
        mode = input(f"{BOLD}Choose mode (easy, normal, hard, or two-player): {RESET}").lower().strip() # User chooses initial difficulty
        if (
            mode == "2p" or mode == "two-player" or mode == "two player"
        ):  # Check for two player mode
            player2 = True
            break
        elif (
            mode == "easy" or mode == "normal" or mode == "hard"
        ):  # If valid difficulty entered, break
            break
        else:  # Otherwise, ask for valid input
            print("Please choose a valid mode.")
    print(play_game(player2, mode))


# Get where user wants to place their X, check if that placement is legal.
def get_user_move(board):
    while True:  # Get user position, keep going until we get valid input
        try:
            position = int(input(f"{BOLD}Player 1 (X), enter your move: {RESET}"))
            position -= 1  # Our value is actually 0 indexed, so lower number by 1

            if is_valid_move(board, position):  # Check that the position is valid
                break
            elif 0 <= position <= 8:  # Check that they inputed a valid square
                print("That square is already occupied.")
            else:  # Otherwise, invalid square
                print("Please choose valid square.")
        except (ValueError):  # If they inputed a non-integer, catch the error and ask for valid square
            print("Please choose valid square.")
    board.make_move((position), "X")  # Make the move


# Only used for a second human player, get where they want to place their O, check if that placement is legal.
def get_user2_move(board):
    while True:  # Get user position, keep going until we get valid input
        try:
            position = int(input(f"{BOLD}Player 2 (O), enter your move: {RESET}"))
            position -= 1  # Our value is actually 0 indexed, so lower number by 1

            if is_valid_move(board, position):  # Check that the position is valid
                break
            elif 0 <= position <= 8:  # Check that they inputed a valid square
                print("That square is already occupied.")
            else:  # Otherwise, invalid square
                print("Please choose valid square.")
        except (
            ValueError
        ):  # If they inputed a non-integer, catch the error and ask for valid square
            print("Please choose valid square.")
    board.make_move((position), "O")  # Make the move


# Logic for our computer moves on all three difficulties
def get_computer_move(board, mode):
    if mode == "easy":  # Easy mode, just randomly choose a square to place on
        position = random.choice(board.available_moves())
        print(f"{BOLD}Computer is thinking...{RESET}")
        time.sleep(0.5)  # Add a delay to make it feel more natural
        board.make_move(position, "O")

    elif mode == "normal":  # Normal mode, use weighted random choice and a flowchart design to make 'smarter' moves, make sure to win when able
        # Iterate through all available moves, check if any of them will result in a win for the computer, if so, make that move
        print(f"{BOLD}Computer is thinking...{RESET}")
        time.sleep(1)  # Add a delay to make it feel more natural, longer delay than easy mode to make it feel like the computer is thinking harder
        for move in board.available_moves():
            board.make_move(move, "O")  # Iterate through all available moves, check if any of them will result in a win for the computer, if so, make that move
            if board.check_winner():
                return
            else:
                board.make_move(move, str(move + 1))  # Reset the square back to its original value if it doesn't result in a win
        # Iterate through all available moves, check if any of them will result in a win for the player, if so, block that move
        for move in board.available_moves():
            board.make_move(move, "X")
            if board.check_winner():
                board.make_move(move, "O")  # Block the player's winning move
                return
            else:
                board.make_move(move, str(move + 1))  # Reset the square back to its original value if it doesn't result in a win
        # If no winning or blocking moves available, try to claim the center square if available, otherwise pick a random corner square, otherwise pick a random square
        if 4 in board.available_moves():  # Check if center square is available
            board.make_move(4, "O")
        elif any(move in board.available_moves() for move in [0, 2, 6, 8]):  # Check if any corner squares are available
            corners = [move for move in [0, 2, 6, 8] if move in board.available_moves()]
            position = random.choice(corners)
            board.make_move(position, "O")
        else:  # Otherwise, pick a random square
            sides = [move for move in [1, 3, 5, 7] if move in board.available_moves()]
            position = random.choice(sides)
            board.make_move(position, "O")

    elif mode == "hard":  # Hard mode will always pick the best possible move using minimax algorithm
        print(f"{BOLD}Computer is thinking...{RESET}")
        time.sleep(1.5)  # Add a delay to make it feel more natural, longer delay than easy and normal mode to make it feel like the computer is thinking harder
        best_score = -float("inf")  # Initialize best score to negative infinity, so any score will be better than it
        best_move = None  # Initialize best move to None
        for move in board.available_moves():  # Iterate through all available moves
            board.make_move(move, "O")  # Make the move
            score = minimax(board, 0, False)  # Get the score for that move using minimax algorithm, starting with the player's turn next, so is_maximizing is False
            board.make_move(move, str(move + 1))  # Reset the square back to its original value
            if (score > best_score):  # If the score is better than the best score, update best score and best move
                best_score = score
                best_move = move
        board.make_move(best_move, "O")  # Make the best move


# The main gameplay loop. Different logic for player vs computer and player vs player, and checks for win or tie after every move. Gets difficulty
def play_game(player2, mode):
    if player2:  # If two player mode
        print("\n")  # New line for spacing
        board.display()
        print("\n")  # new line for spacing
        # Loop until we get a winner or tie, check for win or tie after every move
        while True:
            # Player 1's turn
            get_user_move(board)
            print("\n")  # new line for spacing
            board.display()  # Display board with player's move
            print("\n")  # new line for spacing
            # Check if player 1 won
            winner = board.check_winner()  # Check for a winner
            if winner:
                return f"{BLUE}Player 1 wins!{RESET}"
            # Check for tie
            if board.is_full():
                return f"{YELLOW}It's a tie!{RESET}"

            # Player 2's turn
            get_user2_move(board)
            print("\n")  # new line for spacing
            board.display()  # Display board with player's move
            # Check if player 2 won
            winner = board.check_winner()  # Check for a winner
            if winner:
                return f"{RED}Player 2 wins!{RESET}"

            # Check for tie
            if board.is_full():
                return f"{YELLOW}It's a tie!{RESET}"

    else:  # If player vs computer
        print("\n")  # new line for spacing
        board.display()
        print("\n")  # new line for spacing

        # Loop until we get a winner or tie, check for win or tie after every move
        while True:
            # Player's turn
            get_user_move(board)
            print("\n")  # new line for spacing
            board.display()  # Display board with player's move
            print("\n")  # new line for spacing
            # Check if player won
            winner = board.check_winner()
            if winner:
                return f"{BLUE}Player wins!{RESET}"

            # Check for tie
            if board.is_full():
                return f"{YELLOW}It's a tie!{RESET}"

            # Computer's turn
            get_computer_move(board, mode)
            print("\n")  # new line for spacing
            board.display()  # Display board with computer's move
            print("\n")  # new line for spacing

            # Check if computer won
            winner = board.check_winner()
            if winner:
                return f"{RED}Computer wins!{RESET}"

            # Check for tie
            if board.is_full():
                return f"{YELLOW}It's a tie!{RESET}"


if __name__ == "__main__":  # Only run main if called directly, allows us to test functions
    main()
