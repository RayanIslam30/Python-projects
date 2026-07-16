#A guessing game that uses the random module to choose a number between 1 and the number the user inputs
import random #Import random module

#Keep asking for user to input level until they input a valid number
while True: 
    try:
        level = int(input("Level: ")) #User chooses 'level', the number inputted here is the upper range of guessable numbers
        if level >=1:
            break
    except ValueError:
        pass


number = random.randint(1,level)
#Loop to allow user to keep guessing until they get it right
while True:
    try:
        guess = int(input("Guess: ")) #User guesses a number
        if guess == number: #If guess is right, tell user it's right and then break
            print("Just Right!")
            break
        elif guess < number: #If guess is too small, tell user
            print("Too small!")
        else: #If guess is too large, tell user
            print("Too large!") 
    except ValueError: # User didn't input number, ask again
        pass