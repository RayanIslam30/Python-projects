#Code to test our um program

from um_count import count #Import the count function from um

#Our tests for the countfunction


def test_um_count(): #Run normal test
    assert count("um") == 1 
    assert count("um um um") == 3
    assert count("UM Um uM um") == 4

def test_um_words(): #Test including other words and punctuation
    assert count("hello, um, world") == 1 
    assert count("um, I, um... um!") == 3

def test_um_in_word(): #Test that um is not counted as part of a word
    assert count("strawberry cake is, um, yummy") == 1 
    assert count("yum") == 0
