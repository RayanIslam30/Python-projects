#Code that takes a string and removes all vowels from it

def main():
    #Gets user input for a string and removes all vowels from it using the shorten function
    user_str = input("Enter a string: ")
    no_vowels_str = shorten(user_str)
    print("String without vowels:", no_vowels_str)

def shorten(word): 
    #Removes all vowels from the string by iterating through each character and checking if it is a vowel
    vowels = 'aeiouAEIOU'
    no_vowels_str = ""
    for char in word:
        if char not in vowels:
            no_vowels_str += char
    return no_vowels_str

if __name__ == "__main__": #Only run main if file ran directly
    main()