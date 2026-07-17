#Code to test our bank program using pytest
from bank import value #Import the value function from bank

#Our tests for the value function

def test_value():
    assert value("hello") == 0 #hello gives 0
    assert value("hey") == 20 #greeting starting with 'h' gives 20
    assert value("yo") == 100 #greeting not starting with 'h' gives 100
    assert value("hello, User") == 0 #more text after hello doesn't matter