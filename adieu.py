# Code to ask user for names until they quit, and then say 'adieu' to all the names after

import inflect  # Import module to properly format names

p = inflect.engine()

names = []  # Empty list to store names inputted by user
# Loop to get names, quit loop if ctrl-d inputted
while True:
    try:
        name = input("Name: ")  # Get name from user
        names.append(name)  # Add name to list
    except EOFError:  # If user inputs ctrl-d, end
        print()  # Put out a new line for formatting reasons
        break
# Print our string with proper formatting and 'adieu'
print("Adieu, adieu, to ", end="")
print(p.join(names))
