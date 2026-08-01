#Code to test that the tic-tac-toe program is worked as expected
from tictactoe import play_game,get_computer_move, color_square, Board, is_valid_move #Import our functions to test, only test functions that don't require user input

def test_get_computer_move(): #Check that computer is working right
    board = Board() #Initialize the board class
    get_computer_move(board, "easy") #Get computer move on easy mode
    assert board.board.count("X") == 0 #Check that the computer didn't make a move for the player
    assert board.board.count("O") == 1 #Check that the computer made a move for the computer
    assert len(board.available_moves()) == 8 #Check that the computer made a move and there are now 8 available moves
    get_computer_move(board, "normal") #Get computer move on normal mode
    assert board.board.count("X") == 0 #Check that the computer didn't make a move for the player
    assert board.board.count("O") == 2 #Check that the computer made a move for the computer
    assert len(board.available_moves()) == 7 #Check that the computer made a move and there are now 7 available moves
    get_computer_move(board, "hard") #Get computer move on hard mode
    assert board.board.count("X") == 0 #Check that the computer didn't make a move for the player
    assert board.board.count("O") == 3 #Check that the computer made a move for the computer
    assert len(board.available_moves()) == 6 #Check that the computer made a move and there are now 6 available moves

def test_is_valid_move(): #Check that the is_valid_move function is working right
    board = Board() #Initialize the board class
    assert is_valid_move(board, 0) == True #Check that a valid move returns True
    assert is_valid_move(board, 9) == False #Check that an invalid move returns False
    assert is_valid_move(board, -1) == False #Check that an invalid move returns False
    board.make_move(0, "X") #Make a move at position 0 with player X
    assert is_valid_move(board, 0) == False #Check that an invalid move returns False

def test_color_square(): #Check that the color_square function is working right
    assert color_square("X") == "\033[34mX\033[0m" #Check that X is colored blue
    assert color_square("O") == "\033[31mO\033[0m" #Check that O is colored red
    assert color_square("1") == "1" #Check that numbers are not colored

def test_board_display(): #Check that the board is displaying correctly
    board = Board() #Initialize the board class
    assert board.board == ["1", "2", "3", "4", "5", "6", "7", "8", "9"] #Check that the board is initialized correctly
    board.board = ["X", "O", "X", "O", "X", "O", "X", "O", "X"] #Set the board to a specific state
    assert board.board == ["X", "O", "X", "O", "X", "O", "X", "O", "X"] #Check that the board is set correctly

def test_board_make_move(): #Check that the board is making moves correctly
    board = Board() #Initialize the board class
    board.make_move(0, "X") #Make a move at position 0 with player X
    assert board.board[0] == "X" #Check that the move was made correctly
    board.make_move(1, "O") #Make a move at position 1 with player O
    assert board.board[1] == "O" #Check that the move was made correctly

