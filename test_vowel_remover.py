#Code to test our vowel_remover program
from vowel_remover import shorten #Test the shorten function in vowel_remover

def main(): 
    test_shorten()
#Our test of the shorten function
def test_shorten():
    if shorten("cat") != "ct":
        print("cat was not shortened to ct")
    if shorten("CAT") != "CT":
        print("CAT was not shortened to CT")

if __name__ == "__main__": #Only run main if file ran directly
    main()