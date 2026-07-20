#Code to test our 12h to 24h time converter using pytest

from time_converter import convert #Import the convert function from time_converter

#Our tests for the convert function


def test_convert_hour(): #Run tests without adding minutes to our times
    assert convert("7 AM to 6 PM") == "07:00 to 18:00"
    assert convert("2 AM to 9 AM") == "02:00 to 09:00"
    assert convert("3 PM to 11 PM") == "15:00 to 23:00"


def test_convert_minute(): #Run tests with hours and minutes to the times, as well as mixed inputs
    assert convert("8:00 AM to 7:00 PM") == "08:00 to 19:00"
def test_value_error(): #Give incorrect