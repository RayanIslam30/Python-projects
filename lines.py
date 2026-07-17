#Code to check the amount of lines another program has, not including comments or whitespace

import sys #Import sys to use sys.argv
lines = int(0) #Initialize our count of lines in the program

name = sys.argv[1] #set our file name to file user inputted

with open(name) as file:
    for line in file:
        lines+=1

print(lines)
