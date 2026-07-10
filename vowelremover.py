#Code that takes a string and removes all vowels from it

def main():
    #Gets user input for a string and removes all vowels from it using the remove_vowels function
    user_str = input("Enter a string: ")
    no_vowels_str = remove_vowels(user_str)
    print("String without vowels:", no_vowels_str)

def remove_vowels(str): 
    #Removes all vowels from the string by iterating through each character and checking if it is a vowel
    vowels = 'aeiouAEIOU'
    no_vowels_str = ""
    for char in str:
        if char not in vowels:
            no_vowels_str += char
    return no_vowels_str

main()