    # Tic-Tac-Toe
    #### Video Demo:  <URL HERE>
    #### Description:
    A python script that allows the user to play Tic-Tac-Toe against a computer from the command-line.
    Before the game, the user is able to choose from 3 difficulties for the computer: Easy, Normal, and Hard. 
        I also decided to implement a way for two people to play against each other, activated by the user typing two-player or 2p during difficulty selection. Since I have to get user moves anyway, this wasn't too difficult to implement, but I did choose to include a new function to get the second users moves, as it simplifies the code instead of trying to figure out if the player is using X or O. 
        Player 1 is always X, and the computer or player 2 is always O. I considered randomly deciding who was X or O, but it would complicate the code a lot for not much benefit. 
    The easy mode computer chooses moves completely at random, making it simple even for beginners.
    The normal mode computer implements strategy into their moves, using a weighted random system to try and block the user, prioritize moves that increase their likelihood of winning, and setting up stronger board positions.
    The hard mode computer is incredibly difficult, always playing a perfect game. 
        I used a class for most of logic, with the 'Board' class printing out the board, displaying user and/or computer moves, and checking if those moves are valid. Each square on the board is stored in a list, allowing for each square to be easily changed to either and X or O, and simplify checking if a square is occupied or not. Making the board a class makes the code more simple and easy to read, since almost every function calls to the board, allowing for the code to generally look neater, and it is more clear what each function does, and how the code works.
    To check for a win, we check if all three squares in a row, column, or diagonal are occupied by one player.
    Similar logic is used to check for a full board to determine a tie, checking that every square is occupied by either player.
    This project involves many skills learned in CS50P, including functions, loops, lists and dictionaries, conditionals, libraries, object-oriented programming, and more.


    