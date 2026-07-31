    # Tic-Tac-Toe
    #### Video Demo:  <URL HERE>
    #### Description:
    A python script that allows the user to play Tic-Tac-Toe against a computer from the command-line.

        I also decided to implement a way for two people to play against each other, activated by the user typing two-player or 2p during difficulty selection. Player 1 always uses X, while player 2 uses O.
        
    Before the game, the user is able to choose from 3 difficulties for the computer: Easy, Normal, and Hard. 
        - The easy mode computer chooses moves completely at random, making it simple even for beginners. 
        - The normal mode computer implements strategy into their moves. It uses a weighted decision system to block the player, prioritize winning moves, and favor stronger board positions.
        - The hard mode computer always plays a perfect game. This is done with a minimax algorithm, recursively searching through every possible move to find the best one, assuming both players are playing perfectly.

    I used a class for most of logic,
        
        The Board class has methods for printing out the board, displaying moves on that board, checking if those moves are valid, and checking for a win or tie. 
        The board is stored as a list of nine squares, making it easy to update moves and check for available spaces. Encapsulating this logic in a class keeps the rest of the code organized and easier to read.  
        Each square is labelled with a number 1-9, to make it easier for the user to understand how to play. Initially the squares were unmarked, but I decided it made it too complicated for the player.
        The board checks for wins by testing each row, column, and diagonal for three matching symbols. It also detects ties by determining whether all squares are occupied.
        When checking for a valid move, we check if the index for that square in our list has either an X or O, meaning it is already taken. A loop is also used to keep asking for a move until we get a valid one.
    
    get_user_move and get_user2_move obtain valid moves from the players, while get_computer_move contains the AI logic for all three difficulties. They rely on the Board class for their implementation, calling methods to abstract away some of the checks for valid moves.
    The play_game function is responsible for the main gameplay loop, drawing the board, calling the user and computer move functions, and using the check_winner and is_full class methods to check for a win or draw after each move.

    The test_tictactoe.py file uses pytest to test my functions, making sure they work as intended for a variety of scenarios. 
    
    The main thing I had to learn was how to implement a minimax algorithm, since it wasn't covered in CS50P. I researched how it works, learned how recursive searching is used in situations like mapping all possible game outcomes, and modified the algorithm to work for my tic-tac-toe game. This allowed me to gain experience in python topics that were not covered in the course.

    