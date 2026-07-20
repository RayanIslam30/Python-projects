#Code to test our 12h to 24h time converter using pytest

from time_converter import convert #Import the convert function from time_converter

#Our tests for the convert function


def test_convert_hour(): #Run tests without adding minutes to our times
    assert convert("7 AM to 6 PM") == "07:00 to 18:00"
    assert convert("2 AM to 9 AM") == "02:00 to 09:00"
    assert convert("3 PM to 11 PM") == "15:00 to 23:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_convert_minute(): #Run tests with hours and minutes to the times, as well as mixed inputs
    assert convert("8:30 AM to 7:30 PM") == "08:30 to 19:30"
    assert convert("5:47 AM to 9:28 PM") == "05:47 to 21:28"
    assert convert("5:00 AM to 10:00 AM") == "05:00 to 10:00"

def test_value_error(): #Give incorrect input to see if it is caught
    assert convert("2-10 PM") == "Invalid input"
    assert convert("cat AM to dog PM") == "Invalid input"
    assert convert("13 AM to 19 PM") == "Invalid input"
    assert convert("8:90 AM to 5:64 PM") == "Invalid input"