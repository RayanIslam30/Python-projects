#Code to test our program that calculates minutes since a date using pytest

from minutes_since import calculate #Import the calculate function from minutes_since
import pytest #Check for system exits

#Our tests for the calculate function

def test_calculate_wrong_data(): #A test to see if errors are caught
    with pytest.raises(SystemExit):
        calculate("January 1, 2000")
    with pytest.raises(SystemExit):
        calculate("00-01-30") 
    with pytest.raises(SystemExit):
        calculate("01-30-2000")

