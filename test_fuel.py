#Code to test our two functions in fuel using pytest

import pytest #Import pytest so that we can check exceptions

#Import convert and gauge function from fuel
from fuel import convert, gauge

#Our tests for the convert function
def test_convert():
    assert convert("1/2") == 50 #Check that a normal fraction converts to percentage without %
    assert convert("1/1") == 100 #Check that it allows for 100
    assert convert("0/1") == 0 #Check that it allows for 0
    
#Test for ValueError in convert function
def test_value_error():
    with pytest.raises(ValueError): #Check that it doesn't take non-integers
        convert("cat/dog")
        convert("-1/2")
        convert("1/-2")
        convert("2/1")

#Test for ZeroDivisionError in convert function
def test_zero_division_error():
    with pytest.raises(ZeroDivisionError): #Check that y cannot be 0, or exception is raised
        convert("1/0")

#Our tests for the gauge function
def test_gauge():
    assert gauge(50) == "50%" #Check that a normal case works
    assert gauge(66.67) == "67%" #Check rounding
    assert gauge(1) == "E" #Check that <=1 == E
    assert gauge(99) == "F" #Check that >=99 == F
