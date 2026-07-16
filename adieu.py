#Code to ask user for names until they quit, and then say 'adieu' to all the names after

import inflect #Import module to properly format names

names = [] #Empty list to store names inputted by user

while True:
    try:
        name = input("Name: ") #Get name from user
        names.append(name) #Add name to list
    except EOFError: #If user inputs ctrl-d, end
        break
#Print our string with proper formatting and 'adieu'