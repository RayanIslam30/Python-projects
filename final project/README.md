    # Tic-Tac-Toe
    #### Video Demo:  <URL HERE>
    #### Description:
    A python script that allows the user to play Tic-Tac-Toe against a computer from the command-line.

        I also decided to implement a way for two people to play against each other, activated by the user typing two-player or 2p during difficulty selection. Since I have to get user moves anyway, this wasn't too difficult to implement, but I did choose to include a new function to get the second players moves, since they would be using O, and player 1 always uses X.
        
    Before the game, the user is able to choose from 3 difficulties for the computer: Easy, Normal, and Hard. 
        - The easy mode computer chooses moves completely at random, making it simple even for beginners. This is done by simply selecting one of the empty squares using the random function
        - The normal mode computer implements strategy into their moves, using a weighted random system to try and block the user, prioritize moves that increase their likelihood of winning, and setting up stronger board positions. This is done by using a flowchart system, aiming for the 'smartest' moves first
        - The hard mode computer always plays a perfect game. This is done with a minimax algorithm, recursively searching through every possible move to find the best one, assuming both players are playing perfectly.

    I used a class for most of logic,
        The Board class has methods for printing out the board, displaying moves on that board, checking if those moves are valid, and checking for a win or tie. 
        Each square on the board is stored in a list, allowing for each square to be easily changed to either and X or O, and simplify checking if a square is occupied or not. Making the board a class makes the code more simple and easy to read, since almost every function calls to the board.
        At first, each square was initially empty, and I would print out instructions at the start, but I decided to instead label each square with the number the user can input to occupy that square.
        To check for a win, we check if all three squares in a row, column, or diagonal are occupied by one player.
        Similar logic is used to check for a full board to determine a tie, checking that every square is occupied by either player.
        When checking for a valid move, we check if the index for that square in our list has either an X or O, meaning it is already taken. 
    
    Other functions exist to ask the user for a move and make sure that move is valid
    


    This project involves many skills learned in CS50P, including functions, loops, lists and dictionaries, conditionals, libraries, object-oriented programming, and more. 
    The main thing I had to learn was how to implement a minimax algorithm, since it wasn't covered in CS50P. I researched how it works, learned how recursive searching is used in situations like mapping all possible game outcomes, and modified the algorithm to work for my tic-tac-toe game. This allowed me to gain experience in python topics that were not covered in the course.

    