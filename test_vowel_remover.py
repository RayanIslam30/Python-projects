#Code to test our vowel_remover program using pytest
from vowel_remover import shorten #Test the shorten function in vowel_remover

#Our test of the shorten function
def test_shorten():
        assert shorten("cat") == "ct" #Test lowercase 'a'
        assert shorten("CAT") == "CT" #Test capital 'A'
        assert shorten("aeiouAEIOU") == "" #Test all vowels removed
        assert shorten("Testing.") == "Tstng." #Test punctuation
        assert shorten("abc123") == "bc123" #Test numbers
