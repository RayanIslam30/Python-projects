#Code to test the functions of the cookie jar class using pytest

import pytest #Check for error raises
from cookie_jar import Jar #Import the whole class 

def test_init(): #Test that our initial state is as expected
    jar = Jar() #Initialize the class
    assert jar.capacity == 12 
    assert jar.size == 0
    jar = Jar(10) #Change jar capacity
    assert jar.capacity == 10 
    assert jar.size == 0


def test_str(): #Test that strings work as intended
    jar = Jar() #Initialize the class
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit(): #Test deposit works as intended
    jar = Jar() #Initialize the class
    jar.deposit(3)
    assert jar._size == 3
    jar.deposit(5)
    assert jar._size == 8
    with pytest.raises(ValueError):
        jar.deposit(10)
    

def test_withdraw(): #Test withdraw works as intended
    jar = Jar() #Initialize the class
    jar._size = 10 #Start with 10 cookies
    jar.withdraw(4)
    assert jar._size == 6
    jar.withdraw(6)
    assert jar._size == 0
    with pytest.raises(ValueError):
        jar.withdraw(2)
