#Code to check the amount of lines another program has, not including comments or whitespace

import sys #Import sys to use sys.argv
lines = int(0) #Initialize our count of lines in the program

#Check that sys.argv[1] exists
if len(sys.argv) == 2: #If file is valid, set name variable to file name
    name = sys.argv[1] #set our file name to file user inputted
elif len(sys.argv) == 1: #If sys.argv[1] doesn't exist, quit with too few arguments
    sys.exit("Too few command-line arguments")
else: #If there are more than 1 argument, quit with too many arguments
    sys.exit("Too many command-line arguments")

#Open the file and read it
with open(name) as file:
#Imp
    for line in file: 
        lines+=1 

print(lines)
