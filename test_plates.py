#Code to test our license plate program using pytest

from plates import is_valid #Import the is_valid function from plates

#Our test of is_valid function
def test_is_valid():
    assert is_valid("A") == False #Check for too short
    assert is_valid("ABCD123") == False #Check for too long
    assert is_valid("AB12.") == False #Check for punctuation
    assert is_valid("A1234") == False #Check first two characters are letters
    assert is_valid("ABC000") == False #Check first number 0
    assert is_valid("AB123C") == False #Check no letters after first number
    assert is_valid("ABC123") == True #Check that valid plate is caught