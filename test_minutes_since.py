#Code to test our program that calculates minutes since a date using pytest

from minutes_since import calculate #Import the calculate function from minutes_since

#Our tests for the calculate function

def test_calculate(): #A test for normal input
    ...

def test_calculate_wrong_data(): #A test to see if errors are caught
    assert calculate("January 1, 2000") == "Invalid date"
    assert calculate("00-01-30") == "Invalid date"
    assert calculate("01-30-2000") == "Invalid date"
