#Code to test our IP address checker using pytest

from Ip_address import validate #Import the validate function from Ip_address

#Our tests for the validate function

def test_value():
    assert validate("255.255.255.255") == "Valid" #Valid IP address is valid
    assert validate("0.153.194.255") == "Valid" #Another Valid IP address is valid
    assert validate("0.0.0.0.") == "Invalid" #An extra '.' will make invalid
    assert validate("-100.-2.-9.-234") == "Invalid" #Numbers less than 0 will be invalid
    assert validate("300.407.519.789") == "Invalid" #Numbers greater than 255 will be invalid
    assert validate("200.300.400.500") == "Invalid" #All numbers must be valid, not just first
    assert validate("cat.dog.sheep.fish") == "Invalid" #Must have numbers
    