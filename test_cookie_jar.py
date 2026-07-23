#Code to test the functions of the cookie jar class using pytest

import pytest #Check for error raises
from cookie_jar import Jar #Import the whole class 

def test_init(): #Test that our initial state is as expected
    ...


def test_str(): #Test that strings work as intended
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit(): #Test deposit works as intended
    ...


def test_withdraw(): #Test withdraw works as intended
    ...